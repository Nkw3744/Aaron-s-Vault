---
aliases:
  - CO2 laser chiller
  - CO2 resonator gas
  - laser gas mix CO2
type: technical-reference
category: co2-lasers
applies_to: [co2-laser]
source_reviewed: 2026-08-05
source_scope: BLMA gas connection guide, CO2 OEM practice, Novanta-class condensation guidance
status: generic reference — verify against nameplate and project drawing
---

# CO2 Chiller and Gas Requirements

Return to [[CO2 Laser Cutters]] · [[Technical Reference Index]]

> [!info] When to open this note
> CO₂ resonator cooling and laser (excitation) gas mix — distinct from fiber DI-water dual-loop packages and from assist gas at the nozzle.

> [!warning] Three different "gases"
> 1) Resonator laser gas (He/N₂/CO₂)  
> 2) Assist gas (O₂/N₂/air to the cut)  
> 3) Sometimes purge/air knife  
> Label lines. Never cross-connect.

## Chiller — CO₂ resonator cooling

| Aspect | CO₂ typical | Fiber contrast |
| --- | --- | --- |
| Heat load | Higher — wall efficiency often ~10–15% class | Lower waste heat per optical kW |
| Setpoint | OEM-specific; some RF/water-cooled sources **18–22 °C** | LT 22–26, HT 30–32 common |
| Water chemistry | Strict conductivity specs common | DI/distilled — [[Cooling Water Quality]] |
| Condensation | Cold mirrors/windows sweat if below dew point | Same physics — [[Dew Point and Chiller Setpoints]] |
| Package | Often industrial centralized chiller | CW-5200–6200 on many fiber cells |

**Never assume** a fiber CW dual-loop setpoint sheet transfers to a CO₂ resonator. Read that machine's OEM.

### Chiller install checklist (CO₂)

1. Thermal load (kW) from OEM — size with margin for summer ambient
2. Correct water/glycol mix if specified
3. Flow and pressure within OEM band
4. Conductivity or resistivity meter if required — log baseline
5. Hose insulation in humid rooms
6. Dew-point margin vs setpoint before emission
7. Interlock wiring to laser enable

### Chiller troubleshooting (CO₂-leaning)

| Symptom | Checks |
| --- | --- |
| Power drift with rising water T | Undersized chiller; fouled heat exchanger; ambient |
| Condensation on resonator | Setpoint below dew point; RH high |
| Flow alarm | Same short-loop logic as fiber — [[Chiller Troubleshooting Flowchart]] |
| Conductivity rising | Contamination; need flush/change |

## Laser gas (resonator excitation)

BLMA-style reference for **laser gas** (not assist):

| Gas | Purity (typical ask) |
| --- | --- |
| Helium (He) | 99.999% |
| Nitrogen (N₂) | 99.999% |
| Carbon dioxide (CO₂) | 99.999% |

Supply options: separate bottles into a mixer, or certified premix. Leak integrity is mandatory — resonator performance collapses with air in-leakage.

### Resonator gas install checklist

1. Dedicated lines; stainless/copper as OEM specifies
2. Labels at bottle and machine: He / N₂ / CO₂ / premix
3. Regulators rated for gas and inlet pressure — [[Gas Regulators and PRVs]]
4. Inlet filter per manual
5. Leak test (soap / electronic) after any break
6. Purge / warmup procedure before first lasing
7. Record bottle certificates on machine hub

### Resonator gas troubleshooting

| Symptom | Likely cause |
| --- | --- |
| Won't lase / hard start | Empty gas; wrong mix; air leak |
| Power slowly dies | Leak; contaminated mix; aging tube/slab (OEM) |
| Gas alarm | Pressure switch; mixer fault; bottle change overdue |

## Assist gas (cutting) — still required for metal

Metal CO₂ cutting uses the same purity ideas as fiber:

- O₂ >99.6% typical — [[Oxygen Assist Gas]]
- N₂ ≥99.99% for bright edges — [[Nitrogen Assist Gas]]
- Air only with dry oil-free train — [[Compressed Air Cutting]]

Organic cutting (acrylic, wood): often lower assist pressure; fire and VOC dominate planning — [[Laser Fume Extraction Overview]].

## Gas path mental model

```
Resonator bottles/mixer → laser cavity (sealed path)
Assist bottles/PSA/compressor → cutting head nozzle
Chiller water loop → resonator heat exchanger (± optics)
```

Three systems, three failure trees. Do not chase "low power" in assist pressure if resonator mix is empty.

## Seasonal and condensation notes

Cold resonator setpoints in humid summer are high risk. Apply:

- [[Workshop Humidity and Condensation]]
- [[Dehumidifiers for Laser Rooms]]
- Raise water only within OEM max; prefer lower RH

Novanta-class guidance for water-cooled lasers: coolant below dew point → condensation damage to electronics/optics.

## Related notes

- [[CO2 vs Fiber Auxiliary Differences]]
- [[Laser Water Chillers]]
- [[Assist Gas Overview]]
- [[Gas Pipework and Fittings]]
- [[Cooling Water Quality]]

## Sources

- BLMA installation guides (laser gas vs assist gas)
- Novanta / Synrad-class condensation guidance for water-cooled lasers
- Field CO₂ resonator service practice
