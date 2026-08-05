---
aliases:
  - laser extraction duct
  - static pressure dust collector
type: technical-reference
category: fume-extraction
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: IP Systems fume guide, field duct practice
status: generic reference — verify against nameplate and project drawing
---

# Ductwork and Static Pressure

Return to [[Laser Fume Extraction Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Why installed CFM falls below catalog fan rating; duct design rules.

## Static pressure vs airflow

Fans are rated at **free air** (zero resistance) and at **system curve** (duct + filters). Laser collectors need centrifugal blowers because:

- Cartridge filters add 1000–2500 Pa when loaded
- Long duct runs add friction loss
- Bends add equivalent length

> [!tip] High negative pressure at hood beats oversized free CFM with leaky duct.

## Duct design rules

| Rule | Reason |
| --- | --- |
| Shortest path machine → collector | Minimize loss |
| Gentle bends (≥1.5 duct diameters radius) | Reduce turbulence |
| Increase diameter on long runs | Velocity drop, less loss |
| Seal all joints | Leaks kill zone balance |
| Flexible short connections at machine only | Vibration isolation |
| Ground metal duct | Static electricity on dry dust |

## Velocity hints

| Duct type | Target air velocity |
| --- | --- |
| Main trunk | 15–20 m/s common for dust transport |
| Branch to zone | Balanced dampers |

## Zone balancing

Multi-zone tables need damper adjustment so inactive zones do not steal flow. CNC-controlled dampers must fail-safe open or closed per fire strategy — follow OEM.

## Troubleshooting weak extraction

1. Measure ΔP across filters — replace if high
2. Smoke test at joints — find leaks
3. Verify fan rotation direction
4. Check damper positions under cut
5. Compare motor amp draw to baseline (loaded fan draws more)

## Related notes

- [[Dust Collector Sizing]]
- [[Filter Stages and Maintenance]]

## Sources

- IP Systems how fume extraction works in laser cutting
- PURE-AIR high negative pressure guidance
