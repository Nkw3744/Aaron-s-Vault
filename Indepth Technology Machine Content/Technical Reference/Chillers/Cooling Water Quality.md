---
aliases:
  - chiller water quality
  - deionized water laser
type: technical-reference
category: chillers
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: CW-5200 manual, GWK install checklist, BLMA guide
status: generic reference — verify against nameplate and project drawing
---

# Cooling Water Quality

Return to [[Laser Water Chillers]] · [[Technical Reference Index]]

> [!info] When to open this note
> What water to fill, change intervals, corrosion control, and conductivity awareness.

> [!danger] Never use tap water
> Minerals scale micro-channels; conductivity rises; flow blocks → source failure.

## Approved water types

| Type | Use |
| --- | --- |
| Distilled | Preferred fill |
| Deionized (DI) | Preferred fill |
| Purified / softened | Only if OEM allows |
| **Forbidden** | Tap, mineral, hard well water, oily fluids, particulate coolants |

CO₂ systems may specify stricter conductivity — [[CO2 Chiller and Gas Requirements]].

## Conductivity practice

| Practice | Detail |
| --- | --- |
| Baseline at commissioning | Record on machine hub |
| Rising trend | Contamination/scale → plan change |
| Meter fitted | Log weekly in harsh environments |

CW-series manuals emphasize purity even when no live conductivity display exists.

## Anticorrosive additive

For loops with carbon-steel components:

- Add OEM-specified inhibitor per volume
- Avoid automotive coolants with silicates unless approved

Winter glycol: [[Antifreeze and Winter Operation]].

## Change interval

| Practice | Interval hint |
| --- | --- |
| Standard shop | ~3 months |
| High ambient / dirty | Monthly visual |
| After leak / bio growth | Immediate flush |

### Change procedure

1. Drain with laser and chiller off
2. Flush with clean DI if sediment
3. Refill to green zone (not overfill mark)
4. Run; bleed; recheck level after loop fills
5. Log date

## Fill level

Sight gauge **green zone** — middle to upper. After connecting machine, volume drops as hoses fill — top up again.

## Catastrophic water in source

Outer glass wet on some modules → do not power laser; source replacement likely.

## Related notes

- [[Laser Water Chillers]]
- [[Chiller Troubleshooting Flowchart]]
- [[CW Series Chiller Alarm Codes]]
- [[Dual-Temperature Chiller Circuits]]

## Sources

- CW-5200 user manual (water type)
- GWK installation checklist (distilled/purified water)
- BLMA chiller commissioning guide
