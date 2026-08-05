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
> Calculating safe chiller temperatures from room humidity — the core anti-condensation rule.

## Golden rule

**Any cooled surface exposed to shop air must stay ≥2–3 °C above ambient dew point.**

Includes: cutting head shell, QBH, external optics mounts, cold water hoses in open air.

## Dew point estimate (approximate)

From T (°C) and RH (%):

- Use psychrometric chart, weather app dew point, or hygrometer with dew point display
- Example: 30 °C @ 70% RH → dew point ~24 °C
- HT chiller must then be >26–27 °C minimum on head loop

Do not guess — measure RH and T at machine each shift in summer.

## Recommended setpoints (starting points)

| Circuit | Summer humid | Winter dry |
| --- | --- | --- |
| LT (source) | 24–26 °C | 22–24 °C |
| HT (head/optics) | 30–32 °C | 28–30 °C |

> [!warning] Common mistake
> Setting **both** loops to 22 °C in summer → head sweats → dew alarm or silent window damage.

## Intelligent chiller modes

Some units raise water temp automatically when ambient dew point rises. Preferable to defeating interlocks. Watch source over-temp margin if water runs warm (>30 °C LT).

## Startup sequence (humid day)

1. Dehumidifier/AC on 30+ min — [[Dehumidifiers for Laser Rooms]]
2. Chiller on; verify LT/HT stable
3. Confirm margin ≥2 °C
4. Laser control on
5. Enable emission last

## Shutdown

Disable emission → laser off → chiller may remain on briefly to shed heat — OEM dependent.

## Dew-point alarm response

1. Do not bypass permanently
2. Raise HT setpoint OR lower RH
3. Wait for alarm clear
4. Log event

## Related notes

- [[Fiber Laser Common Alarms]]
- [[Fiber Cable Cooling and Interlocks]]

## Sources

- Yihai understanding dew point alarm laser chiller systems
- Novanta prevent condensation technical bulletin
- Greenstone summer laser maintenance guide
