---
aliases:
  - laser room dehumidifier
  - industrial dehumidifier laser
type: technical-reference
category: environment
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: Yihai dew-point guide, Novanta bulletin, Sieme summer guide
status: generic reference — verify against nameplate and project drawing
---

# Dehumidifiers for Laser Rooms

Return to [[Workshop Humidity and Condensation]] · [[Technical Reference Index]]

> [!info] When to open this note
> Sizing and placing dehumidification when HVAC alone cannot hold RH ≤60%.

## When needed

- Coastal or tropical humid climates
- No dedicated laser-room AC
- Repeated dew-point alarms despite correct chiller setpoints
- Open shop floor with large roller doors (humidity spikes)

Lowering RH 20% can drop dew point ~5–8 °C — significant margin for head cooling.

## Types

| Type | Best for |
| --- | --- |
| Refrigerant dehumidifier | General workshop; 20–30 L/day class common |
| Desiccant industrial | Large volume; low dew point needs |
| HVAC integrated | New builds; best long-term |
| Cabinet mini dehumidifier | Electrical enclosure only (~0.5 L/day+) |

## Placement

- **Laser air intake zone** — local dry bubble if full room enclosure impossible
- Not blowing directly on open QBH (dust movement)
- Drain hose to fixed outlet; do not rely on manual emptying during weekend shutdown
- Keep away from cutting zone spark path

## Sizing (rough)

| Room volume | Starting hint |
| --- | --- |
| 50 m³ laser cell | 20–30 L/day rated unit |
| 100 m³ | 30–50 L/day or HVAC |
| Full open workshop | Room dehumidification often insufficient — build laser enclosure |

Combine with [[Ambient Temperature Limits]] — dehumidifiers add heat.

## Operation with chiller

1. Run dehumidifier before laser enable in summer
2. Confirm RH stable before emission
3. HT loop still must be above dew point — dehumidifier is additive, not replacement

## Maintenance

- Clean filters monthly
- Check drain line for algae block
- Monitor RH meter daily log

## Related notes

- [[Dew Point and Chiller Setpoints]]
- [[Fiber Laser Site Requirements]]

## Sources

- Yihai dew point alarm guide (dehumidifier placement)
- Novanta condensation bulletin
- Sieme summer anti-condensation guide
