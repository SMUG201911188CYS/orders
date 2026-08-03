<task>
Regenerate the NINE character cards. Use the imagegen skill's DEFAULT built-in `image_gen` tool.
Do NOT use scripts/image_gen.py (that CLI fallback needs an OPENAI_API_KEY we do not have).

STYLE REFERENCE — read these existing approved files first:
  D:/Claude/nan2026/orders/art/concepts/style_A_pixel.png   (locked art direction)
  D:/Claude/nan2026/orders/art/concepts/v2/char_05_mio.png  (correct marksman role coding)
  D:/Claude/nan2026/orders/art/concepts/v2/char_08_hotaru.png (correct support role coding)

TWO CORRECTIONS DRIVE THIS PASS — both are hard requirements:

  (1) EVERY ONE OF THE NINE IS A YOUNG WOMAN. This was omitted from the previous prompt and
      several characters came out reading as male or ambiguous. All nine must be unmistakably
      female bishoujo-style anime characters: soft rounded facial features, large expressive
      eyes with visible lashes, softer jawline, and a feminine silhouette, all within the
      SD/chibi proportions. This applies equally to the short-haired ones (Rin, Sora, Mio) —
      short hair must still read clearly as a girl. Keep it wholesome and age-appropriate:
      these are working adults in bulky practical workwear, fully covered, no fanservice,
      no revealing clothing, no suggestive posing.

  (2) HANA'S HAIR BECOMES DEEP PLUM. In the last pass her hair was navy-indigo, which made her
      silhouette disappear into the navy background and navy uniform. Deep plum is lighter than
      the background, is not teal, and is not rose, so it separates from both her role accent
      and the backdrop.

ROLE CODING — keep exactly what worked last pass:

  VANGUARD — the ONLY role that wears a vest.
    Hi-vis safety vest with reflective grey stripes over the navy uniform,
    plus TEAL (#6cc2cf) shoulder epaulettes on both shoulders.
    No brass, no rose on the outfit.

  MARKSMAN — NO VEST. Nothing hi-vis or yellow-green on the body.
    A wide BRASS (#e0ae4d) waist belt with two brass-buckled hip pouches,
    and a small brass collar tab. No teal, no rose, no epaulettes.

  SUPPORT — NO VEST.
    ROSE (#e87b8e) vertical piping down both sides of the navy jacket front,
    plus rose-edged chest pockets. No teal, no brass, no belt, no epaulettes.

LOCKED ACROSS ALL NINE:
  - TRUE PIXEL ART. Chunky visible pixel grid, hard aliased edges, NO anti-aliasing,
    NO soft gradients. High-resolution SNES-era sprite scaled with nearest-neighbor.
  - SD / super-deformed chibi proportions, about 2.5 heads tall.
  - Standing, facing viewer, full body inside frame.
  - Vertical card composition, 2:3, character centered, generous margin top and bottom.
  - Flat dark background #0f1220. Not a scene.
  - Thin 1px brass border rectangle just inside the image edge.
  - NO text, NO letters, NO numbers, NO watermark, NO logo, NO signature.
  - Same dark navy (#1b2030) night-shift work uniform base for everyone, so they read as one squad.
  - Hair colour must stay clearly lighter than the #0f1220 background so every silhouette reads.

PALETTE: background #0f1220 · uniform #1b2030 · skin/ink #eceae3 ·
         teal #6cc2cf · rose #e87b8e · brass #e0ae4d

THE NINE — all young women. Hair and prop are how a player tells individuals apart.

VANGUARD (hi-vis vest + teal epaulettes):
1) D:/Claude/nan2026/orders/art/concepts/v3/char_01_rin.png
   Rin, a girl with a short messy crimson-red bob and one stray ahoge. Courier satchel across
   the body. Mid-stride lean, light on her feet, confident grin.
2) D:/Claude/nan2026/orders/art/concepts/v3/char_02_hana.png
   Hana, a girl with long straight DEEP PLUM hair past the shoulders. Thick flame-resistant
   gloves. Planted wide stance, arms crossed, calm unbothered face.
3) D:/Claude/nan2026/orders/art/concepts/v3/char_03_sora.png
   Sora, a girl with a silver-white short pixie crop and safety goggles pushed up on her
   forehead. Holding a red fire extinguisher braced at the hip. Smirking, shoulders squared.

MARKSMAN (no vest, brass belt + hip pouches):
4) D:/Claude/nan2026/orders/art/concepts/v3/char_04_yui.png
   Yui, a girl with a warm honey-blonde high ponytail. A brass telescopic monocular goggle over
   one eye, clipboard tucked under the other arm. Alert, looking off into the distance.
5) D:/Claude/nan2026/orders/art/concepts/v3/char_05_mio.png
   Mio, a girl with a straight jet-black chin-length bob and blunt fringe. Large over-ear
   headphones around her neck, a folded camera tripod over one shoulder.
   Expressionless, tired half-lidded eyes. Must still clearly read as a girl.
6) D:/Claude/nan2026/orders/art/concepts/v3/char_06_nagi.png
   Nagi, a girl with violet twin tails. Holding a small handheld line-laser emitting one thin
   straight teal beam to the side, a surveying rod strapped to her back. Focused, one eye narrowed.
   (The teal beam is light from her tool, not garment trim — her outfit stays brass-only.)

SUPPORT (no vest, rose vertical piping):
7) D:/Claude/nan2026/orders/art/concepts/v3/char_07_aoi.png
   Aoi, a girl with a light sky-blue bob and a small hair clip. Carrying a white first-aid case
   in both hands, a small flashlight clipped to her chest. Worried, earnest expression.
8) D:/Claude/nan2026/orders/art/concepts/v3/char_08_hotaru.png
   Hotaru, a girl with yellow hair in two low pigtails. Holding up a hand lantern glowing warm
   brass, a boxy portable generator backpack. Cheerful, eyes shut in a smile.
9) D:/Claude/nan2026/orders/art/concepts/v3/char_09_shizu.png
   Shizu, a girl with very long straight white hair. A thick stack of documents cradled in one
   arm, a large rubber stamp raised in the other hand. Deadpan, half-lidded stare.

Create the v3 directory if needed. Verify all nine PNG files exist on disk after writing.
</task>

<default_follow_through_policy>
Choose the most reasonable low-risk interpretation and finish all nine. Do not ask questions.
If the built-in image_gen tool is unavailable, do NOT fall back to the CLI — stop and report why.
</default_follow_through_policy>

<completeness_contract>
All nine files must be written. If one fails, retry it once, then continue and report which
never succeeded. Before finishing, re-check every image against BOTH corrections above:
any character that reads as male or ambiguous is a failure and must be redone;
any marksman or support wearing a hi-vis vest is a failure and must be redone.
</completeness_contract>

<structured_output_contract>
Answer in exactly this form, nothing else:
1. RESULT: OK or PARTIAL or FAILED
2. FILES: one line per file — filename, byte size, exists yes/no
3. CHECK: one line per file — reads clearly as a girl yes/no, and role marker (vest/belt/piping) correct yes/no
4. NOTES: at most two lines
</structured_output_contract>
