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
> Pre-install site survey, customer handover checklist, or verifying why a machine alarms after move.

> [!warning] Local codes apply
> Electrical, fire, and ventilation rules vary by jurisdiction. This note is equipment-oriented, not a compliance certificate.

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

Detail: [[Laser Electrical Supply Requirements]], [[Grounding and EMC Isolation]].

### Foundation and floor

| Item | Typical | Verify |
| --- | --- | --- |
| Floor loading | ≥500 kg/m² or engineer sign-off | ☐ |
| Level | Within OEM shim spec (often 0.05 mm/m) | ☐ |
| Vibration | No heavy presses within isolation zone | ☐ |
| Clearances | Front ≥1.2 m; rear (service) ≥1.5 m | ☐ [[Installation Clearances and Foundations]] |

### Environment

| Item | Typical | Verify |
| --- | --- | --- |
| Ambient temperature | 10–35 °C workshop; 23–27 °C laser zone ideal | ☐ |
| Humidity | ≤75% RH; ≤60% preferred | ☐ [[Workshop Humidity and Condensation]] |
| Dust | Clean install; filter HVAC if needed | ☐ |
| Chiller location | Often separate from laser room (adds heat/humidity) | ☐ |
| Condensation margin | Cooled surfaces ≥ dew point + 2–3 °C | ☐ [[Dew Point and Chiller Setpoints]] |

### Cooling water prep

| Item | Typical | Verify |
| --- | --- | --- |
| Water type | Distilled or deionized for fill | ☐ [[Cooling Water Quality]] |
| Volume | 20–80 L in chiller + loop (model dependent) | ☐ |
| Hose run | ≤10 m common OEM limit | ☐ |
| Inlet pressure | ~4.5–6 bar at chiller (if specified) | ☐ |

### Assist gas

| Gas | Purity (typical) | Notes |
| --- | --- | --- |
| O₂ | >99.6% | Regulator 0.05–1.2 MPa out |
| N₂ | ≥99.99% | Dewar/bulk/PSA; not small cylinders for production |
| Air cutting | Dry, oil-free | Screw + dryer + fine filters |

See [[Assist Gas Overview]], [[Gas Pipework and Fittings]].

### Ventilation and extraction

| Item | Verify |
| --- | --- |
| Dust collector sized for table — [[Dust Collector Sizing]] | ☐ |
| Duct route planned; minimal bends | ☐ |
| Discharge: outdoor or filtered recirc per EHS | ☐ |
| Fire extinguishers per local code | ☐ |

### Compressed air / nitrogen plant (if applicable)

| Item | Verify |
| --- | --- |
| Compressor kW and 16 bar class for air cutting | ☐ |
| Dryer and 0.01 µm filtration chain | ☐ |
| PSA feed air quality if N₂ generator | ☐ [[PSA Nitrogen Generators]] |
| Booster and HP storage for high-pressure N₂ | ☐ |

## Pre-delivery information to collect from OEM

1. Single-line electrical diagram and total kW
2. Chiller model, flow, dual-loop diagram
3. Gas ports: pressure range, fitting type
4. Extraction spigot size and required static pressure
5. Foundation bolt pattern and weight
6. Environmental limits (T, RH, altitude)

## Common site failures

| Symptom after install | Likely site cause |
| --- | --- |
| Random height alarms | Poor ground, EMI from welder |
| Chiller E1/E2 summer | Room >35 °C, blocked vents |
| Condensation alarms | Chiller set too low vs dew point |
| Poor stainless edge | N₂ purity or regulator undersized |
| Lens contamination air cut | No dryer/fine filter |
| Extraction weak at far end | Undersized fan, too many bends |

## Related notes

- [[Fiber Laser Commissioning Sequence]]
- [[Installation Clearances and Foundations]]
- [[Ambient Temperature Limits]]
- [[Dehumidifiers for Laser Rooms]]

## Sources

- GWK fiber laser installation requirements checklist
- Arcus CNC laser cutting environmental setup requirements
