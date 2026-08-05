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
> QBH (Quartz Block Head) connector — the standard high-power fiber interface on industrial fiber lasers.

## What QBH is

**Q**uartz **B**lock **H**ead — water-cooled (or air-cooled low power) connector integrating:

- Mode stripper (cladding power removal)
- AR-coated end cap
- Safety interlock circuit
- Armored cable for machine motion

Powers from ~1 kW to 12 kW+ (QBH class); higher powers use QD/Q+ interfaces.

## Typical specifications (Coherent-class reference)

| Parameter | Typical range |
| --- | --- |
| Wavelength | 915–1080 nm |
| CW power | Up to 10–12 kW (model dependent) |
| Cable length | ≤200 m max catalog; machine runs often 5–20 m |
| Cooling (water QBH) | ~2 L/min; max 8 bar inlet |
| Interlock resistance | ~3.3 kΩ ±5% + line resistance |
| Thermoswitch | ~70 °C trip on some cables |
| Humidity | <80% RH operating |
| Operating temp | 5–50 °C non-condensing |

Air-cooled variants (RQB) for lower power only.

## Mating procedure (field summary)

1. Verify interlock pins clean and dry
2. Remove protective caps only when ready to mate
3. Align keyway; insert straight — no twist force
4. Hand-start threads; torque wrench to OEM N·m value
5. Connect water lines before emission enable
6. Verify interlock continuity before first power

Detail: [[Fiber Connector Cleaning and Inspection]], [[Fiber Cable Cooling and Interlocks]].

## Failure modes

| Sign | Likely issue |
| --- | --- |
| Burn smell at QBH | Contamination, misalignment, cladding power |
| Interlock fault | Loose connector, wet pins, broken cable |
| Power drop | Micro-bend, damaged fiber, dirty end cap |
| Leak at ferrule | O-ring damage; overtighten |

> [!danger] Field splicing
> Do not splice delivery fiber in the field. Return to OEM or authorized fiber lab.

## Related notes

- [[Fiber Cable Bend Radius and Routing]]
- [[Fiber Laser Commissioning Sequence]]

## Local context

Optic cable routing on [[Gweike 3015GAII]] work history.

## Sources

- Coherent QBH fiber optic cable datasheet
- Optizone QBH product reference
