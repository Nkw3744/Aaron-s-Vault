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
> Typical cut-in/cut-out pressures along air → PSA → booster → HP bank → laser. Use for health checks and sag diagnosis.

> [!warning] Drawing and nameplates win
> South-Tek-class numbers below are **illustrative**. Your plant may differ. Never raise pressures above vessel ratings.

## Pressure zones mental model

```
Air compressor → dryer/filters → PSA → N₂ buffer → booster → HP bank → regulator → laser
     ~8–9 bar              ~6–7 bar     ~90–100 psi     ~300 bar bank    ~14–25 bar cut
```

Confusing **bank PSI** with **nozzle bar** is a common commissioning error — [[Nitrogen Booster and HP Storage]].

## South-Tek reference bands (illustrative)

### 250S class (example tier)

| Component | Cut-in / cut-out (psi) | Approx. bar |
| --- | --- | --- |
| Air compressor discharge | 125 / 135 | ~8.6 / 9.3 |
| N₂ generator standby | 90 / 100 | ~6.2 / 6.9 |
| Booster suction (low) | 98 / 70 | ~6.8 / 4.8 |
| Booster high pressure | 3800 / 4350 | ~262 / 300 |

### 270S–410S class (example tier)

| Component | Cut-in / cut-out (psi) |
| --- | --- |
| Air compressor discharge | 115 / 132 |
| N₂ generator standby | 90 / 100 |
| Booster suction (low) | 98 / 80 |
| Booster high pressure | 3800 / 4350 |

## Laser-side process pressure (after regulators)

| Application | Typical nozzle pressure |
| --- | --- |
| Thin SS N₂ | 10–16 bar |
| Thick SS N₂ | 16–25 bar |
| Mild steel N₂ | Material/recipe dependent — [[Nitrogen Assist Gas]] |

Set in CypCut layer **and** confirm with dynamic gauge under flow — [[Gas Regulators and PRVs]].

## Adjustment rules

1. Never exceed vessel / relief valve settings
2. If laser starves: check HP bank and booster recovery before cranking PSA
3. If PSA won't hold standby: fix air compressor discharge first
4. Generator band too narrow → excessive cycling; too wide → purity/pressure drift
5. Log every setpoint change with date, old/new, reason, technician

## Health-check table

| Check | Cadence | Normal |
| --- | --- | --- |
| Buffer in band | Daily glance | Predictable cycles |
| HP bank after regulator | Before SS production | Holds during test pierce |
| Purity analyzer | Daily if fitted | ≥99.99% for SS work |
| Compressor hours vs N₂ output | Weekly trend | No sudden efficiency drop |
| Drain condensate on air side | Daily humid | Water leaving before PSA |

## Pressure tracing procedure (sag diagnosis)

1. Record static: compressor, PSA inlet, buffer, booster suction, bank, laser inlet
2. Run worst-case pierce/cut program
3. Record laser inlet **dynamic** and bank trend
4. Compare to project drawing
5. First stage that collapses = focus of repair — [[Nitrogen System Troubleshooting]]

## Interaction with fiber power class

Higher kW and larger nozzles demand more peak N₂ flow — [[Fiber Laser Power Classes]]. Setpoints alone cannot fix an undersized booster/bank.

## Related notes

- [[Nitrogen System Troubleshooting]]
- [[Nitrogen Booster and HP Storage]]
- [[PSA Nitrogen Generators]]
- [[Gas Regulators and PRVs]]
- [[Air Compressors for Laser Cutting]]

## Sources

- South-Tek laser cutting nitrogen systems operation and troubleshooting reference
