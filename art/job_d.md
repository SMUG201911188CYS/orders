<task>
Use the imagegen skill's DEFAULT built-in `image_gen` tool in EDIT mode for each card below.
Do NOT use scripts/image_gen.py. Issue one edit call per card.

For EVERY card, Image 1 (EDIT TARGET) is the same file, passed as an ACTUAL INPUT IMAGE
(not merely read):
  D:/Claude/nan2026/orders/art/concepts/v3-uniform/char_05_mio.png

=== WHY WE EDIT INSTEAD OF GENERATE ===
Text-only attempts produced figures ranging from 1.8 to 3.8 heads tall. Editing from this
skeleton is what finally locked the set. Keep that lock.

PRESERVE EXACTLY from Image 1:
  - body proportions and head-to-body ratio (about 4 heads tall)
  - the figure's height within the frame, and where the feet sit (the baseline)
  - card framing, the thin brass border, the flat #0f1220 background
  - pixel-art rendering: chunky pixel grid, hard aliased edges, no anti-aliasing, no gradients
  - dark navy #1b2030 work uniform as the base garment
  - a young woman: rounded jaw, small chin, large eyes, thin softly-arched brows,
    narrow sloping shoulders. Wholesome, fully covered practical workwear, no fanservice.

=== WHAT MUST CHANGE — THIS IS THE POINT OF THIS PASS ===
The previous set failed because all nine looked like the same person in different wigs:
identical neutral standing pose, identical face, identical expression.
Each card below now has a written character concept. Express it through the WHOLE figure:
  1. POSE and body line first — this is the strongest differentiator
  2. what she carries and how she holds it
  3. how the uniform is worn differently (open, draped, rolled, buttoned up)
  4. accessories
  5. expression and eyes last
The pose may depart substantially from Mio's — that is expected and wanted.
Only the proportions, figure height, baseline, framing and rendering stay locked.

Goal: if all nine were reduced to black silhouettes, each would still be identifiable.

=== ROLE CODING (validated — keep) ===
  VANGUARD — the ONLY role with a vest. Bright hi-vis YELLOW-GREEN safety vest with reflective
    grey stripes over the navy uniform, plus TEAL (#6cc2cf) shoulder epaulettes on both
    shoulders. No brass anywhere.
  MARKSMAN — NO VEST, nothing hi-vis. Wide BRASS (#e0ae4d) waist belt, brass-buckled hip
    pouches, small brass collar tab. No teal, no rose.
  SUPPORT — NO VEST. ROSE (#e87b8e) vertical piping down both sides of the navy jacket front
    and rose-edged chest pockets. No brass, no teal, no belt.

Remove Mio's own props (over-ear headphones, camera tripod) from every card except her own.
NO text, letters, numbers, watermark, logo or signature anywhere.
Overwrite the existing file at each output path — that is intended.

=== CARDS ===
CARD A -> D:/Claude/nan2026/orders/art/concepts/v4/char_07_aoi.png
  Aoi, SUPPORT. Concept: CRYBABY — terrified of seeing people hurt, yet always runs in first.
  POSE: shoulders curled inward, knees turned slightly toward each other, making her upper body
  read as a small tight bundle.
  CARRIES: a white first-aid case clutched tightly against her chest with both arms.
  UNIFORM WORN AS: sleeves too long, falling over the backs of her hands.
  ACCESSORIES: several plasters pre-stuck on her shoulder ready for use; a bandage wrapped
  around one hand; a small flashlight clipped to her chest.
  FACE: light sky-blue bob with a small hair clip. Large watery eyes brimming with tears,
  reddened rims, downturned outer corners, lips pressed together.

CARD B -> D:/Claude/nan2026/orders/art/concepts/v4/char_08_hotaru.png
  Hotaru, SUPPORT. Concept: AIRHEAD — keeps every light on, always short on fuel.
  POSE: one arm thrust HIGH above her head holding a lantern, so the arm breaks out of the
  normal silhouette. Upper body leaning back, up on her toes.
  CARRIES: a hand lantern glowing warm brass, raised overhead.
  UNIFORM WORN AS: a string of tiny bulbs wound over the rose piping.
  ACCESSORIES: a boxy portable generator backpack; a small bulb pinned in her hair;
  a little bell dangling from the pack.
  FACE: yellow hair in two low pigtails. Eyes shut in happy arcs, blush on both cheeks,
  wide open laughing mouth.

<structured_output_contract>
Answer in exactly this form:
1. MODE: tool and mode used, and whether Image 1 was passed as an input image
2. FILES: one line per card — path, byte size, exists yes/no
3. SILHOUETTE: one line per card — what makes its silhouette distinct
</structured_output_contract>
