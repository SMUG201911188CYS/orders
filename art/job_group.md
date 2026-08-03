<task>
Use the imagegen skill's DEFAULT built-in `image_gen` tool in EDIT mode.
Do NOT use scripts/image_gen.py. Issue one call per output.

For BOTH outputs, Image 1 is the SAME reference, passed as an ACTUAL INPUT IMAGE
(not merely read from disk):
  D:/Claude/nan2026/orders/art/_ref9.png

Image 1 is a reference STRIP: the same nine characters standing side by side, left to right,
each in her own panel. It is NOT the composition you should produce. It exists only so you
can see exactly what each of the nine looks like.

Produce TWO landscape group illustrations at 1536x1024, saved to exactly:
  A -> D:/Claude/nan2026/orders/art/concepts/hero/group_a.png
  B -> D:/Claude/nan2026/orders/art/concepts/hero/group_b.png

=== THE NINE, IN LEFT-TO-RIGHT ORDER OF IMAGE 1 ===
 1 crimson-red short messy bob, long glow-yellow scarf, hi-vis vest, courier satchel
 2 dark plum long hair, heaviest build of the nine, flame-cloth draped over shoulders, hi-vis vest
 3 silver-white short hair, goggles on forehead, hugging a red fire extinguisher, hi-vis vest
 4 blonde high ponytail, brass monocle, lenses hung at the chest, brass waist belt and pouches
 5 black chin-length hair, sleepy half-lidded eyes, long tripod over one shoulder, brass belt
 6 dark purple twin tails, perfectly upright posture, a tall red-and-white survey rod, brass belt
 7 pale blue bob, hugging a white first-aid box with a red cross, rose piping on the jacket
 8 golden blonde twin tails, eyes closed in a wide smile, raised hand lantern, generator backpack
 9 very long white hair past the knees, stack of documents under one arm, raised rubber stamp

=== ABSOLUTE REQUIREMENTS ===
1. ALL NINE must appear, and each must remain recognisably the SAME CHARACTER as in Image 1:
   same hair colour and hairstyle silhouette, same signature prop, same expression type.
   Do not invent a tenth character. Do not drop anyone. Do not swap props between them.
2. ROLE COSTUME CODING must survive exactly:
     characters 1-3 : hi-vis YELLOW-GREEN safety vest with grey reflective stripes,
                      TEAL (#6cc2cf) shoulder epaulettes. No brass.
     characters 4-6 : NO vest. Wide BRASS (#e0ae4d) waist belt and brass-buckled hip pouches.
     characters 7-9 : NO vest. ROSE (#e87b8e) vertical piping down the jacket front.
   All nine wear the same dark navy #1b2030 work uniform underneath.
3. Keep the body proportions of Image 1 — roughly 4 heads tall, young women in fully covered
   practical workwear. Wholesome, no fanservice.
4. RENDERING: pixel art. Chunky visible pixel grid, hard aliased edges, NO anti-aliasing,
   NO smooth gradients, NO airbrush glow. Dithering is fine for shading.
5. PALETTE: a night scene built on #05060a background, #1b2030 near structures,
   #0f1220 far structures, TEAL #6cc2cf cold light, AMBER #e0ae4d warm light,
   ROSE #e87b8e used very sparingly.
6. NO text, letters, numbers, signage glyphs, watermark, logo or signature anywhere.
7. The image must still read clearly when scaled down to about 640 px wide, so keep the nine
   large enough in frame and do not bury them in background detail.

=== A — SHIFT ROLL-OUT, EXTERIOR ===
The nine gathered on the gravel apron outside Signal Post No.3 at night, just before the shift
goes out. The squat concrete-and-steel station and two lattice antenna masts with amber beacons
behind them, chain-link fence, fog. Stagger them in depth — a few a step forward, a few further
back — so it reads as a crew, not a police lineup. Character 1 leaning forward eager at the
front, character 2 standing solid with arms folded, character 8 with the lantern raised lighting
the group. Full body for everyone, feet on the ground.

=== B — THE BRIEFING, INTERIOR ===
The nine crowded around a long console desk in the cramped night-shift control room, looking
down at the order sheets laid out on it. CRT monitors glowing teal along the back wall, an amber
desk lamp on the table, exposed pipes across the ceiling, a black fogged window behind. Some
lean on the desk, some stand behind, character 8's lantern on the table as the warm light source.
Waist-up or three-quarter framing is fine here, but every one of the nine must be visible and
identifiable.
</task>

<default_follow_through_policy>
Pick the most reasonable low-risk interpretation and carry it through. Do not stop to ask
questions about composition or style.
</default_follow_through_policy>

<completeness_contract>
Both images must be generated and saved to the exact paths above before you finish.
After saving each one, verify that all nine characters are present and that the three role
costume groups are still correct. If one is missing or a costume group is wrong, regenerate
that image once.
</completeness_contract>

<structured_output_contract>
Answer with exactly: 1) the two output paths and whether each was written,
2) for each image, one line listing which of the nine you can confirm are visible.
No other prose.
</structured_output_contract>
