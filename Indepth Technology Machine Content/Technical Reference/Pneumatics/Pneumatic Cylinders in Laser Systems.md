---
aliases:
  - pneumatic cylinders laser
  - air cylinder laser machine
type: technical-reference
category: pneumatics
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: Machine OEM pneumatic schematics, general pneumatics practice
status: generic reference — verify against nameplate and project drawing
---

# Pneumatic Cylinders in Laser Systems

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Where cylinders appear on laser cutters, sizing basics, and leak diagnosis.

## Common applications

| Application | Typical cylinder type |
| --- | --- |
| Nozzle changer magazine | Compact double-acting |
| Beam shutter actuator | Short stroke, fast |
| Table clamp dogs | Single-acting spring return |
| Gas valve pilot | Small bore on/off |
| Dust damper actuators | Rotary or linear |
| Lift door / enclosure | Guided linear |

Not to confuse with **proportional assist gas valve** (electronic) — [[Autofocus and Proportional Gas Valves]].

## Supply air

- Often **shop air 5–7 bar** separate from high-pressure cutting air
- Must be filtered and lubricated per OEM — [[FRL Units and Shop Air Plumbing]]
- Do not tee cutting-air HP line to cylinders

## Selection basics (reminder)

| Parameter | Note |
| --- | --- |
| Bore | Force = pressure × area; margin for friction |
| Stroke | Physical limit switches both ends |
| Speed | Flow controls on both directions if needed |
| Mounting | Clevis alignment — side load kills seals |

## Installation

1. Filter-Regulator-Lubricator at branch
2. Soft start — no hammering into hard stops
3. Position reed switches / prox sensors reliably
4. Label pneumatic schematic sheet in cabinet door pocket

## Troubleshooting

| Symptom | Cause |
| --- | --- |
| Slow actuation | Low shop air; leak; undersized valve |
| Intermittent position | Sticking spool; weak solenoid |
| Creep | Seal wear; load on rod side |
| Oil on work | Remove lubricator if OEM specifies dry air to zone |

## Related notes

- [[Nozzle Change and Shutter Actuators]]
- [[FRL Units and Shop Air Plumbing]]

## Sources

- General industrial pneumatics practice
- Typical laser machine auxiliary pneumatic layouts
