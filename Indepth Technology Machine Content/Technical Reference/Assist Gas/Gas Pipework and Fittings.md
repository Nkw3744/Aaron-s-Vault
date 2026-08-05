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
> Pipe materials, routing, leak testing, and labeling for O₂, N₂, and air lines.

## Pipe and hose materials

| Service | Recommended | Avoid |
| --- | --- | --- |
| High-pressure N₂ | Stainless tube, copper (annealed) | PVC, generic rubber on HP |
| O₂ | O₂-clean brass/copper; no oil | Any oil-contaminated fitting |
| Air (cutting) | Stainless, aluminum compressed-air pipe | Black iron without treatment (rust) |
| Low-pressure shop air | Galvanized or aluminum ring-main OK with filters downstream | — |

## Routing rules

1. **Separate runs** for O₂, N₂, and air — color code and label at both ends
2. Slope lines to drain points where moisture possible (air lines)
3. Avoid low points without drains — water traps kill cut quality
4. Minimize flexible hose length on HP N₂; support every 1–2 m
5. Keep gas lines away from welding cables and VFDs where possible
6. Penetration seals through walls — fire stop per code

## Connection to machine

Typical machine inlet: bulkhead fitting with manual shutoff and filter/regulator panel. Match thread (BSP/NPT) exactly — do not force.

Document on machine hub:

- Fitting type and size
- Maximum inlet pressure rating
- Filter element part numbers

## Leak test procedure

1. Pressurize section to 1.1× max working pressure
2. Soap solution or ultrasonic leak detector on every joint
3. Hold 15 min; note pressure drop
4. For O₂: repeat after any component change
5. Record test on commissioning sheet

## Purging after maintenance

When opening HP N₂ line:

1. Isolate supply
2. Vent downstream safely
3. Reconnect; purge with N₂ at low flow before restoring pressure
4. First cuts on scrap — verify gas type in controller

## Common field mistakes

| Mistake | Consequence |
| --- | --- |
| Shared regulator between gases | Contamination, wrong edge |
| Quick-connect on HP without rated coupler | Blow-off, injury |
| Air line tee before fine filter | Oil to head |
| Unlabeled lines after move | Wrong gas in layer |

## Related notes

- [[Gas Regulators and PRVs]]
- [[Air Filtration Stages]]
- [[Fiber Laser Commissioning Sequence]]

## Sources

- BLMA fiber laser gas connection guidelines
- GWK installation checklist (gas connection phase)
