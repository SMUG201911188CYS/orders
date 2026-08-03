# -*- coding: utf-8 -*-
"""v4 카드 아트 → 게임에 꽂을 스프라이트 데이터.

두 가지를 뽑는다.
  1) 32x32 초상화  : 카드에서 머리 부분을 잘라 축소·감색. 얼굴이 실제로 달라야 하므로 실물에서 뽑는다.
  2) 팔레트        : 머리색·옷 액센트를 카드에서 표본. 보드 16x16 은 몸 실루엣을 공유하고
                     팔레트만 갈아끼우면 되므로(엔진이 이미 팔레트 구동) 이것만 있으면 된다.

출력은 기존 drawSprite(ctx, rows, pal, x, y) 가 그대로 먹는 형식이다.
글리프는 '.' 투명 + 0-9a-v 팔레트 인덱스.
"""
import io, os, sys, json
from collections import Counter
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SRC = 'concepts/v4'
KEYS = [('char_01_rin', 'rin'), ('char_02_hana', 'hana'), ('char_03_sora', 'sora'),
        ('char_04_yui', 'yui'), ('char_05_mio', 'mio'), ('char_06_nagi', 'nagi'),
        ('char_07_aoi', 'aoi'), ('char_08_hotaru', 'hotaru'), ('char_09_shizu', 'shizu')]
GL = '0123456789abcdefghijklmnopqrstuv'


def bg_of(im):
    px = im.load()
    m = int(min(im.size) * 0.03)
    return px[m + 2, m + 2]


def is_fig(c, bg, tol=42):
    return abs(c[0]-bg[0]) + abs(c[1]-bg[1]) + abs(c[2]-bg[2]) > tol


def figure_box(im, bg):
    W, H = im.size
    px = im.load()
    m = int(min(W, H) * 0.03)
    xs, ys = [], []
    for y in range(m, H - m, 2):
        for x in range(m, W - m, 2):
            if is_fig(px[x, y], bg):
                xs.append(x); ys.append(y)
    return min(xs), min(ys), max(xs), max(ys)


def skinlike(c):
    r, g, b = c[:3]
    return r > 150 and g > 110 and b > 90 and r >= g >= b and 18 < r - b < 95


# 얼굴을 자동으로 찾는 규칙을 셋(밀도·위치·폭) 다 시도했고 매번 다른 캐릭터가 깨졌다.
# 소품·주먹·머리 위로 든 팔이 캐릭터마다 다르게 방해한다. 9장은 일반 문제가 아니라
# 고정된 9개 이미지이므로, 자동 탐색이 실패하는 둘만 탐색 창을 직접 지정한다.
# 값은 카드 크기(1024x1536)에 대한 비율 (x0, x1, y0, y1).
FACE_WINDOW = {
    'rin':    (0.34, 0.66, 0.08, 0.34),   # 주먹·가방끈 쥔 손이 얼굴보다 조밀하다
    'hotaru': (0.38, 0.74, 0.12, 0.48),   # 랜턴 든 손이 얼굴보다 위에 있다
}


def head_box(im, bg, box, key=None):
    """얼굴 피부 밴드를 찾아 머리 상자를 만든다.

    턱은 '피부 최하단'이 아니라 밀도가 급감하는 지점으로 잡는다. 그러지 않으면
    가슴 앞 소품을 안은 손이 턱으로 잡혀 상자가 몸통까지 늘어난다.
    """
    x0, y0, x1, y1 = box
    W, H = im.size
    w = FACE_WINDOW.get(key)
    if w:
        x0, x1 = int(W * w[0]), int(W * w[1])
        ytop, ybot = int(H * w[2]), int(H * w[3])
    else:
        ytop, ybot = y0, y0 + int((y1 - y0) * 0.55)
    px = im.load()
    rows = {}
    for y in range(max(0, ytop), min(H, ybot)):
        xs = [x for x in range(max(0, x0), min(W, x1), 2) if skinlike(px[x, y])]
        if len(xs) >= 4:
            rows[y] = xs
    if not rows:
        side = x1 - x0
        return (x0, ytop, x0 + side, ytop + side)
    peak = max(rows, key=lambda y: len(rows[y]))
    thr = max(3, len(rows[peak]) * 0.30)
    chin = peak
    for y in sorted(k for k in rows if k > peak):
        if y - chin > 8:
            break
        if len(rows[y]) < thr:
            break
        chin = y
    fx = rows[peak]
    cx = (min(fx) + max(fx)) // 2
    face = max(chin - peak, 12)
    top = max(ytop, int(peak - face * 2.4))
    half = max(chin - top, 40) * 0.60
    return (int(cx - half), top, int(cx + half), int(chin + half * 0.28))


