---
aliases:
  - laser site prep
  - fiber laser installation requirements
type: technical-reference
category: fiber-lasers
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, Arcus environmental and installation guides
status: generic reference — verify against nameplate and project drawing
---

# Fiber Laser Site Requirements

Return to [[Fiber Laser Cutters]] · [[Technical Reference Index]]

> [!info] When to open this note
> Pre-install site survey, customer handover checklist, quoting a new install, or working backward from "why does this recently moved/installed machine keep alarming."

> [!warning] Local codes apply
> Electrical, fire, and ventilation rules vary by jurisdiction (in New Zealand: AS/NZS 3000 wiring rules, local fire authority requirements, WorkSafe guidance on hazardous substances and machine safety). This note is equipment-oriented, not a compliance certificate — always confirm local code requirements separately.

## Why a proper site survey matters

Most "the machine won't perform to spec" and "it worked at the factory but not here" complaints trace back to a site condition that was never checked before delivery: an undersized feeder, no dedicated ground electrode, a compressor sized for hand tools rather than laser air-cutting, or a chiller placed in a hot, humid corner of the workshop. A thorough site survey before delivery is far cheaper than diagnosing the same issues after the machine is bolted down and the customer is already unhappy.

## Site survey checklist

### Power

| Item | Typical requirement | Verify |
| --- | --- | --- |
| Supply voltage | 380 V 3-phase ±5%, 50 Hz (or OEM spec) | ☐ Nameplate |
| Wiring | 3-phase + neutral + PE (five-wire) | ☐ |
| Total capacity | See [[Fiber Laser Power Classes]] | ☐ kW calc |
| Dedicated circuit | No shared welders/compressors on laser feeder | ☐ |
| Phase imbalance | <2.5% | ☐ Measure |
| Voltage fluctuation | <5% under load | ☐ |
| Regulated supply | Stabilizer for laser electronics | ☐ OEM |
| Ground resistance | <4 Ω at electrode (typical OEM ask) | ☐ Test |
| Existing switchboard capacity | Confirm spare breaker capacity, not just spare physical slots | ☐ |
| Cable run distance | Voltage drop over long runs to a remote workshop corner | ☐ Calculate |

Detail: [[Laser Electrical Supply Requirements]], [[Grounding and EMC Isolation]].

### Foundation and floor

| Item | Typical | Verify |
| --- | --- | --- |
| Floor loading | ≥500 kg/m² or engineer sign-off | ☐ |
| Level | Within OEM shim spec (often 0.05 mm/m) | ☐ |
| Vibration | No heavy presses within isolation zone | ☐ |
| Clearances | Front ≥1.2 m; rear (service) ≥1.5 m | ☐ [[Installation Clearances and Foundations]] |
| Slab condition | No major cracks, adequate cure age for new pours | ☐ |
| Access route | Doorway width, crane/forklift path, overhead clearance for delivery | ☐ |

### Environment

| Item | Typical | Verify |
| --- | --- | --- |
| Ambient temperature | 10–35 °C workshop; 23–27 °C laser zone ideal | ☐ |
| Humidity | ≤75% RH; ≤60% preferred | ☐ [[Workshop Humidity and Condensation]] |
| Dust | Clean install; filter HVAC if needed | ☐ |
| Chiller location | Often separate from laser room (adds heat/humidity) | ☐ |
| Condensation margin | Cooled surfaces ≥ dew point + 2–3 °C | ☐ [[Dew Point and Chiller Setpoints]] |
| Direct sunlight / roller doors | Avoid direct solar heating on chiller or control cabinet; large doors cause humidity swings | ☐ |
| Seasonal extremes | Check both summer and winter expectations, not just install-day conditions | ☐ |

### Cooling water prep

| Item | Typical | Verify |
| --- | --- | --- |
| Water type | Distilled or deionized for fill | ☐ [[Cooling Water Quality]] |
| Volume | 20–80 L in chiller + loop (model dependent) | ☐ |
| Hose run | ≤10 m common OEM limit | ☐ |
| Inlet pressure | ~4.5–6 bar at chiller (if specified) | ☐ |
| Supply source for top-ups | Plan for ongoing distilled/DI water supply, not just first fill | ☐ |

