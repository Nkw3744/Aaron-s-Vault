---
aliases:
  - dual temperature chiller
  - low temp high temp chiller loops
  - Lo Hi chiller laser
type: technical-reference
category: chillers
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Yihai dew-point guide, field dual-loop practice, CW dual-temp packages
status: generic reference — verify against nameplate and project drawing
---

# Dual-Temperature Chiller Circuits

Return to [[Laser Water Chillers]] · [[Technical Reference Index]]

> [!info] When to open this note
> Lo/Hi (LT/HT) loops — laser source vs cutting head/QBH — and why the head loop is often **warmer**. Essential summer reading with [[Dew Point and Chiller Setpoints]].

> [!tip] Counter-intuitive rule
> Cold water on the head in a humid shop causes condensation on optics. Warmer HT water is often safer than "colder is always better."

## Two loops, two purposes

| Loop | Common labels | Cools | Typical setpoint |
| --- | --- | --- | --- |
| Low temp (LT) | Lo, T1, circuit 1 | Laser source / fiber module | 22–26 °C |
| High temp (HT) | Hi, T2, circuit 2 | Cutting head, QBH, external optics | 28–32 °C |

Exact labels vary by CW-6100/6200-class and OEM-branded dual chillers — photograph the port stickers into the machine hub.

## Why not both at 22 °C?

| Surface | Exposed to shop air? | If cooled to 22 °C in humid summer |
| --- | --- | --- |
| Source internals | Usually inside cabinet | Lower dew risk if cabinet dry |
| Head / QBH | Yes — open to room | Sweats → water on window, RF, pins |

HT circuit trades slightly warmer optics for dry surfaces. See [[Workshop Humidity and Condensation]].

## Identifying hoses in the field

Document on the machine hub:

| Record | Example |
| --- | --- |
| Which pair → source | Blue pair / ports 1–2 |
| Which pair → head/QBH | Red pair / ports 3–4 |
| Flow arrows | OUT from chiller = cold to load |
| Quick-coupler type | Prevents mix-ups after service |

**Swapped loops** → wrong temperature zone → source over-temp or head condensation. After any hose work, verify with hand temperature on return lines once stable.

## Seasonal adjustment table

| Season | LT action | HT action | Room action |
| --- | --- | --- | --- |
| Hot humid summer | Keep within OEM; watch over-temp margin | Raise toward 30–32 °C | AC + dehumidifier |
| Mild dry | OEM default often OK | 28–30 °C | Monitor dew point |
| Cold winter | Avoid freeze — [[Antifreeze and Winter Operation]] | Can run cooler if dry | Heat room |

Log daily in humid seasons: room T, RH, dew point, LT, HT, margin.

## Intelligent / anti-condensation modes

Some chillers raise water temperature automatically when ambient dew point rises.

| Pros | Cons |
| --- | --- |
| Protects optics without constant manual tweaks | LT may approach source over-temp limit |
| Safer than defeating dew interlocks | Operators must still watch source alarms |

Prefer intelligent mode over jumpering dew-point alarms.

## Single-loop chillers

Lower-kW packages may use one temperature for all loads. Then:

- Apply dew-point rule to exposed head/QBH
- Rely more on room dehumidification — [[Dehumidifiers for Laser Rooms]]
- Do not invent a second loop by teeing hoses incorrectly

## Flow and capacity notes

| Issue | Detail |
| --- | --- |
| Unequal flow | One loop restricted → that zone overheats |
| Shared pump designs | OEM-specific — do not re-pipe without diagram |
| QBH flow | Often ~2 L/min class — [[Fiber Cable Cooling and Interlocks]] |
| Hose length | ≤10 m common — long runs raise ΔT |

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Head sweats / dew alarm | HT too low vs dew point; RH high |
| Source over-temp, head cool | LT flow; capacity; swapped hoses; dirty condenser |
| Both loops same temperature | Mode config; single-loop unit misidentified; failed valve |
| One loop no flow | Kink, closed valve, wrong coupler |
| Condensation only on QBH | HT assignment wrong; QBH on LT by mistake |

## Commissioning checklist

1. Identify LT vs HT ports on chiller and machine
2. Connect correctly; mark hoses permanently
3. Set LT/HT per season and dew point
4. Run 30+ min; measure return temps
5. Confirm no sweat on head/QBH before emission
6. Record setpoints on machine hub

## Related notes

- [[Laser Water Chillers]]
- [[Dew Point and Chiller Setpoints]]
- [[CW Series Chiller Alarm Codes]]
- [[Fiber Cable Cooling and Interlocks]]
- [[Cooling Water Quality]]

## Sources

- Yihai dew point alarm laser chiller guide
- Novanta condensation prevention bulletin
- Field dual-loop CW package practice
