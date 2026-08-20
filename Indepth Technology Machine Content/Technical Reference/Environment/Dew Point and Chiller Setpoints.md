---
aliases:
  - dew point laser chiller
  - chiller setpoint summer
type: technical-reference
category: environment
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Yihai dew-point guide, Novanta bulletin, Greenstone guide
status: generic reference — verify against nameplate and project drawing
---

# Dew Point and Chiller Setpoints

Return to [[Workshop Humidity and Condensation]] · [[Dual-Temperature Chiller Circuits]] · [[Technical Reference Index]]

> [!info] When to open this note
> Calculating safe chiller temperatures from room humidity — the core anti-condensation rule for fiber heads and QBH.

## Golden rule

**Any cooled surface exposed to shop air must stay ≥2–3 °C above ambient dew point.**

Includes: cutting head shell, QBH, external optics mounts, cold water hoses in open air.

## Estimating dew point

From room T (°C) and RH (%):

- Use psychrometric chart, weather-app dew point, or hygrometer with dew-point display
- Example: 30 °C @ 70% RH → dew point ~24 °C → HT must be **>26–27 °C** minimum on head loop

Do not guess — measure at the machine each humid shift.

## Recommended starting setpoints

| Circuit | Summer humid | Winter dry |
| --- | --- | --- |
| LT (source) | 24–26 °C | 22–24 °C |
| HT (head/optics) | 30–32 °C | 28–30 °C |

> [!warning] Common mistake
> Setting **both** loops to 22 °C in summer → head sweats → dew alarm or silent window damage.

Stay within OEM max water temperatures (source over-temp risk if LT too warm).

## Intelligent chiller modes

Units that raise water temp with ambient dew point are preferred over defeating interlocks. Watch source over-temp margin if LT runs warm (>30 °C).

## Humid-day startup sequence

1. Dehumidifier/AC on 30+ min — [[Dehumidifiers for Laser Rooms]]
2. Chiller on; LT/HT stable
3. Confirm margin ≥2–3 °C
4. Laser control on
5. Enable emission last

Shutdown: disable emission → laser off → chiller per OEM (sometimes remains on briefly).

## Dew-point alarm response

1. Do not permanently bypass
2. Raise HT **or** lower RH (or both)
3. Wait for clear; dry any external moisture
4. Inspect optics before cutting — [[Fiber Connector Cleaning and Inspection]]
5. Log event

## Quick field worksheet

| Item | Value |
| --- | --- |
| Room T (°C) | |
| RH (%) | |
| Dew point (°C) | |
| LT set (°C) | |
| HT set (°C) | |
| HT − dew point | must be ≥2–3 °C |
| Action | |

## Related notes

- [[Dual-Temperature Chiller Circuits]]
- [[Workshop Humidity and Condensation]]
- [[Fiber Laser Common Alarms]]
- [[Fiber Cable Cooling and Interlocks]]
- [[CW Series Chiller Alarm Codes]]

## Sources

- Yihai understanding dew point alarm laser chiller systems
- Novanta prevent condensation technical bulletin
- Greenstone summer laser maintenance guide
