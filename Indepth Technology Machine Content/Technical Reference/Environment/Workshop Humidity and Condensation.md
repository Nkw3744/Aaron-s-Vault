---
aliases:
  - laser condensation
  - humidity laser workshop
type: technical-reference
category: environment
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: Novanta condensation bulletin, Greenstone summer guide, Sieme laser summer note
status: generic reference — verify against nameplate and project drawing
---

# Workshop Humidity and Condensation

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Why lasers sweat in summer, where damage occurs, environmental targets, and emergency response when you see droplets on the head or QBH.

> [!danger] Condensation causes hard damage
> Over-temperature is often a soft stop. Moisture on QBH, windows, and PCBs causes permanent optics and electronics failure.

## Mechanism

When a cooled surface (coolant pipe, QBH, head body) is **below the dew point** of surrounding air, water vapor condenses as liquid. On a fiber laser that liquid lands on:

- Protective windows and focus lenses
- QBH interface and interlock pins
- Height-sensor ceramics and RF connectors
- Cabinet electronics if humid air is ingested

## Target environment

| Parameter | Target | Notes |
| --- | --- | --- |
| Room temperature | 22–28 °C ideal | See [[Ambient Temperature Limits]] |
| Relative humidity | ≤60%; ≤50% summer ideal | >70% → inspect urgently |
| Dew point margin | Cooled surfaces ≥ dew point + 2–3 °C | [[Dew Point and Chiller Setpoints]] |

## Prevention hierarchy

1. **Room HVAC** — dedicated laser-zone AC when possible
2. **Dehumidifier** — [[Dehumidifiers for Laser Rooms]]
3. **Chiller setpoints** — raise HT; never both loops at 22 °C in muggy weather — [[Dual-Temperature Chiller Circuits]]
4. **Chiller location** — keep condenser heat/humidity out of laser room when practical
5. **Cabinet discipline** — doors closed while running
6. **Do not defeat dew interlocks**

## If condensation is observed

1. **Disable emission** immediately
2. Power down laser if water is on optics or connectors
3. Lint-free wipe of **external** droplets only — do not wipe coated optics without procedure
4. Run dehumidifier/AC until RH stable (aim <50%)
5. Inspect QBH, window, ceramic, SMA — dry before restart — [[Fiber Connector Cleaning and Inspection]]
6. Fix setpoint/RH root cause; document event

## Seasonal log sheet (copy to machine hub)

| Date | Room T | RH % | Dew point °C | LT °C | HT °C | Margin | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Interaction with other faults

| Seen as… | May actually be condensation |
| --- | --- |
| Capacitance MAX / short | Water in head |
| Interlock intermittent | Wet QBH pins |
| Power drop | Wet/contaminated window |
| Random electronics faults | Cabinet moisture |

## Coastal / NZ summer notes

High RH with moderate °C still yields dangerous dew points. Do not wait for "35 °C heatwave" before enabling dehumidification.

## Related notes

- [[Dew Point and Chiller Setpoints]]
- [[Dehumidifiers for Laser Rooms]]
- [[Ambient Temperature Limits]]
- [[CW Series Chiller Alarm Codes]]
- [[Fiber Cable Cooling and Interlocks]]

## Sources

- Novanta technical bulletin — prevent condensation
- Greenstone summer laser maintenance guide
- Sieme laser summer condensation article
