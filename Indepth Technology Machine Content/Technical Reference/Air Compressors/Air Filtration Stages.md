---
aliases:
  - compressed air filtration laser
  - 0.01 micron filter laser
  - ISO 8573 laser air
type: technical-reference
category: air-compressors
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Arcus installation guide, ISO 8573-1, field filter practice
status: generic reference — verify against nameplate and project drawing
---

# Air Filtration Stages

Return to [[Air Compressors for Laser Cutting]] · [[Technical Reference Index]]

> [!info] When to open this note
> Filter chain order, ratings, ΔP monitoring, and maintenance for oil-free cutting air to the laser head.

> [!danger] Filter order matters
> Fine filter before dryer loads incorrectly and passes moisture. Bypassing "temporarily" is a common window-failure story.

## Typical chain (downstream of compressor)

| Stage | Type | Removes |
| --- | --- | --- |
| 1 | Oil-water separator (at compressor) | Bulk liquid oil/water |
| 2 | Refrigerated dryer | Water vapor → liquid — [[Refrigerated Dryers]] |
| 3 | Coalescing (general) | Aerosol oil, fine water |
| 4 | Coalescing (high efficiency) | Sub-micron oil mist |
| 5 | Particulate / fine (~0.01 µm class) | Particles before head |

Arcus-style air-cutting packages call for multi-stage filtration to **~0.01 µm**.

## ISO 8573-1 planning targets (discuss with OEM)

| Contaminant | Common planning class |
| --- | --- |
| Solids | Class 1 or 2 |
| Water | Class 4 or better after dryer |
| Oil | Class 1 or 2 (≤0.01 mg/m³ class targets) |

Exact class is head/OEM dependent — when in doubt, cleaner is safer for optics.

## Installation rules

1. Coalescing/fine stages **after** dryer only
2. Flow arrows correct — reverse install ruins elements
3. Avoid permanent bypass; if present, lockable + tagged
4. Last fine filter within ~3 m of machine inlet when practical
5. Auto drains on bowls; pipe away from walkways
6. Spare elements on shelf; date installed on bowl tag
7. Differential pressure gauges where fitted — log clean baseline

## Maintenance intervals (indicative)

| Element | Interval hint |
| --- | --- |
| Compressor separator | OEM hours; watch oil in downstream bowls |
| Coalescing | 2000–4000 h or ΔP rise |
| Fine 0.01 µm | 1000–2000 h or ΔP rise |
| After compressor overhaul | Change all downstream |
| After oil event | Change all; inspect windows |

## Troubleshooting

| Symptom | Likely cause |
| --- | --- |
| Window oil burn | Bypass; wrong order; separator failure |
| ΔP high immediately after change | Element backward; wrong micron rating |
| Oil only in fine filter | Missing/failed upstream coalescer |
| Water in fine bowl | Dryer/drain fault — not "bad micron rating" |
| Smell of oil at muffler drains | Fix compressor before blaming laser |

## Verification after service

1. Run 30–60 min under load
2. Inspect first bowls — dry, no oil film
3. Measure dynamic cut pressure
4. Inspect protective window on next break — [[Fiber Connector Cleaning and Inspection]]

## Related notes

- [[Compressed Air Cutting]]
- [[Refrigerated Dryers]]
- [[Screw vs Piston Compressors]]
- [[FRL Units and Shop Air Plumbing]] — control air is a different train

## Sources

- Arcus CNC laser installation (0.01 µm filtration)
- ISO 8573-1 compressed air quality classes
- Field optics failure analysis (oil mist)
