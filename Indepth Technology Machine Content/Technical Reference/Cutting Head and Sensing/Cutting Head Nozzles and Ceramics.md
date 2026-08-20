---
aliases:
  - laser cutting nozzle
  - ceramic ring cutting head
type: technical-reference
category: cutting-head
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Gweike nozzle guidance, Raytools field practice
status: generic reference — verify against nameplate and project drawing
---

# Cutting Head Nozzles and Ceramics

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Nozzle types, ceramic insulator, selection by thickness, maintenance, spares, and why most "height sensor" calls start here.

## Nozzle role

Three jobs at once:

1. Shape the assist-gas jet into the kerf
2. Act as the capacitive electrode for height follow
3. Protect the beam exit geometry (concentricity with focus)

A worn, loose, or slag-bridged nozzle ruins cut quality **and** height sensing.

## Common nozzle families

| Type | Typical use |
| --- | --- |
| Single layer | N₂/air thin sheet — e.g. 1.5 mm dia for ~1–2 mm material |
| Double layer | O₂ thick carbon steel; some high-pressure N₂ |
| OEM special / coated | High-speed packages — match exact head model |

Thread and seat geometry vary (Raytools, Precitec, WSX, etc.). Do not mix brands without confirming compatibility.

Local example: 1.5 mm single layer for 1.2 mm galvanized N₂ — [[Gweike 3015GAII 3 kW CypCut Cutting Parameter Setting]].

## Ceramic ring (body)

| Fact | Field implication |
| --- | --- |
| Insulates nozzle from head body | Crack → short → capacitance MAX / touch alarms |
| Majority of "sensor" call-outs | Replace ceramic before replacing BCS100 |
| Sealing ring must seat fully | Partial seat → C drifts when gas blows |
| Gold contacts must be clean | Oxide/slag → unstable follow |

See [[Height Sensor Alarm Reference]], [[Capacitive Height Sensing BCS100]].

## Selection reminders

| Change | Effect |
| --- | --- |
| Larger orifice | More gas flow; different edge; may need more supply Cv |
| Smaller orifice | Higher jet velocity; clog risk |
| Wrong type for gas | Poor edge; splash |
| ANC pocket mismatch | Crash or half-seat — [[Nozzle Change and Shutter Actuators]] |

## Inspection schedule

| When | Action |
| --- | --- |
| Daily start | Visual orifice; slag bead |
| After crash | New ceramic; inspect nozzle, RF cable, window |
| Poor edge quality | Check wear, diameter, concentricity |
| Height alarms | Clean/replace nozzle first |
| After auto nozzle change | Confirm full mechanical seat |
| Heavy galvanized week | Expect faster fouling — [[Zn and Coated Material Fume Notes]] |

## Cleaning and torque

| Do | Don't |
| --- | --- |
| Brass/wire brush exterior | File or drill the orifice |
| Replace bell-mouthed tips | Reuse cracked ceramics "once more" |
| Firm OEM torque | Pliers on the nozzle face |
| Alcohol on gold contacts | Oil from over-fed FRL on ceramic |

Under-torque → capacitance drift under blow. Over-torque → cracked ceramic.

## Spares kit (service truck)

- 2× of each common nozzle diameter for the heads you support
- 2× ceramic bodies (+ seals)
- 1× SMA/RF cable
- Protective windows (common sizes)
- Capacitance cal plate (clean bare steel)

## Process links

Gas chemistry and pressure: [[Assist Gas Overview]], [[Autofocus and Proportional Gas Valves]].  
Window contamination after nozzle splash: [[Fiber Connector Cleaning and Inspection]].

## Related notes

- [[Capacitive Height Sensing BCS100]]
- [[Height Sensor Alarm Reference]]
- [[Assist Gas Overview]]
- [[Nozzle Change and Shutter Actuators]]
- [[Cutting Parameters Index]]

## Sources

- Gweike cutting parameter nozzle selection tables
- Yihai Raytools service practice (ceramic crack prevalence)
- Field ANC and slag-bridge diagnosis
