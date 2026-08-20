---
aliases:
  - dust collector sizing laser
  - extraction airflow laser table
type: technical-reference
category: fume-extraction
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: ACMAN sizing guide, Arcus environmental guide, field package practice
status: generic reference — verify against nameplate and project drawing
---

# Dust Collector Sizing

Return to [[Laser Fume Extraction Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Estimating required air volume (m³/h) for sheet laser downdraft tables and choosing a collector that still performs with dirty filters.

> [!warning] OEM spigot spec wins
> If the machine manual states required airflow and static at the outlet, that overrides rough formulas below.

## Basic formula (ACMAN-style)

**Air volume (m³/h) ≈ table area (m²) × cutting zone height (m) × air changes per hour**

| Parameter | Typical planning value |
| --- | --- |
| Air changes / hour | 30–50 standard; 50–80 high dust / high power |
| Cutting zone height factor | Often 0.3–0.5 m for calculation (OEM geometry dependent) |
| Margin | +20–30% for stainless/aluminum fine dust |

### Worked example (illustrative only)

- Table 1.5 × 3.0 m → area 4.5 m²
- Height factor 0.4 m, 40 ACH  
- Volume = 4.5 × 0.4 × 40 = **72 m³/h** for that simplified "cell" math  

Integrated commercial packages for full 3015 tables are commonly quoted in the **6000–10000 m³/h** band — use OEM machine + collector pairing, not the toy example alone.

## By table width (market package hints)

| Table width | Machine class | Air volume hint (m³/h) |
| --- | --- | --- |
| 1.5 m (3015) | Small/medium fiber | 6000–8000 |
| 2.0 m (4020) | Medium power | 8000–12000 |
| 3.0–4.0 m | Large / high power | 12000–20000+ |

Cross-check [[Fiber Laser Power Classes]].

## Material and process adjustments

| Factor | Adjustment |
| --- | --- |
| Stainless / aluminum | +20–30% volume; finer filtration |
| Mild steel | Baseline |
| Galvanized | Volume similar; **ZnO exposure** — [[Zn and Coated Material Fume Notes]] |
| High kW / high speed | Upper band of range |
| Oxygen thick CS | Heavy spark/slag — spark arrestance critical |

## Static pressure must be sized too

Volume without pressure capability fails on long ducts and dirty filters. Target fan that delivers design m³/h at:

- Dirty-filter ΔP allowance
- Duct losses — [[Ductwork and Static Pressure]]
- Often ≥2000 Pa class systems for metal laser collectors (verify OEM)

## Central plant vs single machine

| Layout | Rule |
| --- | --- |
| One machine, one collector | Match calculated / OEM volume |
| Central to multiple lasers | Sum peaks × diversity factor; pipe resistance ×1.2–1.5 |
| Future second machine | Leave fan/duct margin now |

## Selection checklist

1. Machine outlet size and required Q / P from manual
2. Materials to be cut (SS/Al/Zn coated?)
3. Duct length and fittings estimate
4. Indoor recirculation vs outdoor discharge (EHS)
5. Filter type and pulse-clean air supply
6. Noise limits at property line
7. Fire/spark detection requirements
8. Spare cartridge availability

## Undersize symptoms

| Symptom | Meaning |
| --- | --- |
| Persistent haze in cabin | Q too low or leaks |
| Filters blind in days | High loading + maybe undersized media area |
| Far zones smoky | Balance / duct / fan curve |
| Smell of VOCs (organics) | Need carbon stage — not only more CFM |

## Related notes

- [[Laser Fume Extraction Overview]]
- [[Filter Stages and Maintenance]]
- [[Ductwork and Static Pressure]]
- [[Fiber Laser Site Requirements]]

## Sources

- ACMAN laser cutting dust extraction sizing article
- Arcus environmental setup (ventilation)
- Field 3015/4020 collector pairing practice
