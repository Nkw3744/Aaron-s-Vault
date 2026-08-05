---
aliases:
  - laser air compressor
  - compressor for laser cutting
type: technical-reference
category: air-compressors
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Arcus installation guide, BLMA gas guidelines
status: generic reference — verify against nameplate and project drawing
---

# Air Compressors for Laser Cutting

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Planning shop air for laser air-cutting assist — not the same as a 7 bar tools-only compressor.

## Requirements summary

| Item | Typical for laser air cutting |
| --- | --- |
| Type | Rotary screw, oil-free or well-treated oil-injected with filtration |
| Pressure | ≥1.6 MPa (16 bar) discharge class |
| Treatment | Dryer + multi-stage filtration to 0.01 µm |
| Receiver | Stabilizes flow; reduces duty cycle |
| Dedicated | Best practice: laser-dedicated treated line |

## System block diagram

```mermaid
flowchart LR
    comp[ScrewCompressor]
    sep[OilWaterSeparator]
    tank[Receiver]
    dryer[RefrigeratedDryer]
    filt[CoalescingAndFineFilter]
    laser[MachineInlet]
    comp --> sep --> tank --> dryer --> filt --> laser
```

## Installation checklist

1. Size kW and flow — [[Compressor Sizing by Laser Power]]
2. Screw vs piston — [[Screw vs Piston Compressors]]
3. Install refrigerated dryer sized for **actual** FAD at pressure dew point target (+3 °C PDP common)
4. Filters after dryer, not before
5. Auto drains on separator, dryer, filters
6. Hard pipe from treatment to laser; slope to drains
7. Do not route laser air through welder or sandblast drops
8. Electrical: often on **separate** circuit from laser — [[Laser Electrical Supply Requirements]]

## Normal operation

- Receiver cycles at moderate rate under production
- Dryer outlet temp near ambient + PDP spec
- Filter ΔP gauges in green; drain bowls dry

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Laser window oil burn | Filtration bypass or wrong filter install order |
| Pressure low at head | Undersized compressor; leaks; long small-bore pipe |
| Water in filters | Dryer failure; no drain |
| Compressor overheats | Poor ventilation; duty cycle exceeded |

## Related notes

- [[Compressed Air Cutting]]
- [[Refrigerated Dryers]]
- [[Air Filtration Stages]]
- [[FRL Units and Shop Air Plumbing]] — shop air ≠ cutting air unless fully treated

## Sources

- Arcus CNC laser installation (compressed air section)
- BLMA gas connection guidelines
