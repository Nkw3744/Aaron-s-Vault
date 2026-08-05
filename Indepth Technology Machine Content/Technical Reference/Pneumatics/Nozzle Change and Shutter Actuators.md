---
aliases:
  - nozzle changer actuator
  - laser shutter cylinder
type: technical-reference
category: pneumatics
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Head OEM options, field service notes
status: generic reference — verify against nameplate and project drawing
---

# Nozzle Change and Shutter Actuators

Return to [[Pneumatic Cylinders in Laser Systems]] · [[Technical Reference Index]]

> [!info] When to open this note
> Automatic nozzle magazines and internal beam shutters — pneumatic service points.

## Automatic nozzle changer (ANC)

If fitted:

- Carousel or linear magazine indexed by cylinder + motor
- Alignment critical — mis-index crashes head
- After change: verify capacitance cal — [[Capacitive Height Sensing BCS100]]

### Service checks

| Check | Frequency |
| --- | --- |
| Magazine position sensors | Monthly |
| Cylinder cushions | Listen for end-stroke bang |
| Nozzle seat cleanliness | Each change cycle |
| Software nozzle ID matches physical | Every setup |

## Beam shutter actuator

Internal safety shutter blocks beam path when:

- Door open (interlocked)
- Maintenance mode
- Some systems during traverse

Failure modes:

- Shutter stuck open → safety violation — **do not override**
- Stuck closed → no beam — check air and solenoid

Often **single-failure-sensitive** — follow OEM lockout procedure.

## Solenoid valves

- 24 VDC common on import machines
- Manual override button for service only with LOTO
- Exhaust mufflers where high cycle noise

## Related notes

- [[Cutting Head Nozzles and Ceramics]]
- [[FRL Units and Shop Air Plumbing]]

## Sources

- Raytools/Precitec ANC documentation summaries
- Laser safety interlock practice
