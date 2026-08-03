<task>
Use the imagegen skill's DEFAULT built-in `image_gen` tool in EDIT mode for each card below.
Do NOT use scripts/image_gen.py. Issue one edit call per card.

For EVERY card, Image 1 (EDIT TARGET) is the same file, passed as an ACTUAL INPUT IMAGE
(not merely read):
  D:/Claude/nan2026/orders/art/concepts/v4/char_06_nagi.png

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
CARD A -> D:/Claude/nan2026/orders/art/concepts/v4/char_06_nagi.png
  Nagi, MARKSMAN. Concept: PERFECTIONIST — she reads the world as straight lines and angles.

  THIS IS A NARROW FIX. Image 1 is her own card and it is almost right.
  Change ONE thing and leave the rest alone.

  THE PROBLEM: a surveying rod is strapped to her back, so all that shows is a short stick
  poking straight up above her head. It reads as an unidentifiable line, not a tool.

  THE FIX: take the rod off her back and put it in her hand.
    - She grips it in one hand at about chest height.
    - The rod stands perfectly VERTICAL beside her, its base resting on the ground next to her
      foot, its top ending a little above her head — like a surveyor planting a staff.
    - Make it clearly a surveying rod: a tall slim pole in alternating RED and WHITE bands with
      small black graduation marks.
    - Nothing at all should remain above her head. Remove the stub of rod behind her hair.
    - Her other arm stays straight down at her side, exactly as it is now.

  PRESERVE EVERYTHING ELSE FROM IMAGE 1 EXACTLY:
    - identical body proportions, figure height, feet position and framing
    - the perfectly upright, symmetrical stance with heels together — she must remain the only
      member of the cast with zero tilt and zero weight shift
    - violet twin tails, the same face, sharp eyes, dead-straight eyebrows, blank expression
    - the brass protractor on a cord at her neck, the row of evenly aligned pens in the chest
      pocket, the brass waist belt, brass-buckled hip pouches and brass collar tab
    - the crease-free navy uniform, the pixel-art rendering, the flat #0f1220 background and
      the thin brass border

  Do NOT add a laser beam, glow, or anything that extends outside the figure toward the frame edge.
  NO text, letters, numbers, watermark or signature.
  Overwrite the file at the output path — that is intended.

<structured_output_contract>
Answer in exactly this form:
1. MODE: tool and mode used, and whether Image 1 was passed as an input image
2. FILES: one line per card — path, byte size, exists yes/no
3. SILHOUETTE: one line per card — what makes its silhouette distinct
</structured_output_contract>
