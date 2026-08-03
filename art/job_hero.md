<task>
Use the imagegen skill's DEFAULT built-in `image_gen` tool. Do NOT use scripts/image_gen.py.
Generate THREE separate landscape images, one call each, at 1536x1024.

Save to exactly these paths (create the folder if needed):
  A -> D:/Claude/nan2026/orders/art/concepts/hero/hero_a.png
  B -> D:/Claude/nan2026/orders/art/concepts/hero/hero_b.png
  C -> D:/Claude/nan2026/orders/art/concepts/hero/hero_c.png

These are BACKGROUND PLATES for a game's title screen. Characters will be composited in
later from existing artwork, so:
  - ABSOLUTELY NO PEOPLE, no figures, no silhouettes of people, no animals.
  - Keep the LOWER THIRD of the frame visually calm and uncluttered (ground, floor, platform).
    Standing figures will be placed there. No large objects in the lower third.

=== SUBJECT: SIGNAL POST No.3 ===
A relay/watch station that only opens at night. Communication runs one way only: an order
sheet is sent down before the shift, and after that nobody can be reached. It is an
industrial night-shift workplace, not a fantasy castle and not a military base.
Mood: quiet, cold, a little lonely, but staffed and functioning. Lived-in, slightly worn.

=== RENDERING — must match the existing game art ===
  - PIXEL ART. Chunky visible pixel grid, hard aliased edges, NO anti-aliasing, NO smooth
    gradients, NO airbrush glow. Dithering is acceptable for shading.
  - Limited palette. Dark night scene built on these exact colours:
      background / sky    #05060a
      structures, near    #1b2030
      structures, far     #0f1220
      cold accent light   #6cc2cf   (teal — screens, indicator lamps, cold fluorescents)
      warm accent light   #e0ae4d   (amber — sodium lamps, lit windows, warning beacons)
      danger accent       #e87b8e   (rose — sparse, only for hazard marks; use very little)
  - The image must read clearly when scaled down to about 500 px wide.
  - NO text, letters, numbers, signage glyphs, watermark, logo or signature anywhere.

=== THE THREE VARIANTS ===

A — EXTERIOR, seen from outside at night.
  A squat concrete-and-steel relay station in fog. Two lattice antenna masts rising behind
  it with slow amber beacons. Chain-link fence and a narrow gravel approach in front.
  A few windows lit cold teal. Power lines running off frame. Distant hills as flat silhouette.
  Lower third: open gravel ground, empty.

B — INTERIOR, the control room where the order sheet is written.
  A cramped night-shift operations room. A long console desk along the back wall with
  CRT-style monitors glowing teal, an amber desk lamp, pinned paper notes and a wall of
  small indicator lights. A large window behind the console shows only black fog outside.
  Exposed pipes and cable trays across the ceiling. A wall clock (no numbers, just marks).
  Lower third: bare concrete floor with faint painted lane markings, empty.

C — THE GATE, the moment before the shift goes out.
  Looking outward from inside the station toward a tall open steel shutter door. Cold teal
  fluorescents overhead inside; beyond the doorway is amber-lit fog and darkness. Lockers,
  a rack of hanging hi-vis gear and a shift board on the left wall. Metal grating steps
  leading down and out through the doorway.
  Lower third: the flat floor and the base of the doorway, empty.
</task>

<default_follow_through_policy>
Pick the most reasonable low-risk interpretation and carry it through to the end.
Do not stop to ask questions about style choices.
</default_follow_through_policy>

<completeness_contract>
All three images must be generated and saved to the exact paths above before you finish.
If a save fails, retry that one. Do not stop after the first plausible result.
</completeness_contract>

<structured_output_contract>
Answer with exactly: 1) the three output paths and whether each was written,
2) one line per image describing what it shows. No other prose.
</structured_output_contract>
