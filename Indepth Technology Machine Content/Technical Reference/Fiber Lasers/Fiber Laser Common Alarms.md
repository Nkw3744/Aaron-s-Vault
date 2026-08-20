---
aliases:
  - fiber laser alarms
  - laser fault codes overview
type: technical-reference
category: fiber-lasers
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: OEM alarm lists, chiller manuals, height-controller field guides
status: generic reference — verify against nameplate and project drawing
---

# Fiber Laser Common Alarms

Return to [[Fiber Laser Cutters]] · [[Technical Reference Index]]

> [!info] When to open this note
> First-pass routing from alarm message to subsystem, before you commit to a deep troubleshooting path. Follow the linked deep notes for step-by-step diagnosis once you know which subsystem is involved.

## Alarm routing map

| Subsystem | Deep reference |
| --- | --- |
| Chiller E1–E6, flow | [[CW Series Chiller Alarm Codes]], [[Chiller Troubleshooting Flowchart]] |
| Dew point / condensation | [[Dew Point and Chiller Setpoints]], [[Workshop Humidity and Condensation]] |
| Height / capacitance | [[Height Sensor Alarm Reference]], [[Capacitive Height Sensing BCS100]] |
| Gas pressure | [[Assist Gas Overview]], [[Gas Regulators and PRVs]] |
| Fiber / interlock | [[Fiber Cable Cooling and Interlocks]] |
| Source over-temp | [[Laser Water Chillers]], [[Cooling Water Quality]] |
| Extraction | [[Filter Stages and Maintenance]], [[Ductwork and Static Pressure]] |
| Electrical / grounding-related instability | [[Grounding and EMC Isolation]], [[Laser Electrical Supply Requirements]] |

## Chiller alarms (CW series common)

| Alarm | Meaning | First actions |
| --- | --- | --- |
| E1 | Ambient too high | Improve ventilation; reduce room temp |
| E2 | Water too hot | Check load, refrigerant, filter, setpoint vs dew point |
| E3 | Water too cold | Raise setpoint; check sensor |
| E4 | Room sensor fault | Replace sensor |
| E5 | Water sensor fault | Replace sensor |
| E6 / flow | Low or no flow | Level, kinks, blocked laser loop, pump |

Full table: [[CW Series Chiller Alarm Codes]].

## Height controller alarms (typical text)

| Message | Likely cause | Action |
| --- | --- | --- |
| Z-axis touching board | Nozzle on sheet, slag bridge, loose nozzle | Clean/replace nozzle; recalibrate |
| Capacitance is 0 | Open circuit — SMA unplugged, broken RF cable | Inspect RF path |
| Capacitance large / MAX | Short — cracked ceramic, water in head | Replace ceramic; dry head |
| Sensor not stable | Ground loop, EMI, loose RF | Ground check; route cables |
| Follow out of range | Warped sheet, bad cal data | Recalibrate on flat plate |
| Network timeout (BCS100) | IP mismatch, cable fault | Check Ethernet and subnet |

Full table: [[Height Sensor Alarm Reference]].

## Laser source alarms (generic)

Exact codes are OEM-specific (IPG, Raycus, MAX Photonics, and others each use their own numbering and wording). Common patterns across brands:

| Pattern | Likely cause | Action |
| --- | --- | --- |
| High temp / overheat | Chiller, low flow, high ambient | Chiller first |
| Interlock open | QBH not seated, door, cable interlock | [[Fiber Cable Cooling and Interlocks]] |
| Back reflection | Wrong nozzle, contaminated window, high reflect material | Optics inspection |
| Emission disabled | External E-stop, key switch, software inhibit | Safety chain |
| Low power output | Diode degradation, dirty QBH end cap, low current command | Compare against commissioning baseline power reading |
| Fiber fuse / fault | Catastrophic fiber damage — often from severe back reflection or crush damage | Do not re-enable; escalate to OEM |

> [!danger] Back-reflection alarms are not nuisance alarms
> Repeated back-reflection events without correcting the root cause (dirty optics, wrong material for the process, wrong nozzle standoff) risk permanently damaging the source. Treat every back-reflection trip as a stop-and-inspect event, not a reset-and-continue event.

## Gas-related symptoms (may not alarm)

