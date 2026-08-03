<task>
Generate the EIGHT remaining character cards. Rin (char_01) is already done — do not touch it.
Use the imagegen skill's DEFAULT built-in `image_gen` tool. Do NOT use scripts/image_gen.py
(that CLI fallback needs an OPENAI_API_KEY we do not have).

STYLE REFERENCE — read these existing approved files first:
  D:/Claude/nan2026/orders/art/concepts/v3/char_01_rin.png   (THE reference — match this exactly:
      art direction, chibi proportions, how female the face reads, how the teal epaulettes sit)
  D:/Claude/nan2026/orders/art/concepts/v2/char_05_mio.png   (correct marksman role coding)
  D:/Claude/nan2026/orders/art/concepts/v2/char_08_hotaru.png (correct support role coding)

HARD REQUIREMENT 1 — EVERY ONE OF THESE IS A YOUNG WOMAN.
An earlier pass omitted this and several came out reading as male or ambiguous.
All eight must be unmistakably female bishoujo-style anime characters: soft rounded facial
features, large expressive eyes with visible lashes, softer jawline, feminine silhouette,
all within SD/chibi proportions. This applies equally to the short-haired ones (Sora, Mio) —
short hair must still read clearly as a girl. Keep it wholesome and age-appropriate: these are
working adults in bulky practical workwear, fully covered, no fanservice, no suggestive posing.

HARD REQUIREMENT 2 — CENTERING.
Vertical card composition, 2:3. The character MUST be centered both horizontally and vertically,
her feet resting on roughly the same baseline in every card, with equal margin left and right.
The Rin card came out shifted to the upper-left with a large empty area below — do not repeat
that. Dynamic poses are fine, but the mass of the figure stays centered in the frame.

ROLE CODING — keep exactly what worked:

  VANGUARD — the ONLY role that wears a vest.
    Hi-vis safety vest with reflective grey stripes over the navy uniform,
    plus TEAL (#6cc2cf) shoulder epaulettes on both shoulders. No brass, no rose.

  MARKSMAN — NO VEST. Nothing hi-vis or yellow-green on the body.
    A wide BRASS (#e0ae4d) waist belt with two brass-buckled hip pouches and a small brass
    collar tab. No teal, no rose, no epaulettes.

  SUPPORT — NO VEST.
    ROSE (#e87b8e) vertical piping down both sides of the navy jacket front, plus rose-edged
    chest pockets. No teal, no brass, no belt, no epaulettes.

LOCKED ACROSS ALL EIGHT:
  - TRUE PIXEL ART. Chunky visible pixel grid, hard aliased edges, NO anti-aliasing,
    NO soft gradients. High-resolution SNES-era sprite scaled with nearest-neighbor.
  - SD / super-deformed chibi proportions, about 2.5 heads tall.
  - Standing, facing viewer, full body inside frame.
  - Flat dark background #0f1220. Not a scene.
  - Thin 1px brass border rectangle just inside the image edge.
  - NO text, NO letters, NO numbers, NO watermark, NO logo, NO signature.
  - Same dark navy (#1b2030) night-shift work uniform base for everyone, so they read as one squad.
  - Hair colour must stay clearly lighter than the #0f1220 background so every silhouette reads.

PALETTE: background #0f1220 · uniform #1b2030 · skin/ink #eceae3 ·
         teal #6cc2cf · rose #e87b8e · brass #e0ae4d

THE EIGHT — all young women.

VANGUARD (hi-vis vest + teal epaulettes):
2) D:/Claude/nan2026/orders/art/concepts/v3/char_02_hana.png
   Hana, a girl with long straight DEEP PLUM hair past the shoulders. Deep plum specifically —
   an earlier pass made her hair navy-indigo and her silhouette vanished into the background.
   Thick flame-resistant gloves. Planted wide stance, arms crossed, calm unbothered face.
3) D:/Claude/nan2026/orders/art/concepts/v3/char_03_sora.png
   Sora, a girl with a silver-white short pixie crop and safety goggles pushed up on her forehead.
   Holding a red fire extinguisher braced at the hip. Smirking, shoulders squared.

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

Verify all eight PNG files exist on disk after writing.
</task>

<default_follow_through_policy>
Choose the most reasonable low-risk interpretation and finish all eight. Do not ask questions.
If the built-in image_gen tool is unavailable, do NOT fall back to the CLI — stop and report why.
</default_follow_through_policy>

<completeness_contract>
All eight files must be written. If one fails, retry it once, then continue and report which
never succeeded. Before finishing, re-check every image against BOTH hard requirements:
any character that reads as male or ambiguous is a failure and must be redone;
any marksman or support wearing a hi-vis vest is a failure and must be redone.
</completeness_contract>

<structured_output_contract>
Answer in exactly this form, nothing else:
1. RESULT: OK or PARTIAL or FAILED
2. FILES: one line per file — filename, byte size, exists yes/no
3. CHECK: one line per file — reads clearly as a girl yes/no, centered yes/no, role marker correct yes/no
4. NOTES: at most two lines
</structured_output_contract>
