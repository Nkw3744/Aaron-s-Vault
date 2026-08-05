---
aliases:
  - CW-5200 alarm codes
  - CW-5000 E1 E2 E6
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
> Decoding E1–E6 on CW-5000/5200/6000 class chillers common on import fiber lasers.

Display alternates between water temperature and error code when alarm active.

## Alarm code table

| Code | Meaning | First actions |
| --- | --- | --- |
| **E1** | Ambient (room) temperature too high | Improve chiller ventilation; reduce room temp below ~35 °C |
| **E2** | Water temperature too high | Check heat load, refrigerant, condenser filter, setpoint vs dew point conflict; cease cutting until stable |
| **E3** | Water temperature too low | Raise setpoint; check sensor; cold ambient |
| **E4** | Room temperature sensor fault | Replace ambient sensor |
| **E5** | Water temperature sensor fault | Replace water sensor |
| **E6** | Flow fault — low or no circulation | Level, pump, kinks, blocked laser channel |

## Flow alarm diagnosis (E6 / flow light)

### Step 1 — Water level

Check rear sight gauge. Fill to green zone. Look for puddles indicating leak.

### Step 2 — Kinks and connections

Both hoses machine↔chiller attached; no crushed hose in cable chain.

### Step 3 — Short-loop bypass test

1. Power off
2. Connect ~1 m hose **chiller OUT → chiller IN** directly
3. Power on
4. If alarm clears: restriction is in **machine loop** (laser blockages, closed valve)
5. If alarm persists: chiller pump, power supply, or internal blockage

### Step 4 — Laser source water ingress

On some modules, water in outer glass indicates source leak — **stop**; service source.

## E2 during summer production

Common stack:

- Room >35 °C
- Dirty condenser gauze
- Heat load from high-duty cutting
- Setpoint too low fighting dew point — review [[Dew Point and Chiller Setpoints]]

## No display but fans run

Possible display fault vs power supply fault — see [[Chiller Troubleshooting Flowchart]].

## Related notes

- [[Fiber Laser Common Alarms]]
- [[Dual-Temperature Chiller Circuits]]

## Sources

- CW-5200 industrial chiller user manual
- CW-5000/5200 maintenance manual
- BRM Lasers CW-5000/5200 alarm support article
