---
aliases:
  - oxygen laser cutting
  - O2 assist gas
type: technical-reference
category: assist-gas
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, industry cutting practice
status: generic reference — verify against nameplate and project drawing
---

# Oxygen Assist Gas

Return to [[Assist Gas Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Carbon steel cutting with exothermic assist, regulator sizing, and safety.

## Role in cutting

Oxygen reacts with iron in the kerf, adding heat and enabling higher speeds on thick mild steel. The edge is oxidized (dark scale) — usually unacceptable for stainless or cosmetic stainless-adjacent parts.

## Specifications (typical)

| Parameter | Value |
| --- | --- |
| Purity | >99.6% |
| Regulator output range | 0.05–1.2 MPa (0.5–12 bar) typical |
| Regulator input | ≥15 MPa rated for HP cylinder/dewar |
| Flow | Depends on thickness and kW — rises with thickness |

## When to use O₂

- Thick carbon/mild steel where speed matters
- Structural parts where edge oxide is acceptable or will be machined
- **Avoid** as first choice on stainless, galvanized (zinc fume), or pre-painted sheet

## Installation

1. Separate O₂ line from N₂ — never share a regulator
2. Use O₂-clean components (no oil-contaminated fittings from shop air tools)
3. Flashback arrestor where required by local code on cylinder setups
4. Vaporizer on liquid O₂ if supply is cryogenic
5. Set controller layer to O₂ before test cut

## Normal operation

- Stable flame-cut-like edge on CS; minimal top dross when tuned
- Pressure increases with thickness (OEM tables in CypCut library)
- Preheat/pierce may use different pressure than cut phase

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Excessive dross | Low pressure, high speed, focus off | Tune pierce; measure dynamic pressure |
| Wide kerf | Too much O₂ | Reduce pressure |
| Alarm on low gas | Cylinder empty; change before zero | Keep residual per [[Assist Gas Overview]] |
| Pop on pierce | Pressure too high for thin sheet | Reduce pierce pressure stage |

## Safety

> [!danger] O₂ enrichment hazard
> Never use O₂ for blowing dust off clothes or workpieces. Leaks in enclosed spaces increase fire intensity. Ventilate. No oil on O₂ fittings.

## Related notes

- [[Gas Regulators and PRVs]]
- [[Nitrogen Assist Gas]]
- [[Fiber Laser Power Classes]]

## Sources

- GWK installation checklist (oxygen purity and regulator table)
