---
aliases:
  - gas regulators laser
  - PRV cutting gas
type: technical-reference
category: assist-gas
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist regulator table
status: generic reference — verify against nameplate and project drawing
---

# Gas Regulators and PRVs

Return to [[Assist Gas Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Selecting and setting pressure-reducing valves for O₂ and N₂; input vs output ratings.

## Regulator vs proportional valve

| Device | Location | Function |
| --- | --- | --- |
| Pressure reducing valve (PRV) | At bulk/cylinder/booster outlet | Steps supply to machine inlet pressure |
| Proportional valve | In cutting head or gas panel | CNC adjusts cut pressure per layer |

Proportional valve: [[Autofocus and Proportional Gas Valves]].

## Typical OEM regulator specs (GWK reference)

| Service | Input rating | Output range |
| --- | --- | --- |
| Nitrogen PRV | ≥15 MPa | 0.2–3.0 MPa |
| Oxygen PRV | ≥15 MPa | 0.05–1.2 MPa |

## Selection rules

1. **Input rating** must exceed maximum supply pressure with margin
2. **Flow coefficient (Cv)** must pass peak flow at set pressure without creep-down under cut
3. Two-stage regulation helps for high-pressure N₂ (booster → line PRV → machine)
4. Separate regulators per gas — never use O₂-regulator on N₂ without full cleaning protocol
5. Gauges: upstream and downstream preferred for diagnosis

## Installation

- Mount upright; keep vent ports clear
- Use pipe dope or tape rated for gas service (O₂-compatible where required)
- Strap cylinders; flex hose only on short spans from manifold
- Lock adjustment screw after commissioning or use tamper seal

## Setting procedure

1. Close machine inlet valve
2. Open supply slowly; check downstream gauge at zero load
3. Adjust PRV to OEM **inlet** pressure spec (static)
4. Open machine valve; run pierce at trial settings
5. Measure at head or machine test port **during flow**
6. Adjust PRV or CypCut layer pressure to match recipe

> [!tip] Dynamic vs static
> A regulator showing 14 bar static may deliver 10 bar under 2 m³/min N₂ flow if undersized.

## Troubleshooting

| Symptom | Likely cause |
| --- | --- |
| Pressure drops only when cutting | Undersized regulator or supply |
| Creep (pressure rises when closed) | Seat debris; failed regulator |
| Gauge bounces | Piston compressor without receiver |
| Cannot reach high pressure | Input supply too low; frozen regulator (CO₂/N₂ cold) |

## Related notes

- [[Gas Pipework and Fittings]]
- [[Nitrogen Booster and HP Storage]]
- [[Nitrogen System Pressure Setpoints]]

## Sources

- GWK fiber laser installation requirements (regulator reference table)
