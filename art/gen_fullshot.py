# -*- coding: utf-8 -*-
"""v4 카드 아트 → 편성 화면에 띄울 전신 샷(데이터 URI).

제약은 하나다. 게임은 링크 하나로 돌아야 하므로 외부 파일을 만들 수 없다.
원본은 장당 1.3~1.8MB 라 그대로는 못 넣는다. 배경을 지우고 인물만 남겨
축소·WebP 로 구운 뒤 base64 로 박는다.

배경을 지우는 이유는 용량이 아니라 화면이다. 카드의 회색 배경을 그대로 두면
어두운 패널 위에 밝은 사각형이 뜬다. 인물만 남기면 패널에 그대로 앉는다.
"""
import io, os, sys, json, base64
from PIL import Image

SRC = 'concepts/v4'
KEYS = [('char_01_rin', 'rin'), ('char_02_hana', 'hana'), ('char_03_sora', 'sora'),
        ('char_04_yui', 'yui'), ('char_05_mio', 'mio'), ('char_06_nagi', 'nagi'),
        ('char_07_aoi', 'aoi'), ('char_08_hotaru', 'hotaru'), ('char_09_shizu', 'shizu')]

# 축소는 반드시 정수배 + NEAREST 로 한다.
#
# 처음엔 260px LANCZOS 로 구웠는데 두 가지가 동시에 나빴다. 이 아트는 픽셀 화풍이라
# 색 경계가 단단한데, LANCZOS 로 줄이면 그 경계가 전부 그라데이션이 된다.
# 선이 뭉개져서 화질을 잃고, 뭉개진 그라데이션은 WebP 가 압축을 못 해서 용량까지 더 냈다.
# (같은 화면 크기로 비교: 260 LANCZOS q70 = 30.9KB/장, 415 NEAREST q80 = 20.9KB/장.
#  해상도가 1.6배인 쪽이 32% 가볍고 눈에 띄게 선명하다.)
#
# 830 은 아래 BOX 의 실폭이다. 그 절반이라 픽셀이 정확히 2:1 로 떨어진다.
DIV = 2
RESAMPLE = Image.NEAREST
QUALITY = 80

# 카드에는 얇은 금색 테두리가 있다(12~16px). 그 안쪽만 쓴다 — 테두리째 넣으면
# 패널 위에 카드가 한 장 더 얹힌 것처럼 보인다.
#
# 잘라내는 상자는 아홉 장 공통이다. 인물마다 딱 맞게 자르면 화면에서 키가 제각각이 되고,
# 비율을 미오에 맞춰 통일한 작업이 통째로 무의미해진다. 아홉의 인물 상자 합집합에
# 여유를 준 값이며(린의 스카프가 오른쪽 끝, 호타루의 랜턴이 위쪽 끝을 정한다),
# 모두 같은 배율로 줄어들므로 화면에서도 카드에서와 같은 키 차이가 남는다.
BOX = (150, 80, 980, 1460)


def bg_of(im):
    px = im.load()
    m = int(min(im.size) * 0.03)
    return px[m + 2, m + 2]


def cutout(im, bg, tol=40):
    """배경색과 가까운 픽셀을 투명으로. 원본이 단색 배경이라 이 정도로 충분하다.
       가장자리를 부드럽게 만들지 않는 건 픽셀 화풍이라 계단이 오히려 맞기 때문."""
    im = im.convert('RGBA')
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            if abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2]) <= tol:
                px[x, y] = (r, g, b, 0)
    return im


out, total = {}, 0
for fn, key in KEYS:
    full = Image.open(os.path.join(SRC, fn + '.png')).convert('RGB')
    bg = full.getpixel((512, 60))          # 테두리 안쪽 배경
    cut = cutout(full.crop(BOX), bg)
    w, h = cut.size
    small = cut.resize((w // DIV, h // DIV), RESAMPLE)
    buf = io.BytesIO()
    small.save(buf, 'WEBP', quality=QUALITY, method=6)
    raw = buf.getvalue()
    total += len(raw)
    out[key] = {'u': 'data:image/webp;base64,' + base64.b64encode(raw).decode('ascii'),
                'w': small.width, 'h': small.height}
    print('%-7s %dx%d  %5.1f KB' % (key, small.width, small.height, len(raw) / 1024.0))

io.open('fullshot.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False))
print('\n합계 %.0f KB · base64 후 약 %.0f KB' % (total / 1024.0, total * 4 / 3 / 1024.0))
