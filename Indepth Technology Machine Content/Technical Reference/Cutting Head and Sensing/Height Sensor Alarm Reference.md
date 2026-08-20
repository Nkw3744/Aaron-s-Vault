---
aliases:
  - height sensor alarms
  - capacitance alarm laser
  - BCS100 alarms
type: technical-reference
category: cutting-head
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Arcus, Yihai Raytools guide, Smart cut FAQ, field BCS100 practice
status: generic reference — verify against nameplate and project drawing
---

# Height Sensor Alarm Reference

Return to [[Capacitive Height Sensing BCS100]] · [[Technical Reference Index]]

> [!info] When to open this note
> Alarm text → meaning → likely cause → fix order for capacitive height systems (BCS100 and similar). Use before replacing expensive amplifiers.

> [!danger] Stop cutting on follow faults
> A crashing head destroys the ceramic, nozzle, window, and sometimes the collimator in seconds. Clear the root cause before production resumes.

## Golden diagnostic order (shop floor)

Do this sequence before swapping BCS100 units:

1. **Nozzle tip** — slag bead? Clean or replace
2. **Ceramic ring** — crack, carbon track, loose? Replace
3. **Nozzle torque** — seated firmly?
4. **SMA / RF cable** — wiggle test while watching live capacitance
5. **Ground path** — sheet ↔ slats ↔ bed ↔ PE — [[Grounding and EMC Isolation]]
6. **Recalibrate** on clean, flat, bare metal
7. **Pre-amp / controller** — last

~80% of "sensor" calls are nozzle/ceramic/slag/ground.

## Alarm / symptom table

| Message / symptom | Meaning | Likely cause | Action |
| --- | --- | --- | --- |
| Z-axis touching board | Zero distance detected | Physical touch, slag bridge, loose nozzle | Clean/replace nozzle; inspect ceramic; recal |
| Capacitance is 0 | Open circuit | RF unplugged, broken SMA, dead pre-amp | Trace RF path end-to-end |
| Capacitance large / MAX | Short to ground | Cracked ceramic, water in head, nozzle shorted to body | Replace ceramic; dry head; check seals |
| Sensor not stable | Noisy signal | Bad ground, EMI, loose RF, rusty sheet | Bonding; cable route; clean plate |
| Follow out of range | Z hit limit | Warped sheet, bad cal, wrong lift | Flat stock; recal; check soft limits |
| Over-distance / limit | Cal lost or touch | Same family as touch / bad cal | One-key / floating head cal |
| Sensor disconnected | Cable or ceramic path open | Physical break | Replace cable/ceramic |
| Z follow error | Often slag on nozzle mid-cut | Contamination; splash | Clean nozzle; review pierce/gas |
| Erratic height jumps | Floating zero or EMI | Ground; VFD; RF intermittent | Ground strap; wiggle test; segregate cables |
| BCS100 network timeout | Comm loss | Ethernet, IP subnet, EMI | Cable/IP; then EMC |
| Capacity change >100 on blow | Mechanical shift under gas | Loose nozzle/ceramic | Reseat; torque; replace ceramic |
| Cal fails immediately Capacity 0 | Open before cal starts | RF path | Same as Capacitance is 0 |
| Poor stability rating after cal | Hardware or plate issue | Dirty plate, crack, EMI | New plate; new ceramic; quiet EMI |

## Blow-air capacitance test

With assist gas blow on (laser off):

- If capacitance shifts a lot (Smart cut FAQ cites >100 unit class changes), suspect ceramic seating or nozzle tightness rather than "software."

## Temperature / process drift

| Cause | Effect |
| --- | --- |
| Hot slag on nozzle | Capacitance drift → false follow |
| Laser scatter heating nozzle | Drift mid-cut |
| Pierce splash (esp. galvanized) | Beads → touch alarms — [[Zn and Coated Material Fume Notes]] |

Fix process (pierce, focus, gas) and hygiene — not only electronics.

## Network / BCS100 specific

| Check | Detail |
| --- | --- |
| IP subnet | Same as CNC motion network |
| Cable | Industrial Ethernet; no random office patch abuse |
| Power | Stable 24 V at unit under load |
| Firmware/config | After board swap, restore OEM config |

## Correlation with other systems

| If alarms cluster when… | Suspect |
| --- | --- |
| Compressor/VFD starts | EMC — [[Grounding and EMC Isolation]] |
| After nozzle auto-change | Seat/clamp — [[Nozzle Change and Shutter Actuators]] |
| Only on rusty sheet | Ground path |
| After head crash | Ceramic + RF cable + mechanical |
| With water on head | Condensation — [[Dew Point and Chiller Setpoints]] |

## Safe response checklist

1. Pause / stop emission
2. Screenshot or write exact alarm text + time
3. Inspect nozzle/ceramic before reset spam
4. Clear root cause
5. Recalibrate
6. Test follow on scrap at low speed
7. Document on machine work log

## Related notes

- [[Capacitive Height Sensing BCS100]]
- [[Cutting Head Nozzles and Ceramics]]
- [[Fiber Laser Common Alarms]]
- [[Grounding and EMC Isolation]]
- [[Autofocus and Proportional Gas Valves]]

## Sources

- Arcus capacitive sensor troubleshooting
- Yihai Raytools capacitive height sensor alarm guide
- Smart cut machinery after-sales FAQ (THC / capacitance)
- Field BCS100 service practice
