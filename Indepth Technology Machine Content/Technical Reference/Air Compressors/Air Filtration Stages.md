---
aliases:
  - compressed air filtration laser
  - 0.01 micron filter laser
type: technical-reference
category: air-compressors
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Arcus installation guide, ISO 8573-1
status: generic reference — verify against nameplate and project drawing
---

# Air Filtration Stages

Return to [[Air Compressors for Laser Cutting]] · [[Technical Reference Index]]

> [!info] When to open this note
> Filter chain order, ratings, and maintenance for oil-free cutting air.

> [!danger] Filter order matters
> Wrong sequence (e.g. fine filter before dryer) loads elements incorrectly and passes moisture.

## Typical chain (downstream of compressor)

| Stage | Type | Removes |
| --- | --- | --- |
| 1 | Oil-water separator (at compressor) | Bulk liquid oil and water |
| 2 | Refrigerated dryer | Water vapor → liquid |
| 3 | Coalescing filter (general) | Aerosol oil, fine water |
| 4 | Coalescing filter (high efficiency) | Sub-micron oil mist |
| 5 | Particulate / fine filter (0.01 µm class) | Particles before head |

Arcus reference: multi-stage to **0.01 µm** for air cutting.

## ISO 8573-1 targets (indicative planning)

Discuss exact class with head OEM. Common target for laser air assist:

- Solid particles: Class 1 or 2
- Water: Class 4 or better after dryer
- Oil: Class 1 or 2 (≤0.01 mg/m³)

## Installation

1. Install **after** dryer only for coalescing/fine stages
2. Flow direction arrows correct
3. Bypass around filter bank discouraged
4. Last filter within 3 m of machine inlet where possible
5. Spare elements on shelf — log change dates

## Maintenance schedule (typical)

| Element | Interval hint |
| --- | --- |
| Separator at compressor | Weekly drain check; element per OEM |
| Coalescing | 2000–4000 h or ΔP rise |
| Fine 0.01 µm | 1000–2000 h or ΔP rise |
| After compressor overhaul | Change all downstream |

## Troubleshooting

| Symptom | Likely cause |
| --- | --- |
| Window contamination | Bypassed filter; wrong element |
| ΔP high immediately | Element installed backward |
| Oil in fine filter only | Missing upstream coalescer |

## Related notes

- [[Compressed Air Cutting]]
- [[Refrigerated Dryers]]
- [[Fiber Connector Cleaning and Inspection]] — if window contaminated

## Sources

- Arcus CNC laser installation (0.01 µm filtration)
- ISO 8573-1 compressed air quality classes
