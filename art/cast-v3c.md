<task>
Generate EIGHT character cards. Use the imagegen skill's DEFAULT built-in `image_gen` tool.
Do NOT use scripts/image_gen.py (that CLI fallback needs an OPENAI_API_KEY we do not have).

STYLE REFERENCE — read this first and match its art direction exactly:
  D:/Claude/nan2026/orders/art/concepts/v3/char_01_rin.png
Rin is the approved baseline: true pixel art, chunky visible pixel grid, hard aliased edges,
no anti-aliasing, no gradients, SD chibi about 2.5 heads tall, and — importantly — her face
reads clearly as a girl. Match that face language.

=== HARD REQUIREMENT: EVERY CHARACTER IS A YOUNG WOMAN ===

Two earlier passes failed this. Saying "female" abstractly was not enough — one card came out
androgynous because the pose and hair notes pulled the other way. So this is specified concretely.
Apply ALL of these to every one of the eight:

  FACE   - rounded soft jaw, small narrow chin, full cheeks
         - large eyes, thick dark upper lash line, visible lower lashes
         - thin softly-arched eyebrows. NEVER thick, straight or angular brows
  BUILD  - narrow sloping shoulders, clearly narrower than the hips
         - small hands, slim forearms
  HAIR   - even the short cuts must be soft and rounded in volume, with wispy strands framing
           the cheeks and a curved nape. NEVER a flat, boxy or masculine crop
  POSE   - relaxed and asymmetric: slight head tilt, weight on one leg, one shoulder lower
         - NEVER squared shoulders, NEVER a wide planted power stance, NEVER hand-on-hip swagger

Keep everything wholesome and age-appropriate. These are working adults in bulky practical
workwear, fully covered. No fanservice, no revealing clothing, no suggestive posing.

=== CENTERING ===
Vertical 2:3 card. The figure is centered horizontally AND vertically, feet on roughly the same
baseline across all cards, equal margin left and right. Do not shift the figure to a corner or
leave a large empty band on one side.

=== ROLE CODING (already validated, keep exactly) ===

  VANGUARD — the ONLY role that wears a vest.
    Hi-vis safety vest with reflective grey stripes over the navy uniform,
    plus TEAL (#6cc2cf) shoulder epaulettes on both shoulders. No brass, no rose.

  MARKSMAN — NO VEST. Nothing hi-vis or yellow-green on the body.
    Wide BRASS (#e0ae4d) waist belt with two brass-buckled hip pouches, small brass collar tab.
    No teal, no rose, no epaulettes.

  SUPPORT — NO VEST.
    ROSE (#e87b8e) vertical piping down both sides of the navy jacket front, rose-edged chest
    pockets. No teal, no brass, no belt, no epaulettes.

=== LOCKED ACROSS ALL EIGHT ===
  - Flat dark background #0f1220. Not a scene.
  - Thin 1px brass border rectangle just inside the image edge.
  - NO text, letters, numbers, watermark, logo or signature anywhere.
  - Same dark navy (#1b2030) night-shift work uniform base, so they read as one squad.
  - Hair colour clearly lighter than the #0f1220 background so every silhouette reads.

PALETTE: background #0f1220 · uniform #1b2030 · skin/ink #eceae3 ·
         teal #6cc2cf · rose #e87b8e · brass #e0ae4d

=== THE EIGHT ===

VANGUARD (hi-vis vest + teal epaulettes):
D:/Claude/nan2026/orders/art/concepts/v3/char_02_hana.png
   Hana. Long straight DEEP PLUM hair past the shoulders — deep plum specifically, an earlier
   pass made it navy-indigo and her silhouette vanished into the background.
   Thick flame-resistant gloves. Calm unbothered face, arms loosely folded, head tilted slightly.
D:/Claude/nan2026/orders/art/concepts/v3/char_03_sora.png
   Sora. Short silver-white hair, but SOFT and rounded — side-swept fringe, wispy strands at the
   cheeks, curved nape. Safety goggles pushed up on her forehead. Holding a red fire extinguisher
   at her side with both hands. Small confident smile, weight on one leg, shoulders relaxed and
   uneven. (An earlier attempt gave her a boxy pixie crop, angular brows and squared shoulders
   and read as a boy — do not repeat that.)

MARKSMAN (no vest, brass belt + hip pouches):
D:/Claude/nan2026/orders/art/concepts/v3/char_04_yui.png
   Yui. Warm honey-blonde high ponytail with soft loose strands. Brass telescopic monocular
   goggle over one eye, clipboard hugged to her chest. Alert, looking off into the distance,
   head tilted.
D:/Claude/nan2026/orders/art/concepts/v3/char_05_mio.png
   Mio. Jet-black chin-length bob with a blunt fringe, soft rounded volume and wispy cheek
   strands. Large over-ear headphones around her neck, a folded camera tripod resting against
   one shoulder. Sleepy half-lidded eyes, faint frown, slouched relaxed posture.
   She must clearly read as a girl — a previous attempt of hers read as a boy.
D:/Claude/nan2026/orders/art/concepts/v3/char_06_nagi.png
   Nagi. Violet twin tails. Holding a small handheld line-laser emitting one thin straight teal
   beam to the side, a surveying rod strapped to her back. Focused, one eye narrowed, leaning
   slightly forward. (The teal beam is light from her tool, not garment trim — outfit stays brass-only.)

SUPPORT (no vest, rose vertical piping):
D:/Claude/nan2026/orders/art/concepts/v3/char_07_aoi.png
   Aoi. Light sky-blue bob with a small hair clip. Carrying a white first-aid case in both hands
   held in front of her, small flashlight clipped to her chest. Worried, earnest, shoulders drawn in.
D:/Claude/nan2026/orders/art/concepts/v3/char_08_hotaru.png
   Hotaru. Yellow hair in two low pigtails. Holding up a hand lantern glowing warm brass, boxy
   portable generator backpack. Cheerful, eyes shut in a smile, leaning back slightly.
D:/Claude/nan2026/orders/art/concepts/v3/char_09_shizu.png
   Shizu. Very long straight white hair. A thick stack of documents cradled in one arm, a large
   rubber stamp raised in the other hand. Deadpan, half-lidded stare, head tipped to one side.

Verify all eight PNG files exist on disk after writing.
</task>

<default_follow_through_policy>
Choose the most reasonable low-risk interpretation and finish all eight. Do not ask questions.
If the built-in image_gen tool is unavailable, do NOT fall back to the CLI — stop and report why.
If a filesystem read of a reference image fails with "fs sandbox helper failed", report it
immediately and stop. Do not retry in a loop.
</default_follow_through_policy>

<completeness_contract>
All eight files must be written. If one fails, retry it once, then continue and report which
never succeeded. Before finishing, re-check each image against the FACE / BUILD / HAIR / POSE
list above; anything that reads as male or ambiguous is a failure and must be redone.
</completeness_contract>

<structured_output_contract>
Answer in exactly this form, nothing else:
1. RESULT: OK or PARTIAL or FAILED
2. FILES: one line per file — filename, byte size, exists yes/no
3. CHECK: one line per file — reads clearly as a girl yes/no, centered yes/no, role marker correct yes/no
4. NOTES: at most two lines
</structured_output_contract>
