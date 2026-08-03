# -*- coding: utf-8 -*-
"""카드의 인물 배치를 실측한다.

등신비는 '머리 높이'로 재야 한다. 앞선 판본은 머리 '폭'을 썼는데,
폭은 머리 크기가 아니라 헤어스타일(뾰족머리/보브)에 좌우돼 결과가 뒤집혔다.

머리 높이 = 인물 상단 ~ 목. 목은 머리가 가장 넓어진 뒤 처음 나타나는
가로폭 극소점으로 잡는다. chibi 일수록 등신수가 작다.
"""
import sys, glob, os
from PIL import Image


def analyze(path):
    im = Image.open(path).convert('RGB')
    W, H = im.size
    px = im.load()
    m = int(min(W, H) * 0.03)          # 금색 테두리 안쪽만
    bg = px[m + 2, m + 2]

    def is_fig(c):
        return (abs(c[0] - bg[0]) + abs(c[1] - bg[1]) + abs(c[2] - bg[2])) > 42

    rows = []
    for y in range(m, H - m):
        xmin = xmax = None
        cnt = 0
        for x in range(m, W - m):
            if is_fig(px[x, y]):
                cnt += 1
                if xmin is None:
                    xmin = x
                xmax = x
        rows.append((y, cnt, xmin, xmax))

    solid = [r for r in rows if r[1] > 6]
    if not solid:
        return None
    top, bot = solid[0][0], solid[-1][0]
    fig_h = bot - top
    widths = {r[0]: (r[3] - r[2]) for r in solid}

    # 머리 최대폭 위치 -> 그 아래로 내려가며 첫 극소점(목)
    upper = [y for y in widths if y <= top + fig_h * 0.55]
    upper.sort()
    if not upper:
        return None
    wmax_y = max(upper, key=lambda y: widths[y])
    neck_y, neck_w = None, None
    for y in [y for y in upper if y > wmax_y]:
        w = widths[y]
        if neck_w is None or w < neck_w:
            neck_w, neck_y = w, y
        elif w > neck_w * 1.35:        # 다시 넓어짐 = 어깨. 목은 지났다
            break
    head_h = (neck_y - top) if neck_y else None
    heads = (fig_h / head_h) if head_h else None

    xs = [r[2] for r in solid]
    xe = [r[3] for r in solid]
    cx = (min(xs) + max(xe)) / 2.0

    return dict(name=os.path.basename(path),
                fig_pct=100.0 * fig_h / H,
                base_pct=100.0 * bot / H,
                heads=heads,
                cx_off=100.0 * (cx - W / 2.0) / W)


paths = sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else 'concepts/v3/char_*.png'))
print('%-22s %9s %9s %9s %10s' % ('file', 'heads', 'fig_h%', 'base%', 'x_off%'))
out = []
for p in paths:
    r = analyze(p)
    if not r:
        print('%-22s  FAIL' % os.path.basename(p))
        continue
    out.append(r)
    print('%-22s %8.2f %8.1f%% %8.1f%% %9.1f%%'
          % (r['name'], r['heads'] or 0, r['fig_pct'], r['base_pct'], r['cx_off']))

if out:
    hd = [r['heads'] for r in out if r['heads']]
    fh = [r['fig_pct'] for r in out]
    bs = [r['base_pct'] for r in out]
    xo = [abs(r['cx_off']) for r in out]
    print('')
    print('heads   min %.2f  max %.2f  spread %.2f   (smaller = more chibi)'
          % (min(hd), max(hd), max(hd) - min(hd)))
    print('fig_h%%  min %.1f  max %.1f  spread %.1f pt' % (min(fh), max(fh), max(fh) - min(fh)))
    print('base%%   min %.1f  max %.1f  spread %.1f pt' % (min(bs), max(bs), max(bs) - min(bs)))
    print('x_off%%  worst %.1f' % max(xo))
