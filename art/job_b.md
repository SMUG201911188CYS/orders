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
CARD A -> D:/Claude/nan2026/orders/art/concepts/v4/char_03_sora.png
  Sora, VANGUARD. Concept: DOJIKKO — highly competent, yet keeps tripping.
  POSE: caught in the instant of losing her balance. Upper body pitched forward, one foot
  slightly lifted off the ground, the other braced. Unstable, not a steady stand.
  CARRIES: a red fire extinguisher hugged against her chest with both arms, which is what
  drags her centre of mass forward.
  UNIFORM WORN AS: the hi-vis vest has slipped off one shoulder; one bootlace is undone.
  ACCESSORIES: safety goggles pushed up on her forehead; several plasters on her arms and cheek.
  FACE: short silver-white hair, soft and rounded with wispy strands. Big eyes whose focus is
  very slightly misaligned, one brow raised higher than the other, sheepish embarrassed smile.

CARD B -> D:/Claude/nan2026/orders/art/concepts/v4/char_04_yui.png
  Yui, MARKSMAN. Concept: THE OBSERVER — trusts twenty years of records over her own eyes.
  POSE: body squared to the viewer but head turned sharply to the side, sighting something far
  away. Still and attentive.
  CARRIES: nothing in her hands; both hands rest near the belt.
  UNIFORM WORN AS: buttoned neatly; record cards fanned out and tucked along the brass belt.
  ACCESSORIES: a brass telescopic monocular over one eye; SEVERAL spare lenses on cords hanging
  around her neck and chest, making her upper silhouette lumpy and cluttered.
  FACE: warm honey-blonde high ponytail. The monocular eye looks magnified by the lens while
  the other is narrowed. Neutral, focused.

<structured_output_contract>
Answer in exactly this form:
1. MODE: tool and mode used, and whether Image 1 was passed as an input image
2. FILES: one line per card — path, byte size, exists yes/no
3. SILHOUETTE: one line per card — what makes its silhouette distinct
</structured_output_contract>