| Symptom | Likely cause |
| --- | --- |
| Yellow stainless edge | Low N₂ purity or pressure |
| Burnt lens air cut | Oil or water in air line |
| Pressure drop under cut | Undersized regulator or supply |
| O₂ low alarm | Empty dewar; change before full depletion |
| Inconsistent piercing | Pressure staging wrong for material thickness |
| Excessive dross despite correct N₂ pressure | Nozzle wear, focus drift, or speed too high for gas delivery |

See [[Nitrogen Assist Gas]], [[Compressed Air Cutting]].

## Extraction alarms

| Symptom | Likely cause |
| --- | --- |
| High ΔP alarm | Clogged filters |
| Weak suction at head | Duct leak, undersized fan |
| Dust in cabinet | Negative pressure lost |
| Fan trips on overload | Filter loading too high, motor issue, or duct blockage forcing fan outside its curve |

See [[Filter Stages and Maintenance]], [[Ductwork and Static Pressure]].

## Motion and encoder alarms (brief)

Not covered in deep detail in this library (motion control is highly controller-specific), but the common categories a technician should recognize:

| Pattern | Likely cause |
| --- | --- |
| Servo fault / overcurrent | Mechanical binding, drive fault, encoder feedback loss |
| Soft limit trip | Position drift, homing not run after power cycle, mechanical crash history |
| Following error | Servo tuning, mechanical load change, encoder noise (sometimes grounding-related) |

If a "motion" alarm coincides with height-sensor instability or intermittent behavior, check grounding before assuming a drive or encoder hardware fault — see [[Grounding and EMC Isolation]].

## Correlating multiple alarms

A single root cause frequently produces alarms that look unrelated:

| Root cause | Alarms it can produce |
| --- | --- |
| Poor machine grounding | Height sensor instability, encoder noise, intermittent E-stop faults |
| High summer humidity | Chiller dew-point/condensation alarm, height sensor drift from moisture on ceramic, optics contamination over time |
| Undersized N₂ supply | Gas pressure alarm during long cuts, poor edge quality, booster overheat alarm on PSA systems |
| Compressor sharing laser electrical feeder | Voltage sag alarms, servo faults, control system resets — all coincide with compressor start cycles |

When two or more "unrelated" alarms started at the same time, look for one of these shared causes before troubleshooting each alarm independently.

## Safe response order

1. **Stop emission** if optics, head crash, or unknown fault
2. **Note exact alarm text** and screenshot event log
3. **Identify subsystem** using table above
4. **Physical inspect** before resetting (nozzle, water, gas, ground)
5. **Clear root cause** — avoid alarm reset loops
6. **Document** on machine work log

> [!warning] Alarm-reset loops
> Repeatedly clearing an alarm and re-running without finding the physical cause is one of the most common ways a minor fault (a loose SMA connector, a slightly low water level) becomes an expensive one (a crashed head, a damaged source). If the same alarm returns twice, stop and diagnose properly rather than resetting a third time.

## "Alarm cleared itself" — still investigate

| Pattern | Investigate |
| --- | --- |
| Clears when compressor stops | EMI / ground — [[Grounding and EMC Isolation]] |
| Clears after warmup | Flow/viscosity, cold glycol, condensation drying |
| Clears when door closed firmly | Interlock / PE / shield |
| Clears after nozzle wipe | Slag bead — fix hygiene, not only wipe |

## Cross-system quick matrix

| If you see… | Open first |
| --- | --- |
| E1–E6 / flow light | [[CW Series Chiller Alarm Codes]] |
| Capacitance / follow / touching board | [[Height Sensor Alarm Reference]] |
| Dew / condensation | [[Dew Point and Chiller Setpoints]] |
| Interlock / QBH | [[Fiber Cable Cooling and Interlocks]] |
| Yellow SS edge (may not hard-alarm) | [[Nitrogen Assist Gas]] |
| Smoke in cabin | [[Laser Fume Extraction Overview]] |

## Related notes

- [[Fiber Laser Commissioning Sequence]]
- [[Fiber Laser Power Classes]]
- [[Fiber Laser Cutters]]

## Sources

- CW-5200 user manual alarm tables
- Arcus capacitive sensor troubleshooting guide
- BCS100 field documentation summaries
