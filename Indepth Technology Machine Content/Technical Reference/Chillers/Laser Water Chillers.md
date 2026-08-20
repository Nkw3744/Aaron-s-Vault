---
aliases:
  - laser chiller
  - water chiller fiber laser
type: technical-reference
category: chillers
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: CW-5200 manual, GWK install checklist, BLMA chiller guide
status: generic reference — verify against nameplate and project drawing
---

# Laser Water Chillers

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Chiller role, connection, fill, normal operation, and entry points to dual-loop, water quality, and alarm notes.

## Function

Removes heat from:

- Laser source (resonator / fiber module)
- Cutting head optics and QBH (often separate loop)
- Sometimes delivery-fiber cooling

Without stable cooling: power drift, over-temp alarms, source shutdown.

## Common models (China-market fiber packages)

| Model class | Typical laser match |
| --- | --- |
| CW-5000 / CW-5200 | ~0.5–2 kW class |
| CW-6000 / CW-6100 / CW-6200 | ~2–6 kW; dual temp |
| OEM industrial | 8 kW+ |

Alarms: [[CW Series Chiller Alarm Codes]]. Flowchart: [[Chiller Troubleshooting Flowchart]].

## Connection convention

**Chiller OUT → machine IN** (cold to load)  
**Machine OUT → chiller IN** (warm return)

Verify stickers — some manuals reverse wording. Dual-loop: [[Dual-Temperature Chiller Circuits]].

## Fill and commissioning

1. Distilled/DI water — [[Cooling Water Quality]]
2. Fill to green zone (not overfill mark)
3. Run pump; bleed air
4. Recheck level after loop fills
5. Set LT/HT for season and dew point — [[Dew Point and Chiller Setpoints]]
6. Run 30+ min before emission
7. Winter: glycol/heat plan — [[Antifreeze and Winter Operation]]

## Hose and routing

| Parameter | Typical OEM hint |
| --- | --- |
| Max hose length | ≤10 m |
| Avoid | Kinks, door crush, sharp bends |
| Insulation | Helpful on returns in humid shops |

## Normal operation

| Observation | Meaning |
| --- | --- |
| Pump continuous when powered | Normal |
| Compressor/fans cycle on load | Normal |
| Stable ±1–3 °C of setpoint | Healthy control |
| No leaks at QBH couplers | OK |

## Local context

Chiller plug-in on [[Gweike 3015GAII]] work history.

## CO₂ note

Different setpoints/chemistry possible — [[CO2 Chiller and Gas Requirements]].

## Related notes

- [[Fiber Laser Commissioning Sequence]]
- [[Ambient Temperature Limits]]
- [[Workshop Humidity and Condensation]]

## Sources

- CW-5200 user manual
- BLMA chiller installation procedure
- GWK installation checklist (chiller phase)
