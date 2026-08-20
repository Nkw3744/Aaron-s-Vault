---
aliases:
  - gas piping laser
  - assist gas fittings
type: technical-reference
category: assist-gas
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: BLMA installation guide, GWK install checklist, field practice
status: generic reference — verify against nameplate and project drawing
---

# Gas Pipework and Fittings

Return to [[Assist Gas Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Pipe materials, routing, leak testing, labeling, and purging for O₂, N₂, and cutting-air lines — the physical plant between bulk supply and the machine inlet.

> [!warning] HP nitrogen
> Bank pressures can be hundreds of bar before the process regulator. Use rated components and whip restraints — [[Nitrogen Booster and HP Storage]].

## Materials by service

| Service | Recommended | Avoid |
| --- | --- | --- |
| High-pressure N₂ | Stainless tube, copper (annealed) | PVC, garden hose, unrated rubber |
| O₂ | O₂-clean brass/copper; hydrocarbon-free | Any oily fitting from shop air tools |
| Air (cutting) | Stainless / aluminium compressed-air pipe after treatment | Untreated rusty black iron straight to head |
| Low-pressure shop/control air | Galvanized or Al ring-main + FRL | Tee into cutting-air fine filters |

## Routing rules

1. **Separate runs** for O₂, N₂, and cutting air — colour-code and label both ends
2. Slope air lines to drain points; no undrained low points (water traps kill windows)
3. Minimise HP N₂ flexible hose; support hard pipe every 1–2 m
4. Keep gas lines away from welding cables and VFD outputs where practical
5. Fire-stop wall penetrations per local code
6. Whip restraints / cables on HP flexible leads
7. Protect outdoor runs from UV and impact

## Machine connection

Document on the machine hub note:

| Record | Why |
| --- | --- |
| Fitting type and size (BSP/NPT) | Prevents forced wrong adapters |
| Max inlet pressure rating | Protects machine gas panel |
| Filter element part numbers | Spares |
| Which bulkhead is O₂ / N₂ / air | Prevents swap after service |

Match threads exactly — do not force NPT into BSP.

## Leak test procedure

1. Isolate sections; pressurize to **1.1×** max working pressure (qualified practice)
2. Soap solution or ultrasonic detector on every joint
3. Hold ~15 minutes; note pressure drop
4. Repeat after any O₂ component change
5. Record pass/fail, date, and technician on commissioning sheet

## Purging after maintenance

When opening an HP N₂ or O₂ line:

1. Isolate supply; vent downstream safely
2. Reconnect; purge with the **correct** gas at low flow before restoring pressure
3. First cuts on scrap — verify CypCut/FSCUT gas type matches physical hookup
4. Recheck dynamic pressure — [[Gas Regulators and PRVs]]

## Common field mistakes

| Mistake | Consequence |
| --- | --- |
| Shared regulator between gases | Contamination; wrong edge chemistry |
| Unrated quick-connect on HP | Blow-off injury |
| Air tee before fine filter | Oil to head — [[Air Filtration Stages]] |
| Unlabeled lines after move | Wrong gas selected in layer |
| Long soft hose as main N₂ run | Pressure drop; hose failure risk |
| Ignoring low-point drains on air | Water slug to dryer/filters |

## Interaction with other systems

| System | Link |
| --- | --- |
| PSA / booster | HP bank piping standards |
| Air cutting plant | Dryer → filter → machine drop only |
| Control pneumatics | Separate FRL — [[FRL Units and Shop Air Plumbing]] |
| Commissioning | [[Fiber Laser Commissioning Sequence]] |

## Related notes

- [[Gas Regulators and PRVs]]
- [[Oxygen Assist Gas]]
- [[Nitrogen Assist Gas]]
- [[Compressed Air Cutting]]
- [[Assist Gas Overview]]

## Sources

- BLMA fiber laser gas connection guidelines
- GWK installation checklist (gas connection phase)
- Field HP N₂ piping practice
