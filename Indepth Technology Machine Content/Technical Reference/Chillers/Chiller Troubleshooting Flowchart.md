---
aliases:
  - chiller fault finding
  - water chiller diagnosis
type: technical-reference
category: chillers
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: CW maintenance manual, BRM support, field practice
status: generic reference — verify against nameplate and project drawing
---

# Chiller Troubleshooting Flowchart

Return to [[Laser Water Chillers]] · [[Technical Reference Index]]

> [!info] When to open this note
> Step-by-step decision tree for chiller alarms and no-cool conditions.

## Start

**Alarm or overtemperature?** → Note code — [[CW Series Chiller Alarm Codes]]

---

## Branch A — Flow alarm (E6 or flow light)

```
Power off → Check water level in green zone
    ↓ low
Add DI water; inspect for leaks
    ↓ OK
Inspect hoses for kinks/disconnect
    ↓ OK
Short-loop test (chiller out→in)
    ↓ passes
Fault in machine cooling path — valves, laser blockages
    ↓ fails
Open chiller — check pump, filter, internal pipe
```

---

## Branch B — High water temp (E2)

```
Room temp >35°C?
    yes → Ventilate; AC; clean condenser filter
    ↓ no
Condenser fan running?
    no → Refrigeration fault; technician
    ↓ yes
Heat load excessive (high power cut + low setpoint)?
    yes → Review setpoint vs dew point
    ↓
Refrigerant leak or failed compressor — technician
```

---

## Branch C — No power / dead display

```
Plug and breaker OK?
    ↓ yes
Front fuse (if fitted) — replace after finding cause
    ↓
Internal switching supply — technician
```

---

## Branch D — Pump runs, no cooling

Fans never start on load → refrigeration circuit or parameter config

Check factory default parameters per manual after any controller change.

---

## Branch E — Condensation / dew alarm (OEM chiller feature)

Not E1–E6 — separate interlock:

1. Measure room T and RH
2. Calculate dew point — [[Dew Point and Chiller Setpoints]]
3. Raise HT loop or lower RH
4. Do not disable interlock without risk acceptance

---

## When to stop and escalate

- Water inside laser module
- Repeated E5/E4 after sensor swap
- Refrigerant work required
- Any electrical burn smell

## Related notes

- [[Cooling Water Quality]]
- [[Workshop Humidity and Condensation]]

## Sources

- CW-5000/5200 maintenance manual flow diagnostic
- BRM Lasers chiller alarm guide
