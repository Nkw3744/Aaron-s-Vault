---
aliases:
  - air cutting fiber laser
  - compressed air assist
type: technical-reference
category: assist-gas
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Arcus installation guide, BLMA gas connection guidelines
status: generic reference — verify against nameplate and project drawing
---

# Compressed Air Cutting

Return to [[Assist Gas Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Cost-effective assist for suitable thin mild steel; compressor and filtration requirements; when to prefer N₂ instead.

> [!danger] Oil and water destroy optics
> A single oil-mist event can fracture the protective window. Never bypass dryer or fine filters.

## Role

Shop compressed air replaces N₂ on selected thin carbon-steel jobs. Edge oxidizes more than N₂. Requires **clean, dry, oil-free** air at elevated pressure versus tools air.

## Typical requirements

| Parameter | Typical |
| --- | --- |
| Compressor | Oil-free screw preferred — [[Screw vs Piston Compressors]] |
| Discharge | ≥1.6 MPa (16 bar) class common; up to ~3.0 MPa max on many heads |
| Dryer | Refrigerated mandatory — [[Refrigerated Dryers]] |
| Filtration | Coalescing + ~0.01 µm — [[Air Filtration Stages]] |
| Quality | ISO 8573 oil toward Class 1–2 |

## When air cutting makes sense

- Thin mild steel where edge color is acceptable
- High volume, cost-sensitive work
- Machine/head explicitly approved for air assist
- Treated air plant already correctly sized — [[Compressor Sizing by Laser Power]]

## When to avoid

- Stainless / aluminum bright-edge requirements → [[Nitrogen Assist Gas]]
- Unknown piston compressor quality
- Any oil in line history until plant fixed
- Galvanized without fume controls — still Zn hazard — [[Zn and Coated Material Fume Notes]]

## Installation checklist

1. Dedicated screw compressor (or dedicated treated branch)
2. Separator → receiver → dryer → coalescing → fine filter
3. Auto drains tested
4. Hard pipe; short flex at machine
5. CypCut layer gas type = **Air** (not N₂ with air connected)
6. Dynamic pressure measured under pierce
7. First hours: inspect window frequently

## Normal operation

| Observation | Meaning |
| --- | --- |
| Slightly darker edge vs N₂ | Expected |
| Stable dynamic pressure | Supply OK |
| Dry filter bowls | Treatment OK |
| Rising filter ΔP over weeks | Normal — schedule change |

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Window cracks / burn spots | Oil or water | Stop; replace window; fix filtration |
| Poor cut | Low dynamic pressure | Size/leaks — [[Air Compressors for Laser Cutting]] |
| Water in bowl | Dryer/drain | Service dryer |
| Variable quality | Piston pulsing | Screw + receiver |
| Oil smell at drains | Separator failure | Fix compressor before cutting |

## Recipe discipline

Keep separate CypCut layers and validation records for air vs N₂ — do not silently substitute. See [[Cutting Parameters Index]] and local [[Gweike 3015GAII 3 kW CypCut Cutting Parameter Setting]].

## Related notes

- [[Assist Gas Overview]]
- [[Air Filtration Stages]]
- [[PSA Nitrogen Generators]] — alternative assist path

## Sources

- Arcus CNC laser installation (air cutting setup)
- BLMA fiber laser gas connection guidelines
