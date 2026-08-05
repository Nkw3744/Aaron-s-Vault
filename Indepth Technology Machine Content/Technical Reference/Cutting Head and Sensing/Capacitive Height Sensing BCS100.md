---
aliases:
  - BCS100 height control
  - capacitive height sensor laser
type: technical-reference
category: cutting-head
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Arcus capacitive troubleshooting, Pendstar BCS100 guide, Smart cut FAQ
status: generic reference — verify against nameplate and project drawing
---

# Capacitive Height Sensing BCS100

Return to [[Technical Reference Index]]

> [!info] When to open this note
> How capacitive height follow works (BCS100 and similar), calibration, and hardware path.

## Principle

Measures capacitance between **nozzle** (electrode) and **sheet** (grounded workpiece). Controller converts capacitance → distance → Z servo follow during cut.

Not laser triangulation — purely electrical field.

## Signal path

```
Nozzle → ceramic ring → SMA/RF cable → pre-amplifier box on head → BCS100 controller → Z drive
```

Components:

| Part | Role |
| --- | --- |
| Nozzle | Electrode tip; must be concentric |
| Ceramic ring | Insulator; cracks cause shorts |
| SMA (RF) cable | High-frequency signal; fragile |
| Pre-amp box | Amplifies weak signal |
| BCS100 | Calibration, follow, network to CNC |

Family reference: BCS100 appears in Gweike 3015GAII manual family.

## Calibration procedure (generic)

1. Clean nozzle face and ceramic — no slag bridge
2. Firm nozzle torque per OEM
3. Move to center of **clean flat metal** plate (bare steel best)
4. Run "floating head calibration" / one-key cal in software
5. Check stability rating — should be Excellent/Good
6. Test follow at traverse speed before full power cut

Recalibrate after: nozzle change, ceramic change, crash, large temperature swing.

## Key parameters (controller)

| Parameter | Notes |
| --- | --- |
| Cut height | Often 0.5–1.0 mm band; material dependent |
| Lift height | Safe traverse Z |
| Follow gain | Match to machine dynamics |
| DIF value | Diagnostic; >30 may indicate poor contact (Smart cut FAQ) |

Do not set follow height below 0.5 mm without OEM approval — pierce splash risk.

## Grounding requirement

Sheet → slats → bed → machine ground must be low impedance. Poor ground → unstable capacitance, wandering height.

## Network (BCS100 Ethernet)

- IP in same subnet as CNC motion controller
- Timeout alarms if cable fault — check IP and physical link

## Related notes

- [[Height Sensor Alarm Reference]]
- [[Cutting Head Nozzles and Ceramics]]

## Sources

- Arcus troubleshooting capacitive sensor errors
- Pendstar BCS100 sensing issues guide
- Smart cut after-sales FAQ (THC / capacitance)
