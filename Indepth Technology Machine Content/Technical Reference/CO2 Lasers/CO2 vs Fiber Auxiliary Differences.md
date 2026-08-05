---
aliases:
  - fiber vs CO2 auxiliary
  - CO2 fiber differences install
type: technical-reference
category: co2-lasers
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: Arcus, BLMA, multi-OEM install comparisons
status: generic reference — verify against nameplate and project drawing
---

# CO2 vs Fiber Auxiliary Differences

Return to [[CO2 Laser Cutters]] · [[Fiber Laser Cutters]] · [[Technical Reference Index]]

> [!info] When to open this note
> Side-by-side auxiliary equipment differences for installers crossing between technologies.

## Quick comparison table

| Auxiliary | Fiber laser | CO₂ laser |
| --- | --- | --- |
| **Beam delivery** | QBH fiber — [[QBH Fiber Delivery Cable]] | Mirrors, bellows, alignment |
| **Chiller** | CW dual-loop; DI water; HT anti-condensation | Often larger unit; sometimes lower setpoint; see [[CO2 Chiller and Gas Requirements]] |
| **Resonator gas** | None (solid state) | He/N₂/CO₂ 99.999% class possible |
| **Assist gas** | O₂/N₂/air high pressure | Similar for metal; lower assist on organics |
| **Air compressor** | 16 bar screw for air cut | Less common on pure organic shops |
| **N₂ PSA** | Common for SS fiber production | Same if metal CO₂ cutting |
| **Extraction** | Metal particulate primary | + VOC/odor — carbon stage — [[Filter Stages and Maintenance]] |
| **Height sense** | Capacitive on metal | May differ on non-conductive — capacitive limited |
| **Electrical** | High kW, 380 V class | Total kW often higher incl. blower |
| **Condensation** | QBH/head dew point critical | Mirror window condensation risk |
| **Startup** | Chiller → laser enable | Often warmup, gas flow purge |

## Shared auxiliaries (same reference notes)

These topics apply to **both** with parameter differences only:

- [[Assist Gas Overview]] — purity and regulators
- [[Gas Pipework and Fittings]]
- [[Laser Fume Extraction Overview]] — sizing differs by fume type
- [[Laser Electrical Supply Requirements]]
- [[Grounding and EMC Isolation]]
- [[Pneumatic Cylinders in Laser Systems]]

## Installer mindset shift

| Fiber tech habit | CO₂ adjustment |
| --- | --- |
| Check QBH interlock | Check mirror cleanliness and alignment |
| Dual chiller setpoints | May single large loop + lower temp |
| Metal dust filters | Add carbon for acrylic/wood |
| Cap height follow always | Verify sensing mode on material |

## Fleet note (Indepth Technology)

Current vault machines are **fiber** (Gweike, JQ). Use CO₂ section when servicing non-fleet CO₂ equipment or comparing customer quotes.

## Related notes

- [[CO2 Chiller and Gas Requirements]]
- [[Technical Reference Index]]

## Sources

- BLMA fiber/CO2 installation guides
- Arcus environmental and installation documentation
