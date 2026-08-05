---
aliases:
  - fiber laser commissioning
  - laser first power on
type: technical-reference
category: fiber-lasers
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: GWK install checklist, BLMA installation guide, field commissioning practice
status: generic reference — verify against nameplate and project drawing
---

# Fiber Laser Commissioning Sequence

Return to [[Fiber Laser Cutters]] · [[Technical Reference Index]]

> [!info] When to open this note
> Ordered bring-up from mechanical install through first validated coupon. Complements [[Indepth Technology Machine Content/Installation Checklists/LaserCutter_Installation_Checklist.xlsx|installation checklist]].

> [!danger] No production until proven
> Do not run full sheets on internet parameters. Follow [[Cutting Parameters Index]] status rules.

## Phase 1 — Mechanical and utilities (power off)

| Step | Action | Reference |
| --- | --- | --- |
| 1 | Verify level, anchor bolts, clearance | [[Installation Clearances and Foundations]] |
| 2 | Install chiller; fill with DI/distilled water to green zone | [[Cooling Water Quality]] |
| 3 | Connect chiller out→machine in, machine out→chiller in; no kinks | [[Laser Water Chillers]] |
| 4 | Route delivery fiber; respect bend radius; support at QBH | [[Fiber Cable Bend Radius and Routing]] |
| 5 | Mount cutting head; torque QBH per OEM | [[QBH Fiber Delivery Cable]] |
| 6 | Connect assist gas lines; leak test | [[Gas Pipework and Fittings]] |
| 7 | Connect extraction; blank off unused ports | [[Ductwork and Static Pressure]] |
| 8 | Dress all cables; separate power from signal where possible | [[Grounding and EMC Isolation]] |

## Phase 2 — Electrical (control power first)

| Step | Action | Reference |
| --- | --- | --- |
| 9 | Verify supply voltage and phase rotation | [[Laser Electrical Supply Requirements]] |
| 10 | Megger/isolation checks per OEM if required | |
| 11 | Connect PE ground; measure resistance | [[Grounding and EMC Isolation]] |
| 12 | Power CNC and chiller only; no laser enable yet | |

## Phase 3 — Chiller and water loop

| Step | Action | Reference |
| --- | --- | --- |
| 13 | Run chiller; bleed air; check level | [[Chiller Troubleshooting Flowchart]] |
| 14 | Set Lo/Hi loop temps per season — [[Dew Point and Chiller Setpoints]] | |
| 15 | Run 30+ min; confirm stable temps, no leaks | |
| 16 | If flow alarm: short-loop test (out→in hose) | [[CW Series Chiller Alarm Codes]] |

## Phase 4 — Control and motion

| Step | Action | Reference |
| --- | --- | --- |
| 17 | Power laser control; homing all axes | |
| 18 | Test limits and interlocks | |
| 19 | Verify encoder direction, soft limits | |
| 20 | Jog Z manually; confirm no crash | |

## Phase 5 — Height system

| Step | Action | Reference |
| --- | --- | --- |
| 21 | Inspect nozzle, ceramic, SMA cable | [[Cutting Head Nozzles and Ceramics]] |
| 22 | Calibrate capacitive sensor on clean flat plate | [[Capacitive Height Sensing BCS100]] |
| 23 | Test follow at low speed over plate | |
| 24 | Record DIF/stability rating | |

## Phase 6 — Beam path (OEM procedure)

| Step | Action | Reference |
| --- | --- | --- |
| 25 | Red pointer / coaxial alignment per head manual | |
| 26 | Low-power shot on tape or ceramic tile | |
| 27 | Inspect spot centering in nozzle | |
| 28 | Replace protective window if contaminated | [[Fiber Connector Cleaning and Inspection]] |

## Phase 7 — Gas and extraction

| Step | Action | Reference |
| --- | --- | --- |
| 29 | Set regulator; measure dynamic pressure at cut | [[Gas Regulators and PRVs]] |
| 30 | Purge lines; verify gas type in controller | [[Assist Gas Overview]] |
| 31 | Start extraction; check damper positions | [[Laser Fume Extraction Overview]] |

## Phase 8 — First cuts (coupons only)

| Step | Action | Reference |
| --- | --- | --- |
| 32 | Export/backup factory material library | [[Cutting Parameters Index]] |
| 33 | Select material/thickness; start from factory or controlled card | |
| 34 | Label coupons; one variable at a time | |
| 35 | Inspect edge, dross, kerf, window | |
| 36 | Record validated settings or mark commissioning | |

## Sign-off record (minimum)

Record on machine hub or recipe note:

- Date, technician
- Source S/N, head model, fiber length
- Chiller setpoints (Lo/Hi)
- Gas type, purity evidence, measured cut pressure
- Nozzle type/diameter
- CypCut/FSCUT version
- Coupon photos or inspection result

## Related notes

- [[Fiber Laser Site Requirements]]
- [[Fiber Laser Common Alarms]]
- [[Gweike 3015GAII]] — example local machine

## Sources

- GWK installation checklist commissioning phases
- BLMA fiber laser installation guide (chiller, gas, electrical sequence)
