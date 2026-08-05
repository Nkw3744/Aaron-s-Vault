---
aliases:
  - laser kW comparison
  - fiber laser power sizing
type: technical-reference
category: fiber-lasers
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, Arcus environmental guide, industry sizing tables
status: generic reference — verify against nameplate and project drawing
---

# Fiber Laser Power Classes

Return to [[Fiber Laser Cutters]] · [[Technical Reference Index]]

> [!info] When to open this note
> Comparing electrical supply, gas flow, chiller capacity, extraction, and compressor sizing across 1–3 kW, 4–6 kW, and 8–12 kW+ machines.

> [!warning] Nameplate wins
> Rated laser power ≠ wall draw. Always size auxiliaries from manufacturer bills of quantity and measured load.

## Class overview

| Class | Typical rated power | Primary use |
| --- | --- | --- |
| Entry / job shop | 1–3 kW | Thin mild steel, stainless to ~6 mm, air or N₂ |
| Mid production | 4–6 kW | 6–16 mm carbon steel, stainless, aluminum |
| Heavy / high speed | 8–12 kW+ | Thick plate, high feed rates, large tables |

## Electrical supply (typical total cell)

Includes laser, servos, chiller, extraction fan, controls — not compressor unless on same feeder.

| Laser class | Laser source wall draw (approx.) | Total cell hint (approx.) | Supply notes |
| --- | --- | --- | --- |
| 1–3 kW | 9–15 kW | 20–30 kW | 380 V 3-phase common; dedicated circuit |
| 4–6 kW | 15–25 kW | 30–45 kW | Phase imbalance <2.5%; regulator recommended |
| 8–12 kW | 25–45 kW | 45–70 kW+ | Often separate transformer; verify with OEM |

See [[Laser Electrical Supply Requirements]].

## Assist gas flow (nitrogen cutting, indicative)

GWK-style reference values for planning — measure on site under cut load.

| Laser power | N₂ flow reference (m³/min) | Output pressure reference |
| --- | --- | --- |
| ≤3 kW | ~1.5 | up to ~2.0 MPa |
| >3 kW to 6 kW | ~2.2 | up to ~2.0 MPa |
| 8 kW+ | 3+ | OEM spec; booster often required |

Purity: N₂ ≥99.99% for stainless and bright edges — [[Nitrogen Assist Gas]].

## Chiller sizing hint

| Laser class | Typical chiller | Loops |
| --- | --- | --- |
| 1–3 kW | 1.5–2 kW refrigeration (CW-5200/6000 class) | Single or dual |
| 4–6 kW | 3–5 kW refrigeration (CW-6100/6200) | Dual-temp preferred |
| 8–12 kW+ | OEM matched unit, often 8 kW+ cooling | Dual mandatory |

Dual-loop concept: [[Dual-Temperature Chiller Circuits]].

## Air cutting (compressed air assist)

Requires oil-free dry air to ~1.6–3.0 MPa depending on head and material. Higher power = higher sustained flow.

| Laser class | Compressor hint |
| --- | --- |
| 1–3 kW | 11–15 kW screw + dryer + filtration |
| 4–6 kW | 15–22 kW screw, 16 bar class common |
| 8 kW+ | Sized from OEM CFM at cut pressure; often 22 kW+ |

See [[Compressor Sizing by Laser Power]] and [[Compressed Air Cutting]].

## Fume extraction hint

| Laser class | Air volume hint (m³/h) | Notes |
| --- | --- | --- |
| 1–3 kW on 3015 table | 6000–8000 | Increase for stainless/aluminum fine dust |
| 4–6 kW on 4020 | 8000–12000 | High speed ↑ loading |
| 8 kW+ large bed | 12000–20000+ | Central plant common |

Formula: [[Dust Collector Sizing]].

## Cutting head and optics

Higher power generally means:

- Larger core delivery fiber (50 µm → 100 µm common step at 6 kW+)
- Water-cooled QBH mandatory above ~2 kW continuous
- Head rated for power and duty; protective window spec changes

See [[QBH Fiber Delivery Cable]].

## When upgrading power on same machine

Changing source kW without replacing head, fiber, chiller, gas, and extraction is unsafe. Treat as full subsystem review:

1. Head and fiber power rating
2. Chiller kW and flow
3. N₂ booster / HP storage if using PSA
4. Extraction and duct
5. Electrical feeder and breaker
6. Re-commission all recipes — [[Cutting Parameters Index]]

## Related notes

- [[Fiber Laser Cutters]]
- [[Fiber Laser Site Requirements]]
- [[Compressor Sizing by Laser Power]]
- [[Dust Collector Sizing]]
- [[Dual-Temperature Chiller Circuits]]

## Sources

- GWK fiber laser installation requirements checklist (gas flow table)
- Arcus CNC environmental setup guide (power budgeting)
