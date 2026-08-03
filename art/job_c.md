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
CARD A -> D:/Claude/nan2026/orders/art/concepts/v4/char_05_mio.png
  Mio, MARKSMAN. Concept: PERPETUALLY SLEEPY — three years of night shifts, navigates by sound.
  Keep her existing design and pose largely as-is; this is a light touch-up only.
  POSE: same slouched stand, back slightly rounded, one hand in a pocket.
  CARRIES: folded camera tripod resting across one shoulder as a long diagonal.
  UNIFORM WORN AS: collar turned up to cover the neck.
  ACCESSORIES: large over-ear headphones around the neck; a small energy jelly pouch held in
  her mouth by the corner.
  FACE: jet-black chin-length bob with blunt fringe. Heavy half-lidded eyes, visible dark
  circles beneath them, smallest highlights of the nine, blank expression.

CARD B -> D:/Claude/nan2026/orders/art/concepts/v4/char_06_nagi.png
  Nagi, MARKSMAN. Concept: PERFECTIONIST — sees the world as straight lines and angles.
  POSE: rigidly upright, heels together, arms pressed straight down against her sides.
  She must be the ONLY one of the nine who is perfectly vertical and symmetrical — no tilt,
  no weight shift, no lean.
  CARRIES: a surveying rod strapped to her back forming an exact vertical line.
  UNIFORM WORN AS: pressed without a single wrinkle; the brass belt buckle exactly centred.
  ACCESSORIES: a protractor on a cord at her neck; several pens lined up evenly in a sleeve pocket.
  FACE: violet twin tails. Sharp upturned eyes, dead-straight eyebrows, one eye slightly narrowed.
  Do NOT include a laser beam or any glow extending outside the figure.

<structured_output_contract>
Answer in exactly this form:
1. MODE: tool and mode used, and whether Image 1 was passed as an input image
2. FILES: one line per card — path, byte size, exists yes/no
3. SILHOUETTE: one line per card — what makes its silhouette distinct
</structured_output_contract>
