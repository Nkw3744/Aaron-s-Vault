---
aliases:
  - CO2 laser chiller
  - CO2 resonator gas
type: technical-reference
category: co2-lasers
applies_to: [co2-laser]
source_reviewed: 2026-08-05
source_scope: BLMA gas connection guide, CO2 OEM practice
status: generic reference — verify against nameplate and project drawing
---

# CO2 Chiller and Gas Requirements

Return to [[CO2 Laser Cutters]] · [[Technical Reference Index]]

> [!info] When to open this note
> CO₂ resonator cooling and laser gas mix — distinct from fiber DI-water loops.

## Chiller (CO₂ resonator cooling)

| Aspect | CO₂ typical | Fiber reference |
| --- | --- | --- |
| Heat load | Higher — efficiency ~10–15% | Lower wall draw per cut kW |
| Setpoint | OEM specific; often **18–22 °C** class for some RF tubes | LT 22–26, HT 30–32 |
| Water chemistry | Strict — conductivity spec common | DI/distilled — [[Cooling Water Quality]] |
| Condensation | Cold mirror/window risk — same dew point rule | [[Dew Point and Chiller Setpoints]] |
| Unit size | Often industrial centralized | CW-5200–6200 on fiber |

Never assume fiber chiller spec transfers to CO₂ resonator without OEM sheet.

## Laser gas (resonator excitation)

BLMA-style reference for **laser gas** (not assist gas):

| Gas | Purity (typical) |
| --- | --- |
| Helium (He) | 99.999% |
| Nitrogen (N₂) | 99.999% |
| Carbon dioxide (CO₂) | 99.999% |

Premixed bottles or gas mixer panel — leak test critical.

Separate from **assist gas** (O₂/N₂/air to cutting head) — [[Assist Gas Overview]].

## Assist gas on CO₂ metal cutting

Similar purity to fiber when cutting steel/stainless with O₂/N₂. Organic materials (acrylic, MDF):

- Lower assist pressure
- Extraction must handle VOC — [[Filter Stages and Maintenance]]

## Installation checklist

1. Chiller capacity from OEM kW thermal load
2. Resonator gas lines: stainless/copper; labeled He/N₂/CO₂
3. Assist lines separate color code
4. Filter on gas inlet to resonator per manual
5. Warmup and purge procedure before first lasing
6. Water quality test if conductivity specified

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Power drift | Gas mix; water temp; mirror dirty |
| High water temp | Undersized chiller; fouled heat exchanger |
| Gas alarm | Leak; empty bottle; mixer fault |

## Related notes

- [[CO2 vs Fiber Auxiliary Differences]]
- [[Laser Water Chillers]]
- [[Gas Regulators and PRVs]]

## Sources

- BLMA fiber laser installation guide (laser gas vs assist gas section)
- Novanta/Synrad-class water-cooled laser condensation guidance
