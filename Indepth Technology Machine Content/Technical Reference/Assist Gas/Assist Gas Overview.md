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
> Choosing O₂, N₂, or air; purity and pressure planning; piping overview.

> [!warning] Dynamic pressure matters
> Regulator gauge at rest ≠ pressure under cut flow. Measure at the head during a pierce or cut.

## Three assist gases

| Gas | Typical use | Edge quality | Notes |
| --- | --- | --- | --- |
| Oxygen (O₂) | Mild/carbon steel | Oxidized, exothermic assist | Faster on thick CS; not for bright SS |
| Nitrogen (N₂) | Stainless, aluminum, bright CS | Clean, minimal oxide | High purity and pressure |
| Compressed air | Thin CS, cost-sensitive | Some oxidation | Requires dry oil-free chain |

Deep dives: [[Oxygen Assist Gas]], [[Nitrogen Assist Gas]], [[Compressed Air Cutting]].

## Purity requirements (typical OEM)

| Gas | Minimum purity |
| --- | --- |
| O₂ | >99.6% |
| N₂ (cutting) | ≥99.99% |
| N₂ (laser cavity purge, if used) | 99.999% class |
| Air (cutting) | Dry, oil ≤0.01 mg/m³ class after filtration |

## Pressure ranges (indicative)

| Gas | Supply | Regulated cut range (typical) |
| --- | --- | --- |
| O₂ | Cylinder/dewar/bulk | 0.05–1.2 MPa (0.5–12 bar) |
| N₂ | Dewar/bulk/PSA+booster | 0.2–3.0 MPa (2–30 bar) |
| Air | Screw compressor + treatment | Up to ~3.0 MPa max on many heads |

Regulators: [[Gas Regulators and PRVs]].

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

Proportional valve control: [[Autofocus and Proportional Gas Valves]].

## Material selection quick guide

| Material | Common first choice |
| --- | --- |
| Mild steel thin | N₂ or air |
| Mild steel thick | O₂ |
| Stainless | N₂ |
| Aluminum | N₂ or air |
| Galvanized | N₂ preferred; fume caution — [[Zn and Coated Material Fume Notes]] |
| Copper/brass | N₂; reflectivity caution |

Machine recipes: [[Cutting Parameters Index]].

## Installation checklist

1. Identify gas types machine will use; label lines at source and head
2. Size regulators for **input** pressure (N₂ HP often 15 MPa class in)
3. Use copper or stainless hard line near head; avoid low-grade hose on HP N₂
4. Install check valves and filters where OEM specifies
5. Leak test at 1.1× working pressure with soap or electronic detector
6. Purge lines before first cut after gas change
7. Never fully empty cylinders — keep residual pressure above atmospheric

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Edge oxidation on SS | N₂ purity, pressure under flow |
| Blow-out on pierce | Pressure too high for thickness |
| Yellow/black SS edge | Contaminated N₂ or wrong gas selected in layer |
| Pressure unstable | Regulator undersized; booster tank empty |
| Oil on lens (air cut) | Filtration chain — [[Air Filtration Stages]] |

## Related notes

- [[Gas Pipework and Fittings]]
- [[PSA Nitrogen Generators]]
- [[Compressor Sizing by Laser Power]]

## Sources

- GWK fiber laser installation requirements (gas table)
- Arcus CNC laser installation checklist (gas section)
