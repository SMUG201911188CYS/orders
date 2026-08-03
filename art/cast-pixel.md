<task>
Generate NINE character cards for a game roster, using the imagegen skill's DEFAULT built-in
`image_gen` tool. Do NOT use scripts/image_gen.py (that CLI fallback needs an OPENAI_API_KEY
we do not have).

STYLE REFERENCE — read this existing approved file first and match it closely:
  D:/Claude/nan2026/orders/art/concepts/style_A_pixel.png
That file is the locked art direction. Every one of the nine must look like it came from the
same sprite sheet as that reference.

LOCKED ACROSS ALL NINE (do not vary):
  - TRUE PIXEL ART. Chunky visible pixel grid, hard aliased edges, NO anti-aliasing,
    NO soft gradients, NO airbrush. Reads like a high-resolution SNES-era sprite
    scaled up with nearest-neighbor.
  - SD / super-deformed chibi proportions, about 2.5 heads tall.
  - Standing, facing the viewer, full body visible inside the frame.
  - Vertical trading-card composition, 2:3 aspect, character centered,
    generous empty margin at top and bottom.
  - Flat dark background field #0f1220. Not a scene. No props on the floor, no shadows cast on walls.
  - A thin 1px brass (#e0ae4d) border rectangle just inside the image edge.
  - NO text, NO letters, NO numbers, NO watermark, NO logo, NO signature anywhere.
  - Every character wears the same base uniform: a dark navy (#1b2030) night-shift work uniform.
    They must read as one squad. Only hair, accent trim, and the held prop differ.

PALETTE (the game's actual palette — stay inside it):
  background #0f1220 · uniform #1b2030 · skin/ink #eceae3
  teal #6cc2cf · rose #e87b8e · brass #e0ae4d

ROLE ACCENT — the trim colour on the vest/uniform encodes the role. This must be obvious:
  VANGUARD  -> teal  #6cc2cf trim
  MARKSMAN  -> brass #e0ae4d trim
  SUPPORT   -> rose  #e87b8e trim

THE NINE. Hair colour and silhouette are the primary way a player tells them apart,
so keep each one strongly distinct.

VANGUARD (teal trim):
1) D:/Claude/nan2026/orders/art/concepts/char_01_rin.png
   Rin. Short messy crimson-red bob with one stray ahoge strand. Hi-vis yellow safety vest with
   teal trim. Courier satchel across the body. Light on her feet, mid-stride lean, confident grin.
2) D:/Claude/nan2026/orders/art/concepts/char_02_hana.png
   Hana. Long straight deep-teal hair past the shoulders. Bulky quilted work jumper with teal trim,
   thick flame-resistant gloves. Planted wide stance, arms crossed, calm unbothered face.
3) D:/Claude/nan2026/orders/art/concepts/char_03_sora.png
   Sora. Silver-white short crop, safety goggles pushed up on the forehead. Teal-trimmed vest.
   Holding a red fire extinguisher braced at the hip like a battering tool. Smirking, shoulders squared.

MARKSMAN (brass trim):
4) D:/Claude/nan2026/orders/art/concepts/char_04_yui.png
   Yui. Bright blonde high ponytail. Brass-trimmed vest. A brass telescopic monocular goggle over
   one eye, clipboard tucked under the other arm. Alert, looking slightly off into the distance.
5) D:/Claude/nan2026/orders/art/concepts/char_05_mio.png
   Mio. Straight jet-black chin-length bob, blunt fringe. Brass-trimmed vest. Large over-ear
   headphones around the neck, a folded camera tripod carried over one shoulder. Expressionless, tired eyes.
6) D:/Claude/nan2026/orders/art/concepts/char_06_nagi.png
   Nagi. Violet twin tails. Brass-trimmed vest. Holding a small handheld line-laser emitting one
   thin straight teal beam to the side, a surveying rod strapped to her back. Focused, one eye narrowed.

SUPPORT (rose trim):
7) D:/Claude/nan2026/orders/art/concepts/char_07_aoi.png
   Aoi. Light sky-blue bob with a small clip. Rose-trimmed vest. Carrying a white first-aid case
   in both hands, a small flashlight clipped to the chest. Worried, earnest expression.
8) D:/Claude/nan2026/orders/art/concepts/char_08_hotaru.png
   Hotaru. Yellow hair in two low pigtails. Rose-trimmed vest. Holding up a hand lantern that glows
   warm brass, a boxy portable generator backpack on her back. Cheerful, eyes shut in a smile.
9) D:/Claude/nan2026/orders/art/concepts/char_09_shizu.png
   Shizu. Very long straight white hair. Rose-trimmed vest. A thick stack of documents cradled in one
   arm, a large rubber stamp raised in the other hand. Deadpan, half-lidded stare.

Verify all nine PNG files exist on disk after writing.
</task>

<default_follow_through_policy>
Choose the most reasonable low-risk interpretation and finish all nine. Do not ask questions.
If the built-in image_gen tool is unavailable, do NOT fall back to the CLI — stop and report why.
</default_follow_through_policy>

<completeness_contract>
All nine files must be written. Do not stop after the first few. If one generation fails,
retry that one once, then continue with the rest. Report any that never succeeded.
</completeness_contract>

<structured_output_contract>
Answer in exactly this form, nothing else:
1. RESULT: OK or PARTIAL or FAILED
2. FILES: one line per file — filename, byte size, exists yes/no
3. TOOL: which tool produced them
4. NOTES: at most two lines
</structured_output_contract>
