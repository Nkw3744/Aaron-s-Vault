---
aliases:
  - nitrogen booster laser
  - HP nitrogen storage
  - N2 bottle bank laser
type: technical-reference
category: nitrogen-systems
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: South-Tek N2 systems reference, field PSA packages
status: generic reference — verify against nameplate and project drawing
---

# Nitrogen Booster and HP Storage

Return to [[PSA Nitrogen Generators]] · [[Technical Reference Index]]

> [!info] When to open this note
> Boosting PSA buffer N₂ to laser cut pressures and storing it in HP banks. Use when diagnosing pressure sag on pierce or sizing banks.

> [!danger] High pressure
> Banks often store ~200–300 bar. Whip restraints, trained personnel, and relief valves are mandatory. Do not confuse bank pressure with nozzle pressure.

## Why the booster exists

PSA buffer typically holds N₂ around ~6–10 bar (90–100 psi class). Fiber N₂ cutting often needs **~1.4–2.5 MPa (14–25 bar) under flow** at the head — sometimes higher. The booster compresses buffer gas into an HP storage bank; regulators then step down to process pressure.

## Typical pressure zones (South-Tek class reference)

| Zone | Typical band |
| --- | --- |
| Air compressor discharge | ~115–135 psi (8–9 bar) |
| N₂ generator / buffer standby | ~90–100 psi |
| Booster suction | ~70–98 psi cut-in/out |
| HP storage working | ~3800–4350 psi (~260–300 bar) **bank** |
| Laser process (after regulator) | Often 14–25 bar cutting |

Detail tables: [[Nitrogen System Pressure Setpoints]].

## HP storage (16-pack / tube bank)

| Function | Notes |
| --- | --- |
| Absorb pierce peaks | Without huge instantaneous booster flow |
| Regulator supply | Stable inlet to process PRV |
| Safety | Relief valves; chained bottles; periodic hydro / certification per local law |
| Labeling | Max bank pressure on manifold |

Undersized storage → pressure sag on long pierce at high kW / large nozzle.

## Sizing hints

| Driver | Effect |
| --- | --- |
| Higher laser kW | Higher N₂ flow — [[Fiber Laser Power Classes]] |
| Larger nozzle | More orifice flow |
| Duty cycle | Continuous cutting vs intermittent |
| Booster speed | Recovery time between peaks |

Measure dynamic pressure during worst-case program — do not trust idle gauges.

## Installation checklist

1. Booster interlocked against low buffer suction (anti-cavitation)
2. Non-return valves between zones
3. Process regulator rated for bank inlet pressure — [[Gas Regulators and PRVs]]
4. Leak test HP side at 1.1× working (qualified tech)
5. Whip checks / restraints on flexible HP leads
6. Vent relief valves safely
7. Label max pressures; log setpoints

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Sag mid-cut | Small bank; slow booster; leak | Trace — [[Nitrogen System Troubleshooting]] |
| Booster continuous | Leak or laser flow > design | HP leak test; nozzle/duty audit |
| Cannot reach cut pressure | Empty bank; regulator fault; low suction | Check bands |
| Booster overheat | High ambient; wrong suction band; duty | Cool; adjust; service |
| Purity OK but weak cut | Pressure/flow — not CMS | This note's domain |

## Related notes

- [[PSA Nitrogen Generators]]
- [[Nitrogen Assist Gas]]
- [[Gas Pipework and Fittings]]
- [[Nitrogen System Pressure Setpoints]]

## Sources

- South-Tek laser cutting nitrogen systems reference
- Field PSA + booster package practice
