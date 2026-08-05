---
aliases:
  - height sensor alarms
  - capacitance alarm laser
type: technical-reference
category: cutting-head
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Arcus, Yihai Raytools guide, Smart cut FAQ
status: generic reference — verify against nameplate and project drawing
---

# Height Sensor Alarm Reference

Return to [[Capacitive Height Sensing BCS100]] · [[Technical Reference Index]]

> [!info] When to open this note
> Alarm text → cause → fix order for capacitive height systems.

> [!danger] Stop cutting on follow faults
> A crashing head destroys optics in seconds. Do not restart production until root cause cleared.

## Diagnostic order (shop floor)

1. **Nozzle tip** — slag bead? Clean or replace
2. **Ceramic ring** — crack, carbon track? Replace
3. **Nozzle torque** — loose?
4. **SMA/RF cable** — wiggle test while watching capacitance value
5. **Ground** — bed, slats, sheet rust under part
6. **Recalibrate** on clean flat plate
7. **Pre-amp / BCS100** — last swap

## Alarm table

| Message / symptom | Meaning | Likely cause | Action |
| --- | --- | --- | --- |
| Z-axis touching board | Zero distance detected | Touch, slag bridge, loose nozzle | Clean; recal |
| Capacitance is 0 | Open circuit | RF unplugged, broken cable, dead amp | Trace RF path |
| Capacitance large / MAX | Short to ground | Cracked ceramic, water in head | Replace ceramic; dry |
| Sensor not stable | Noisy signal | Bad ground, EMI, loose RF | Ground; reroute cables |
| Follow out of range | Z limit hit | Warped sheet, bad cal data | Flat stock; recal |
| Over-distance / limit | Cal lost or touch | Same as touch | One-key cal |
| Sensor disconnected | Cable/ceramic | Physical break | Replace parts |
| Z follow error | Slag on nozzle | Contamination | Wire brush nozzle |
| Erratic height jumps | Ground or slag | Floating zero | Ground strap; clean |
| BCS100 network timeout | Comm loss | IP, cable | Network check |
| Capacity change >100 on blow | Mechanical shift | Ceramic install, loose nozzle | Re-seat ceramic; torque |

## Blow-air capacitance test

With assist gas blow on: if capacitance shifts >100 units, check ceramic seating and nozzle tightness (Smart cut guidance).

## Temperature drift

Laser scatter heating nozzle or hot slag changes capacitance — clean nozzle; verify coaxial alignment.

## Related notes

- [[Fiber Laser Common Alarms]]
- [[Cutting Head Nozzles and Ceramics]]

## Sources

- Arcus capacitive sensor troubleshooting
- Yihai Raytools capacitive height sensor alarm guide
- Smart cut machinery after-sales FAQ
