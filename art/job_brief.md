<task>
Use the imagegen skill's DEFAULT built-in `image_gen` tool. Do NOT use scripts/image_gen.py.
Produce FOUR images. Each uses a DIFFERENT technique, described per variant below.
All four depict THE SAME SCENE (see "THE SCENE"). Save to exactly:

  V1 -> D:/Claude/nan2026/orders/art/concepts/hero/brief_v1.png
  V2 -> D:/Claude/nan2026/orders/art/concepts/hero/brief_v2.png
  V3 -> D:/Claude/nan2026/orders/art/concepts/hero/brief_v3.png
  V4 -> D:/Claude/nan2026/orders/art/concepts/hero/brief_v4.png

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

=== V1 — EDIT THE ROOM PLATE ===
EDIT MODE. Image 1 (EDIT TARGET), passed as an ACTUAL INPUT IMAGE:
  D:/Claude/nan2026/orders/art/concepts/hero/hero_b.png
That file is an empty version of this exact room, already drawn in the correct pixel-art style.
PRESERVE its rendering exactly - the chunky pixel grid, hard aliased edges, the palette, the
console, the CRTs, the pipes. Your only job is to ADD the nine characters around the desk and
put order sheets on it. Match the new figures to the existing pixel grid: same pixel size, same
hard edges, no anti-aliasing, no soft shading. The characters must look like they were drawn by
the same hand at the same resolution as the room.
Also pass as a second input image, for character likeness only:
  D:/Claude/nan2026/orders/art/_ref9.png
Figures about 4 heads tall.

=== V2 — LOW-RESOLUTION CANVAS CONSTRAINT ===
GENERATE MODE (no edit target). Pass as input image, for likeness only:
  D:/Claude/nan2026/orders/art/_ref9.png
Render this as if it were a single screen from a 16-bit console game: imagine the artwork is
drawn on a canvas only 384 x 256 pixels and then scaled up 4x with nearest-neighbour. Individual
pixels must be visible as hard squares. No diagonal line may be smooth - every diagonal is a
visible staircase of square pixels. Shading is done with dithering patterns of two flat colours,
never with a gradient. At this tiny canvas size a face is only about 10 pixels wide, so the
characters MUST be SD / chibi with big heads, about 4 heads tall, or they will not read.

=== V3 — EDIT THE CHARACTER STRIP ===
EDIT MODE. Image 1 (EDIT TARGET), passed as an ACTUAL INPUT IMAGE:
  D:/Claude/nan2026/orders/art/_ref9.png
That strip contains the nine characters standing side by side at the EXACT proportions and the
EXACT rendering we want. Take those nine figures and REARRANGE them into the briefing scene.
PRESERVE from the strip: each figure's head-to-body ratio, body build, face, hair, costume and
prop, and the rendering style. CHANGE: their poses (now leaning over a desk and looking down),
the camera framing, and the background (now the control room described above). It is fine to
crop some figures at the waist where the desk hides them.
The output is landscape 1536x1024, NOT a strip.

=== V4 — EXPLICIT SD VOCABULARY, NO REFERENCE ===
GENERATE MODE. Do NOT pass any input image. Rely only on this description.
Style: Japanese SD / chibi character art, the proportions used for "super-deformed" mascot
sprites - the head is a FULL QUARTER of the total body height, the body is short and stubby,
hands and feet are small and simplified. Think of a 16-bit tactical RPG portrait scene.
Rendering: pixel art with a visible pixel grid, hard aliased edges, flat colour fills, dithered
shadows, absolutely no anti-aliasing and no airbrush gradients.
</task>

<default_follow_through_policy>
Pick the most reasonable low-risk interpretation and carry it through. Do not stop to ask
questions about composition or style.
</default_follow_through_policy>

<completeness_contract>
All four images must be generated and saved to the exact paths above before you finish.
For each one, after saving, check: are all nine present, are the three costume groups correct,
and do the figures look about 4 heads tall. Report honestly - do NOT claim a variant succeeded
on proportions if it did not. If a save fails, retry that variant once.
</completeness_contract>

<structured_output_contract>
Answer with exactly one line per variant, in this form:
  V<n> | written: yes/no | all nine: yes/no | costume groups correct: yes/no |
  heads tall (your honest estimate): <number> | pixel grid visible: yes/no
No other prose.
</structured_output_contract>
