---
aliases:
  - FRL unit laser
  - shop air plumbing laser
type: technical-reference
category: pneumatics
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: ISO 8573 practice, machine electrical cabinet pneumatics
status: generic reference — verify against nameplate and project drawing
---

# FRL Units and Shop Air Plumbing

Return to [[Pneumatic Cylinders in Laser Systems]] · [[Technical Reference Index]]

> [!info] When to open this note
> Filter-Regulator-Lubricator units for **machine control air** — separate from laser cutting air.

## Two air systems on many lasers

| System | Pressure | Quality | Serves |
| --- | --- | --- | --- |
| Cutting assist air | Up to 16–30 bar | Dry, oil-free — [[Air Filtration Stages]] | Head cut/pierce |
| Shop/control air | 5–7 bar | FRL filtered; may be lubricated | Cylinders, valves, some gas pilots |

**Never confuse the two.**

## FRL components

| Unit | Function |
| --- | --- |
| Filter | Remove water and particulate |
| Regulator | Set stable 5–6 bar to cabinet |
| Lubricator | Optional mist for cylinder seals — omit if OEM specifies dry |

Mount upstream of machine cabinet with drip leg and auto drain.

## Plumbing layout

```
Ring main → branch shutoff → FRL → machine cabinet → solenoid manifold → cylinders
```

- Hard copper/aluminum near machine; flex only at vibration points
- Shutoff valve for service
- Pressure gauge after regulator

## Maintenance

| Item | Interval |
| --- | --- |
| Drain filter bowl | Daily in humid shops |
| Element replacement | Per ΔP or 6–12 months |
| Regulator drift check | Annual |

## Troubleshooting

| Symptom | Check |
| --- | --- |
| All valves weak | Regulator set; main shutoff |
| One cylinder slow | Local restriction; valve exhaust blocked |
| Water in cabinet | Failed FRL filter; no drip leg |

## Related notes

- [[Air Compressors for Laser Cutting]] — high-pressure system separate
- [[Gas Pipework and Fittings]]

## Sources

- ISO 8573 compressed air quality
- Standard machine pneumatic schematic practice
