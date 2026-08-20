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
> CO₂ laser subsystem map, how they differ from fiber at a system level, and which auxiliary notes still apply. Use when servicing or quoting CO₂ equipment (Indepth fleet is primarily fiber).

> [!warning] Different toolkit
> A fiber tech's QBH/BCS100 habits do not fully transfer. Mirror alignment, resonator gas, and VOC extraction are first-class CO₂ skills.

## How a CO₂ laser cuts (brief)

CO₂ lasers emit at **10.6 µm** (far infrared). Energy is delivered through a **flying-optics** path of mirrors and bellows (not a fiber). Focused into the material with a ZnSe or similar focusing lens (metal-cutting heads) or through different optics for non-metals. Assist gas still ejects molten/vaporized material on metal cuts; many organic applications use lower assist pressure and different extraction chemistry.

## CO₂ vs fiber (headline)

| Aspect | CO₂ laser | Fiber laser |
| --- | --- | --- |
| Wavelength | 10.6 µm | ~1070 nm |
| Beam delivery | Mirrors + bellows | Fiber + QBH |
| Resonator | Gas discharge / RF slab / similar | Diode-pumped fiber module |
| Resonator gas | He / N₂ / CO₂ mix often required | None |
| Typical materials | Organics strong; metals possible with limits | Metals primary |
| Wall efficiency | Lower → more waste heat | Higher |
| Chiller | Often large; sometimes colder setpoints | Dual-loop CW packages common |
| Height sensing | Capacitive works on metal; limited on non-conductors | Capacitive standard on sheet metal |

Full auxiliary comparison: [[CO2 vs Fiber Auxiliary Differences]].

## Subsystem map

| Subsystem | CO₂-specific notes | Shared reference |
| --- | --- | --- |
| Resonator | Gas refill, RF/DC supply, mirror optics internal | [[CO2 Chiller and Gas Requirements]] |
| Beam path | Alignment critical; bellows smoke seals | — |
| Cutting head / lens | ZnSe focus; different consumables than fiber | Assist gas still [[Assist Gas Overview]] |
| Assist gas | O₂/N₂/air for metal; lower pressure on organics | [[Gas Regulators and PRVs]] |
| Chiller | Thermal load often higher per optical watt | [[Laser Water Chillers]] (fiber-centric — verify CO₂ OEM) |
| Extraction | Particulate **plus VOC/odor** | [[Laser Fume Extraction Overview]], carbon stage |
| CNC | Similar motion ideas; process libraries differ | — |
| Safety | Class 4; door interlocks; different wavelength eyewear | Local laser safety rules |

## Beam path maintenance (field reality)

| Task | Why it matters |
| --- | --- |
| Mirror inspection / cleaning schedule | Contamination burns spots; power drops |
| Bellows integrity | Smoke ingress coats optics |
| Alignment after bump / move | Multi-mirror path; not "plug and play" like QBH |
| Lens check | Thermal lensing / focus shift from dirty ZnSe |

Carry CO₂-specific cleaning materials and alignment tools — not in a fiber-only kit.

## Materials and process notes

| Material family | Notes |
| --- | --- |
| Acrylic, wood, plastics | Strong CO₂ absorption; fire and VOC risk |
| Mild steel | O₂ assist common historically |
| Stainless / aluminum | Fiber usually preferred today; CO₂ possible with caveats |
| Reflective metals | Back-reflection risk — OEM procedures |

## Assist gas

Metal cutting purity concepts match fiber — [[Oxygen Assist Gas]], [[Nitrogen Assist Gas]], [[Compressed Air Cutting]].  
Organic cutting: verify head max pressure; extraction must handle fumes — [[Filter Stages and Maintenance]].

## When a fiber-trained tech arrives at a CO₂ site

1. Confirm resonator gas supply (bulk or premix) and leak-test status
2. Read chiller setpoint and water chemistry from **that** OEM — [[CO2 Chiller and Gas Requirements]]
3. Inspect mirrors/bellows before blaming "laser power"
4. Confirm extraction has carbon/VOC capability if cutting organics
5. Do not assume capacitive height works on acrylic — different sensing or fixed Z
6. Warm-up and purge procedures before first lasing

## Alarm / fault orientation (generic)

| Pattern | CO₂ angle |
| --- | --- |
| Power low, resonator "OK" | Mirrors/lens dirty or misaligned |
| Gas alarm | Mix leak, empty bottle, mixer fault |
| Over-temp | Undersized chiller; fouled exchanger |
| Fire / smoke alarm in cell | Organic cutting — extraction and fire plan |

Fiber-style alarm routing still useful for shared auxiliaries: [[Fiber Laser Common Alarms]] (chiller/gas/extraction sections).

## Indepth Technology fleet note

Vault machines ([[Gweike 3015GAII]], [[Gweike 4020GA]], [[JQ-2040E]], [[JQ-2060E]]) are **fiber**. Keep this CO₂ hub for customer sites, quotes, and training contrast.

## Related notes

- [[CO2 vs Fiber Auxiliary Differences]]
- [[CO2 Chiller and Gas Requirements]]
- [[Fiber Laser Cutters]]
- [[Technical Reference Index]]

## Sources

- BLMA dual-use / installation guides (gas and chiller sections)
- Industry CO₂ laser maintenance practice
- Arcus environmental comparisons
