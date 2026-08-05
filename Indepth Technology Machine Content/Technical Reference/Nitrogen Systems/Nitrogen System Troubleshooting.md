---
aliases:
  - nitrogen plant troubleshooting
  - PSA nitrogen faults
type: technical-reference
category: nitrogen-systems
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: South-Tek N2 reference, field service practice
status: generic reference — verify against nameplate and project drawing
---

# Nitrogen System Troubleshooting

Return to [[PSA Nitrogen Generators]] · [[Technical Reference Index]]

> [!info] When to open this note
> Symptom-based diagnosis along the compressed air → PSA → booster → laser path.

## Diagnostic order

Follow air path upstream to downstream:

1. [[Air Compressors for Laser Cutting]] — discharge pressure and quality
2. [[Refrigerated Dryers]] and [[Air Filtration Stages]]
3. PSA generator — buffer pressure, cycle, purity
4. [[Nitrogen Booster and HP Storage]]
5. [[Gas Regulators and PRVs]] at laser
6. Cut quality — [[Nitrogen Assist Gas]]

## Symptom table

| Symptom | Likely causes | Actions |
| --- | --- | --- |
| Yellow stainless edge | Low purity, low cut pressure, wrong gas in layer | Analyzer; dynamic pressure; CypCut gas type |
| Purity OK but pressure sag | Undersized booster/bank; leak | HP leak test; time booster recovery |
| Generator won't reach standby | Low feed air pressure; inlet filter blocked | Check compressor; replace inlet filter |
| Rapid CMS degradation | Oil/water on feed air | Fix treatment; replace beds per OEM |
| Booster overheats | High duty; suction pressure too low | Adjust bands — [[Nitrogen System Pressure Setpoints]] |
| Compressor runs 100% | Undersized for PSA + laser air | Flow audit |
| O₂ waste vent loud change | Valve timing fault | OEM service |
| Laser gas alarm, plant OK | Machine regulator; solenoid | Isolate laser leg |

## Pressure tracing procedure

1. Record pressures at: compressor discharge, PSA inlet, buffer, booster suction, bank, laser inlet (static)
2. Run test pierce; record laser inlet **dynamic**
3. Compare to project drawing setpoints
4. Identify first stage where drop exceeds spec

## Feed air quality test

If purity failed:

- Capture air sample at PSA inlet if possible
- Check oil carryover test paper at coalescer drain
- Verify dryer PDP

## When to call OEM

- CMS replacement
- Booster valve rebuild
- Purity analyzer calibration
- Any HP vessel or relief valve issue

## Related notes

- [[Assist Gas Overview]]
- [[Fiber Laser Common Alarms]]

## Sources

- South-Tek laser cutting nitrogen systems reference
- Field PSA package service practice
