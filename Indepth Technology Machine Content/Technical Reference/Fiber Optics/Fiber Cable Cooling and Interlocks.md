---
aliases:
  - fiber cable interlock
  - QBH water cooling
type: technical-reference
category: fiber-optics
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Coherent QBH datasheet, laser safety interlock practice
status: generic reference — verify against nameplate and project drawing
---

# Fiber Cable Cooling and Interlocks

Return to [[QBH Fiber Delivery Cable]] · [[Technical Reference Index]]

> [!info] When to open this note
> Water flow to QBH, interlock circuit, and thermoswitch behavior.

## Water cooling (water-cooled QBH)

| Parameter | Typical |
| --- | --- |
| Flow | ~2 L/min |
| Max inlet pressure | ~8 bar |
| Pressure drop | ~0.9 bar at 2 L/min |
| Temperature | Follow chiller HT/LT assignment — often head loop |

Connect before first emission. Verify no leaks at quick couplers — slow drips corrode interlock pins.

## Interlock circuit

Purpose: prevent laser emission if QBH unmated or cable fault.

| Check | Method |
| --- | --- |
| Resistance | OEM spec ~3.3 kΩ ±5% plus cable length term |
| Continuity | Multimeter at source interlock pins with cable mated |
| Pin condition | Dry, unbent, no corrosion |

Open interlock → emission disabled — often reported as generic laser fault.

## Thermoswitch

Some cables include ~70 °C ±5 °C switch on connector body. Trip indicates:

- Cooling failure
- Cladding power from bad alignment
- Hot environment + no flow

Reset often requires cooling below ~30 °C.

## Integration with machine safety chain

Typical chain: E-stop → door → water flow → interlock → enable

Do not bypass interlocks for "testing" without controlled service procedure.

## Troubleshooting

| Fault | Check |
| --- | --- |
| Interlock alarm, cable OK | Pin wetness; resistance out of spec |
| QBH hot | Flow; HT setpoint; alignment |
| Intermittent enable | Loose mate; flex fatigue at connector |

## Related notes

- [[Dual-Temperature Chiller Circuits]]
- [[CW Series Chiller Alarm Codes]]
- [[Fiber Laser Common Alarms]]

## Sources

- Coherent QBH datasheet (cooling and interlock specifications)
