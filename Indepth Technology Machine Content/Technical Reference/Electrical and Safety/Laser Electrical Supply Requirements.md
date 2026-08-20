---
aliases:
  - laser electrical supply
  - 380V laser power
  - laser power quality
type: technical-reference
category: electrical
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, Arcus environmental guide, field commissioning practice
status: generic reference — verify against nameplate and project drawing
---

# Laser Electrical Supply Requirements

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Three-phase supply specs, total cell kW planning, dedicated circuits, voltage quality, transformers, and pre-energization checks before first power-on.

> [!warning] Licensed electrician
> Mains work must comply with local wiring rules (NZ: AS/NZS 3000). This note is equipment specification support for installers coordinating with the electrician — not a wiring certificate.

## Typical supply (import fiber lasers)

| Parameter | Common OEM ask | Notes |
| --- | --- | --- |
| Voltage | 380 V 3-phase ±5% (also 400 V / 415 V sites) | Nameplate wins |
| Frequency | 50 Hz (60 Hz models exist) | Wrong frequency = wrong fans/pumps |
| Wiring | 3-phase + N + PE (five-wire) | Confirm N is actually landed |
| Phase imbalance | <2.5% | Measure under load |
| Voltage fluctuation | <5% under load | Sag during pierce/cut |

Always photograph the door nameplate and single-line diagram into the machine hub.

## What "total cell kW" includes

| Load | Typical share |
| --- | --- |
| Laser source wall draw | Significant — not equal to optical kW |
| Axis servos / drives | Surge on accel |
| Chiller | Continuous when running |
| Extraction fan | Large inductive start |
| Controls, lighting, options | Smaller continuous |
| **Compressor** | Often **separate** feeder — avoid sharing weak laser circuit |

Indicative totals — detail in [[Fiber Laser Power Classes]]:

| Laser optical class | Indicative cell total |
| --- | --- |
| 1–3 kW | ~20–30 kW |
| 4–6 kW | ~30–45 kW |
| 8 kW+ | ~45–70 kW+ |

## Dedicated circuit rules

| Do | Don't |
| --- | --- |
| Dedicated breaker for laser cell | Share with welder, large compressor, crane VFD |
| Correctly rated cable for continuous + inrush | Undersize "because optical kW is only 3" |
| Stabilizer / regulator on laser electronics if OEM requires | Put compressor **through** the same small stabilizer |
| Label isolation point for LOTO | Ambiguous multi-machine DB boards |

Arcus/GWK guidance: regulated supply for machine/laser stability; keep heavy inductive loads off that regulated branch.

## Single-phase auxiliaries

Some cabinets need 220–240 V ±5% for controls, HMI, or accessories. Confirm:

- Derived from which phase (balance loading)
- UPS only where OEM specifies (not a substitute for bad mains)

## Transformers (step-up / step-down)

If site voltage ≠ machine nameplate:

| Requirement | Practice |
| --- | --- |
| kVA rating | Continuous cell load + inrush margin |
| Vector / earthing | Match OEM and local MEN rules |
| Order timing | Lead-time item — decide before machine lands |
| Location | Ventilated; not blocking laser clearances |

## Power quality symptoms vs laser faults

| Symptom | Often electrical | Often machine |
| --- | --- | --- |
| Random CNC reboot | Sag / spike | PSU fault |
| Source over-temp with cool water | Undervoltage → inefficiency | Real chiller fault |
| Servo following error on accel | Soft supply | Tuning / mechanics |
| Chiller E1 with cool room | Supply instability to fans | Real ambient heat |

Measure with a logger during a real cut cycle before replacing expensive modules.

## Pre-energization checklist

1. Confirm nameplate V/Hz vs site supply
2. Megger / insulation tests if OEM requires (dry loops)
3. PE continuity and earth resistance — [[Grounding and EMC Isolation]]
4. Phase rotation — correct motor direction on pumps/fans
5. Torque check main lugs; no paint under PE lugs
6. E-stop chain continuity; doors open = inhibit
7. Voltage L1-L2, L2-L3, L3-L1, each to N and PE — log
8. Energize control power first; then chiller; laser enable last — [[Fiber Laser Commissioning Sequence]]

## Under-load verification (after first cuts)

| Measurement | When |
| --- | --- |
| Phase voltages | Idle and cutting |
| Phase currents | Peak pierce / thick cut |
| Imbalance % | Calculate from voltages |
| Stabilizer output | If fitted |

## Coordination with compressor and extractor

| Load | Guidance |
| --- | --- |
| Screw compressor | Prefer separate circuit; soft-start/VFD — [[Compressor Sizing by Laser Power]] |
| Dust collector | Large DOL start can sag laser — staged start or VFD |
| Welder | Never same feeder as laser CNC |

## Related notes

- [[Fiber Laser Site Requirements]]
- [[Fiber Laser Power Classes]]
- [[Grounding and EMC Isolation]]
- [[Installation Clearances and Foundations]]
- [[CW Series Chiller Alarm Codes]] — some "chiller" issues are supply

## Sources

- GWK fiber laser installation requirements (electrical table)
- Arcus CNC environmental setup (power quality section)
- Field commissioning practice on 380 V fiber cells
