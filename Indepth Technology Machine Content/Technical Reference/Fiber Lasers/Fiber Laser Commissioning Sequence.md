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
> Ordered bring-up from mechanical install through first validated coupon. Complements [[Indepth Technology Machine Content/Installation Checklists/LaserCutter_Installation_Checklist.xlsx|installation checklist]]. Also useful after a machine relocation, major repair, or long shutdown, when a full re-commission is safer than assuming everything is still correct.

> [!danger] No production until proven
> Do not run full sheets on internet parameters. Follow [[Cutting Parameters Index]] status rules — every recipe must move from Reference → Commissioning → Validated before it is used on production work.

## Why sequence matters

Powering everything on at once and immediately trying to cut hides the source of a fault inside a pile of simultaneous unknowns. Commissioning in phases — utilities before electronics, electronics before motion, motion before the beam, beam before gas, gas before cutting — means that when something goes wrong you already know it must be in the phase you just started, not somewhere in the whole machine.

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

At the end of Phase 1, nothing electrical has been energized yet. This is the point to double-check every physical connection against the OEM drawing, because it is far easier to fix a wrongly routed hose or cable now than after cladding and covers go back on.

## Phase 2 — Electrical (control power first)

| Step | Action | Reference |
| --- | --- | --- |
| 9 | Verify supply voltage and phase rotation | [[Laser Electrical Supply Requirements]] |
| 10 | Megger/isolation checks per OEM if required | |
| 11 | Connect PE ground; measure resistance | [[Grounding and EMC Isolation]] |
| 12 | Power CNC and chiller only; no laser enable yet | |

Do not enable the laser source or motion drives at this stage. The goal is only to confirm the control system boots, the HMI is responsive, and there are no obvious wiring faults (blown fuses, tripped breakers, error screens on power-up) before anything moves or lases.

## Phase 3 — Chiller and water loop

| Step | Action | Reference |
| --- | --- | --- |
| 13 | Run chiller; bleed air; check level | [[Chiller Troubleshooting Flowchart]] |
| 14 | Set Lo/Hi loop temps per season — [[Dew Point and Chiller Setpoints]] | |
| 15 | Run 30+ min; confirm stable temps, no leaks | |
| 16 | If flow alarm: short-loop test (out→in hose) | [[CW Series Chiller Alarm Codes]] |

Watch specifically for slow leaks that only appear once the loop has been running under pressure and thermal cycling for a while — a fitting that looked fine on initial connection can weep after the first heat-up/cool-down cycle. Recheck fitting tightness after this 30-minute run, before covers go on.

## Phase 4 — Control and motion

| Step | Action | Reference |
| --- | --- | --- |
| 17 | Power laser control; homing all axes | |
| 18 | Test limits and interlocks | |
| 19 | Verify encoder direction, soft limits | |
| 20 | Jog Z manually; confirm no crash | |

Confirm the emergency stop chain and all door interlocks function correctly before proceeding — this is the last easy point to verify safety systems with the head still at low risk of collision, before beam and gas are introduced.

## Phase 5 — Height system

| Step | Action | Reference |
| --- | --- | --- |
| 21 | Inspect nozzle, ceramic, SMA cable | [[Cutting Head Nozzles and Ceramics]] |
| 22 | Calibrate capacitive sensor on clean flat plate | [[Capacitive Height Sensing BCS100]] |
| 23 | Test follow at low speed over plate | |
| 24 | Record DIF/stability rating | |

A poor stability rating at this stage (rather than "Good" or "Excellent") should be resolved before moving on — do not proceed to beam alignment or first cuts hoping the sensor will "settle in." It will not; a poor calibration reading almost always traces to a physical fault (ceramic seating, grounding, RF cable) that gets harder to diagnose once the machine is buried under production noise.

## Phase 6 — Beam path (OEM procedure)

| Step | Action | Reference |
| --- | --- | --- |
| 25 | Red pointer / coaxial alignment per head manual | |
| 26 | Low-power shot on tape or ceramic tile | |
| 27 | Inspect spot centering in nozzle | |
| 28 | Replace protective window if contaminated | [[Fiber Connector Cleaning and Inspection]] |

Follow the head manufacturer's exact alignment procedure — Precitec, Raytools, WSX, and other head brands each have their own coaxiality check method and tolerances. A miscentered beam produces asymmetric kerfs and accelerates nozzle wear even when every other subsystem is correct.

## Phase 7 — Gas and extraction

| Step | Action | Reference |
| --- | --- | --- |
| 29 | Set regulator; measure dynamic pressure at cut | [[Gas Regulators and PRVs]] |
| 30 | Purge lines; verify gas type in controller | [[Assist Gas Overview]] |
| 31 | Start extraction; check damper positions | [[Laser Fume Extraction Overview]] |

Confirm the controller's selected gas type for each layer actually matches what is physically connected — a common commissioning mistake is leaving a demo/factory-test layer set to the wrong gas type, which then quietly produces poor edge quality that gets blamed on "bad parameters" rather than a wrong gas selection.

## Phase 8 — First cuts (coupons only)

| Step | Action | Reference |
| --- | --- | --- |
| 32 | Export/backup factory material library | [[Cutting Parameters Index]] |
| 33 | Select material/thickness; start from factory or controlled card | |
| 34 | Label coupons; one variable at a time | |
| 35 | Inspect edge, dross, kerf, window | |
| 36 | Record validated settings or mark commissioning | |

Run the speed ladder before the focus ladder, and the focus ladder before touching gas pressure — changing more than one variable between coupons makes it impossible to attribute a result to its actual cause. See the local example in [[Gweike 3015GAII 3 kW CypCut Cutting Parameter Setting]] for a worked commissioning card.

## Sign-off record (minimum)

Record on machine hub or recipe note:

- Date, technician
- Source S/N, head model, fiber length
- Chiller setpoints (Lo/Hi)
- Gas type, purity evidence, measured cut pressure
- Nozzle type/diameter
- CypCut/FSCUT version
- Coupon photos or inspection result
- Ground resistance measurement
- Any deviations from OEM defaults and why

## Re-commissioning after relocation or major repair

The same eight phases apply, but with extra emphasis on:

1. **Re-verify level and anchoring** — even a small shift in level changes height-sensor and motion behavior
2. **Re-check ground resistance** — moving a machine often disconnects it from its original electrode
3. **Re-calibrate height sensing from scratch** — do not assume old calibration data is still valid
4. **Re-run the coupon ladder** even if "the same recipe worked before the move" — optics, alignment, and gas delivery can all shift slightly during transport

## Related notes

- [[Fiber Laser Site Requirements]]
- [[Fiber Laser Common Alarms]]
- [[Gweike 3015GAII]] — example local machine

## Sources

- GWK installation checklist commissioning phases
- BLMA fiber laser installation guide (chiller, gas, electrical sequence)
