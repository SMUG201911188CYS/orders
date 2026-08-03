<task>
Generate FOUR concept-art style directions for a game character card, using the imagegen skill's
DEFAULT built-in `image_gen` tool. Do NOT use scripts/image_gen.py (CLI fallback needs an
OPENAI_API_KEY we do not have).

Same character in all four, so only the ART DIRECTION differs and the comparison is fair.

CHARACTER (identical across all four):
  Name: Rin. A night-shift signal-station worker girl.
  SD / super-deformed chibi proportions, roughly 2.5 heads tall.
  Short messy crimson-red bob hair with one stray ahoge strand.
  Hi-vis yellow safety vest with reflective stripes, worn over a dark navy work uniform.
  A courier satchel slung across the body.
  Standing, facing the viewer, full body visible, confident small grin.

COMPOSITION (identical across all four):
  Vertical trading-card composition, 2:3 aspect.
  Character centered, full body inside frame, generous margin at top and bottom.
  Background is a flat dark field, NOT a detailed scene.
  No text, no letters, no numbers, no watermark, no logo anywhere in the image.
  No frame decoration beyond what each style below specifies.

PALETTE (identical across all four) — this is the game's actual palette, keep to it:
  background  #0f1220
  panel       #1b2030
  ink         #eceae3
  ally accent #6cc2cf  (teal)
  foe accent  #e87b8e  (rose)
  gold accent #e0ae4d  (brass)

Write these four files:

1. D:/Claude/nan2026/orders/art/concepts/style_A_pixel.png
   PIXEL ART. True chunky pixel grid, hard aliased edges, no anti-aliasing, no gradients.
   Limited palette drawn from the list above. Reads like a high-resolution SNES-era sprite
   scaled up with nearest-neighbor. Thin 1px brass border.

2. D:/Claude/nan2026/orders/art/concepts/style_B_cel.png
   CLEAN CEL ANIME. Crisp uniform lineart, flat two-tone cel shading, no gradients,
   modern anime key-art finish. Thin brass border.

3. D:/Claude/nan2026/orders/art/concepts/style_C_nightglow.png
   NIGHT GLOW. Same cel base but lit almost entirely by practical light sources at night:
   the hi-vis vest stripes and a lantern glow rim-light the figure against near-black.
   Strong value contrast, teal and brass light, deep shadow. Moody, cinematic.

4. D:/Claude/nan2026/orders/art/concepts/style_D_paper.png
   PAPER DOCUMENT. Looks silkscreen/risograph printed on an old duty-roster form.
   Strictly limited to 3 inks: brass, teal, and near-black on aged off-white paper.
   Visible halftone dot texture and slight ink misregistration offset.
   Rubber-stamp and punched-hole motifs at the edges. Deliberately flat and graphic.

Verify each of the four PNG files exists on disk after writing.
</task>

<default_follow_through_policy>
Choose the most reasonable low-risk interpretation and finish all four. Do not ask questions.
If the built-in image_gen tool is unavailable, do NOT fall back to the CLI — stop and report why.
</default_follow_through_policy>

<completeness_contract>
All four files must be written. Do not stop after the first plausible result.
If one generation fails, retry it once, then report which one failed and why.
</completeness_contract>

<structured_output_contract>
Answer in exactly this form, nothing else:
1. RESULT: OK or PARTIAL or FAILED
2. FILES: one line per file — path, byte size, exists yes/no
3. TOOL: which tool produced them
4. NOTES: at most two lines
</structured_output_contract>
