---
aliases:
  - QBH connector
  - fiber delivery cable laser
type: technical-reference
category: fiber-optics
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Coherent QBH datasheet, Optizone fiber cable reference
status: generic reference — verify against nameplate and project drawing
---

# QBH Fiber Delivery Cable

Return to [[Technical Reference Index]]

> [!info] When to open this note
> QBH (Quartz Block Head) — the standard high-power fiber interface on industrial fiber lasers: what it is, ratings, mating, and failure modes.

## What QBH is

**Q**uartz **B**lock **H**ead — typically water-cooled (air-cooled variants for lower power) integrating:

- Mode stripper (cladding power removal)
- AR-coated end cap
- Safety interlock circuit
- Armored cable for machine motion

Powers roughly from ~1 kW to 12 kW+ in QBH class; higher powers may use QD/Q+ interfaces.

## Typical specifications (Coherent-class reference)

| Parameter | Typical range |
| --- | --- |
| Wavelength | 915–1080 nm |
| CW power | Up to 10–12 kW (model dependent) |
| Cable length | Catalog ≤200 m; machines often 5–20 m |
| Cooling (water) | ~2 L/min; max ~8 bar inlet |
| Interlock | ~3.3 kΩ ±5% + line resistance |
| Thermoswitch | ~70 °C trip on some cables |
| Humidity | <80% RH operating |
| Operating temp | 5–50 °C non-condensing |

## Mating procedure (field summary)

1. Verify pins clean and dry
2. Remove caps only when ready
3. Align keyway; insert straight — no twist force
4. Hand-start threads; torque to OEM N·m
5. Connect water before emission enable
6. Verify interlock continuity
7. Dress cable with correct bend radius — [[Fiber Cable Bend Radius and Routing]]

Cleaning: [[Fiber Connector Cleaning and Inspection]]. Cooling/interlocks: [[Fiber Cable Cooling and Interlocks]].

## Failure modes

| Sign | Likely issue |
| --- | --- |
| Burn smell at QBH | Contamination, misalignment, cladding power |
| Interlock fault | Loose mate, wet pins, broken cable |
| Power drop | Micro-bend, damaged fiber, dirty end cap |
| Leak at ferrule | O-ring; overtighten |
| Hot connector | No flow; thermoswitch pending trip |

> [!danger] No field splicing
> Delivery fiber repair is OEM/lab work. Replace the cable assembly.

## Local context

Optic cable routing documented on [[Gweike 3015GAII]] work history.

## Commissioning checklist

1. Cable length and part number recorded
2. Route photos; bend radius OK
3. Mate torque logged
4. Water flow verified
5. Interlock resistance in spec
6. Low-power confidence checks per OEM

## Related notes

- [[Fiber Laser Commissioning Sequence]]
- [[Dual-Temperature Chiller Circuits]]
- [[Fiber Laser Cutters]]

## Sources

- Coherent QBH fiber optic cable datasheet
- Optizone QBH product reference
- Field QBH failure patterns
