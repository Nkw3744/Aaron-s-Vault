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
> What water to fill the chiller with, change intervals, and corrosion control.

> [!danger] Never use tap water
> Minerals scale laser micro-channels; conductivity rises; flow blocks → source failure.

## Approved water types

| Type | Use |
| --- | --- |
| Distilled water | Preferred fill |
| Deionized (DI) water | Preferred fill |
| Purified / softened water | Acceptable if OEM allows |
| **Forbidden** | Tap water, mineral water, well water with hardness |

Also forbidden: oily liquids, particulate-laden coolant, undiluted glycol as sole fill without OEM approval.

## Conductivity (general guidance)

Many fiber OEMs target low conductivity for direct source cooling. CW-series manuals emphasize purity over a specific number on display. If conductivity meter fitted:

- Record baseline at commissioning
- Rising trend → contamination or scale → plan change

Some CO₂ systems specify different chemistry — [[CO2 Chiller and Gas Requirements]].

## Anticorrosive additive

For loops containing **carbon steel** components (some chiller tanks, external heat exchangers):

- Add OEM-specified corrosion inhibitor quantity per volume
- Do not use automotive coolant unless explicitly approved (silicates can gel)

## Change interval

| Practice | Interval hint |
| --- | --- |
| Standard shop | ~3 months |
| High ambient / hard use | Monthly inspect color |
| After leak or biological growth | Immediate full flush |

Procedure:

1. Drain loop with laser and chiller off
2. Flush with clean DI if sediment present
3. Refill to green zone
4. Run bleed; check level
5. Log date on chiller or machine hub

## Fill level

Use sight gauge **green zone** — middle to upper. "FULL" mark often means overfill when loop is empty. After connecting machine, recheck — volume drops as hoses fill.

## Water in laser source (catastrophic)

If outer glass on fiber module shows water: **do not power laser**. Source replacement likely. See BRM Lasers chiller support notes on tube inspection.

## Related notes

- [[Antifreeze and Winter Operation]]
- [[Chiller Troubleshooting Flowchart]]

## Sources

- CW-5200 user manual (water type)
- GWK installation checklist (distilled/purified water)
- BLMA chiller commissioning guide
