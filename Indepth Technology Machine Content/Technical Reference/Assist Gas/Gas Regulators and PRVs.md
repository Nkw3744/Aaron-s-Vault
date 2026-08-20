---
aliases:
  - gas regulators laser
  - PRV cutting gas
type: technical-reference
category: assist-gas
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist regulator table, field dynamic pressure practice
status: generic reference — verify against nameplate and project drawing
---

# Gas Regulators and PRVs

Return to [[Assist Gas Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Selecting and setting pressure-reducing valves for O₂ and N₂; input vs output ratings; why static gauge readings lie during a cut.

## Regulator vs proportional valve

| Device | Location | Function |
| --- | --- | --- |
| PRV / regulator | Bulk, cylinder, or HP bank outlet | Steps supply down toward machine inlet |
| Proportional valve | Head or gas panel | CNC sets cut pressure per CypCut layer |

Proportional hardware: [[Autofocus and Proportional Gas Valves]].

## Typical OEM regulator specs (GWK reference)

| Service | Input rating | Output range |
| --- | --- | --- |
| Nitrogen PRV | ≥15 MPa | 0.2–3.0 MPa |
| Oxygen PRV | ≥15 MPa | 0.05–1.2 MPa |

HP N₂ banks (~300 bar) need regulators rated for that inlet — [[Nitrogen Booster and HP Storage]].

## Selection rules

1. **Input rating** exceeds maximum supply with margin
2. **Flow capacity (Cv)** holds pressure under peak pierce/cut flow
3. Two-stage regulation helps (bank → line → machine)
4. Separate regulators per gas; O₂-clean components for oxygen
5. Upstream and downstream gauges for diagnosis
6. Correct seat/elastomer materials for the gas

## Setting procedure (field)

1. Close machine inlet valve
2. Open supply slowly; set **static** downstream pressure
3. Open machine; run pierce at trial settings
4. Measure at head or test port **during flow**
5. Adjust PRV and/or CypCut layer pressure to match recipe
6. Lock adjuster; record value on machine hub

> [!tip] Dynamic vs static
> A regulator showing 14 bar static may deliver ~10 bar under 2 m³/min N₂ if undersized. Always commission with a flowing measurement.

## Installation

- Mount per OEM orientation; keep vents clear
- Thread sealant rated for gas service (O₂-compatible where required)
- Short flex only; whip checks on HP
- Label gas type and max pressures at the regulator

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Drop only when cutting | Undersized regulator or supply | Upsize; check bank/booster |
| Creep when idle | Seat debris / failed regulator | Rebuild/replace |
| Gauge bounce | Piston compressor / tiny receiver | Screw + receiver — [[Screw vs Piston Compressors]] |
| Cannot reach high P | Low inlet; empty bank; freeze | Trace upstream |
| Frost on N₂ regulator | High flow / cryogenic | Check vaporizer capacity |
| O₂ smell / heating at regulator | Contamination / wrong parts | Stop; O₂-clean protocol |

## Interaction with recipes

CypCut commanded pressure cannot exceed what the PRV and supply can deliver under flow. Marginal plants show up as "recipe worked yesterday" when ambient or duty changes — [[Nitrogen System Pressure Setpoints]], [[Cutting Parameters Index]].

## Related notes

- [[Gas Pipework and Fittings]]
- [[Oxygen Assist Gas]]
- [[Nitrogen Assist Gas]]
- [[Compressed Air Cutting]]
- [[Nitrogen Booster and HP Storage]]

## Sources

- GWK fiber laser installation requirements (regulator table)
- Field dynamic pressure commissioning practice
