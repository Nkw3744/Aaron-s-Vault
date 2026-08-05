---
aliases:
  - fiber bend radius laser
  - fiber cable routing laser
type: technical-reference
category: fiber-optics
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Coherent datasheet, fiber installation best practices
status: generic reference — verify against nameplate and project drawing
---

# Fiber Cable Bend Radius and Routing

Return to [[QBH Fiber Delivery Cable]] · [[Technical Reference Index]]

> [!info] When to open this note
> Minimum bend radius, drag-chain routing, and support for armored delivery fiber.

> [!warning] Verify cable datasheet
> Industry rule-of-thumb is **20× cable OD** (dynamic/install) and **10× OD** (static). Your armored laser cable may specify larger — OEM wins.

## Bend radius rules

| Condition | Typical guideline |
| --- | --- |
| During install / motion | ≥20× outer diameter |
| Permanent static route | ≥10× outer diameter |
| Torsion | OEM max °/m — often ~90°/m class |

Example: 25 mm OD armor → dynamic radius ~500 mm (20×).

## Routing checklist

1. **No kinks** — treat like hydraulic hose under tension
2. Support every 1–2 m on overhead tray; strain relief at QBH and source
3. Drag chain: use segregated compartment; radius at chain entry ≥ cable minimum
4. Do not tie fiber to moving axis cables with tight zip ties — use soft loops
5. Keep away from welding cables and VFD power lines
6. Service loop at source for maintenance — not coiled tight on floor
7. Label "DO NOT STEP" on floor crossings

## Common damage locations

- Chain entrance pinch point
- QBH hang stress when Z-axis at top
- Crush under machine feet during move
- Sharp 90° tray corners without formers

## Inspection

- Armor dents, heat discoloration, stiff sections
- Connector temperature warm but not hot (>45 °C suspect)
- Light leak at armor — **stop using**

## After suspected damage

1. Disable emission
2. Visual + interlock test
3. Power meter check at low power if OEM procedure exists
4. Replace cable if any doubt — repair not field DIY

## Related notes

- [[Fiber Cable Cooling and Interlocks]]
- [[Installation Clearances and Foundations]]

## Sources

- Coherent QBH cable mechanical specifications
- Fiber optic bend radius installation guidelines (FOA/industry practice)
