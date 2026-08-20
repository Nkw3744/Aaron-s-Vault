---
aliases:
  - CW-5200 alarm codes
  - CW-5000 E1 E2 E6
  - S&A chiller alarms
type: technical-reference
category: chillers
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: CW-5200 user manual, CW maintenance manual, BRM Lasers support
status: generic reference — verify against nameplate and project drawing
---

# CW Series Chiller Alarm Codes

Return to [[Laser Water Chillers]] · [[Technical Reference Index]]

> [!info] When to open this note
> Decoding E1–E6 on CW-5000/5200/6000-class (S&A-style) chillers common on import fiber lasers. Display often alternates between water temperature and the error code when an alarm is active.

> [!warning] Confirm model
> Dual-temperature CW-6100/6200 units may show loop-specific behaviour. Always note which circuit (LT/HT) is out of band — [[Dual-Temperature Chiller Circuits]].

## Alarm code table

| Code | Meaning | First actions |
| --- | --- | --- |
| **E1** | Ambient (room) temperature too high | Improve chiller ventilation; reduce room temp; clean condenser gauze; check clearances |
| **E2** | Water temperature too high | Cease heavy cutting; check heat load, refrigerant, condenser, setpoint vs duty and dew-point conflict |
| **E3** | Water temperature too low | Raise setpoint; check sensor; cold ambient / winter start |
| **E4** | Room temperature sensor fault | Replace ambient sensor |
| **E5** | Water temperature sensor fault | Replace water sensor |
| **E6** | Flow fault — low or no circulation | Level, pump, kinks, blocked laser channel — see below |

Full decision tree: [[Chiller Troubleshooting Flowchart]].

## What the front panel is telling you

| Observation | Meaning |
| --- | --- |
| Red alarm light + code | Active fault; laser interlock may be open |
| Temperature and code alternating | Normal alarm display mode |
| Flow light / E6 with pump silent | Pump not running — level, PSU, or pump dead |
| Flow light / E6 with pump running | Restriction or false flow sensor |
| No display, fans dead | Mains / fuse / internal supply |

## Flow alarm diagnosis (E6) — detailed

### Step 1 — Water level
- Sight gauge in **green zone** (middle to upper)
- Top up with DI/distilled only — [[Cooling Water Quality]]
- Hunt for puddles under chiller, machine, and QBH couplers

### Step 2 — External hoses
- Both hoses attached; quick-couplers fully locked
- No crush in cable chain or under doors
- Correct polarity: chiller OUT → machine IN
- Dual-loop: both pairs connected

### Step 3 — Short-loop bypass test
1. Power off
2. Connect ~1 m hose **chiller OUT → chiller IN** (bypass machine)
3. Power on
4. **Alarm clears** → restriction is in the **machine** cooling path (valves, laser blockages, head/QBH kink)
5. **Alarm persists** → chiller pump, switching supply, internal pipe/filter

### Step 4 — Laser source water ingress
On some modules, water visible in outer glass indicates a source leak. **Stop.** Do not keep filling and running — source service/replacement territory.

### Step 5 — Winter viscosity
Glycol mix too rich or ice-cold start → sluggish flow until warm — [[Antifreeze and Winter Operation]].

## E1 — ambient too high

| Check | Action |
| --- | --- |
| Room >35 °C | AC / shift load — [[Ambient Temperature Limits]] |
| Condenser inlet hotter than room | Recirculating hot air — relocate / duct |
| Dirty condenser gauze | Clean |
| Clearance blocked | [[Installation Clearances and Foundations]] |
| Chiller in same sealed room as laser | Heat stacking — vent or separate |

## E2 — water too high (summer stack)

Common combination:

1. Hot room
2. Dirty condenser
3. High cutting duty
4. LT setpoint fighting humidity strategy
5. Low water / poor heat transfer (old water)

Also review [[Dew Point and Chiller Setpoints]] — operators sometimes lower water aggressively in summer and create condensation risk while still hitting E2 under load.

## E3 — water too low

| Cause | Action |
| --- | --- |
| Setpoint too low for ambient | Raise toward OEM default |
| Sensor fault (also E5) | Compare IR on hose vs display |
| Cold start overnight | Allow warm-up before emission |

## E4 / E5 — sensor faults

- Reseat connectors first
- Replace sensor with OEM part
- If new sensor still faults → controller board (escalate)

## Dual-temperature specifics

| Symptom | Check |
| --- | --- |
| Only head sweats | HT too low vs dew point |
| Only source over-temps | LT flow/capacity; swapped hoses |
| Same code, both loops hot | Shared refrigeration capacity exceeded |

## No display / dead front

1. Wall plug and breaker
2. Front fuse (if fitted) — replace after finding cause
3. Internal switching supply — technician
4. Distinguish from laser HMI interlock messages — [[Fiber Laser Common Alarms]]

## After clearing any alarm

1. Run 15–30 min; confirm stable temperature
2. Confirm LT/HT and dew-point margin before emission
3. Log code, cause, fix on machine work record
4. If same code returns twice → stop reset loops; escalate diagnosis

## Related notes

- [[Laser Water Chillers]]
- [[Chiller Troubleshooting Flowchart]]
- [[Cooling Water Quality]]
- [[Antifreeze and Winter Operation]]
- [[Dual-Temperature Chiller Circuits]]
- [[Ambient Temperature Limits]]

## Sources

- CW-5200 industrial chiller user manual
- CW-5000/5200 maintenance manual
- BRM Lasers CW-5000/5200 alarm support article
