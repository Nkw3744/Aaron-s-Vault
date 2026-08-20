---
aliases:
  - compressor kW laser power
  - air compressor sizing laser
type: technical-reference
category: air-compressors
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Arcus install guide, OEM package tables, field estimates
status: generic reference — verify against nameplate and project drawing
---

# Compressor Sizing by Laser Power

Return to [[Air Compressors for Laser Cutting]] · [[Technical Reference Index]]

> [!info] When to open this note
> Rough motor kW and flow planning for air-cutting assist (and dual PSA feed) by laser class.

> [!warning] Request OEM air consumption
> Nozzle diameter, pierce time, and duty cycle dominate real m³/min. Tables below are planning estimates only.

## Motor kW vs laser class (screw, ~16 bar class)

| Laser optical power | Indicative screw motor kW | Notes |
| --- | --- | --- |
| 1–3 kW | 11–15 kW | Single machine, thin sheet air cut |
| 4–6 kW | 15–22 kW | Higher pierce duty |
| 8–12 kW | 22–37 kW+ | Larger receiver typical |
| Multiple machines | Sum peak flows + ≥20% margin | Central plant |

Pair with [[Fiber Laser Power Classes]] and [[Screw vs Piston Compressors]].

## Flow planning method

1. Obtain max assist air flow from head/machine manual (m³/min at rated pressure)
2. Add 20–30% for leaks and future larger nozzles
3. Verify FAD on compressor curve at **16 bar** (not 7 bar brochure)
4. Size receiver for pierce peaks (often 500–1000 L class for mid-size screws — OEM dependent)
5. Add dryer and filter ΔP into pressure budget

## Pressure budget example

| Stage | Typical loss |
| --- | --- |
| Treatment train (dryer + filters) | 0.3–0.8 bar |
| Pipe run | 0.1–0.3 bar per 10 m if undersized bore |
| Machine inlet → nozzle | Internal + proportional valve |

Head needs dynamic pressure per recipe — often 10–16 bar on air cut — [[Compressed Air Cutting]].

## Dual duty: air cut + PSA

| Scenario | Sizing approach |
| --- | --- |
| Air cut OR PSA, not both peak | Size for larger of the two + margin |
| Simultaneous | Sum peaks + 20–30% |
| Unknown simultaneity | Assume simultaneous for production plants |

Starving PSA feed to favor air cut causes purity collapse — [[PSA Nitrogen Generators]].

## Electrical coordination

| Issue | Guidance |
| --- | --- |
| Inrush sag on laser | Separate compressor feeder; soft-start/VFD screw |
| Stabilizer | On laser electronics — not on compressor through undersized unit |
| Detail | [[Laser Electrical Supply Requirements]] |

## Receiver and piping tips

| Item | Practice |
| --- | --- |
| Receiver | After separator; ASME/local coded; relief valve |
| Main header | Large bore; slope to drains |
| Laser drop | Treated air only after dryer/filters |
| Tools drops | Tee **upstream** of laser fine filters only if acceptable — prefer separate |

## Undersize symptoms

| Symptom | Meaning |
| --- | --- |
| Pressure collapses on pierce | FAD or receiver too small |
| Compressor never unloads | Continuous demand > capacity |
| Dryer PDP rises under load | Dryer also undersized for FAD |
| Cut quality varies with duty | Supply marginal |

## Oversizing caveats

Huge compressors short-cycling on tiny demand waste energy and can wet the system if dryer is oversized badly. Prefer VFD screw or correctly staged plant.

## Related notes

- [[Air Compressors for Laser Cutting]]
- [[Refrigerated Dryers]]
- [[Air Filtration Stages]]
- [[Nitrogen System Pressure Setpoints]]

## Sources

- Arcus CNC installation (16 bar screw minimum)
- Industry package sizing practice
