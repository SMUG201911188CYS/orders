# -*- coding: utf-8 -*-
"""타이틀 키 비주얼 = 생성한 브리핑 그림(brief_v2)을 잘라 줄여 데이터 URI 로.

brief_v2 를 고른 이유는 art/job_v2.md 에 있다. 요약하면, 화풍을 형용사로 요구하는 대신
"384x256 캔버스를 4배 확대한 화면"이라는 불가능한 조건으로 못박으니 SD 비율과 픽셀 격자가
같이 따라왔다. 같은 장면을 네 기법으로 뽑아 비교한 결과다(brief_v1~v4).

자르기는 세로만 한다. 아홉이 가로 폭을 거의 다 쓰고 있어서 가로로 자르면 양 끝의
린과 시즈가 잘린다. 크기는 정확히 1/2 + NEAREST — 비정수 배율로 줄이면 픽셀 경계가
그라데이션이 되어 화질도 잃고 WebP 용량도 되레 늘어난다(gen_fullshot.py 와 같은 이유).
"""
import io, base64
from PIL import Image

SRC = 'concepts/hero/brief_v2.png'
BOX = (0, 120, 1536, 984)          # 천장과 아래쪽 콘솔을 덜어낸다. 짝수라야 1/2 이 떨어진다

im = Image.open(SRC).convert('RGB').crop(BOX)
small = im.resize((im.width // 2, im.height // 2), Image.NEAREST)
buf = io.BytesIO()
small.save(buf, 'WEBP', quality=80, method=6)
raw = buf.getvalue()
io.open('hero.txt', 'w', encoding='utf-8').write(
    'data:image/webp;base64,' + base64.b64encode(raw).decode('ascii'))
print('%dx%d  %.0f KB  (base64 %.0f KB)'
      % (small.width, small.height, len(raw) / 1024.0, len(raw) * 4 / 3 / 1024.0))
