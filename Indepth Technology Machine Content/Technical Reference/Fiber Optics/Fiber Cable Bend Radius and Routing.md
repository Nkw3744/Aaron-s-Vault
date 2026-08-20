---
aliases:
  - fiber bend radius laser
  - fiber cable routing laser
  - QBH cable routing
type: technical-reference
category: fiber-optics
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Coherent QBH datasheet, FOA/industry bend-radius practice, field drag-chain installs
status: generic reference — verify against nameplate and project drawing
---

# Fiber Cable Bend Radius and Routing

Return to [[QBH Fiber Delivery Cable]] · [[Technical Reference Index]]

> [!info] When to open this note
> Minimum bend radius, drag-chain routing, support, and inspection after moves — the #1 mechanical killer of delivery fibers besides connector abuse.

> [!warning] Datasheet wins
> Rule of thumb: **20× OD dynamic**, **10× OD static**. Armored laser cables often need **larger** radii. OEM cable drawing overrides this note.

## Bend radius rules

| Condition | Typical guideline | Example 25 mm OD armor |
| --- | --- | --- |
| Install / motion (dynamic) | ≥20× outer diameter | ≥500 mm radius |
| Permanent static route | ≥10× outer diameter | ≥250 mm radius |
| Torsion | OEM max °/m (often ~90°/m class) | Do not corkscrew in chain |

Bend **radius** ≠ bend **diameter**. A 500 mm radius is a 1000 mm diameter loop.

## Why bends kill fibers

Tight bends cause micro-bending and macro-bending loss, stress cracks in glass, and eventual catastrophic failure under kW power. Damage may be invisible externally until power drop, heat at QBH, or sudden interlock/power faults.

## Routing checklist

1. **No kinks** — treat like high-pressure hydraulic hose
2. Support every 1–2 m on tray; strain relief at source and QBH
3. Drag chain: dedicated compartment; entry radius ≥ cable minimum
4. Soft loops — never tight zip-ties crushing armor against power cables
5. Segregate from welding leads and VFD outputs — [[Grounding and EMC Isolation]]
6. Service loop at source for maintenance — large radius, not a tight coil on the floor
7. Floor crossings: protective cover + "DO NOT STEP" labeling
8. Z-axis top position: verify QBH hang does not tighten bend below minimum
9. Document route photos on machine hub after install

## High-risk damage locations

| Location | Failure mode |
| --- | --- |
| Drag-chain entrance | Pinch / below-radius bend |
| QBH at Z top | Hang stress / sharp droop |
| Under machine feet during move | Crush |
| Sharp 90° tray corners | Macrobend without former |
| Forklift path | Impact |
| Tight tie to servo cable | Abrasion + EMI adjacency |

## Drag-chain practice

| Do | Don't |
| --- | --- |
| Use separators; fiber alone in cell | Mix with oily pneumatics dripping on armor |
| Verify chain bending radius ≥ cable | Force cable into too-small chain |
| Leave length for full axis travel + margin | Stretch taut at end of travel |
| Inspect chain wear plates | Ignore black dust from chain (contaminates area) |

## Inspection routine

| When | Look for |
| --- | --- |
| Daily walk-by | Armor dents, new rub marks |
| After crash / axis fault | Localized stiff section |
| After machine move | Crush points; re-dress |
| If power drop / heat | Armor discoloration; light leak — **stop** |

Suspect heat: connector or armor >~45 °C under load → investigate cooling and alignment — [[Fiber Cable Cooling and Interlocks]].

## After suspected damage

1. Disable emission
2. Visual inspection full length
3. Interlock resistance check
4. Low-power OEM test procedure if available
5. Replace cable if any doubt — **no field splicing** of delivery fiber

## Clearance and layout

Plan cable path at site survey with [[Installation Clearances and Foundations]]. Overhead tray preferred over floor snakes.

## Related notes

- [[QBH Fiber Delivery Cable]]
- [[Fiber Connector Cleaning and Inspection]]
- [[Fiber Cable Cooling and Interlocks]]
- [[Fiber Laser Commissioning Sequence]]

## Sources

- Coherent QBH cable mechanical specifications
- FOA / industry fiber bend-radius installation guidance
- Field drag-chain failure patterns on fiber lasers
