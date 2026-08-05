---
aliases:
  - refrigerated air dryer
  - laser air dryer
type: technical-reference
category: air-compressors
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Arcus/BLMA install guides, ISO 8573 practice
status: generic reference — verify against nameplate and project drawing
---

# Refrigerated Dryers

Return to [[Air Compressors for Laser Cutting]] · [[Technical Reference Index]]

> [!info] When to open this note
> Mandatory drying stage before laser cutting air reaches the head.

> [!warning] Mandatory for laser air cutting
> Compressed air without drying will carry water vapor that condenses in lines and on the protective window.

## Function

Cools compressed air to ~3 °C pressure dew point (typical refrigerated class), condensing water for removal. Reduces liquid water reaching coalescing and fine filters.

## Selection

| Parameter | Guidance |
| --- | --- |
| Flow rating | Match or exceed compressor FAD at working pressure |
| Inlet temperature | Size derated if compressor room hot (>40 °C) |
| Pressure drop | Typically 0.2–0.5 bar — account in head pressure |
| Placement | After receiver, before fine filters |

Desiccant dryers used where very low PDP required (<−40 °C) — less common on standard fiber air-cut packages.

## Installation checklist

1. Mount vertical; clearances for fan service
2. Correct flow direction arrow
3. Auto drain on separator bowl — test daily in humid climates
4. Bypass not installed unless maintenance plan exists
5. Earth ground per manual

## Normal operation

- Condensate visible in drain during production
- Outlet air line cool to touch vs hot compressor discharge
- No continuous water at laser inlet filter bowl

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Water in laser filter | Failed dryer, bypass open, drain stuck | Service dryer; clean drain |
| Dryer alarm / high temp | Dirty condenser, poor ventilation | Clean fins; improve airflow |
| Pressure drop high | Undersized or blocked | Check ΔP; upsize |
| Oil in dryer bowl | Upstream separator failed | Fix compressor separator first |

## Related notes

- [[Air Filtration Stages]]
- [[Workshop Humidity and Condensation]] — ambient RH affects line condensation after dryer

## Sources

- Arcus CNC laser installation (refrigerated dryer mandatory)
- BLMA fiber laser installation guide
