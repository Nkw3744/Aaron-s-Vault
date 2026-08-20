---
aliases:
  - laser extraction duct
  - static pressure dust collector
  - duct design laser fume
type: technical-reference
category: fume-extraction
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: IP Systems fume guide, field duct practice, centrifugal fan curves
status: generic reference — verify against nameplate and project drawing
---

# Ductwork and Static Pressure

Return to [[Laser Fume Extraction Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Why installed airflow falls below catalog fan CFM; duct design rules; balancing multi-zone tables; leak and ΔP diagnosis.

> [!tip] Pressure beats vanity CFM
> A high free-air CFM rating with leaky duct and loaded filters often underperforms a smaller fan with short sealed duct and real static capability.

## Static pressure vs airflow

Fans are published at free air (near zero resistance) and along a **fan curve** against system resistance. Laser dust collectors need centrifugal blowers because:

| Resistance source | Typical effect |
| --- | --- |
| Cartridge filters (clean) | Hundreds of Pa |
| Cartridge filters (loaded) | Often 1000–2500+ Pa |
| Long duct + many bends | Large friction + dynamic loss |
| Spark trap / cyclone | Additional ΔP |

Required: airflow **at the system ΔP**, not brochure free CFM. See [[Dust Collector Sizing]], [[Filter Stages and Maintenance]].

## Duct design rules

| Rule | Reason |
| --- | --- |
| Shortest practical machine → collector path | Minimize loss |
| Gentle bends (≥1.5× duct diameter radius) | Reduce turbulence and wear |
| Increase diameter on long runs | Lower velocity loss |
| Seal all joints (clamps + sealant as specified) | Leaks destroy zone balance |
| Flex only short at machine | Vibration isolation without collapse |
| Ground / bond metal duct | Static on dry dust — [[Grounding and EMC Isolation]] |
| Support duct; no sagging flex | Sag = water/dust traps + extra loss |
| Avoid consecutive tight elbows | Equivalent length stacks fast |

## Velocity hints

| Duct | Target hint |
| --- | --- |
| Main trunk | ~15–20 m/s common for dust transport |
| Branches | Balanced so inactive zones do not steal flow |
| Pickup at table | Per OEM zone design |

Too slow → dust dropout in duct. Too fast → noise, wear, unnecessary ΔP.

## Multi-zone tables

Partitioned downdraft tables use dampers (manual or CNC) so only active zones draw hard.

| Check | Pass |
| --- | --- |
| Damper actuators move freely | [[Pneumatic Cylinders in Laser Systems]] |
| CNC zone matches physical damper | Smoke test |
| Fail-safe position known | Fire strategy per OEM |
| Seals between zones | No massive cross-leak |

## Leak hunting method

1. Run fan with filters clean; note baseline motor amps and ΔP
2. Smoke pencil / theatrical smoke at joints
3. Listen for hiss at flex connections
4. Compare airflow at hood vs expected
5. Re-seal; re-measure

## Troubleshooting weak extraction

| Symptom | Checks |
| --- | --- |
| Smoke in cabinet | Fan off; filters loaded; damper closed; door open |
| Weak far zones | Undersized fan; duct leak; wrong damper map |
| High ΔP, low flow | Loaded filters — change |
| Low ΔP, low flow | Fan rotation wrong; belt slip; open leak before filter |
| Dust in clean plenum | Broken cartridge seal |
| Noise / vibration | Loose duct; fan imbalance; collapsed flex |

### Fan rotation

Wrong 3-phase rotation → fan "runs" but moves little air. Check arrow on housing after any electrical work — [[Laser Electrical Supply Requirements]].

## Design coordination with sizing

1. Calculate required volume — [[Dust Collector Sizing]]
2. Sketch duct length and fittings → estimate resistance
3. Select fan that delivers volume **at that ΔP with dirty filter allowance**
4. Prefer short outdoor stack; rain cap that does not choke discharge

## Commissioning checklist

1. Duct route matches drawing; diameters labeled
2. All joints sealed; bonding jumpers on flexible breaks
3. Dampers named and mapped in CNC
4. Baseline: clean-filter ΔP, amps, smoke clear time
5. Photo gauges for later comparison
6. Fire/spark controls per local code verified

## Related notes

- [[Laser Fume Extraction Overview]]
- [[Dust Collector Sizing]]
- [[Filter Stages and Maintenance]]
- [[Zn and Coated Material Fume Notes]]

## Sources

- IP Systems how fume extraction works in laser cutting
- PURE-AIR high negative pressure guidance
- Field duct balancing on partitioned tables
