---
aliases:
  - QBH cleaning
  - fiber connector inspection
  - protective window contamination
type: technical-reference
category: fiber-optics
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: OEM fiber handling practice, field service protocols
status: generic reference — verify against nameplate and project drawing
---

# Fiber Connector Cleaning and Inspection

Return to [[QBH Fiber Delivery Cable]] · [[Technical Reference Index]]

> [!info] When to open this note
> When and how to inspect QBH interfaces and cutting-head protective windows before mating or after a contamination event.

> [!danger] Cleanroom discipline
> A single particle on a high-power interface can burn into the quartz face. Cap connectors when open; work in the cleanest area available.

## When to inspect

| Trigger | Action |
| --- | --- |
| First mate at install | Microscope if available; clean; mate |
| Any unplanned disconnect | Full inspect before remate |
| Smoke / oil / zinc event | Window + QBH path |
| Power drop / mode quality change | Optics first |
| After shipping / relocation | Always |
| Intermittent interlock | Pins + moisture |

## Tools

- Laser-grade lint-free wipes
- IPA 99%+ or OEM cleaning fluid
- Fiber microscope ~200–400× (service kit)
- Clean dust caps (do not reuse dirty caps)
- Gloves; no bare-finger quartz contact
- Torch for external armor/heat discoloration

## QBH end-face procedure (summary)

1. Emission disabled; verify zero energy state
2. Remove cap; inspect under microscope if available
3. Wipe ferrule face one direction with damp wipe
4. Dry pass with clean wipe
5. Re-inspect — no streaks, pits, particles, burns
6. Mate immediately or recap
7. Verify interlock after mate — [[Fiber Cable Cooling and Interlocks]]

Do not blow with oily shop air. Do not use cotton buds that shed.

## Protective window (cutting head)

Downstream consumable — separate from QBH:

| Practice | Detail |
| --- | --- |
| Replace on schedule or when pitted/burned | Often cheaper than polish attempts |
| Clean only with approved method | Many techs replace rather than field-polish |
| Contamination sources | Zn splash, oily air cut, slag, condensation |

See [[Zn and Coated Material Fume Notes]], [[Compressed Air Cutting]], [[Dew Point and Chiller Setpoints]].

## Contamination source map

| Source | Prevention |
| --- | --- |
| Dirty air cutting | Dryer + 0.01 µm chain |
| Head crash / pierce splash | Nozzle hygiene; pierce tune |
| Condensation | HT setpoint / dehumidifier |
| Hand oil | Gloves; cap discipline |
| Dusty open QBH on floor | Never park open connector upward in dust |

## Pass / fail visual cues

| Cue | Action |
| --- | --- |
| Rainbow oil film | Stop; fix air plant; replace window |
| Burn crater on window | Replace; check focus/gas/alignment |
| Haze after galv week | Expect shorter window life |
| Black particle on QBH face | Clean; if burned into face → OEM cable service |
| Green crust on pins | Clean carefully; dry; find water source |

## After cleaning — restart sequence

1. Mate QBH; torque
2. Water on; leak check
3. Interlock OK
4. Low-power / red-light checks per OEM
5. Capacitance cal if head was opened — [[Capacitive Height Sensing BCS100]]
6. Coupon before production sheet

## Related notes

- [[QBH Fiber Delivery Cable]]
- [[Fiber Cable Bend Radius and Routing]]
- [[Cutting Head Nozzles and Ceramics]]
- [[Air Filtration Stages]]

## Sources

- Coherent QBH handling specifications
- General high-power fiber connector cleaning practice
- Field window failure patterns (oil, Zn, condensation)
