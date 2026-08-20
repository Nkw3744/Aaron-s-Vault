---
aliases:
  - pneumatic cylinders laser
  - air cylinder laser machine
type: technical-reference
category: pneumatics
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: Machine OEM pneumatic schematics, general industrial pneumatics practice
status: generic reference — verify against nameplate and project drawing
---

# Pneumatic Cylinders in Laser Systems

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Where cylinders appear on laser cutters, how they are supplied, sizing reminders, leak diagnosis, and how to tell control-air problems from cutting-gas problems.

> [!warning] Two air systems
> Shop/control air (≈5–7 bar) for cylinders is **not** the same as high-pressure cutting assist air (often 10–30 bar). Never tee HP cutting air into cylinder circuits.

## Role on a laser cell

Pneumatic cylinders convert shop compressed air into linear (or rotary) motion for machine auxiliaries. They are not part of the optical path, but when they fail the machine often looks "dead" or unsafe: doors will not lock, dampers will not open, nozzle changers jam, shutters will not prove closed.

Do not confuse cylinder on/off valves with the **proportional assist-gas valve** that meters cutting pressure — that is covered in [[Autofocus and Proportional Gas Valves]].

## Common applications

| Application | Typical cylinder type | Notes |
| --- | --- | --- |
| Nozzle changer magazine | Compact double-acting | See [[Nozzle Change and Shutter Actuators]] |
| Beam shutter | Short stroke, fast; often spring-return | Safety-critical |
| Table clamp / dogs | Single-acting spring return | Hold sheet against vibration |
| Gas valve pilot | Small bore on/off | Pilots larger process valves |
| Dust damper / zone damper | Rotary vane or linear | Extraction zone control — [[Ductwork and Static Pressure]] |
| Lift door / enclosure | Guided linear (rodless or twin rod) | Side-load sensitive |
| Pallet change / shuttle | Large bore double-acting | Often separate air drop |
| Scrap / drawer locks | Compact | Interlocked with cycle |

## Supply air requirements

| Parameter | Typical |
| --- | --- |
| Pressure | 5–7 bar (70–100 psi) at machine FRL |
| Quality | Filtered; lubricated **only if OEM specifies** |
| Source | Shop ring main — not laser cutting HP train |
| Treatment | [[FRL Units and Shop Air Plumbing]] |

Cutting-air train (screw compressor → dryer → 0.01 µm filters) is for the **head**. Cylinder air can share a dirty shop compressor only if the FRL and drains are maintained — water in cylinders is a top field complaint.

## Force and sizing reminder

Approximate force (N) ≈ pressure (bar) × piston area (cm²) × 10.

| Bore (mm) | Area (cm²) | Force at 6 bar (approx.) |
| --- | --- | --- |
| 16 | 2.0 | ~120 N |
| 25 | 4.9 | ~295 N |
| 32 | 8.0 | ~480 N |
| 40 | 12.6 | ~755 N |
| 50 | 19.6 | ~1180 N |

Allow margin for:

- Seal friction and side load
- Spring return force opposing extend
- Acceleration of guided masses (doors)

Stroke must clear physical stops with cushion or flow control — slamming accelerates seal wear and can trip proximity switches falsely.

## Mounting and alignment

| Rule | Why |
| --- | --- |
| Clevis / eye aligned with load | Side load destroys rod seals |
| Guided load for long strokes | Prevents rod bend |
| Soft start / flow controls | Avoids end-stroke hammer |
| Sensors at both ends when used for interlocks | Prove position, not just "commanded" |

## Installation checklist

1. Branch shutoff valve upstream of FRL
2. FRL oriented correctly (filter bowl down); auto drain working
3. Regulator set to OEM pressure; lock knob after set
4. Lubricator drip rate per OEM — or remove if dry-air zone
5. Soft-start or progressive fill if large door cylinders
6. Reed / proximity sensors adjusted; cable strain-relieved
7. Pneumatic schematic in cabinet door pocket, marked with actual pressures
8. Label each solenoid ("shutter", "damper Z1", etc.)

## Leak diagnosis method

1. Isolate machine branch; note pressure hold time on gauge after shutoff
2. Soap-test fittings, then mufflers (blocked muffler ≠ leak but slows return)
3. Listen at cylinder rod seals under pressure (extend and retract)
4. Check quick-exhaust valves and silencers for continuous hiss
5. Ultrasonic leak detector useful in noisy shops

A continuous compressor short-cycle with laser idle often points to control-air leaks, not cutting-gas use.

## Troubleshooting

| Symptom | Likely causes | Actions |
| --- | --- | --- |
| All actuators slow | Low shop pressure; clogged FRL; undersized supply pipe | Check ring main; clean filter; measure at FRL outlet |
| One cylinder slow | Flow control closed; kinked tube; sticky spool | Adjust speed screws; replace tube; cycle valve manually |
| Intermittent position | Sensor gap; sticking spool; weak solenoid voltage | Adjust sensor; clean valve; measure 24 V under load |
| Creep under load | Seal wear; check valve leakage; vertical load | Rebuild cylinder; add pilot check if OEM allows |
| Bang at end of stroke | No cushion; flow too open | Set cushions / restrictors |
| Oil mist on workpiece | Lubricator over-fed | Reduce drip or remove for that zone |
| Water from muffler | Failed FRL drain; wet ring main | Drain daily; fix dryer upstream |

## Common field mistakes

- Using cutting-air HP regulator as cylinder supply — seals blow, dangerous
- Over-lubricating "to help" — oil on height sensor ceramics and windows
- Ignoring muffler clog — return stroke fails, interlock never makes
- Bypassing shutter or door cylinder sensors to clear alarms

## Related notes

- [[Nozzle Change and Shutter Actuators]]
- [[FRL Units and Shop Air Plumbing]]
- [[Air Compressors for Laser Cutting]] — separate HP system
- [[Autofocus and Proportional Gas Valves]] — not a cylinder

## Sources

- General industrial pneumatics practice (ISO 4414 concepts)
- Typical laser machine auxiliary pneumatic layouts
