---
aliases:
  - assist gas laser cutting
  - cutting gas overview
type: technical-reference
category: assist-gas
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, Arcus gas setup, BLMA installation guide
status: generic reference — verify against nameplate and project drawing
---

# Assist Gas Overview

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Choosing O₂, N₂, or air; purity and pressure planning; gas path overview. Start here before the gas-specific deep notes.

> [!warning] Dynamic pressure matters
> Regulator gauge at rest ≠ pressure under cut flow. Measure at the head during pierce/cut.

## Three assist gases

| Gas | Typical use | Edge quality | Deep note |
| --- | --- | --- | --- |
| Oxygen (O₂) | Mild/carbon steel | Oxidized, exothermic | [[Oxygen Assist Gas]] |
| Nitrogen (N₂) | Stainless, Al, bright CS | Clean, minimal oxide | [[Nitrogen Assist Gas]] |
| Compressed air | Thin CS, cost-sensitive | Some oxidation | [[Compressed Air Cutting]] |

## Purity requirements (typical OEM)

| Gas | Minimum purity |
| --- | --- |
| O₂ | >99.6% |
| N₂ (cutting) | ≥99.99% |
| Air (cutting) | Dry, oil-free after filtration |

## Pressure ranges (indicative)

| Gas | Supply | Regulated cut range (typical) |
| --- | --- | --- |
| O₂ | Cylinder/dewar/bulk | 0.05–1.2 MPa |
| N₂ | Dewar/bulk/PSA+booster | 0.2–3.0 MPa |
| Air | Screw + treatment | Up to ~3.0 MPa on many heads |

Regulators: [[Gas Regulators and PRVs]]. Pipework: [[Gas Pipework and Fittings]].

## Gas path diagram

```mermaid
flowchart LR
    supply[BulkCylinderPSA]
    prv[PressureRegulator]
    solenoid[SolenoidValves]
    prop[ProportionalValve]
    head[CuttingHeadNozzle]
    supply --> prv --> solenoid --> prop --> head
```

Proportional control: [[Autofocus and Proportional Gas Valves]].

## Material selection quick guide

| Material | Common first choice |
| --- | --- |
| Mild steel thin | N₂ or air |
| Mild steel thick | O₂ |
| Stainless | N₂ |
| Aluminum | N₂ or air |
| Galvanized | N₂ preferred; fume caution — [[Zn and Coated Material Fume Notes]] |
| Copper/brass | N₂; reflectivity caution |

Recipes: [[Cutting Parameters Index]].

## Installation checklist

1. Identify gases; label lines both ends
2. Size regulators for **input** pressure
3. Copper/stainless hard line near head
4. Filters/check valves per OEM
5. Leak test at 1.1× working
6. Purge after gas changes
7. Never fully empty cylinders — keep residual

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Edge oxidation on SS | N₂ purity/pressure |
| Blow-out on pierce | Pressure too high for thickness |
| Yellow/black SS edge | Contaminated N₂ / wrong layer gas |
| Pressure unstable | Undersized regulator/supply |
| Oil on lens (air cut) | [[Air Filtration Stages]] |

## Related notes

- [[PSA Nitrogen Generators]]
- [[Compressor Sizing by Laser Power]]
- [[Fiber Laser Power Classes]]

## Sources

- GWK fiber laser installation requirements (gas table)
- Arcus CNC laser installation checklist (gas section)
