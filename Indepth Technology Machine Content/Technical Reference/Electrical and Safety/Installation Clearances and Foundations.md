---
aliases:
  - laser installation clearances
  - laser foundation requirements
type: technical-reference
category: electrical
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, Arcus environmental guide
status: generic reference — verify against nameplate and project drawing
---

# Installation Clearances and Foundations

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Floor loading, service clearances, anchor points, and layout for laser + auxiliaries.

## Service clearances (typical OEM)

| Zone | Minimum clearance |
| --- | --- |
| Operator front / sides | ≥1.2 m |
| Laser source / rear service | ≥1.5 m |
| Chiller ventilation | OEM panel clearance — often 0.5–1 m each side |
| Fiber service loop | No bend violation — [[Fiber Cable Bend Radius and Routing]] |

Confirm on installation drawing for exact machine (4020 vs 3015 differ).

## Floor loading

| Requirement | Typical |
| --- | --- |
| Uniform load | ≥500 kg/m² |
| Point loads | Spread with sole plates if on epoxy over weak slab |
| Level | 0.05 mm/m class after shim — verify OEM |

Structural engineer sign-off for mezzanine installs.

## Foundation and anchoring

1. Receive anchor bolt pattern drawing before pour (or drill template for existing slab)
2. Grout after level — not dry shims only on production machines
3. Isolate from active vibration sources (stamping press) or use isolation trench

## Auxiliary placement layout

Suggested zoning:

```
[Laser cell] — clean, controlled T/RH
[Chiller] — often adjacent room or ventilated alcove
[Compressor/dryer] — separate noisy room
[N2 PSA] — ventilated; away from cutting spark
[Dust collector] — outside or plant room; short duct path
```

Chiller-to-laser hose ≤10 m common limit — [[Laser Water Chillers]].

## Overhead considerations

- Crane access for source lift on large machines
- Overhead tray for fiber — no climbing on cable armor
- Lighting at operator panel without glare on safety glass

## Relocation checklist

| Step | Action |
| --- | --- |
| 1 | Document level and anchor locations |
| 2 | Drain chiller; cap water lines |
| 3 | Cap QBH and gas lines |
| 4 | Re-level; re-torque anchors |
| 5 | Re-commission full sequence — [[Fiber Laser Commissioning Sequence]] |

## Related notes

- [[Fiber Laser Site Requirements]]
- [[Ambient Temperature Limits]]
- [[Gweike 4020GA]] — layout PDFs in machine folder

## Sources

- Arcus CNC environmental setup (clearances and floor loading)
- GWK installation checklist (site and foundation phases)
