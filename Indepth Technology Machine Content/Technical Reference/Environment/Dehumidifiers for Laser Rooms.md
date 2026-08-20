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
> Sizing and placing dehumidification when HVAC alone cannot hold RH ≤60%, or when dew-point alarms persist despite correct chiller setpoints.

## When needed

- Coastal / tropical humidity
- No dedicated laser-room AC
- Repeated dew-point or condensation events
- Open fab with roller doors (RH spikes)
- Summer production with HT already at OEM max

Lowering RH ~20% can drop dew point ~5–8 °C — large safety margin for head/QBH cooling.

## Types

| Type | Best for | Notes |
| --- | --- | --- |
| Refrigerant dehumidifier | General workshops | 20–50 L/day class common |
| Desiccant industrial | Large volume / low dew point | Higher capital |
| HVAC integrated | New builds | Best long-term |
| Cabinet mini unit | Electrical enclosure only | ~0.5 L/day+; not whole room |

## Placement rules

| Do | Don't |
| --- | --- |
| Create a dry bubble at laser air intake | Blow dust directly across open QBH |
| Pipe condensate to drain | Rely on full bucket over weekends |
| Keep clear of spark/slag paths | Block chiller condenser airflow |
| Combine with closed machine doors | Expect one small unit to dry a whole open bay |

## Sizing (rough)

| Space | Starting hint |
| --- | --- |
| ~50 m³ enclosed laser cell | 20–30 L/day rated |
| ~100 m³ | 30–50 L/day or HVAC |
| Open workshop | Often need enclosure + local unit; room-only may fail |

Dehumidifiers add heat — coordinate with [[Ambient Temperature Limits]].

## Operation with chiller

1. Start dehumidifier/AC before laser enable on humid days
2. Confirm RH and dew point margin — [[Dew Point and Chiller Setpoints]]
3. Set HT loop above dew point + 2–3 °C
4. Emission last
5. Leave dehumidifier on overnight in muggy spells if safe/drained

## Maintenance

| Task | Interval |
| --- | --- |
| Clean air filter | Monthly (sooner if dusty) |
| Check drain for algae/block | Weekly |
| Verify RH meter calibration | Seasonal |
| Empty/verify pump | Daily if no hard drain |

## Troubleshooting

| Symptom | Action |
| --- | --- |
| RH won't fall | Undersized; open doors; wet processes nearby |
| Unit ices up | Low ambient; dirty filter; OEM defrost issue |
| Water on floor | Drain fail — risk for electrics |
| Still get head sweat | HT still too low; or local RH at head higher than room average |

## Related notes

- [[Workshop Humidity and Condensation]]
- [[Dual-Temperature Chiller Circuits]]
- [[Fiber Laser Site Requirements]]
- [[Dew Point and Chiller Setpoints]]

## Sources

- Yihai dew point alarm guide (dehumidifier placement)
- Novanta condensation bulletin
- Sieme summer anti-condensation guide