### Assist gas

| Gas | Purity (typical) | Notes |
| --- | --- | --- |
| O₂ | >99.6% | Regulator 0.05–1.2 MPa out |
| N₂ | ≥99.99% | Dewar/bulk/PSA; not small cylinders for production |
| Air cutting | Dry, oil-free | Screw + dryer + fine filters |

See [[Assist Gas Overview]], [[Gas Pipework and Fittings]].

Also confirm the **logistics** of gas supply, not just the specification:

- Delivery access for a dewar truck (turning circle, gate width, decant point distance from the machine)
- Storage compound requirements for cylinders if used as backup supply
- Contract lead time for bulk/dewar refill versus expected consumption rate at full production

### Ventilation and extraction

| Item | Verify |
| --- | --- |
| Dust collector sized for table — [[Dust Collector Sizing]] | ☐ |
| Duct route planned; minimal bends | ☐ |
| Discharge: outdoor or filtered recirc per EHS | ☐ |
| Fire extinguishers per local code | ☐ |
| Roof/wall penetration approved if discharging outside | ☐ |
| Noise impact on adjacent occupied spaces | ☐ |

### Compressed air / nitrogen plant (if applicable)

| Item | Verify |
| --- | --- |
| Compressor kW and 16 bar class for air cutting | ☐ |
| Dryer and 0.01 µm filtration chain | ☐ |
| PSA feed air quality if N₂ generator | ☐ [[PSA Nitrogen Generators]] |
| Booster and HP storage for high-pressure N₂ | ☐ |
| Plant room ventilation and noise isolation | ☐ |

## Pre-delivery information to collect from OEM

1. Single-line electrical diagram and total kW
2. Chiller model, flow, dual-loop diagram
3. Gas ports: pressure range, fitting type
4. Extraction spigot size and required static pressure
5. Foundation bolt pattern and weight
6. Environmental limits (T, RH, altitude)
7. Shipping dimensions and weight breakdown per crate (for crane/forklift planning)
8. Commissioning engineer requirements — do they need scaffolding, specific tools, network access?

## Layout planning

A rough but useful zoning approach for the whole cell, not just the laser footprint:

```
[Laser cell] — clean, controlled T/RH, away from doors and direct sun
[Chiller] — adjacent room or ventilated alcove, ≤10 m hose run
[Compressor/dryer] — separate noisy/vibrating room if possible
[N2 PSA plant] — ventilated; away from sparks and cutting zone
[Dust collector] — outside or plant room; shortest practical duct path
[Gas storage] — dewar/cylinder compound per local hazardous substance rules
```

See [[Installation Clearances and Foundations]] for detail on each zone.

## Common site failures

| Symptom after install | Likely site cause |
| --- | --- |
| Random height alarms | Poor ground, EMI from welder |
| Chiller E1/E2 summer | Room >35 °C, blocked vents |
| Condensation alarms | Chiller set too low vs dew point |
| Poor stainless edge | N₂ purity or regulator undersized |
| Lens contamination air cut | No dryer/fine filter |
| Extraction weak at far end | Undersized fan, too many bends |
| Voltage sag when compressor starts | Compressor sharing laser feeder |
| Machine "moved fine, now faults constantly" | Ground electrode not re-tested at new site, or re-leveled without re-checking anchor torque |
| Nuisance nuisance-tripping breaker | Breaker sized for name-plate current only, not inrush |

## Post-install verification (before handover)

1. Re-measure phase voltages and imbalance under laser load, not just at idle
2. Re-measure ground resistance after all trades have finished (concrete cutting, other electrical work can disturb electrodes)
3. Confirm dynamic gas pressure at the head during a real pierce, not just static regulator reading
4. Log a baseline room temperature/humidity reading for future comparison
5. Photograph final installation state (cable routing, gas connections, duct runs) for the machine hub note

## Related notes

- [[Fiber Laser Commissioning Sequence]]
- [[Installation Clearances and Foundations]]
- [[Ambient Temperature Limits]]
- [[Dehumidifiers for Laser Rooms]]
- [[Laser Electrical Supply Requirements]]

## Sources

- GWK fiber laser installation requirements checklist
- Arcus CNC laser cutting environmental setup requirements
