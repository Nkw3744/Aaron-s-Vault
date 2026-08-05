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
> Motorized focus vs fixed focus, proportional assist-gas pressure control in head/panel.

## Autofocus (motorized focus)

- Collimating/focusing lens group moved by motor under CNC command
- **Cut Focus** field in CypCut layers — position relative to nozzle tip
- Zero convention and sign vary by head — confirm before copying internet recipes
- Calibration: focal length test on coupon or OEM procedure

Fixed-focus heads: shim packs or manual adjustment — record mechanical setting per recipe.

Local context: autofocus wiring mentioned in Gweike 3015GAII family manual.

## Proportional gas valve

| Function | Detail |
| --- | --- |
| Command | CypCut **Gas pressure** layer field |
| Hardware | PWM/current-driven valve at head or gas panel |
| Feedback | Some systems open-loop; high-end closed-loop pressure sensor |

**Static regulator gauge ≠ cut pressure.** Measure under pierce/cut flow at test port.

## Piercing vs cutting pressure

Many recipes use:

- Lower pressure or staged pierce
- Ramp to cut pressure after penetration
- Extra puffing (gas-only cooldown)

Mis-set pierce → splash on window, especially galvanized — [[Zn and Coated Material Fume Notes]].

## Interaction with FRL/regulator upstream

```
Bulk PRV → machine inlet → proportional valve → nozzle
```

Proportional valve needs minimum inlet pressure margin — if inlet sag, cut pressure cannot reach setpoint.

See [[Gas Regulators and PRVs]].

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Pressure command no effect | Solenoid; proportional valve coil; layer gas type |
| Slow pressure response | Undersized supply; sticky valve |
| Focus drift | Autofocus encoder; collision; temperature |

## Related notes

- [[Gweike 3015GAII 3 kW CypCut Cutting Parameter Setting]] — CypCut field definitions
- [[Assist Gas Overview]]
- [[Cutting Head Nozzles and Ceramics]]

## Sources

- BOCHU CypCut user manual process layer definitions
- Gweike 3015GAII family installation manual (autofocus reference)
