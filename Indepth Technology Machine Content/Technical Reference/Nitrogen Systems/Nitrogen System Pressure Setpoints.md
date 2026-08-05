---
aliases:
  - N2 pressure setpoints
  - nitrogen plant pressures
type: technical-reference
category: nitrogen-systems
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: South-Tek laser cutting nitrogen systems reference
status: generic reference — verify against nameplate and project drawing
---

# Nitrogen System Pressure Setpoints

Return to [[PSA Nitrogen Generators]] · [[Technical Reference Index]]

> [!info] When to open this note
> Typical cut-in/cut-out pressures along the air→N₂→booster→laser path. **Always verify against project drawing and nameplates.**

## South-Tek reference bands (illustrative)

Values from published laser-cutting N₂ package documentation. Your plant may differ.

### 250S class system (example tier)

| Component | Cut-in / cut-out (psi) |
| --- | --- |
| Air compressor discharge | 125 / 135 |
| N₂ generator standby | 90 / 100 |
| Booster suction (low) | 98 / 70 |
| Booster high pressure | 3800 / 4350 (~300 bar bank) |

### 270S–410S class systems (example tier)

| Component | Cut-in / cut-out (psi) |
| --- | --- |
| Air compressor discharge | 115 / 132 |
| N₂ generator standby | 90 / 100 |
| Booster suction (low) | 98 / 80 |
| Booster high pressure | 3800 / 4350 |

## Laser-side process pressure

After HP bank regulators — separate from bank storage:

| Application | Typical nozzle pressure |
| --- | --- |
| Thin SS N₂ | 10–16 bar |
| Thick SS N₂ | 16–25 bar |
| Mild steel N₂ | Material dependent — [[Nitrogen Assist Gas]] |

Set in CypCut layer + confirm with dynamic gauge.

## Adjustment rules

1. Never raise bank pressure above vessel rating
2. Adjust compressor discharge first if feed starved
3. Generator standby band: too narrow → excessive cycling; too wide → purity drift
4. Log all setpoint changes with date and reason

## Health checks (daily / weekly)

| Check | Normal |
| --- | --- |
| Buffer pressure stable in band | Cycles predictably |
| HP bank after regulator | Holds during test pierce |
| Purity analyzer | ≥99.99% when cutting SS |
| Compressor hours vs N₂ output | No sudden efficiency drop |

## Related notes

- [[Nitrogen System Troubleshooting]]
- [[Nitrogen Booster and HP Storage]]
- [[Gas Regulators and PRVs]]

## Sources

- South-Tek laser cutting nitrogen systems operation and troubleshooting reference
