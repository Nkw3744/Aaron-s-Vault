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
> Step-by-step decision tree for chiller alarms and no-cool conditions — use this when [[CW Series Chiller Alarm Codes]] has told you *what* the alarm means but you need the structured path to actually resolve it.

## How to use this flowchart effectively

Work through exactly one branch at a time, in order, and do not skip a step because it "probably isn't the problem" — the value of a flowchart like this is precisely that it catches the boring, common causes before you spend time on rare, complex ones. Most chiller call-outs resolve at Step 1 or 2 of whichever branch applies; escalation to genuine refrigeration or electronic component failure is comparatively rare.

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

> [!warning] Never just replace a blown fuse and walk away
> A fuse rarely blows for no reason. If a fuse has failed, look for the underlying cause (a shorted component, a pump seizure drawing excess current) before simply fitting a new fuse and re-energizing — otherwise the replacement fuse is likely to blow again, or worse, something downstream that should have been protected sustains damage first.

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

> [!danger] Disabling condensation interlocks
> Some technicians are tempted to disable a nuisance condensation interlock to "get production moving." This removes a genuine protection against water damage to optics and electronics — only do this as a documented, customer-acknowledged temporary measure while the real fix (dehumidification or setpoint correction) is scheduled, never as a permanent solution.

---

## Branch F — Chiller runs but cutting performance degrades slowly over weeks

Not a hard alarm at all, but worth including because it is a real and common pattern:

```
Check water clarity/color — see Cooling Water Quality
    ↓ discolored
Schedule flush and refill
    ↓ clear
Check condenser filter cleanliness
    ↓ dirty
Clean filter; re-test performance
    ↓ clean
Check setpoint drift — has anyone changed it since commissioning?
    ↓ unchanged
Consider refrigerant charge or compressor wear — technician/OEM
```

---

## When to stop and escalate

- Water inside laser module
- Repeated E5/E4 after sensor swap
- Refrigerant work required
- Any electrical burn smell
- Any symptom that returns immediately after a fix that should have resolved it — repeating the same fix a third time without a different diagnosis is a sign to escalate rather than persist

## Related notes

- [[Cooling Water Quality]]
- [[Workshop Humidity and Condensation]]
- [[CW Series Chiller Alarm Codes]]

## Sources

- CW-5000/5200 maintenance manual flow diagnostic
- BRM Lasers chiller alarm guide
