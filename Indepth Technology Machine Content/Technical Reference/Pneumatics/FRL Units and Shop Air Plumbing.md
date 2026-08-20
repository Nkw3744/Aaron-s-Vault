---
aliases:
  - FRL unit laser
  - shop air plumbing laser
  - filter regulator lubricator laser
type: technical-reference
category: pneumatics
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: ISO 8573 practice, machine electrical cabinet pneumatics, field FRL service
status: generic reference — verify against nameplate and project drawing
---

# FRL Units and Shop Air Plumbing

Return to [[Pneumatic Cylinders in Laser Systems]] · [[Technical Reference Index]]

> [!info] When to open this note
> Filter–Regulator–Lubricator (FRL) units and shop air plumbing for **machine control air** — doors, dampers, ANC, shutter pilots — not the high-pressure cutting air train.

> [!warning] Two air systems
> Cutting assist air can be 16–30 bar class with oil-free fine filtration. Control air is usually 5–7 bar through an FRL. Mixing them damages seals and contaminates optics.

## Two air systems on many lasers

| System | Pressure | Quality | Serves |
| --- | --- | --- | --- |
| Cutting assist air | Up to ~1.6–3.0 MPa (16–30 bar) | Dry, oil-free — [[Air Filtration Stages]] | Head cut/pierce |
| Shop / control air | 0.5–0.7 MPa (5–7 bar) | FRL filtered; lubricated only if OEM requires | Cylinders, solenoids, some gas pilots |

Deep HP train: [[Air Compressors for Laser Cutting]], [[Compressed Air Cutting]].

## What each FRL stage does

| Stage | Function | Field tip |
| --- | --- | --- |
| **Filter** | Removes water droplets and particulate | Bowl down; auto-drain preferred |
| **Regulator** | Sets stable pressure to cabinet | Lock after set; gauge after regulator |
| **Lubricator** | Optional oil mist for cylinder seals | Many laser zones specify **dry** — omit or shut off |

Order is always F → R → L (filter first). Installing lubricator upstream of filter oils the filter media and ruins regulation.

## Recommended plumbing layout

```
Shop ring main
  → branch shutoff (lockable)
  → drip leg / drop with drain
  → FRL assembly
  → machine cabinet bulkhead
  → solenoid manifold
  → cylinders / pilots
```

| Rule | Reason |
| --- | --- |
| Hard pipe (copper/aluminium) near machine | Fewer leaks than soft hose |
| Flex only at vibration points | Avoids fatigue cracks |
| Shutoff for service | LOTO without whole shop downtime |
| Gauge after regulator | Diagnose starvation under load |
| Label "CONTROL AIR — NOT CUTTING AIR" | Prevents wrong hose connection after service |

## Pressure settings (typical)

| Destination | Typical set |
| --- | --- |
| General cabinet | 5–6 bar |
| Heavy door cylinders | Per OEM — may need 6–7 bar |
| Soft-start modules | Ramp fill to avoid slam |

Measure **at the FRL outlet under simultaneous actuation** (e.g. door + damper). Static 6 bar that collapses to 3 bar under load means undersized branch or clogged filter.

## Lubricator policy

| OEM says | Action |
| --- | --- |
| Lubricate cylinders | Set drip rate (often 1 drop per X cycles — start lean) |
| Dry air to head area / sensors | Blank or bypass lubricator; use dry-compatible seals |
| Mixed zones | Separate dry branch after filter/regulator, lubricated branch only to specified valves |

Over-oiling is a common cause of oily ceramic rings and unstable height sensing — [[Height Sensor Alarm Reference]].

## ISO 8573 context (control air)

Control air is less critical than cutting air, but wet dirty air still sticks valve spools. Practical targets:

| Contaminant | Practical goal |
| --- | --- |
| Water | No liquid in bowl after daily drain |
| Particles | Filter element not grey/black packed |
| Oil | Only intentional lubricator mist, not compressor carry-over |

If compressor oil appears in the FRL bowl, fix the compressor separator before blaming the laser.

## Maintenance schedule

| Item | Interval | Action |
| --- | --- | --- |
| Drain filter bowl | Daily in humid shops; weekly dry climates | Empty; verify auto-drain |
| Filter element | 6–12 months or ΔP rise | Replace; note date on bowl |
| Regulator drift | Annual | Compare set vs load; replace if hunting |
| Lubricator oil level | Weekly if used | Top with OEM oil only |
| Soft hose | Annual visual | Crack, swell, oil soft spots |

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| All valves weak | Regulator set low; main shutoff partly closed; clogged filter | Measure outlet under load |
| Water in cabinet | Failed drain; no drip leg; wet ring main | Fix drains; add drip leg |
| Oil on work / optics | Lubricator over-fed; wrong zone | Reduce/remove lubricator |
| Pressure hunts | Failed regulator diaphragm | Replace regulator |
| One branch dead | Local shutoff; kinked tube; manifold gasket | Trace from FRL forward |
| Compressor short-cycles laser idle | Control-air leaks | Soap-test from FRL to cylinders |

## Commissioning checklist

1. Confirm separate HP cutting inlet vs control-air inlet on machine
2. Install FRL with correct flow arrows and bowl orientation
3. Set regulator; lock; document pressure on machine hub
4. Confirm lubricator policy with OEM manual
5. Cycle every pneumatic function; no end-stroke bang
6. 15-minute hold test after shutoff — note pressure drop

## Related notes

- [[Pneumatic Cylinders in Laser Systems]]
- [[Nozzle Change and Shutter Actuators]]
- [[Air Compressors for Laser Cutting]]
- [[Gas Pipework and Fittings]]
- [[Compressed Air Cutting]]

## Sources

- ISO 8573 compressed air quality classes (context)
- Standard machine pneumatic schematic practice
- Field FRL service experience on import fiber laser packages
