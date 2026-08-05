---
aliases:
  - laser electrical supply
  - 380V laser power
type: technical-reference
category: electrical
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, Arcus environmental guide
status: generic reference — verify against nameplate and project drawing
---

# Laser Electrical Supply Requirements

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Three-phase supply, capacity, dedicated circuits, and stabilizers for laser cells.

> [!warning] Licensed electrician
> Mains work must comply with local wiring rules (NZ: AS/NZS 3000). This note is equipment spec only.

## Typical supply (import fiber lasers)

| Parameter | Common spec |
| --- | --- |
| Voltage | 380 V 3-phase ±5% (or OEM: 400 V, 415 V) |
| Frequency | 50 Hz (60 Hz models exist) |
| Wiring | 3-phase + neutral + PE (five-wire) |
| Phase imbalance | <2.5% |
| Voltage fluctuation | <5% under load |

Confirm exact value on machine nameplate and door diagram.

## Capacity planning

Total cell kW ≈ laser + servos + chiller + extraction + controls.

| Laser class | Indicative total | See |
| --- | --- | --- |
| 1–3 kW | 20–30 kW | [[Fiber Laser Power Classes]] |
| 4–6 kW | 30–45 kW | |
| 8 kW+ | 45–70 kW+ | |

Add compressor separately if on same feeder — often **avoid**.

## Dedicated circuit rules

- **Do not** share breaker with welders, large compressors, or VFD lifts on same weak feeder
- Laser CNC and source sensitive to sags and spikes
- Stabilizer/regulator on laser electronics per OEM — Arcus/GWK recommend regulated supply for machine/laser stability

## Single-phase loads

220 V ±5% for some auxiliaries (controls, lights) — separate from 3-phase balance issue.

## Step-up / step-down transformers

If site voltage wrong (e.g. 240 V only): transformer sized for **inrush + continuous** laser+kW label. Include in order upfront — lead time item.

## Pre-energization checks

| Check | Method |
| --- | --- |
| Phase rotation | Correct motor direction — record |
| Voltage each phase | Log under no load |
| Ground bond | See [[Grounding and EMC Isolation]] |
| Emergency stop chain | Continuity |

## Related notes

- [[Fiber Laser Site Requirements]]
- [[Compressor Sizing by Laser Power]] — electrical coordination
- [[Installation Clearances and Foundations]]

## Sources

- GWK fiber laser installation requirements (electrical table)
- Arcus CNC environmental setup (power quality section)
