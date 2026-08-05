---
aliases:
  - laser dust filter maintenance
  - HEPA laser extraction
type: technical-reference
category: fume-extraction
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: IP Systems, OMTech fume guide, field maintenance
status: generic reference — verify against nameplate and project drawing
---

# Filter Stages and Maintenance

Return to [[Laser Fume Extraction Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Filter types, change intervals, and ΔP monitoring for laser dust collectors.

## Typical stages

| Stage | Captures | Maintenance |
| --- | --- | --- |
| Spark trap / baffle | Sparks, coarse slag | Inspect weekly |
| Pre-filter / cyclone | Large particulate | Empty bin; replace pre-filter |
| Primary cartridge | Metal oxide dust | Pulse-clean; replace on ΔP |
| HEPA / high efficiency (if fitted) | Sub-micron | Replace per ΔP or schedule |
| Activated carbon (optional) | Odors, VOCs | CO₂ organics; saturated media change |

Metal fiber cutting usually emphasizes **particulate cartridges**; carbon added for mixed processes.

## Pulse-jet cleaning

Many collectors reverse-pulse cartridges during fan run. Check:

- Air supply to pulse valves
- Sequence timer
- Not over-pulsing (can embed dust)

## Change indicators

| Method | Action threshold |
| --- | --- |
| ΔP gauge | OEM red zone — often 1500–2500 Pa rise from clean |
| Visual smoke escape | Immediate inspection |
| Flow anemometer at hood | Drop >20% from baseline |

Plan maintenance on **loaded** performance, not calendar alone — but log dates.

## Safe filter change

> [!danger] Zinc and metal dust
> Wear respirator rated for fine particulate; follow SDS. Galvanized fume history — [[Zn and Coated Material Fume Notes]].

1. Fan off; isolate power
2. Allow chamber to settle
3. Ground cartridge to avoid static spark on aluminum dust
4. Bag cartridges; dispose per local hazardous waste rules for metal dust
5. Check seals on install

## Troubleshooting

| Symptom | Cause |
| --- | --- |
| ΔP high immediately after change | Wrong cartridge; seal missing |
| Dust in clean air plenum | Broken cartridge inner seal |
| Pulse ineffective | Low pulse air pressure |

## Related notes

- [[Ductwork and Static Pressure]]
- [[Dust Collector Sizing]]

## Sources

- IP Systems fume extraction filtration stages
- OMTech fume extractor buying guide (multi-stage filtration)
