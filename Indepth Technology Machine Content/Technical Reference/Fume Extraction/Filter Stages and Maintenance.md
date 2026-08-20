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
> Filter types, change intervals, pulse-cleaning, ΔP monitoring, and safe cartridge handling for laser dust collectors.

## Typical stages

| Stage | Captures | Maintenance |
| --- | --- | --- |
| Spark trap / baffle | Sparks, coarse slag | Inspect weekly |
| Pre-filter / cyclone | Large particulate | Empty bin; replace pre-filter |
| Primary cartridge | Metal oxide dust | Pulse-clean; replace on ΔP |
| HEPA / high efficiency (if fitted) | Sub-micron | Replace per ΔP/schedule |
| Activated carbon (optional) | Odors, VOCs | Essential for many CO₂ organics |

Metal fiber cutting emphasizes particulate cartridges; add carbon for coatings/organics — [[Zn and Coated Material Fume Notes]], [[CO2 vs Fiber Auxiliary Differences]].

## Pulse-jet cleaning

| Check | Why |
| --- | --- |
| Pulse air supply pressure | Weak pulse → permanent blinding |
| Sequence timer / valves | Stuck valve = one dirty cartridge forever |
| Not over-pulsing | Can embed dust in media |
| Compressed air quality to pulse | Wet pulse air damages valves |

## Change indicators

| Method | Action threshold |
| --- | --- |
| ΔP gauge | OEM red zone — often large rise from clean baseline |
| Visible smoke escape | Immediate inspection |
| Hood airflow drop | >~20% from commissioning baseline |
| Smell breakthrough (carbon) | Carbon saturated |

Log clean ΔP at commissioning — [[Ductwork and Static Pressure]].

## Safe filter change

> [!danger] Fine metal and zinc dust
> Wear respirator rated for fine particulate per risk assessment. Do not dry-shake cartridges indoors.

1. Fan off; isolate power/LOTO
2. Allow chamber to settle
3. Ground cartridge handling on aluminum dust systems (static)
4. Bag cartridges; dispose per local hazardous waste rules for metal dust
5. Inspect seals; install new set with correct orientation
6. Restart; confirm ΔP near clean baseline
7. Record date/hours on collector log

## Troubleshooting

| Symptom | Cause |
| --- | --- |
| ΔP high right after change | Wrong cartridge; missing seal; plastic shipping cap left on |
| Dust in clean air plenum | Broken media / seal leak |
| Pulse ineffective | Low pulse air; failed diaphragm |
| Short cartridge life | Undersized collector; wrong media; galv/SS loading — [[Dust Collector Sizing]] |

## Maintenance schedule (indicative)

| Task | Interval |
| --- | --- |
| Bin empty / spark trap | Daily–weekly by duty |
| ΔP log | Each shift on heavy production |
| Pulse system check | Monthly |
| Full cartridge set | Per ΔP or OEM hours |
| Carbon stage | Per odor/VOC breakthrough |

## Related notes

- [[Ductwork and Static Pressure]]
- [[Dust Collector Sizing]]
- [[Laser Fume Extraction Overview]]
- [[Zn and Coated Material Fume Notes]]

## Sources

- IP Systems fume extraction filtration stages
- OMTech fume extractor buying guide (multi-stage)
- Field cartridge change practice on metal laser cells
