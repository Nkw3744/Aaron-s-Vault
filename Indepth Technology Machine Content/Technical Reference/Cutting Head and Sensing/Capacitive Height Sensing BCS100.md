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
> How capacitive height follow works (BCS100 and similar), signal path, calibration, grounding, and network basics.

## Principle

Measures capacitance between **nozzle** (electrode) and **sheet** (grounded workpiece). Controller converts C → distance → Z servo follow so cut height stays constant over warped sheet.

Not optical triangulation — purely electric field. Paint, rust, and isolation break the measurement.

## Signal path

```
Nozzle → ceramic ring → SMA/RF cable → pre-amp on head → BCS100 → Z drive / CNC
```

| Part | Role | Common failure |
| --- | --- | --- |
| Nozzle | Electrode tip | Slag bead, loose, wrong dia |
| Ceramic | Insulator | Crack (~most "sensor" faults) |
| SMA/RF | HF signal | Break, intermittent on flex |
| Pre-amp | Amplify | Moisture, impact |
| BCS100 | Cal, follow, network | Config/IP/EMI |

Family note: BCS100 appears in Gweike 3015GAII manuals — verify installed unit.

## Calibration procedure (generic)

1. Clean nozzle face and ceramic — no slag bridge
2. Torque nozzle per OEM
3. Move to centre of **clean flat bare metal**
4. Run floating-head / one-key calibration
5. Stability rating Excellent/Good
6. Test follow at traverse before full-power cut

Recalibrate after: nozzle/ceramic change, crash, ANC cycle issues, large temperature swing.

## Key parameters

| Parameter | Notes |
| --- | --- |
| Cut height | Often 0.5–1.0 mm band; material dependent |
| Lift height | Safe traverse Z |
| Follow gain | Match machine dynamics |
| DIF | Diagnostic; large values can mean poor contact |

Do not set follow height below ~0.5 mm without OEM approval.

## Grounding requirement

```
Nozzle → sheet → slats → bed → PE
```

Detail: [[Grounding and EMC Isolation]]. Poor ground → unstable C → [[Height Sensor Alarm Reference]].

## Network (BCS100 Ethernet)

- Same IP subnet as CNC
- Timeout alarms: cable, IP, EMI
- After board swap: restore OEM config

## Daily / shift checks

| Check | Pass |
| --- | --- |
| Nozzle clean | No bead |
| Follow on scrap | Smooth, no jump |
| No new alarms | — |

## Related notes

- [[Height Sensor Alarm Reference]]
- [[Cutting Head Nozzles and Ceramics]]
- [[Nozzle Change and Shutter Actuators]]
- [[Fiber Laser Common Alarms]]

## Sources

- Arcus troubleshooting capacitive sensor errors
- Pendstar BCS100 sensing issues guide
- Smart cut after-sales FAQ (THC / capacitance)
