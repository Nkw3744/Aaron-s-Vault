---
aliases:
  - dual temperature chiller
  - low temp high temp chiller loops
type: technical-reference
category: chillers
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Yihai dew-point guide, field dual-loop practice
status: generic reference — verify against nameplate and project drawing
---

# Dual-Temperature Chiller Circuits

Return to [[Laser Water Chillers]] · [[Technical Reference Index]]

> [!info] When to open this note
> Lo/Hi loops — source vs cutting head — and why head temperature is often **higher** than source.

## Two loops, two purposes

| Loop | Common label | Cools | Typical setpoint |
| --- | --- | --- | --- |
| Low temp (LT) | Lo, circuit 1 | Laser source / fiber module | 22–26 °C |
| High temp (HT) | Hi, circuit 2 | Cutting head, QBH, optics | 28–32 °C |

> [!tip] Counter-intuitive
> Head loop is warmer to **prevent condensation** on optics exposed to shop air. See [[Dew Point and Chiller Setpoints]].

## Why not both at 22 °C?

In humid shops, cold head plumbing sweats → water on optics → power loss, short circuits, window damage. HT circuit trades slightly warmer optics for dry surfaces.

## Connection identification

Document on machine:

- Which hose pair goes to source vs head
- Color coding (often red/blue or numbered)
- Flow direction arrows

Swapped loops → wrong temperature zone → alarms or condensation.

## Seasonal adjustment

| Season | Action |
| --- | --- |
| Summer high RH | Raise HT setpoint; lower room RH — [[Dehumidifiers for Laser Rooms]] |
| Winter | Antifreeze or heated room — [[Antifreeze and Winter Operation]] |
| Shoulder | Log dew point vs both setpoints daily |

## Intelligent / anti-condensation modes

Some chillers raise water temperature automatically when ambient dew point rises. Safer for optics than fixed 22 °C on head in summer; may approach source over-temp limits — monitor source alarm margin.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Head sweats, dew alarm | HT setpoint too low vs dew point |
| Source over-temp | LT flow; chiller capacity; room >35 °C |
| One loop warm, one cold | Valve setting; wrong hose connection |
| Both loops same temp | Controller mode; single-loop chiller misidentified |

## Single-loop chillers

Lower kW packages may use one temperature for all loads. Still apply dew point rule to exposed optics — may need room dehumidification instead of HT circuit.

## Related notes

- [[Workshop Humidity and Condensation]]
- [[Fiber Cable Cooling and Interlocks]]

## Sources

- Yihai dew point alarm laser chiller guide
- Novanta condensation prevention bulletin
