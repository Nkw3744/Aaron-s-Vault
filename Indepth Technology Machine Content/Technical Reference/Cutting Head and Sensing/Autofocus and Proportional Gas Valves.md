---
aliases:
  - proportional gas valve laser
  - autofocus laser head
type: technical-reference
category: cutting-head
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: CypCut field definitions, BOCHU manual summaries, head OEM docs
status: generic reference — verify against nameplate and project drawing
---

# Autofocus and Proportional Gas Valves

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Motorized focus vs fixed focus, and proportional assist-gas pressure control in the head/panel — how CypCut layer fields map to hardware.

## Autofocus (motorized focus)

| Topic | Detail |
| --- | --- |
| Mechanism | Motor moves collimating/focusing group under CNC command |
| CypCut field | **Cut Focus** — position relative to nozzle tip (convention varies) |
| Zero / sign | Confirm on installed head before copying internet recipes |
| Calibration | Focal test on coupon or OEM procedure |
| Fixed-focus heads | Shim packs / manual adjust — record mechanical setting per recipe |

Local context: autofocus wiring appears in Gweike 3015GAII family manuals; verify installed head.

### Autofocus troubleshooting

| Symptom | Check |
| --- | --- |
| Focus drift mid-job | Encoder; collision; thermal; loose mount |
| Same number, different result after head swap | Zero convention changed |
| Motor alarms | Cable; limit; bind after crash |

## Proportional gas valve

| Function | Detail |
| --- | --- |
| Command | CypCut **Gas pressure** layer field |
| Hardware | PWM/current-driven valve at head or gas panel |
| Feedback | Open-loop common; some closed-loop with sensor |

**Static regulator ≠ cut pressure.** Measure under pierce/cut — [[Gas Regulators and PRVs]].

### Supply margin

```
Bulk PRV → machine inlet → proportional valve → nozzle
```

If inlet sags, commanded pressure cannot be reached regardless of CypCut number.

## Piercing vs cutting pressure

Many recipes use:

- Lower or staged pierce pressure
- Ramp to cut pressure after penetration
- Extra puffing (gas-only) after pierce

Mis-set pierce → window splash (worse on galvanized) — [[Zn and Coated Material Fume Notes]].

## Interaction with nozzles and height

| Change | Recheck |
| --- | --- |
| Nozzle diameter | Gas flow and focus window |
| Ceramic/nozzle seat | Capacitance cal — [[Capacitive Height Sensing BCS100]] |
| Gas type in layer | Physical gas must match |

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Pressure command no effect | Solenoid; coil; layer gas type; enable |
| Slow pressure response | Undersized supply; sticky valve |
| Pressure overshoot | Tuning; failed feedback sensor |
| Good static, weak cut | Dynamic supply / Cv |

## Related notes

- [[Gweike 3015GAII 3 kW CypCut Cutting Parameter Setting]] — field definitions
- [[Assist Gas Overview]]
- [[Cutting Head Nozzles and Ceramics]]
- [[Cutting Parameters Index]]

## Sources

- BOCHU CypCut user manual process layer definitions
- Gweike 3015GAII family installation manual (autofocus reference)
- Field proportional-valve diagnosis
