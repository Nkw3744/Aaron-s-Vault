---
aliases:
  - refrigerated air dryer
  - laser air dryer
  - PDP compressed air
type: technical-reference
category: air-compressors
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Arcus/BLMA install guides, ISO 8573 practice, field dryer service
status: generic reference — verify against nameplate and project drawing
---

# Refrigerated Dryers

Return to [[Air Compressors for Laser Cutting]] · [[Technical Reference Index]]

> [!info] When to open this note
> Mandatory drying stage before laser cutting air reaches fine filters and the head. Use for sizing, placement, condensate drains, and water-in-line faults.

> [!danger] Mandatory for laser air cutting
> Compressed air without drying carries water vapor that condenses in lines and on the protective window. Bypass "for a day" is how windows die.

## Function

A refrigerated dryer cools compressed air to a typical **pressure dew point (PDP) around +3 °C**, condenses moisture, separates liquid, then reheats the air slightly to reduce downstream pipe sweating. It does **not** remove oil aerosols — that is the filter train's job — [[Air Filtration Stages]].

## Placement in the train

```
Compressor → separator → receiver → refrigerated dryer → coalescing → fine 0.01 µm → machine
```

| Rule | Why |
| --- | --- |
| After receiver | Buffer flow; cooler inlet air |
| Before fine filters | Wet filters load and channel |
| Not before compressor | Meaningless |
| Bypass only with maintenance plan | Accidental open bypass = wet laser |

## Selection parameters

| Parameter | Guidance |
| --- | --- |
| Flow rating | ≥ compressor FAD at working pressure |
| Inlet temperature | Derate if compressor room >40 °C |
| Ambient at dryer | Needs condenser ventilation |
| Pressure drop | Often 0.2–0.5 bar — include in head pressure budget |
| Electrical | Dedicated circuit preferred; not through laser stabilizer |

### Desiccant dryers

Use when OEM demands very low PDP (e.g. <−40 °C) or extreme humidity + long outdoor pipe runs. Less common on standard fiber air-cut packages; higher cost and purge air consumption.

## Installation checklist

1. Flow arrows correct; vertical mount as OEM requires
2. Clearance for condenser fan service
3. Auto drain on separator — test daily in humid climate
4. Drain piped to tundish / oily-water handling (not across walkway)
5. Inlet filtration if compressor oil carry-over high
6. Earth ground per manual
7. No permanent open bypass without lockable valve and tag procedure
8. Record model, PDP rating, and install date on machine/air hub notes

## Normal operation — what good looks like

| Check | Normal |
| --- | --- |
| Condensate | Regular drain pulses during production |
| Dryer outlet pipe | Cooler than compressor discharge; not ice-blocked |
| Laser inlet filter bowl | Dry or only trace moisture |
| PDP indicator (if fitted) | In green / near rated PDP |
| Condenser | Clean fins; free airflow |

## Interaction with ambient humidity

Even with a good dryer, long uninsulated pipes in a cold plant can re-condense. Keep laser branch short after treatment; add drains at low points — [[Gas Pipework and Fittings]], [[Workshop Humidity and Condensation]].

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Water in laser filter | Dryer failed; bypass open; drain stuck | Close bypass; service dryer; clear drain |
| Dryer high-temp / alarm | Dirty condenser; poor ventilation; high inlet T | Clean fins; improve room airflow |
| High pressure drop | Undersized dryer; iced evaporator; blockage | Check ΔP; thaw/service; upsize |
| Oil in dryer bowl | Upstream separator failed | Fix compressor separator first |
| No condensate ever | Drain failed closed **or** dryer not cooling | Do not assume "air is dry" |
| Ice on dryer | Over-cooling fault / low load | OEM service |

## Field test when "maybe the dryer is bad"

1. Confirm compressor and dryer running 30+ min under load
2. Crack drain — should see liquid in humid weather / after load
3. Feel outlet vs inlet temperature difference
4. Check bypass valve position and tags
5. Inspect first coalescing bowl downstream — water here = dryer or drain fault
6. Only then blame machine proportional valve or head

## Maintenance

| Task | Interval |
| --- | --- |
| Clean condenser | Monthly dusty shops |
| Test auto drain | Weekly (daily humid) |
| Refrigeration service | Per OEM hours / if PDP drifts |
| Replace pre-filter (if fitted) | With ΔP rise |

## Related notes

- [[Air Filtration Stages]]
- [[Compressed Air Cutting]]
- [[Screw vs Piston Compressors]]
- [[Compressor Sizing by Laser Power]]
- [[Workshop Humidity and Condensation]]

## Sources

- Arcus CNC laser installation (refrigerated dryer mandatory)
- BLMA fiber laser installation guide
- ISO 8573 compressed air quality practice
