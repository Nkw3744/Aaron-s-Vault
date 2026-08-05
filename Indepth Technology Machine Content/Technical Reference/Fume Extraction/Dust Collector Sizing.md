---
aliases:
  - dust collector sizing laser
  - extraction airflow laser table
type: technical-reference
category: fume-extraction
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: ACMAN sizing guide, Arcus environmental guide
status: generic reference — verify against nameplate and project drawing
---

# Dust Collector Sizing

Return to [[Laser Fume Extraction Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Estimating required air volume (m³/h) for sheet laser downdraft tables.

## Basic formula (ACMAN method)

**Air volume (m³/h) = table area (m²) × cutting zone height (m) × air changes per hour**

| Parameter | Typical value |
| --- | --- |
| Air changes per hour | 30–50 (standard); 50–80 high dust/high power |
| Cutting zone height | Effective capture height under slats — often 0.3–0.5 m for calculation |
| Safety margin | +20–30% for stainless/aluminum fine dust |

### Example — 1.5 × 3 m table

- Area = 4.5 m²
- Height factor 0.4 m, 40 changes/h  
- Volume = 4.5 × 0.4 × 40 = **72 m³/h per "cell"** — OEM methods vary; full table often quoted 6000–10000 m³/h integrated

Use OEM machine spec when available — overrides rough calc.

## By table width (market packages)

| Table width | Typical machine class | Air volume hint (m³/h) |
| --- | --- | --- |
| 1.5 m (3015) | Small/medium fiber | 6000–8000 |
| 2.0 m (4020) | Medium power | 8000–12000 |
| 3.0–4.0 m | Large/high power | 12000–20000+ |

See [[Fiber Laser Power Classes]].

## Material adjustments

| Material | Adjustment |
| --- | --- |
| Stainless / aluminum | +20–30% volume; finer filters |
| Mild steel | Baseline |
| Galvanized | Baseline volume but **zinc fume** EHS — [[Zn and Coated Material Fume Notes]] |

## Power and speed

High kW + high feed → more fume mass rate. Size toward upper band or verify with OEM for ≥6 kW.

## Central vs single machine

| Layout | Rule |
| --- | --- |
| Single machine | Match calculated volume |
| Central plant | Sum peaks × simultaneous factor; pipe resistance ×1.2–1.5 |

## Static pressure

Fan must deliver required airflow **at system ΔP**, often ≥2000 Pa class for long duct + loaded filters — [[Ductwork and Static Pressure]].

## Related notes

- [[Filter Stages and Maintenance]]
- [[Laser Fume Extraction Overview]]

## Sources

- ACMAN laser cutting dust extraction solution sizing article
- Arcus environmental setup (ventilation requirements)
