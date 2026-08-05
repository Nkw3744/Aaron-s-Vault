---
aliases:
  - CO2 laser cutter reference
  - CO2 laser overview
type: technical-reference
category: co2-lasers
applies_to: [co2-laser]
source_reviewed: 2026-08-05
source_scope: BLMA installation guide, industry CO2 practice, Arcus comparisons
status: generic reference — verify against nameplate and project drawing
---

# CO2 Laser Cutters

Return to [[Technical Reference Index]]

> [!info] When to open this note
> CO₂ laser subsystem map and links to auxiliaries that differ from fiber.

## CO₂ vs fiber (headline)

| Aspect | CO₂ laser | Fiber laser |
| --- | --- | --- |
| Wavelength | 10.6 µm | ~1070 nm |
| Beam delivery | Mirrors + bellows | Fiber + QBH |
| Resonator gas | He/N₂/CO₂ mix | Solid-state diode pumped |
| Typical materials | Organics, acrylic, wood, some metals (lower reflect issues on non-metals) | Metals primary |
| Efficiency | Lower; more heat | Higher wall efficiency |
| Chiller | Often lower temp, larger load | Dual-loop common |

Full comparison: [[CO2 vs Fiber Auxiliary Differences]].

## Subsystem map

| Subsystem | CO₂ notes |
| --- | --- |
| Resonator | Gas refill; mirror optics internal |
| Beam path | Flying optics alignment critical |
| Assist gas | O₂/N₂/air for metal; often N₂ for organics edge |
| Chiller | Large thermal load — [[CO2 Chiller and Gas Requirements]] |
| Extraction | VOC/odor + particulate — carbon filter common |
| Power | Often high total kW including blower and vacuum |

## Beam path maintenance

- Mirror cleaning schedule — contamination burns spots
- Bellows integrity — smoke ingress
- Alignment after any bump — not field trivial on long beds

## Assist gas

Same purity concepts as fiber for metal cutting — [[Assist Gas Overview]].  
Organic cutting may use lower pressure; verify head spec.

## When service tech sees CO₂ on site

1. Confirm resonator gas supply (bulk or premix)
2. Water chemistry and chiller capacity — different from fiber CW-5200 packages
3. Extraction must handle **VOCs** not just metal dust
4. Mirror alignment tools may be required — not in fiber toolkit

## Related notes

- [[CO2 vs Fiber Auxiliary Differences]]
- [[CO2 Chiller and Gas Requirements]]
- [[Fiber Laser Cutters]] — primary fleet reference

## Sources

- BLMA dual-use installation guide (gas and chiller sections)
- Industry CO2 laser maintenance practice
