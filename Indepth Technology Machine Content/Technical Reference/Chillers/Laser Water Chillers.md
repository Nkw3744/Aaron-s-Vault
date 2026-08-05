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
> Chiller role, connection, fill, and normal operation for fiber and CO₂ lasers.

## Function

Removes heat from:

- Laser source ( resonator / fiber module)
- Cutting head optics and QBH (often separate loop)
- Sometimes delivery fiber cooling circuit

Without stable cooling: power drift, over-temp alarms, source shutdown.

## Common models (China-market fiber packages)

| Model class | Typical laser match |
| --- | --- |
| CW-5000 / CW-5200 | 0.5–2 kW class |
| CW-6000 / CW-6100 / CW-6200 | 2–6 kW; dual temp |
| OEM branded industrial | 8 kW+ |

Alarm detail: [[CW Series Chiller Alarm Codes]].

## Connection convention

**Chiller OUT → machine IN** (cold to load)  
**Machine OUT → chiller IN** (warm return)

Verify arrow stickers on both chiller and laser labels — some OEMs reverse terminology in manuals.

## Fill and commissioning

1. Use distilled or deionized water — [[Cooling Water Quality]]
2. Fill to middle/top of green on sight gauge — not "FULL" overfill mark
3. Run pump; bleed air at high points in laser loop
4. Check level again after loop fills
5. Set temperature setpoints — [[Dual-Temperature Chiller Circuits]], [[Dew Point and Chiller Setpoints]]
6. Run 30 min before enabling laser emission

## Normal operation

- Pump runs continuously when chiller powered
- Compressor fan cycles on load
- Water temp stable ±1–3 °C of setpoint depending on controller
- No leaks at QBH water lines or quick couplers

## Hose and routing

| Parameter | Typical OEM hint |
| --- | --- |
| Max hose length | ≤10 m total run |
| Avoid | Kinks, sharp bends, crushing in door tracks |
| Insulation | Optional on return line in humid shops |

## Troubleshooting entry

[[Chiller Troubleshooting Flowchart]] · [[CW Series Chiller Alarm Codes]]

## CO₂ note

CO₂ lasers often use lower water temperature setpoints and different chemistry — [[CO2 Chiller and Gas Requirements]].

## Related notes

- [[Antifreeze and Winter Operation]]
- [[Fiber Laser Commissioning Sequence]]

## Local context

Water chiller plug-in documented on [[Gweike 3015GAII]] work history.

## Sources

- CW-5200 user manual
- BLMA chiller installation procedure
- GWK installation checklist (chiller phase)
