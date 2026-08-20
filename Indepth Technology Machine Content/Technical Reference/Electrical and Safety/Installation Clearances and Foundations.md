---
aliases:
  - laser installation clearances
  - laser foundation requirements
  - laser floor loading
type: technical-reference
category: electrical
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, Arcus environmental guide, field layout practice
status: generic reference — verify against nameplate and project drawing
---

# Installation Clearances and Foundations

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Floor loading, service clearances, anchoring, auxiliary equipment zoning, and relocation checks. Use at site survey and before the machine arrives.

> [!warning] Drawing wins
> 3015, 4020, and 2060 packages differ. Use the machine layout PDF (e.g. [[Gweike 4020GA]] layout folder) over generic numbers below.

## Service clearances (typical OEM)

| Zone | Minimum (typical) | Purpose |
| --- | --- | --- |
| Operator front / sides | ≥1.2 m | Sheet handling, safe stance |
| Laser source / rear service | ≥1.5 m | Fiber, source swap, electrics |
| Chiller condenser sides | 0.5–1.0 m each | Airflow — blocked = E1/E2 |
| Extraction / duct service | Enough to pull cartridges | Filter change without dismantling cell |
| Fiber service loop | No bend violation | [[Fiber Cable Bend Radius and Routing]] |

Also reserve aisle for forklift / pallet change if shuttle table fitted.

## Floor loading

| Requirement | Typical | Notes |
| --- | --- | --- |
| Uniform load | ≥500 kg/m² | Or structural engineer sign-off |
| Point loads | Sole plates on weak epoxy | Avoid cracking thin toppings |
| Level after shim | Often 0.05 mm/m class | Verify OEM |

Mezzanines and suspended slabs: engineer required — laser + sheet stack + people is not a light office load.

## Foundation and anchoring

1. Obtain anchor bolt pattern **before** pour (or use drill template on existing slab)
2. Rough position machine; jack/shim to level in both axes
3. Grout / epoxy anchors per OEM — production machines rarely sit on dry shims alone long-term
4. Re-check level after grout cure and after first week of production (settling)
5. Isolate from stamping presses / shears — vibration ditch or distance

Vibration symptoms: unstable height follow, poor edge quality, encoder noise — also check [[Grounding and EMC Isolation]].

## Auxiliary placement zoning

Suggested layout for heat, noise, humidity, and hose length:

```
[Laser cell]          — cleanest T/RH control; operator access
[Chiller]             — ventilated alcove or separate room (adds heat/humidity)
[Compressor + dryer]  — noisy; heat; drains
[N₂ PSA / booster]    — ventilated; away from sparks
[Dust collector]      — plant room or outdoors; short duct to table
```

| Constraint | Typical limit |
| --- | --- |
| Chiller hose run | ≤10 m common OEM ask — [[Laser Water Chillers]] |
| Extraction duct | Short + few bends — [[Ductwork and Static Pressure]] |
| Dehumidifier | Near laser intake — [[Dehumidifiers for Laser Rooms]] |

Do not park the chiller condenser against a wall with zero clearance "to save space."

## Overhead and material flow

| Item | Check |
| --- | --- |
| Crane / hoist for source | Path clear for kW upgrades or warranty swap |
| Overhead cable tray | Fiber supported; no step-on armor |
| Lighting | Readable HMI; no glare on safety glass |
| Sheet infeed / outfeed | Does not block E-stop or egress |
| Fire extinguisher access | Per local code; not trapped behind pallets |

## Environmental envelope at the pad

Clearances alone are not enough if the pad is in a hot, humid corner:

- [[Ambient Temperature Limits]]
- [[Workshop Humidity and Condensation]]
- [[Fiber Laser Site Requirements]]

## Relocation checklist

| Step | Action |
| --- | --- |
| 1 | Photo level readings, anchor positions, hose/cable routes |
| 2 | Drain chiller; cap water; note glycol mix if any — [[Antifreeze and Winter Operation]] |
| 3 | Cap QBH; protect fiber; label gas lines — [[QBH Fiber Delivery Cable]] |
| 4 | Move; re-level; re-torque anchors |
| 5 | Re-bond PE; re-measure earth — [[Grounding and EMC Isolation]] |
| 6 | Full bring-up — [[Fiber Laser Commissioning Sequence]] |
| 7 | Recalibrate height; coupon-check recipes — [[Cutting Parameters Index]] |

## Survey form (copy to job notes)

| Item | Value / pass |
| --- | --- |
| Floor capacity confirmed | ☐ |
| Clearances front/rear/sides | ☐ |
| Anchor pattern received | ☐ |
| Chiller location / hose length | ☐ |
| Extractor location / duct route | ☐ |
| Electrical capacity / dedicated circuit | ☐ |
| Vibration sources nearby | ☐ |
| Crane access | ☐ |

## Related notes

- [[Fiber Laser Site Requirements]]
- [[Ambient Temperature Limits]]
- [[Laser Electrical Supply Requirements]]
- [[Gweike 4020GA]] — layout PDFs
- [[JQ-2060E]] — layout PDFs

## Sources

- Arcus CNC environmental setup (clearances and floor loading)
- GWK installation checklist (site and foundation phases)
- Field layout practice on 3015/4020-class installs
