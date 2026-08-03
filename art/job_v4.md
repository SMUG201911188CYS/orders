<task>
Use the imagegen skill DEFAULT built-in image_gen tool. Do NOT use scripts/image_gen.py.
Produce ONE image only, saved to exactly:
  D:/Claude/nan2026/orders/art/concepts/hero/brief_v4.png

=== WHY THIS PASS EXISTS ===
A previous attempt at this scene got the nine characters and their costumes right, but failed
on two things:
  (a) the figures came out 6-7 heads tall. They must be SD / chibi, about 4 heads tall.
  (b) the rendering came out smooth cel-shaded with anti-aliasing. It must be hard pixel art.
Each variant below attacks those two failures with a different technique. Do not blend the
techniques - run each one as specified so we can compare which technique works.

=== THE SCENE (identical for all four) ===
Landscape 1536x1024. Night-shift briefing inside the control room of Signal Post No.3.
Nine young women crowded around a long console desk, all looking DOWN at loose order sheets
laid out on the desk surface. Behind them: a wall of CRT monitors glowing teal, exposed pipes
across the ceiling, a black fogged window. An oil lantern on the desk is the warm light source,
plus one amber desk lamp. Some lean on the desk with both hands, some stand behind looking over
shoulders. Every one of the nine must be visible and identifiable.

=== THE NINE (left to right in the reference strip) ===
 1 crimson-red short messy bob, long glow-yellow scarf, courier satchel
 2 dark plum long hair, heaviest build, dark flame-cloth draped over both shoulders
 3 silver-white short hair, goggles on forehead, hugging a red fire extinguisher
 4 blonde high ponytail, brass monocle, camera lenses hung at the chest
 5 black chin-length hair, sleepy half-lidded eyes, long tripod over one shoulder
 6 dark purple twin tails, rigidly upright, a tall red-and-white striped survey rod
 7 pale blue bob, hugging a white first-aid box with a red cross
 8 golden blonde twin tails, eyes closed in a wide open-mouthed smile, oil lantern
 9 very long white hair past the knees, stack of documents, raised rubber stamp

=== NON-NEGOTIABLE FOR ALL FOUR ===
- All nine present. No tenth character. No swapped props.
- ROLE COSTUME CODING, over the same dark navy #1b2030 uniform:
    1,2,3 : hi-vis YELLOW-GREEN safety vest, grey reflective stripes, TEAL #6cc2cf epaulettes
    4,5,6 : NO vest. Wide BRASS #e0ae4d waist belt, brass-buckled hip pouches
    7,8,9 : NO vest. ROSE #e87b8e vertical piping down the jacket front
- Palette: #05060a darkest, #1b2030 near surfaces, #0f1220 far surfaces,
  TEAL #6cc2cf cold light, AMBER #e0ae4d warm light, ROSE #e87b8e sparingly.
- Young women in fully covered practical workwear. Wholesome, no fanservice.
- NO text, letters, numbers, signage glyphs, watermark, logo or signature anywhere.

=== V4 — EXPLICIT SD VOCABULARY, NO REFERENCE ===
GENERATE MODE. Do NOT pass any input image. Rely only on this description.
Style: Japanese SD / chibi character art, the proportions used for "super-deformed" mascot
sprites - the head is a FULL QUARTER of the total body height, the body is short and stubby,
hands and feet are small and simplified. Think of a 16-bit tactical RPG portrait scene.
Rendering: pixel art with a visible pixel grid, hard aliased edges, flat colour fills, dithered
shadows, absolutely no anti-aliasing and no airbrush gradients.

</task>

<default_follow_through_policy>
가장 합리적인 저위험 해석을 택해 끝까지 진행. 구도·화풍을 되묻지 말 것.
</default_follow_through_policy>

<completeness_contract>
이미지를 지정 경로에 저장한 뒤 끝낸다. 아홉이 다 있는지, 역할 복장 3군이 맞는지, 등신이 몇인지 스스로 확인하고 정직하게 보고한다. 안 됐으면 됐다고 하지 말 것.
</completeness_contract>

<structured_output_contract>
정확히 한 줄: written yes/no | all nine yes/no | costume groups yes/no | heads tall <숫자> | pixel grid yes/no
</structured_output_contract>
