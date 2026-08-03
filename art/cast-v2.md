<task>
Regenerate the NINE character cards with a corrected role-coding scheme, using the imagegen
skill's DEFAULT built-in `image_gen` tool. Do NOT use scripts/image_gen.py (the CLI fallback
needs an OPENAI_API_KEY we do not have).

STYLE REFERENCE — read these two existing approved files first:
  D:/Claude/nan2026/orders/art/concepts/style_A_pixel.png   (locked art direction)
  D:/Claude/nan2026/orders/art/concepts/char_08_hotaru.png  (correct accent treatment: no vest,
                                                             coloured piping on a navy jacket)
Match that pixel art direction exactly.

WHY THIS IS A REGENERATION — read carefully, this is the whole point of the pass:
In the previous attempt the role accent colour failed. A hi-vis YELLOW vest was put on several
characters, and yellow is visually identical to the brass accent, so the marksman role accent was
swallowed by the vest. Teal sleeve stripes also leaked onto a marksman. Fix it by coding role with
BOTH a colour AND a distinct garment shape, and by making the vest exclusive to one role.

ROLE CODING — this is now the strictest requirement in the whole task:

  VANGUARD — the ONLY role that wears a vest.
    * Hi-vis safety vest with reflective grey stripes, worn over the navy uniform.
    * Plus TEAL (#6cc2cf) shoulder epaulettes on BOTH shoulders — short rectangular teal tabs.
    * No brass and no rose anywhere on the outfit.

  MARKSMAN — NO VEST AT ALL. Nothing hi-vis, nothing yellow-green, on the body.
    * A wide BRASS (#e0ae4d) belt at the waist with two brass-buckled side pouches on the hips.
    * A small brass collar tab at the throat.
    * No teal and no rose anywhere on the outfit. No shoulder epaulettes.

  SUPPORT — NO VEST AT ALL.
    * ROSE (#e87b8e) vertical piping running down both sides of the navy jacket front,
      plus rose-edged chest pockets. Exactly like the hotaru reference file.
    * No teal and no brass anywhere on the outfit. No belt, no epaulettes.

So a player can tell the role three ways at once: vest / belt / piping, and teal / brass / rose.

LOCKED ACROSS ALL NINE (do not vary):
  - TRUE PIXEL ART. Chunky visible pixel grid, hard aliased edges, NO anti-aliasing,
    NO soft gradients. High-resolution SNES-era sprite scaled with nearest-neighbor.
  - SD / super-deformed chibi proportions, about 2.5 heads tall.
  - Standing, facing viewer, full body inside frame.
  - Vertical card composition, 2:3, character centered, generous margin top and bottom.
  - Flat dark background #0f1220. Not a scene.
  - Thin 1px brass border rectangle just inside the image edge.
  - NO text, NO letters, NO numbers, NO watermark, NO logo, NO signature.
  - Base garment is the same dark navy (#1b2030) night-shift uniform for everyone,
    so they read as one squad.

PALETTE: background #0f1220 · uniform #1b2030 · skin/ink #eceae3 ·
         teal #6cc2cf · rose #e87b8e · brass #e0ae4d

THE NINE — hair and prop are how a player tells individuals apart, keep them strongly distinct.

VANGUARD (hi-vis vest + teal epaulettes):
1) D:/Claude/nan2026/orders/art/concepts/v2/char_01_rin.png
   Rin. Short messy crimson-red bob with one stray ahoge. Courier satchel across the body.
   Mid-stride lean, light on her feet, confident grin.
2) D:/Claude/nan2026/orders/art/concepts/v2/char_02_hana.png
   Hana. Long straight DARK NAVY-INDIGO hair past the shoulders — deliberately NOT teal, so the
   teal epaulettes stay readable against it. Thick flame-resistant gloves.
   Planted wide stance, arms crossed, calm unbothered face.
3) D:/Claude/nan2026/orders/art/concepts/v2/char_03_sora.png
   Sora. Silver-white short crop, safety goggles pushed up on the forehead. Holding a red fire
   extinguisher braced at the hip. Smirking, shoulders squared.

MARKSMAN (no vest · brass belt + hip pouches):
4) D:/Claude/nan2026/orders/art/concepts/v2/char_04_yui.png
   Yui. Warm honey-blonde high ponytail. A brass telescopic monocular goggle over one eye,
   clipboard tucked under the other arm. Alert, looking off into the distance.
5) D:/Claude/nan2026/orders/art/concepts/v2/char_05_mio.png
   Mio. Straight jet-black chin-length bob with a blunt fringe. Large over-ear headphones around
   the neck, a folded camera tripod over one shoulder. Expressionless, tired eyes.
6) D:/Claude/nan2026/orders/art/concepts/v2/char_06_nagi.png
   Nagi. Violet twin tails. Holding a small handheld line-laser emitting one thin straight teal
   beam to the side, a surveying rod strapped to her back. Focused, one eye narrowed.
   (The teal beam is light from her tool, not garment trim — her outfit stays brass-only.)

SUPPORT (no vest · rose vertical piping):
7) D:/Claude/nan2026/orders/art/concepts/v2/char_07_aoi.png
   Aoi. Light sky-blue bob with a small hair clip. Carrying a white first-aid case in both hands,
   a small flashlight clipped to the chest. Worried, earnest expression.
8) D:/Claude/nan2026/orders/art/concepts/v2/char_08_hotaru.png
   Hotaru. Yellow hair in two low pigtails. Holding up a hand lantern glowing warm brass,
   a boxy portable generator backpack. Cheerful, eyes shut in a smile.
9) D:/Claude/nan2026/orders/art/concepts/v2/char_09_shizu.png
   Shizu. Very long straight white hair. A thick stack of documents cradled in one arm,
   a large rubber stamp raised in the other hand. Deadpan, half-lidded stare.

Create the v2 directory if needed. Verify all nine PNG files exist on disk after writing.
</task>

<default_follow_through_policy>
Choose the most reasonable low-risk interpretation and finish all nine. Do not ask questions.
If the built-in image_gen tool is unavailable, do NOT fall back to the CLI — stop and report why.
</default_follow_through_policy>

<completeness_contract>
All nine files must be written. If one fails, retry it once, then continue with the rest and
report which never succeeded. Before finishing, re-check each image against the ROLE CODING rules
above — a marksman or support character wearing a hi-vis vest is a failure and must be redone.
</completeness_contract>

<structured_output_contract>
Answer in exactly this form, nothing else:
1. RESULT: OK or PARTIAL or FAILED
2. FILES: one line per file — filename, byte size, exists yes/no
3. ROLE CHECK: one line per file — role, and whether vest/belt/piping matches the rule
4. NOTES: at most two lines
</structured_output_contract>
