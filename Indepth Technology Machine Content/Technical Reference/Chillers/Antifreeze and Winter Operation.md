---
aliases:
  - chiller antifreeze
  - glycol laser chiller winter
type: technical-reference
category: chillers
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: Arcus install guide, CW manual, field winter practice
status: generic reference — verify against nameplate and project drawing
---

# Antifreeze and Winter Operation

Return to [[Laser Water Chillers]] · [[Technical Reference Index]]

> [!info] When to open this note
> Preventing frozen chiller loops in unheated workshops.

## Options

| Strategy | When |
| --- | --- |
| Heated laser room (≥10 °C) | Best for precision; no glycol |
| Propylene glycol mix | Unheated shop; OEM-approved ratio |
| Drain for shutdown season | Long idle in cold climate |

Arcus guidance: propylene glycol in chiller **or** heated room — not frozen idle machine with water fill.

## Glycol selection

- **Propylene glycol** (food/industrial non-toxic) — preferred over ethylene if people nearby
- Mix ratio per OEM for minimum design temperature (often −10 to −20 °C protection)
- Never guess automotive green coolant brand without laser OEM approval

## Effects of glycol

| Effect | Note |
| --- | --- |
| Heat transfer | Slightly reduced — chiller works harder |
| Viscosity | Higher at cold — flow alarm risk at startup |
| Conductivity | May change — monitor if meter fitted |
| Change interval | May shorten — inspect color |

Warm chiller room or circulate before high-power cutting on frosty mornings.

## Startup in cold shop

1. Confirm room or loop above freeze point
2. Power chiller; verify flow before laser enable
3. If E3 (low temp) alarm — raise setpoint gradually — [[CW Series Chiller Alarm Codes]]
4. Avoid immediate full power until water at stable setpoint

## Summer transition

If glycol was seasonal:

- Flush and return to DI/distilled only for best cooling efficiency
- Or maintain year-round mix if climate swings both ways

## Related notes

- [[Cooling Water Quality]]
- [[Ambient Temperature Limits]]

## Sources

- Arcus CNC laser installation (winter antifreeze note)
- CW-5200 maintenance documentation
