---
aliases:
  - nitrogen booster laser
  - HP nitrogen storage
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
> Boosting PSA output to laser cut pressures (often 20–30 bar class at regulator).

## Why booster exists

PSA buffer typically holds N₂ at ~6–10 bar (90–100 psi class). Fiber laser N₂ cutting often needs **2.0 MPa (20 bar)+ under flow**. Booster compresses from buffer to high-pressure storage bank.

## Typical pressure zones (South-Tek class reference)

| Zone | Typical band |
| --- | --- |
| Air compressor discharge | ~115–135 psi (8–9 bar) class |
| N₂ generator standby (buffer) | ~90–100 psi |
| Booster suction | ~70–98 psi cut-in/out |
| HP storage working | ~3800–4350 psi (~260–300 bar) **bank** |
| Laser process (after regulator) | 14–25 bar common for cutting |

> [!warning] Bank vs cut pressure
> HP storage is often 200–300 bar in bottle banks; regulators step down to process pressure. Verify your drawing — do not confuse bank PSI with nozzle pressure.

## HP storage (16-pack / tube bank)

- Stores boosted N₂ to absorb pierce peaks
- Regulators on bank outlet set process pressure
- Safety: relief valves, chain bottles, periodic hydro test per local law

## Sizing hints

Undersized storage → pressure sag on long pierce at high kW:

- More HP volume or faster booster
- Check [[Fiber Laser Power Classes]] flow column
- Measure dynamic pressure during worst-case program

## Installation checklist

1. Booster interlocked with buffer low pressure — won't cavitate
2. Non-return valves between zones
3. Regulator rated for bank input
4. Leak test HP side at 1.1× working pressure
5. Label maximum bank pressure on manifold

## Troubleshooting

| Symptom | Likely cause |
| --- | --- |
| Pressure sag mid-cut | Small HP bank; booster too slow |
| Booster runs continuously | Leak on HP side; laser flow exceeds design |
| Cannot reach cut pressure | Regulator input low; empty bank |

See [[Nitrogen System Troubleshooting]].

## Related notes

- [[Gas Regulators and PRVs]]
- [[Nitrogen System Pressure Setpoints]]

## Sources

- South-Tek laser cutting nitrogen systems reference (pressure setpoint tables)