def emit(im, bg, box, size):
    x0, y0, x1, y1 = box
    x0 = max(0, x0); y0 = max(0, y0)
    crop = im.crop((x0, y0, min(im.width, x1), min(im.height, y1)))
    # 정사각 캔버스에 얹어 비율을 지킨다
    s = max(crop.size)
    sq = Image.new('RGB', (s, s), bg)
    sq.paste(crop, ((s - crop.width) // 2, (s - crop.height) // 2))
    small = sq.resize((size, size), Image.NEAREST)
    q = small.convert('P', palette=Image.ADAPTIVE, colors=14).convert('RGB')
    px = q.load()

    cols = Counter()
    for y in range(size):
        for x in range(size):
            if is_fig(px[x, y], bg, 46):
                cols[px[x, y]] += 1
    order = [c for c, _ in cols.most_common(len(GL))]
    idx = {c: GL[i] for i, c in enumerate(order)}
    rows = []
    for y in range(size):
        r = ''
        for x in range(size):
            c = px[x, y]
            r += idx.get(c, '.') if is_fig(c, bg, 46) else '.'
        rows.append(r)
    pal = {g: '#%02x%02x%02x' % c for c, g in idx.items()}
    return rows, pal


def sample_colors(im, bg, box, hb):
    """머리색은 '얼굴 상자' 안에서만 뽑는다. 인물 상단 밴드로 잡으면 소품 때문에
       밴드가 아래로 밀려 제복 남색이 머리색으로 찍힌다(실제로 9명 중 6명이 그랬다).
       추가로 제복색(#1b2030 근처)과 배경은 후보에서 뺀다."""
    px = im.load()
    UNIFORM = (0x1b, 0x20, 0x30)
    def near(c, t, d=52):
        return abs(c[0]-t[0]) + abs(c[1]-t[1]) + abs(c[2]-t[2]) < d
    hx0, hy0, hx1, hy1 = [int(v) for v in hb]
    hair = Counter()
    # 머리카락은 턱 위에 있다. 상자 아래쪽은 가슴 앞에 든 소품(소화기·구급함)이
    # 들어오는 구역이라 잘라낸다 — 이걸 안 하면 소라가 빨강, 아오이가 흰색으로 찍힌다.
    hy_lim = hy0 + int((hy1 - hy0) * 0.70)
    for y in range(max(0, hy0), min(im.height, hy_lim)):
        for x in range(max(0, hx0), min(im.width, hx1)):
            c = px[x, y]
            if not is_fig(c, bg) or skinlike(c):
                continue
            if near(c, bg, 70) or near(c, UNIFORM):
                continue
            if sum(c) < 90:                 # 눈동자·외곽선 같은 아주 어두운 픽셀 제외
                continue
            # 형광 조끼·스카프(연두)는 머리색이 아니다. 목에 두른 린이 이걸로 찍혔었다.
            # 호타루의 금발(r>g)과 아오이의 하늘색(b 높음)은 이 조건에 안 걸린다.
            if c[1] > 150 and c[0] > 150 and c[2] < 110 and c[1] >= c[0]:
                continue
            hair[c] += 1
    x0, y0, x1, y1 = box
    cloth = Counter()
    for y in range(y0 + int((y1-y0)*0.40), y0 + int((y1-y0)*0.62), 2):
        for x in range(x0, x1, 2):
            c = px[x, y]
            if is_fig(c, bg) and not skinlike(c) and not near(c, UNIFORM) and max(c)-min(c) > 30:
                cloth[c] += 1
    hxc = hair.most_common(1)[0][0] if hair else (140, 120, 130)
    cxc = cloth.most_common(1)[0][0] if cloth else (60, 80, 120)
    return hxc, cxc


def hexs(c):
    return '#%02x%02x%02x' % tuple(c)


def mix(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c)


HAIR_HEX = {                 # cast-scenarios.md 의 설계값
    'rin':    (0xc8, 0x38, 0x3c),   # 진홍
    'hana':   (0x6b, 0x2f, 0x45),   # 자주
    'sora':   (0xcf, 0xc9, 0xc2),   # 은백
    'yui':    (0xd9, 0xa8, 0x60),   # 금발
    'mio':    (0x3a, 0x37, 0x40),   # 흑발
    'nagi':   (0x5a, 0x45, 0x70),   # 보라
    'aoi':    (0x7d, 0xa6, 0xcd),   # 하늘
    'hotaru': (0xf0, 0xc0, 0x5a),   # 노랑
    'shizu':  (0xe8, 0xe4, 0xe6),   # 백발
}

# 옷 색도 표본이 실패하는 경우가 있다. 소라는 가슴에 빨간 소화기를 안고 있어
# 옷 표본이 소화기 빨강으로 찍혔고, 전위인데 지원(빨강) 색을 입어 판 위에서
# 시즈와 구분이 안 됐다. 역할색은 판독성이라 여기만 손으로 박는다.
CLOTH_HEX = {'sora': (0xbc, 0xc2, 0x3a)}

out = {}
for fn, key in KEYS:
    p = os.path.join(SRC, fn + '.png')
    im = Image.open(p).convert('RGB')
    bg = bg_of(im)
    box = figure_box(im, bg)
    hb = head_box(im, bg, box, key)
    rows, pal = emit(im, bg, hb, 32)
    _, cloth = sample_colors(im, bg, box, hb)
    # 머리색은 표본이 아니라 설계값이다. 카드에서 역추출하면 소품·조끼·반사띠에
    # 걸려 매번 다른 한 명이 틀렸다(제복 남색 → 소화기 빨강 → 형광 스카프 → 반사 회색).
    hair = HAIR_HEX[key]
    cloth = CLOTH_HEX.get(key, cloth)
    out[key] = dict(por=rows, porpal=pal,
                    pal={'L': '#12101a', 'S': '#f7d7b4', 's': '#d99a72',
                         'H': hexs(hair), 'h': hexs(mix(hair, .62)), 'G': hexs(mix(hair, 1.28)),
                         'E': '#1a1824', 'W': '#ffffff',
                         'C': hexs(cloth), 'c': hexs(mix(cloth, .65)), 'A': '#f0e6d2'})
    filled = sum(r.count('.') for r in rows)
    print('%-7s 머리 %s  옷 %s  초상 투명률 %d%%' % (key, hexs(hair), hexs(cloth), filled * 100 // (32 * 32)))

io.open('sprites9.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False))
print('\nsprites9.json 기록 · 캐릭터 %d명' % len(out))
