---
aliases:
  - nitrogen plant troubleshooting
  - PSA nitrogen faults
type: technical-reference
category: nitrogen-systems
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: South-Tek N2 reference, field PSA package service
status: generic reference — verify against nameplate and project drawing
---

# Nitrogen System Troubleshooting

Return to [[PSA Nitrogen Generators]] · [[Technical Reference Index]]

> [!info] When to open this note
> Symptom-based diagnosis from compressed air through PSA, booster, HP bank, and laser inlet. Walk the air path — do not start at the cutting head.

## Diagnostic order (always)

1. [[Air Compressors for Laser Cutting]] — discharge pressure, temperature, duty
2. [[Refrigerated Dryers]] + [[Air Filtration Stages]] — water/oil before PSA
3. PSA generator — buffer pressure, cycle, purity
4. [[Nitrogen Booster and HP Storage]]
5. [[Gas Regulators and PRVs]] at laser
6. Cut quality / CypCut gas type — [[Nitrogen Assist Gas]]

## Master symptom table

| Symptom | Likely causes | Actions |
| --- | --- | --- |
| Yellow/gold stainless edge | Low purity; low dynamic cut pressure; wrong gas in layer | Analyzer; dynamic P; CypCut gas type |
| Purity OK, pressure sags mid-cut | Undersized booster/bank; HP leak | Leak test HP; time bank recovery |
| Generator won't reach standby | Low feed air; inlet filter; valve fault | Compressor band; replace inlet filter |
| Rapid CMS degradation | Oil/water on feed air | Fix treatment; OEM bed service |
| Booster overheats / continuous run | High duty; low suction; HP leak | Setpoints — [[Nitrogen System Pressure Setpoints]]; find leak |
| Compressor 100% duty | Undersized for PSA + laser air | Flow audit; staging |
| O₂ waste vent sound change | Valve timing / CMS issue | OEM service |
| Laser gas alarm, plant gauges OK | Machine regulator/solenoid/hose | Isolate laser leg |
| Purity analyzer jumpy | Sample line wet/dirty; sensor due cal | Dry sample; calibrate |
| Buffer OK, booster won't start | Interlock; suction below cut-in; electrical | Check suction band and enable chain |

## Pressure tracing procedure

1. Tag gauges: compressor discharge, PSA inlet, buffer, booster suction, bank, laser inlet (static)
2. Photograph or log values at idle
3. Run a labeled test pierce at production nozzle/pressure
4. Log laser inlet dynamic + bank trend every 5–10 s through pierce
5. Identify first stage that leaves its band
6. Repair that stage before adjusting unrelated setpoints

## Feed-air quality checks (purity failures)

| Test | Pass hint |
| --- | --- |
| Dryer condensate production | Dryer actually cooling |
| Coalescing bowl | No free oil |
| PDP / dryer status | Near rated PDP |
| PSA inlet filter ΔP | Not choked |
| Compressor separator service history | On interval |

Oil on CMS → expensive bed replacement. Fix air treatment first.

## Laser-side isolation test

If plant pressures look normal:

1. Cap or isolate machine inlet; watch plant hold
2. If plant holds and laser still alarms → machine regulator, hose, proportional valve, solenoid
3. If plant falls with laser isolated → plant leak

## Purity vs pressure (do not confuse)

| Edge symptom | First metric |
| --- | --- |
| Yellow SS, pressure gauge OK | Purity / contamination |
| Good purity certificate, weak blow | Dynamic pressure / flow |
| Both marginal | Undersized system for kW/nozzle |

## When to call OEM / specialist

- CMS bed replacement
- Booster valve rebuild / HP packing
- Purity analyzer calibration gases
- Relief valve / vessel certification issues
- Control PLC program faults

## Safety notes

| Hazard | Practice |
| --- | --- |
| HP nitrogen (~300 bar banks) | Trained personnel; whip checks; stand clear of end caps |
| O₂-rich PSA waste vent | Ventilate; no ignition sources |
| Confined spaces | N₂ enrichment / O₂ displacement risk |

## Related notes

- [[Nitrogen System Pressure Setpoints]]
- [[Assist Gas Overview]]
- [[Fiber Laser Common Alarms]]
- [[Compressed Air Cutting]] — if dual-use compressor

## Sources

- South-Tek laser cutting nitrogen systems reference
- Field PSA package service practice
