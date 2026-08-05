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
> Why lasers sweat in summer, damage mechanisms, and environmental targets.

> [!danger] Condensation causes hard damage
> Over-temperature is often a soft stop. Moisture on QBH, windows, and PCBs causes permanent optics and electronics failure.

## Mechanism

When **coolant or cold metal** is below the **dew point** of surrounding air, water vapor condenses into liquid on surfaces — QBH ferrule, head window, cabinet walls, fiber connector.

## Target environment

| Parameter | Target | Alarm threshold hint |
| --- | --- | --- |
| Room temperature | 22–28 °C ideal | >35 °C chiller struggle |
| Relative humidity | ≤60%; ≤50% summer ideal | >70% trigger inspection |
| Dew point margin | Coolant ≥ dew point + 2–3 °C | Log daily in humid seasons |

## Damage sites

- Protective window and focus lens
- QBH interface
- Height sensor electronics
- CNC control boards if cabinet humid air ingested

## Prevention hierarchy

1. **Room HVAC** — separate AC for laser zone if possible
2. **Dehumidifier** — [[Dehumidifiers for Laser Rooms]]
3. **Chiller setpoints** — [[Dew Point and Chiller Setpoints]], [[Dual-Temperature Chiller Circuits]]
4. **Do not locate chiller in same room** — adds heat and moisture load
5. **Cabinet doors closed** during running

## If condensation observed

1. **Disable emission** immediately
2. Power down laser if water on optics
3. Lint-free wipe **external** droplets only — do not touch coated optics without procedure
4. Run dehumidifier/AC until RH stable <50%
5. Inspect all optics dry before restart
6. Fix setpoint/RH root cause — do not just reset alarm

## Seasonal log sheet (suggested)

| Date | Room T | RH % | Dew point °C | LT set | HT set | Margin | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Related notes

- [[Ambient Temperature Limits]]
- [[Fiber Connector Cleaning and Inspection]]

## Sources

- Novanta technical bulletin — prevent condensation
- Greenstone summer laser maintenance guide
- Sieme laser summer condensation article
