---
aliases:
  - laser grounding
  - EMC laser installation
type: technical-reference
category: electrical
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: Arcus environmental guide, capacitive sensing field guides
status: generic reference — verify against nameplate and project drawing
---

# Grounding and EMC Isolation

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Protective earth, ground resistance targets, and EMI issues affecting height sensing and CNC stability.

## Protective grounding (PE)

Arcus/GWK-style targets (verify OEM):

| Item | Typical |
| --- | --- |
| Ground electrode | Independent copper rod ≥2.4 m |
| Ground resistance | <4 Ω at installation |
| Ground conductor | ≥16 mm² copper to machine PE bar |
| Bonding | Slats, bed, dust collector duct (where specified) |

Poor PE → **capacitive height instability** — [[Capacitive Height Sensing BCS100]].

## Machine ground bar

- All services enter common reference: gas panels, extraction, cable trays
- No ground loops through building steel alone without engineered bond
- Check after machine relocation — re-measure resistance

## EMC / electrical noise

Sources of interference:

| Source | Mitigation |
| --- | --- |
| Arc welding nearby | Separate circuit; physical distance ≥10 m class recommendation |
| VFD compressors | Filter; separate feeder |
| Welding on slats while sensing | Unstable capacitance during weld — sequence work |
| RF cable parallel to power | Separate tray; cross at 90° |

Symptoms: random height jumps, BCS100 network drops, encoder faults.

## Height sensing ground path

Capacitive system measures nozzle vs **grounded workpiece**:

```
Nozzle → sheet → slats → bed → PE
```

Rust paint on slats, plastic pads, or isolated sheet → floating reference → alarms.

Fix: clean contact points; grounding straps; bare metal cal plate.

## Lightning and surge

Outdoor duct and long cable runs: consider surge protection on sensitive networks per local practice.

## Related notes

- [[Height Sensor Alarm Reference]]
- [[Laser Electrical Supply Requirements]]
- [[Fiber Cable Bend Radius and Routing]] — route away from VFD cables

## Sources

- Arcus CNC environmental setup (grounding table)
- Arcus capacitive sensor troubleshooting (grounding section)
