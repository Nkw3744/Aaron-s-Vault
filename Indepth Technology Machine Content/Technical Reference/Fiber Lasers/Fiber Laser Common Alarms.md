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
> First-pass routing from alarm message to subsystem. Follow linked deep notes for step-by-step diagnosis.

## Alarm routing map

| Subsystem | Deep reference |
| --- | --- |
| Chiller E1–E6, flow | [[CW Series Chiller Alarm Codes]], [[Chiller Troubleshooting Flowchart]] |
| Dew point / condensation | [[Dew Point and Chiller Setpoints]], [[Workshop Humidity and Condensation]] |
| Height / capacitance | [[Height Sensor Alarm Reference]], [[Capacitive Height Sensing BCS100]] |
| Gas pressure | [[Assist Gas Overview]], [[Gas Regulators and PRVs]] |
| Fiber / interlock | [[Fiber Cable Cooling and Interlocks]] |
| Source over-temp | [[Laser Water Chillers]], [[Cooling Water Quality]] |

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

Exact codes are OEM-specific (IPG, Raycus, MAX, etc.). Common patterns:

| Pattern | Likely cause | Action |
| --- | --- | --- |
| High temp / overheat | Chiller, low flow, high ambient | Chiller first |
| Interlock open | QBH not seated, door, cable interlock | [[Fiber Cable Cooling and Interlocks]] |
| Back reflection | Wrong nozzle, contaminated window, high reflect material | Optics inspection |
| Emission disabled | External E-stop, key switch, software inhibit | Safety chain |

## Gas-related symptoms (may not alarm)

| Symptom | Likely cause |
| --- | --- |
| Yellow stainless edge | Low N₂ purity or pressure |
| Burnt lens air cut | Oil or water in air line |
| Pressure drop under cut | Undersized regulator or supply |
| O₂ low alarm | Empty dewar; change before full depletion |

See [[Nitrogen Assist Gas]], [[Compressed Air Cutting]].

## Extraction alarms

| Symptom | Likely cause |
| --- | --- |
| High ΔP alarm | Clogged filters |
| Weak suction at head | Duct leak, undersized fan |
| Dust in cabinet | Negative pressure lost |

See [[Filter Stages and Maintenance]], [[Ductwork and Static Pressure]].

## Safe response order

1. **Stop emission** if optics, head crash, or unknown fault
2. **Note exact alarm text** and screenshot event log
3. **Identify subsystem** using table above
4. **Physical inspect** before resetting (nozzle, water, gas, ground)
5. **Clear root cause** — avoid alarm reset loops
6. **Document** on machine work log

## Related notes

- [[Fiber Laser Commissioning Sequence]]
- [[Fiber Laser Power Classes]]

## Sources

- CW-5200 user manual alarm tables
- Arcus capacitive sensor troubleshooting guide
- BCS100 field documentation summaries
