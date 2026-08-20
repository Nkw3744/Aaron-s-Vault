---
aliases:
  - nozzle changer actuator
  - laser shutter cylinder
  - ANC laser
type: technical-reference
category: pneumatics
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Head OEM options (Raytools/Precitec-class ANC), field service notes, laser safety interlock practice
status: generic reference — verify against nameplate and project drawing
---

# Nozzle Change and Shutter Actuators

Return to [[Pneumatic Cylinders in Laser Systems]] · [[Technical Reference Index]]

> [!info] When to open this note
> Automatic nozzle magazines (ANC), beam shutter cylinders, and the solenoid valves that drive them. Use when diagnosing a failed auto-change, a shutter interlock fault, or commissioning a head that has ANC options.

> [!warning] Safety-critical actuators
> Beam shutters and door-related pneumatics sit in the machine safety chain. Never defeat a shutter interlock with a jumper "just to test." Use OEM service mode and LOTO.

## Why these actuators matter

Most of the laser's pneumatics are convenience or process (clamps, dampers). Two exceptions are safety-critical or process-critical:

1. **Beam shutter** — must reliably block emission when the door opens or the controller commands safe state
2. **Automatic nozzle changer (ANC)** — if misaligned, the head can crash into the magazine or leave a half-seated nozzle, destroying the ceramic and capacitive sensing path

Shop air for these is **control air** (typically 5–7 bar), not cutting assist air. See [[FRL Units and Shop Air Plumbing]].

---

## Automatic nozzle changer (ANC)

### What it is

Optional head or gantry-mounted magazine that stores several nozzles (often 4–8). On a CypCut/FSCUT or similar command, the head moves to a change position, a cylinder or motor indexes the magazine, and a pneumatic or spring clamp swaps the nozzle.

| Architecture | How it works | Field notes |
| --- | --- | --- |
| Rotary carousel | Cylinder or stepper indexes pockets | Alignment of pocket to head axis is critical |
| Linear magazine | Cylinder slides rack under nozzle | Watch end-of-stroke cushions |
| Manual rack with auto clamp | Operator preloads; machine only clamps | Lower risk; still needs seat cleanliness |

### Alignment and crash risk

Mis-index by even a few millimetres can:

- Drive the ceramic into the wrong pocket wall
- Leave the nozzle half-threaded so capacitance floats
- Bend the SMA/RF cable or pre-amp mount during the change motion

After any ANC service or crash:

1. Jog to change position with emission disabled
2. Verify pocket centre under nozzle visually
3. Run one change cycle empty (no cut)
4. Recalibrate capacitive sensor — [[Capacitive Height Sensing BCS100]]
5. Confirm software nozzle ID / diameter matches the physical nozzle — wrong ID gives wrong gas/pressure assumptions in some libraries

### Service checks

| Check | Frequency | Pass criteria |
| --- | --- | --- |
| Magazine position sensors (reed/prox) | Monthly | Both ends report cleanly; no chatter |
| Cylinder cushions / flow controls | Monthly | Soft end-stroke, no metal bang |
| Nozzle seat and pocket cleanliness | Every change cycle | No slag, oxide flakes, or oil |
| Clamp force / spring return | Quarterly | Nozzle fully seated; cannot spin free by hand |
| Software nozzle ID vs physical | Every setup | Matches diameter and type (single/double) |
| SMA cable clearance during change | After any head work | Cable not pinched at end of stroke |

### ANC troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Change cycle aborts mid-way | Sensor not made; air pressure low | Check FRL set pressure; sensor gap |
| Nozzle drops during cut | Clamp under-torque or worn spring | Replace clamp kit; torque per OEM |
| Capacitance unstable after change | Nozzle not fully seated; dirty ceramic contact | Reseat; clean; recalibrate |
| Magazine jams | Pocket deformed; foreign object | Inspect pockets; straighten or replace |
| Head crashes into magazine | Soft limit / change position wrong | Re-teach change position; check origin |

---

## Beam shutter actuator

### Function

An internal shutter (blade or paddle) in the cutting head or beam path blocks the laser when:

- Enclosure / door interlock is open
- Controller is in maintenance or pause modes that require beam inhibit
- Some machines park the shutter closed during rapid traverse (OEM-dependent)

The actuator is usually a short-stroke, fast double-acting (or spring-return) cylinder with end-position sensing.

### Failure modes (treat seriously)

| Failure | Risk | Response |
| --- | --- | --- |
| Stuck **open** | Beam can exit when door open — Class 4 hazard | Stop use. Do not bypass. Repair or replace. |
| Stuck **closed** | No cutting beam; may look like source fault | Check air, solenoid, mechanical bind, sensor |
| Sensor false "closed" | Controller thinks shutter safe when open | Verify sensor with mechanical confirmation |
| Slow close | Race against door open time | Flow controls, spring force, air pressure |

> [!danger] Stuck open shutter
> Treat as a safety system failure. Isolate laser enable. Do not run production with a temporary jumper across the shutter closed switch.

### Service procedure (generic)

1. LOTO electrical and gas as required by OEM
2. Confirm zero energy / emission inhibited
3. Cycle shutter with manual solenoid override **only** under LOTO and with beam path verified blocked by other means if OEM allows
4. Listen for free motion; feel for bind
5. Confirm both end sensors
6. Restore auto mode; door-open test with emission key in safe position

---

## Solenoid valves

| Item | Typical field value |
| --- | --- |
| Coil voltage | 24 VDC common on import fiber machines |
| Manual override | Push-button or screwdriver override — service only with LOTO |
| Exhaust | Fit mufflers on high-cycle valves; clogged muffler slows return |
| Spool sticking | Contaminated shop air — fix FRL first |

### Coil check

- Measure coil resistance vs spare (open = burned coil)
- Voltage at coil under command (not only at PLC output if long cable)
- LED on valve body (if fitted) vs actual motion — LED on but no motion = mechanical/air issue

---

## Interaction with height sensing and nozzles

ANC and shutter work are frequent sources of secondary height faults:

- Half-seated nozzle after auto-change → [[Height Sensor Alarm Reference]]
- Damaged ceramic from magazine crash → [[Cutting Head Nozzles and Ceramics]]
- Oil from lubricator mist on nozzle/ceramic if FRL over-oiled → clean and correct lubricator drip rate

---

## Commissioning checklist (ANC + shutter)

1. FRL pressure set to OEM (often 5–6 bar) — [[FRL Units and Shop Air Plumbing]]
2. All ANC and shutter sensors report correct state at rest
3. One full auto nozzle change each pocket; confirm seat
4. Capacitance calibration after change
5. Door open → shutter closed within OEM time; emission inhibit proven
6. Document nozzle map (pocket vs diameter) on machine hub

## Related notes

- [[Pneumatic Cylinders in Laser Systems]]
- [[Cutting Head Nozzles and Ceramics]]
- [[FRL Units and Shop Air Plumbing]]
- [[Capacitive Height Sensing BCS100]]
- [[Height Sensor Alarm Reference]]

## Sources

- Raytools / Precitec-class ANC documentation summaries
- Laser safety interlock practice (shutter in emission chain)
- Field service notes on magazine crash and capacitance drift after auto-change
