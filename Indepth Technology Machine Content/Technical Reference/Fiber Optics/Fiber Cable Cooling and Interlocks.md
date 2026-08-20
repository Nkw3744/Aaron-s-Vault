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
> Water flow to water-cooled QBH, interlock resistance, thermoswitch behavior, and how these sit in the emission enable chain.

## Water cooling (water-cooled QBH)

| Parameter | Typical (Coherent-class) |
| --- | --- |
| Flow | ~2.0 L/min |
| Max inlet pressure | ~8 bar |
| Pressure drop | ~0.9 bar at 2 L/min |
| Loop assignment | Often HT / head loop — [[Dual-Temperature Chiller Circuits]] |

Connect and verify leak-free **before** first emission. Slow drips corrode interlock pins and short RF paths.

### Cooling checklist

1. Correct IN/OUT on QBH
2. Flow visible (if indicator fitted) or measured
3. No seepage at ferrule after 15 min run
4. Return temperature plausible vs supply
5. HT setpoint above dew point — [[Dew Point and Chiller Setpoints]]

Air-cooled QBH/RQB variants exist for lower power only — do not assume air-cool on multi-kW cutters.

## Interlock circuit

Purpose: inhibit emission if QBH unmated, cable broken, or connector unsafe.

| Check | Method |
| --- | --- |
| Resistance | ~3.3 kΩ ±5% + cable length term (OEM) |
| Continuity | Meter at source interlock with cable mated |
| Pins | Dry, straight, no green corrosion |
| Mate torque | OEM N·m — loose = intermittent |

Open interlock → emission disabled — may appear as generic "laser fault" or "interlock" on HMI — [[Fiber Laser Common Alarms]].

## Thermoswitch

Some cables include ~70 °C ±5 °C switch on the connector.

| Trip suggests | Action |
| --- | --- |
| No/low water flow | Restore cooling first |
| Cladding power (alignment/contamination) | Inspect optics; clean — [[Fiber Connector Cleaning and Inspection]] |
| Hot ambient + marginal flow | Improve cooling / ambient |

Reset often needs cooling below ~30 °C.

## Safety chain position

Typical enable chain (simplified):

```
E-stop → doors → chiller/flow OK → QBH interlock → key/enable → emission
```

Never jumper QBH interlock for "testing" without controlled OEM procedure and beam-path safety.

## Troubleshooting

| Fault | Checks |
| --- | --- |
| Interlock alarm, cable looks seated | Wet pins; resistance OOS; broken conductor in armor |
| QBH hot | Flow; HT assignment; contamination; bend damage |
| Intermittent enable when gantry moves | Flex fatigue at connector; drag-chain pinch — [[Fiber Cable Bend Radius and Routing]] |
| Trip after all-day cutting | Thermal; dirty window raising back-reflection/heat |

## Related notes

- [[QBH Fiber Delivery Cable]]
- [[Laser Water Chillers]]
- [[CW Series Chiller Alarm Codes]]
- [[Fiber Laser Commissioning Sequence]]

## Sources

- Coherent QBH datasheet (cooling and interlock specifications)
- Field interlock troubleshooting on import fiber packages
