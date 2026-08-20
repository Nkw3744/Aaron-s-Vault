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
> Preventing frozen chiller loops in unheated workshops, choosing glycol, cold-start procedure, and summer transition.

> [!danger] Freeze = cracked plant
> A water-filled chiller left below 0 °C can split tanks, fittings, and laser cold plates. Prevention is cheaper than source replacement.

## Options

| Strategy | When to use |
| --- | --- |
| Heated laser / chiller room (≥10 °C) | Best for process stability; may avoid glycol |
| Propylene glycol mix (OEM ratio) | Unheated shop; frost risk nights |
| Full drain for long shutdown | Seasonal idle in hard-freeze climate |

Arcus-style guidance: propylene glycol **or** heated room — do not leave plain water idle in freezing conditions.

## Glycol selection

| Prefer | Avoid |
| --- | --- |
| Propylene glycol, OEM-specified | Random automotive "green" coolant with silicates unless approved |
| Mix ratio for design minimum ambient (often −10 to −20 °C protection) | Guessing concentration with no refractometer |
| Compatible corrosion inhibitor package | Mixing leftover chemistries from other machines |

Use a glycol refractometer / test strip to verify concentration after mixing.

## Effects of glycol on the system

| Effect | Field note |
| --- | --- |
| Slightly reduced heat transfer | Chiller works harder — notice in summer if left year-round |
| Higher viscosity when cold | E6 / flow alarms on icy mornings until warm |
| Conductivity may change | Log baseline — [[Cooling Water Quality]] |
| Shorter inspect interval | Watch colour, cloudiness, smell |

## Cold-start procedure

1. Confirm room or loop is above freeze point (or glycol protection adequate)
2. Power chiller alone; verify flow before laser enable
3. If **E3** (water too low) — raise setpoint gradually — [[CW Series Chiller Alarm Codes]]
4. Wait until LT/HT stable before emission
5. Avoid immediate full-power thick plate from cold soak
6. Recheck dew-point margin if room is heated and humid — [[Dew Point and Chiller Setpoints]]

## Summer transition

| Choice | Action |
| --- | --- |
| Seasonal glycol | Flush; return to DI/distilled for best cooling |
| Year-round mix | Accept capacity hit; keep concentration logged |
| Heated room only | Drain unnecessary; verify heaters fail-safe |

## Freeze damage signs

- Cracked fittings or chiller tank seams
- Sudden massive leak on first thaw
- Pump seizure after ice
- Repeated unexplained low level after top-ups

Do not "just keep filling" — inspect for cracked cold plates.

## Checklist before winter season

| Item | ☐ |
| --- | --- |
| Decide heat vs glycol strategy | |
| Mix/test glycol % if used | |
| Label chiller with mix ratio and date | |
| Verify room heater or thermostat | |
| Brief operators on cold-start order | |
| Stock DI water for top-ups (not tap) | |

## Related notes

- [[Cooling Water Quality]]
- [[Ambient Temperature Limits]]
- [[Chiller Troubleshooting Flowchart]]
- [[Dual-Temperature Chiller Circuits]]
- [[Laser Water Chillers]]

## Sources

- Arcus CNC laser installation (winter antifreeze note)
- CW-5200 maintenance documentation
- Field freeze-failure cases
