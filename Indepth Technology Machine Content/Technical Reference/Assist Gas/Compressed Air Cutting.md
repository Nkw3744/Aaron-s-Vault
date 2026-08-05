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
> Cost-effective assist for suitable thin mild steel; compressor and filtration requirements.

> [!danger] Oil and water destroy optics
> A single oil mist event can fracture the protective window. Never bypass dryer or fine filters.

## Role

Shop compressed air replaces N₂ on selected thin carbon steel jobs. Edge will oxidize more than N₂ cut. Requires **clean, dry, oil-free** air at elevated pressure compared to shop tools.

## Typical requirements

| Parameter | Typical |
| --- | --- |
| Compressor type | Oil-free screw (preferred) |
| Discharge pressure | ≥1.6 MPa (16 bar) class common; up to ~3.0 MPa max on machine |
| Dryer | Refrigerated (mandatory) + optional desiccant |
| Filtration | Coalescing + 0.01 µm (or OEM spec) |
| Air quality class | ISO 8573-1 target 1.x.x or better for oil content |

Full chain: [[Air Filtration Stages]], [[Refrigerated Dryers]], [[Air Compressors for Laser Cutting]].

## When air cutting makes sense

- Thin mild steel (often ≤3 mm) where edge color acceptable
- High volume, cost-sensitive work
- Machine and head explicitly approved for air assist

## When to avoid

- Stainless or aluminum requiring bright edge
- Unknown compressor quality (piston without treatment)
- Any sign of oil in line

## Installation checklist

1. Dedicated screw compressor — not shared with dirty shop tools without full treatment
2. Oil-water separator at compressor outlet
3. Refrigerated dryer sized for flow and ambient
4. Coalescing filter + particulate filter at dryer outlet
5. Fine filter immediately before machine inlet
6. Auto drain traps on all separators
7. Hard pipe main run; flexible only at machine connection
8. Set CypCut layer gas type to **Air** — not N₂ with air connected

## Normal operation

- Slightly darker edge vs N₂
- Higher noise at pierce
- Filter differential pressure rises over weeks — schedule change

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Window cracks / burn spots | Oil or water | Stop; replace window; fix filtration |
| Poor cut | Low pressure under flow | Size compressor — [[Compressor Sizing by Laser Power]] |
| Water in bowl | Failed dryer or drain | Service dryer; check drains daily in humid climate |
| Variable quality | Piston compressor pulsing | Upgrade to screw + receiver |

## Related notes

- [[Screw vs Piston Compressors]]
- [[Nitrogen Assist Gas]]
- [[Gweike 3015GAII 3 kW CypCut Cutting Parameter Setting]] — air vs N₂ commissioning context

## Sources

- Arcus CNC laser installation (air cutting setup)
- BLMA fiber laser gas connection guidelines
