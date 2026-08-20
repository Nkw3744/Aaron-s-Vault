---
aliases:
  - oxygen laser cutting
  - O2 assist gas
type: technical-reference
category: assist-gas
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, industry cutting practice, oxygen safety practice
status: generic reference — verify against nameplate and project drawing
---

# Oxygen Assist Gas

Return to [[Assist Gas Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Carbon steel cutting with exothermic O₂ assist — purity, regulators, process expectations, and oxygen-specific safety.

> [!danger] Oxygen enrichment hazard
> Never use O₂ to blow dust off clothes or workpieces. Oil + oxygen = fire risk. Ventilate enclosed spaces. Use O₂-clean components.

## Role in cutting

Oxygen reacts with iron in the kerf (exothermic oxidation), adding heat beyond the laser alone. That enables higher speeds and thicker mild/carbon steel capability versus inert assist on the same kW. The tradeoff is an **oxidized edge** (dark scale) — usually unacceptable for stainless cosmetic edges or parts that need bright oxide-free finish.

## Specifications (typical OEM)

| Parameter | Typical value |
| --- | --- |
| Purity | >99.6% |
| Regulator output range | 0.05–1.2 MPa (0.5–12 bar) |
| Regulator input rating | ≥15 MPa for HP cylinder/dewar service |
| Flow | Rises strongly with thickness and nozzle orifice |

Always measure **dynamic** pressure under pierce/cut — [[Gas Regulators and PRVs]].

## When to use O₂

| Use | Avoid as first choice |
| --- | --- |
| Thick mild/carbon steel for speed | Stainless bright edge |
| Structural parts where oxide OK or will be machined | Galvanized first trials (Zn fume + process) — [[Zn and Coated Material Fume Notes]] |
| OEM library O₂ layers for CS | Pre-painted sheet without SDS review |

## Supply options

| Source | Notes |
| --- | --- |
| HP cylinders | Small shops; change before empty; residual pressure practice |
| Liquid O₂ + vaporizer | Production flow |
| Bulk | High volume |

Keep residual pressure in cylinders — do not run to absolute zero (moisture/contaminant ingress risk; machine low-gas alarms).

## Installation checklist

1. Dedicated O₂ regulator — never share with N₂ without full O₂-clean protocol
2. O₂-clean fittings; no oily shop-air parts
3. Flashback arrestor where required by local code / OEM
4. Vaporizer on liquid supply; ice/frost management
5. Line labeled OXYGEN at source and machine
6. Leak test with O₂-compatible method
7. Controller layer set to O₂ before test cut
8. Separate from cutting-air and N₂ hard lines — [[Gas Pipework and Fittings]]

## Normal operation — what good looks like

| Observation | Meaning |
| --- | --- |
| Stable oxidized edge on CS | Process in window |
| Controlled spark/ejecta | Pressure/speed appropriate |
| Pierce establishes without excessive blow-out | Pierce pressure staged correctly |
| No oil film anywhere on O₂ train | Cleanliness OK |

## Process troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Heavy dross | Low pressure, high speed, focus off | Measure dynamic P; tune focus/speed |
| Wide kerf / burned top | Too much O₂ / power | Reduce pressure or power |
| Pop on pierce | Pressure too high for thin sheet | Lower pierce stage |
| Incomplete cut | Pressure/speed/focus; purity | Coupon ladder — [[Cutting Parameters Index]] |
| Low-gas alarm | Empty supply | Change with residual left |
| Unstable pressure | Undersized regulator/vaporizer | Upsize; check freeze |

## Safety detail

| Rule | Reason |
| --- | --- |
| No oil/grease on O₂ wetted parts | Hydrocarbon + O₂ fire |
| No O₂ for cleaning | Clothing fire / enrichment |
| Ventilate pits / small rooms | Enrichment increases fire intensity |
| Correct materials | Some elastomers unsuitable for O₂ |
| Cylinder handling | Chained; correct regulator |

## Interaction with other systems

- Extraction still required — oxidized fume/particulate — [[Laser Fume Extraction Overview]]
- Do not store O₂ hoses coiled with oily air hoses
- Proportional valve and CypCut gas type must match physical O₂ — [[Autofocus and Proportional Gas Valves]]

## Related notes

- [[Assist Gas Overview]]
- [[Nitrogen Assist Gas]]
- [[Gas Regulators and PRVs]]
- [[Fiber Laser Power Classes]]
- [[Cutting Parameters Index]]

## Sources

- GWK installation checklist (oxygen purity and regulator table)
- Industrial oxygen handling practice
- Field mild-steel O₂ cutting experience
