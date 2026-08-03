# -*- coding: utf-8 -*-
"""등신비 검사 — 소품에 오염되지 않는 방법.

앞선 두 방법이 실패한 이유:
  - 머리 '폭'  : 헤어스타일에 좌우돼 결과가 뒤집혔다
  - 목 검출    : 머리카락이 어깨에 닿으면 목이 안 잡힌다
  - 경계상자   : 삼각대·측량봉·치켜든 팔이 인물 높이를 부풀린다

그래서 얼굴 피부색 덩어리를 먼저 찾는다. 피부는 소품에 없다.
  턱끝  = 얼굴 피부 덩어리의 아래끝
  머리끝 = 얼굴 x범위 바로 위쪽에서 이어지는 비배경 픽셀의 위끝 (머리카락 포함)
  발끝  = 이미지에서 가장 아래 비배경 행 (부츠)
  등신  = (발끝 - 머리끝) / (턱끝 - 머리끝)
"""
import sys, glob, os
from PIL import Image


def skin(c):
    r, g, b = c
    return (r > 150 and g > 110 and b > 90
            and r >= g >= b
            and r - b > 18 and r - b < 95
            and abs(g - b) < 55)


def analyze(path):
    im = Image.open(path).convert('RGB')
    W, H = im.size
    px = im.load()
    m = int(min(W, H) * 0.03)
    bg = px[m + 2, m + 2]

    def fig(x, y):
        c = px[x, y]
        return (abs(c[0]-bg[0]) + abs(c[1]-bg[1]) + abs(c[2]-bg[2])) > 42

    # 1) 얼굴: 상반부에서 피부 픽셀이 가장 몰린 가로 밴드를 찾는다
    rows = {}
    for y in range(m, int(H * 0.55)):
        cnt = 0
        xs = []
        for x in range(m, W - m):
            if skin(px[x, y]):
                cnt += 1
                xs.append(x)
        if cnt >= 8:
            rows[y] = (cnt, min(xs), max(xs))
    if not rows:
        return dict(name=os.path.basename(path), err='피부 미검출')

    # 얼굴 밴드 = 폭이 가장 넓은 행 주변으로 연속된 구간
    peak = max(rows, key=lambda y: rows[y][0])
    ys = sorted(rows)
    face_rows = [peak]
    for y in [v for v in ys if v > peak]:
        if y - face_rows[-1] > 6:
            break
        face_rows.append(y)
    for y in sorted([v for v in ys if v < peak], reverse=True):
        if face_rows[0] - y > 6:
            break
        face_rows.insert(0, y)

    chin = max(face_rows)
    fx0 = min(rows[y][1] for y in face_rows)
    fx1 = max(rows[y][2] for y in face_rows)
    fcx = (fx0 + fx1) / 2.0
    fw = fx1 - fx0

    # 2) 머리끝: 얼굴 중심 ±0.9*얼굴폭 안에서, 얼굴부터 위로 끊기지 않고 이어지는 곳까지
    lo = max(m, int(fcx - fw * 0.9))
    hi = min(W - m, int(fcx + fw * 0.9))
    top = peak
    y = peak
    while y > m:
        if any(fig(x, y) for x in range(lo, hi)):
            top = y
            y -= 1
        else:
            break

    # 3) 발끝: 가장 아래 비배경 행
    foot = None
    for y in range(H - m - 1, m, -1):
        if sum(1 for x in range(m, W - m) if fig(x, y)) > 6:
            foot = y
            break
    if foot is None:
        return dict(name=os.path.basename(path), err='발 미검출')

    head_h = chin - top
    body_h = foot - top
    return dict(name=os.path.basename(path),
                heads=(body_h / head_h) if head_h > 0 else 0,
                head_pct=100.0 * head_h / H,
                body_pct=100.0 * body_h / H,
                top_pct=100.0 * top / H,
                foot_pct=100.0 * foot / H)


paths = sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else 'concepts/v4/char_*.png'))
res = []
print('%-22s %7s %9s %9s %9s' % ('file', 'heads', 'head_h%', 'body_h%', 'foot%'))
for p in paths:
    r = analyze(p)
    if r.get('err'):
        print('%-22s  %s' % (r['name'], r['err']))
        continue
    res.append(r)
    print('%-22s %7.2f %8.1f%% %8.1f%% %8.1f%%'
          % (r['name'], r['heads'], r['head_pct'], r['body_pct'], r['foot_pct']))

if res:
    hd = sorted(r['heads'] for r in res)
    ft = [r['foot_pct'] for r in res]
    med = hd[len(hd) // 2]
    print('')
    print('등신  최소 %.2f  중앙 %.2f  최대 %.2f  폭 %.2f' % (hd[0], med, hd[-1], hd[-1] - hd[0]))
    print('발끝  최소 %.1f%%  최대 %.1f%%  폭 %.1f pt' % (min(ft), max(ft), max(ft) - min(ft)))
    print('')
    print('중앙값 대비 편차:')
    for r in sorted(res, key=lambda r: -abs(r['heads'] - med)):
        d = r['heads'] - med
        mark = '  <-- 벗어남' if abs(d) > med * 0.15 else ''
        print('  %-22s %+.2f (%+.0f%%)%s' % (r['name'], d, 100.0 * d / med, mark))
