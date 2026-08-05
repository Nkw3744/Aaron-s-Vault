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
> Stainless and bright-edge cutting, purity requirements, supply options (dewar vs PSA).

## Role in cutting

Nitrogen is an inert assist: it blows molten metal from the kerf without reacting. Produces bright edges on stainless and aluminum. Requires **higher pressure and flow** than oxygen on many applications.

## Specifications (typical)

| Parameter | Value |
| --- | --- |
| Purity (cutting) | ≥99.99% (4N) |
| Purity (some bright SS apps) | 99.995%+ preferred |
| Output pressure range | 0.2–3.0 MPa (2–30 bar) at head |
| HP supply | Dewar, bulk tank, or PSA + booster |
| Flow (indicative) | ~1.5 m³/min @ ≤3 kW; ~2.2 m³/min @ >3 kW |

Flow table: [[Fiber Laser Power Classes]].

## Supply options

| Source | Best for | Notes |
| --- | --- | --- |
| Liquid N₂ dewar | Most production shops | Vaporizer required; steady flow |
| Bulk tank | High consumption | Contract supply |
| PSA generator | On-site generation | Needs clean dry air feed — [[PSA Nitrogen Generators]] |
| Gas cylinders | **Not** production | Exhaust in ~20 min on continuous cut |

## Why purity matters

Low purity → yellow/gold oxide on stainless, inconsistent edge, faster nozzle wear. Contamination often traced to:

- Wrong regulator or mixed lines
- PSA not reaching setpoint purity
- Booster sucking air if buffer tank low

## Installation checklist

1. Dedicated N₂ regulator rated for input pressure (15 MPa class common)
2. Booster and HP bottle bank if cutting above PSA output
3. Line material: stainless or copper; avoid permeable hose on HP sections
4. Filter at machine inlet per OEM
5. Record purity certificate or analyzer reading at commissioning

## Normal operation

- Bright silver edge on SS when pressure and focus correct
- Higher pitch noise at high N₂ pressure — normal
- Consumption scales with orifice/nozzle diameter and duty cycle

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Yellow/gold SS edge | Purity or pressure | Verify 4N; measure under flow |
| Edge burr | Low pressure, worn nozzle | Increase pressure; swap nozzle |
| Pressure collapse mid-cut | Undersized booster/storage | [[Nitrogen Booster and HP Storage]] |
| Cost spike | Leak, pierce time too long | Leak test; tune pierce |

## PSA plant cross-reference

If shop uses on-site N₂: [[Nitrogen System Pressure Setpoints]], [[Nitrogen System Troubleshooting]].

## Related notes

- [[Compressed Air Cutting]] — lower cost alternative for some CS
- [[Zn and Coated Material Fume Notes]] — N₂ on galvanized still produces zinc fume

## Sources

- GWK installation requirements (nitrogen purity and flow)
- South-Tek laser cutting nitrogen systems reference
