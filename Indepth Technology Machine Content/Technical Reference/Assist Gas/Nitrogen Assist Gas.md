---
aliases:
  - nitrogen laser cutting
  - N2 assist gas
type: technical-reference
category: assist-gas
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, South-Tek N2 systems reference
status: generic reference — verify against nameplate and project drawing
---

# Nitrogen Assist Gas

Return to [[Assist Gas Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Stainless and bright-edge cutting — purity, pressure, supply options (dewar vs PSA), and yellow-edge diagnosis.

## Role

Nitrogen is an inert assist: blows molten metal from the kerf without oxidizing. Produces bright edges on stainless and aluminum. Needs **higher pressure and flow** than oxygen on many jobs.

## Specifications (typical)

| Parameter | Value |
| --- | --- |
| Purity (cutting) | ≥99.99% (4N) |
| Bright SS apps | 99.995%+ preferred |
| Output at head | 0.2–3.0 MPa (2–30 bar) typical range |
| Supply | Dewar/bulk or PSA + booster |
| Flow hint | ~1.5 m³/min @ ≤3 kW; ~2.2 m³/min @ >3 kW |

Flow context: [[Fiber Laser Power Classes]].

## Supply options

| Source | Best for | Notes |
| --- | --- | --- |
| Liquid N₂ dewar | Most production | Vaporizer required |
| Bulk tank | High consumption | Contract supply |
| PSA generator | On-site | Needs clean dry air — [[PSA Nitrogen Generators]] |
| Gas cylinders | **Not** production | Exhaust in minutes on continuous cut |

## Why purity matters

Low purity → yellow/gold oxide on stainless, inconsistent edge, faster nozzle wear. Trace contamination to:

- Mixed/wrong lines
- PSA not at setpoint purity
- Booster sucking air on low buffer
- Leaks pulling atmosphere

## Installation checklist

1. Dedicated N₂ regulator rated for inlet (15 MPa / bank class as needed)
2. Booster + HP bank if cutting above PSA buffer pressure
3. Stainless/copper hard line; minimal HP hose
4. Inlet filter per OEM
5. Purity certificate or analyzer at commissioning
6. Dynamic pressure test under cut

## Normal operation

| Observation | Meaning |
| --- | --- |
| Bright silver SS edge | Process + purity OK |
| High pitch at high P | Normal |
| Stable dynamic P | Supply sized OK |

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Yellow/gold SS edge | Purity or pressure | Analyzer; dynamic P |
| Edge burr | Low P; worn nozzle | Raise P; swap nozzle |
| Pressure collapse mid-cut | Booster/storage | [[Nitrogen Booster and HP Storage]] |
| Cost spike | Leak; long pierce | Leak test; tune pierce |

## Galvanized note

N₂ preferred for edge but **does not eliminate Zn fume** — [[Zn and Coated Material Fume Notes]].

## Related notes

- [[Compressed Air Cutting]]
- [[Nitrogen System Troubleshooting]]
- [[Gas Regulators and PRVs]]
- [[Cutting Parameters Index]]

## Sources

- GWK installation requirements (nitrogen purity and flow)
- South-Tek laser cutting nitrogen systems reference
