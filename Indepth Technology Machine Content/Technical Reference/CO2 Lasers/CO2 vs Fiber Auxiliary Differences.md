---
aliases:
  - fiber vs CO2 auxiliary
  - CO2 fiber differences install
type: technical-reference
category: co2-lasers
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: Arcus, BLMA, multi-OEM install comparisons
status: generic reference — verify against nameplate and project drawing
---

# CO2 vs Fiber Auxiliary Differences

Return to [[CO2 Laser Cutters]] · [[Fiber Laser Cutters]] · [[Technical Reference Index]]

> [!info] When to open this note
> Side-by-side auxiliary differences for installers and service techs who work both technologies — what to reuse from the fiber library and what to rethink.

## Quick comparison table

| Auxiliary | Fiber laser | CO₂ laser |
| --- | --- | --- |
| **Beam delivery** | QBH fiber — [[QBH Fiber Delivery Cable]] | Mirrors, bellows, alignment |
| **Chiller** | CW dual-loop; DI water; HT anti-condensation | Often larger; sometimes lower setpoint — [[CO2 Chiller and Gas Requirements]] |
| **Resonator gas** | None (solid state) | He/N₂/CO₂ 99.999% class possible |
| **Assist gas** | O₂/N₂/air high pressure | Similar for metal; lower assist on organics |
| **Air compressor** | 16 bar screw for air cut | Less common on pure organic shops |
| **N₂ PSA** | Common for SS fiber production | Same if metal CO₂ cutting |
| **Extraction** | Metal particulate primary | + VOC/odor — carbon stage |
| **Height sense** | Capacitive on metal | May differ / limited on non-conductive |
| **Electrical** | High kW, 380 V class | Total kW often higher incl. blower |
| **Condensation** | QBH/head dew point critical | Mirror/window condensation risk |
| **Startup** | Chiller → enable | Warmup, gas purge, then enable |

## Shared auxiliaries (same reference notes apply)

These topics apply to **both**, with parameter differences only:

| Topic | Note |
| --- | --- |
| Assist gas purity & regulators | [[Assist Gas Overview]], [[Gas Regulators and PRVs]] |
| Pipework & leak test | [[Gas Pipework and Fittings]] |
| Fume capture principles | [[Laser Fume Extraction Overview]] |
| Electrical supply quality | [[Laser Electrical Supply Requirements]] |
| Grounding / EMC | [[Grounding and EMC Isolation]] |
| Control pneumatics | [[Pneumatic Cylinders in Laser Systems]] |
| Site clearances | [[Installation Clearances and Foundations]] |
| Humidity / dew point physics | [[Workshop Humidity and Condensation]], [[Dew Point and Chiller Setpoints]] |

## Installer mindset shifts

| Fiber habit | CO₂ adjustment |
| --- | --- |
| Check QBH interlock & bend radius | Check mirror cleanliness and multi-mirror alignment |
| Dual chiller Lo/Hi setpoints | May be single large loop; read OEM °C |
| Metal dust cartridges | Add carbon for acrylic/wood/VOC |
| Cap height follow always | Verify sensing mode vs material conductivity |
| Coupon recipe from CypCut fiber library | Different process physics — do not paste fiber tables into CO₂ |
| "No resonator gas" | Budget He/N₂/CO₂ logistics and leak integrity |

## Extraction differences in practice

| Contaminant | Fiber metal cut | CO₂ organic cut |
| --- | --- | --- |
| Fine metal oxide | Primary | Sometimes (if metal) |
| VOC / odor | Secondary (coatings) | Primary |
| Fire load | Hot slag / sparks | Flammable offcuts & fumes |
| Filter emphasis | Cartridge / HEPA | + activated carbon |

See [[Filter Stages and Maintenance]], [[Zn and Coated Material Fume Notes]] (coatings apply to both).

## Chiller differences in practice

| Concern | Fiber | CO₂ |
| --- | --- | --- |
| Typical package | CW-5200/6000 dual-temp | Larger industrial unit common |
| Head anti-sweat | HT loop ~30–32 °C | Still respect dew point on cold optics |
| Fasting / freeze | Same glycol/heat rules | Same physics |
| Water chemistry | DI/distilled | Often stricter conductivity specs |

## Commissioning sequence contrast

**Fiber:** [[Fiber Laser Commissioning Sequence]] (chiller → fiber mate → height cal → coupons).

**CO₂ (extra steps):** resonator gas on and leak-tight → warmup/purge → mirror alignment verification → lens check → then assist gas and extraction → coupons. Do not skip purge because "fiber doesn't need it."

## Quoting / customer education

When a customer compares fiber vs CO₂ quotes, auxiliaries often decide real cost:

- Fiber: PSA N₂ or HP air plant for metal production
- CO₂: resonator gas + larger chiller + VOC extraction + alignment skill availability

Point them at [[Fiber Laser Power Classes]] vs this note rather than optical kW alone.

## Indepth fleet

Primary machines are fiber. Use this note when:

- Supporting a customer CO₂ machine
- Explaining why fiber site prep differs from an old CO₂ cell reuse
- Training new techs on technology boundaries

## Related notes

- [[CO2 Laser Cutters]]
- [[CO2 Chiller and Gas Requirements]]
- [[Fiber Laser Cutters]]
- [[Technical Reference Index]]

## Sources

- BLMA fiber/CO₂ installation guides
- Arcus environmental and installation documentation
- Field practice crossing technologies
