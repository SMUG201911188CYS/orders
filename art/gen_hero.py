# -*- coding: utf-8 -*-
"""타이틀 키 비주얼 = 생성한 신호소 배경 + 기존 캐릭터 컷아웃 아홉.

인물까지 통째로 생성하지 않는 이유: 아홉 얼굴이 전부 다시 그려져 확정한 캐릭터와
어긋난다. 비율을 미오에 맞춰 잠근 작업이 무너진다. 배경만 생성하고, 인물은
편성 화면이 쓰는 것과 같은 원본에서 잘라 세운다 — 화면 어디서 보든 같은 사람이다.

python gen_hero.py [a|b|c]
"""
import io, os, sys, base64
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PLATE = 'concepts/hero/hero_%s.png' % (sys.argv[1] if len(sys.argv) > 1 else 'a')
SRC = 'concepts/v4'
BOX = (150, 80, 980, 1460)          # gen_fullshot.py 와 같은 상자 = 같은 배율
KEYS = ['char_01_rin', 'char_02_hana', 'char_03_sora', 'char_04_yui', 'char_05_mio',
        'char_06_nagi', 'char_07_aoi', 'char_08_hotaru', 'char_09_shizu']

FIG_H   = 330       # 인물 키(px). 배경 1024 기준으로 건물보다 확실히 앞에 서는 크기
BASELINE = 960      # 발이 닿는 y. 자갈 바닥 한가운데
DIM      = 0.82     # 인물을 배경 밝기에 맞춰 살짝 낮춘다. 안 하면 스티커처럼 뜬다


def cutout(im, bg, tol=40):
    im = im.convert('RGBA')
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, _ = px[x, y]
            if abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2]) <= tol:
                px[x, y] = (r, g, b, 0)
    return im


def figure(fn):
    full = Image.open(os.path.join(SRC, fn + '.png')).convert('RGB')
    cut = cutout(full.crop(BOX), full.getpixel((512, 60)))
    bb = cut.getbbox()                       # 인물만 남기고 여백을 턴다
    cut = cut.crop(bb)
    w = max(1, int(round(cut.width * FIG_H / float(cut.height))))
    # 정수배가 아니므로 NEAREST 는 톱니가 심하다. 여기서는 배경에 얹히는 작은 그림이라
    # LANCZOS 로 부드럽게 줄이는 편이 낫다(파일이 아니라 픽셀 그대로 합성한다).
    return cut.resize((w, FIG_H), Image.LANCZOS)


plate = Image.open(PLATE).convert('RGBA')
W, H = plate.size
figs = [figure(k) for k in KEYS]

# 아홉을 가로로 고르게. 폭이 넘치면 조금씩 겹친다 — 줄지어 선 것처럼 보인다.
total = sum(f.width for f in figs)
margin = int(W * 0.035)
span = W - margin * 2
gap = (span - total) / float(len(figs) - 1)      # 음수면 겹침

shadow = Image.new('RGBA', plate.size, (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
x = float(margin)
place = []
for f in figs:
    cx = x + f.width / 2.0
    rw, rh = f.width * 0.42, 9
    sd.ellipse([cx - rw, BASELINE - rh, cx + rw, BASELINE + rh], fill=(0, 0, 0, 150))
    place.append((f, int(round(x))))
    x += f.width + gap
plate.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(7)))

for f, px_ in place:
    if DIM != 1.0:
        f = Image.merge('RGBA', [c.point(lambda v: int(v * DIM)) for c in f.split()[:3]]
                        + [f.split()[3]])
    plate.alpha_composite(f, (px_, BASELINE - f.height))

out = plate.convert('RGB')
out.save('concepts/hero/hero_composed.png')

# 화면에는 640px 로 뜬다. 정수배로 줄여야 픽셀 경계가 안 뭉갠다(gen_fullshot.py 와 같은 이유).
small = out.resize((W // 2, H // 2), Image.NEAREST)
buf = io.BytesIO()
small.save(buf, 'WEBP', quality=78, method=6)
raw = buf.getvalue()
io.open('hero.txt', 'w', encoding='utf-8').write(
    'data:image/webp;base64,' + base64.b64encode(raw).decode('ascii'))
print('%dx%d  %.0f KB  (base64 %.0f KB)' % (small.width, small.height,
                                            len(raw) / 1024.0, len(raw) * 4 / 3 / 1024.0))
