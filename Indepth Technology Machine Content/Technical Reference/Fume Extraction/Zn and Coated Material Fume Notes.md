---
aliases:
  - galvanized fume laser
  - zinc fume laser cutting
  - coated sheet laser fume
type: technical-reference
category: fume-extraction
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Gweike cutting guidance, occupational health practice for ZnO fume
status: generic reference — verify against nameplate and project drawing
---

# Zn and Coated Material Fume Notes

Return to [[Laser Fume Extraction Overview]] · [[Technical Reference Index]]

> [!info] When to open this note
> Extra controls when cutting galvanized, zinc-coated, painted, or primed sheet. Read before the first galvanized job on a machine and when briefing operators who treat "galv" like plain mild steel.

> [!danger] Zinc fume fever risk
> Zinc vaporizes before steel melts. Fine ZnO particulate can cause metal fume fever — flu-like illness well known in welding and equally relevant to laser cutting coated steel. Extraction mandatory; enclosure closed.

## Mechanism

Galvanized sheet (HDG or EG) carries a zinc coating. At the kerf the laser vaporizes zinc (boiling point ~907 °C) long before the steel substrate is fully processed. Result:

- Zinc-containing fume and ultrafine particulate
- White/grey deposits on nozzle, window, and ceramic
- Faster filter loading than bare mild steel
- Health exposure risk independent of whether assist gas is N₂ or air

N₂ improves edge chemistry but **does not stop zinc vaporization**.

## Why this is its own note

Zinc fume is a distinct occupational hazard from generic iron oxide dust, with a recognized acute syndrome and exposure standards under most OSH frameworks (NZ: HSWA / workplace exposure standards and SDS). Operators underestimate it because the sheet looks like ordinary mild steel until the cut starts.

## Coating types and related hazards

| Material | Extra hazard | Notes |
| --- | --- | --- |
| Hot-dip galvanized (HDG) | ZnO fume | Thick coating → more fume |
| Electro-galvanized (EG) | ZnO fume | Still requires closed enclosure |
| Painted / powder-coated | VOC + metal | Carbon stage may help odor — [[Filter Stages and Maintenance]] |
| Primer / shop coat | Mixed | Treat as coated until SDS known |
| Aluminized / Zn-Al | Metal fume | Check SDS; extraction still mandatory |

## Process notes (cutting)

| Topic | Guidance |
| --- | --- |
| Preferred assist | N₂ when edge quality matters — [[Nitrogen Assist Gas]] |
| Air assist | Possible on thin CS; still produces Zn fume |
| Pierce | Violent; splash contaminates window — extra puffing may help |
| Nozzle/window | Inspect more often than bare steel |
| Local recipe | [[Gweike 3015GAII 3 kW CypCut Cutting Parameter Setting#Current application — 1.2 mm galvanized sheet]] |

## Extraction requirements

| Control | Action |
| --- | --- |
| Enclosure | Closed during cut — non-negotiable |
| Fan | At working negative pressure **before** pierce |
| Zone dampers | Open under active cut area |
| Filters | Inspect more frequently under galv production |
| Filter change | Respirator per risk assessment; bag cartridges; no dry shaking indoors |
| Housekeeping | Avoid sweeping dry zinc dust — wet or HEPA vacuum methods per site rules |

### Why "fan before pierce" matters

Pierce on galvanized is often the single densest Zn fume burst. Extraction that only ramps after motion starts misses the peak. Confirm ΔP / airflow established before the pierce command.

## Exposure controls (workplace)

1. Workplace exposure assessment for ZnO and fine particulate
2. SDS for the specific coated product on the floor
3. Respiratory protection during filter service if assessment requires
4. Training: symptoms of metal fume fever (fever, chills, myalgia, usually hours after exposure)
5. Do not dismiss post-shift flu-like illness after heavy galv cutting

> [!warning] NZ context
> Manage under HSWA and applicable exposure standards. This note is technical support, not a full COSHH/risk assessment substitute.

## Customer / operator briefing checklist

When a shop runs galvanized for the first time:

1. Enclosure stays closed — stricter than bare mild steel habit
2. Filters load faster — schedule mid-job checks on heavy weeks
3. Flu-like symptoms after galv shifts → review extraction, not "tough it out"
4. Spent cartridges are not general waste — local hazardous waste rules for metal dust
5. Window/nozzle life will shorten — budget consumables

## Cut quality vs health (do not confuse)

| Observation | Likely conversation |
| --- | --- |
| White/grey smoke, acrid smell | Fume / extraction / enclosure |
| Yellow/gold edge on **stainless** | N₂ purity/pressure — not Zn |
| Dross on galv carbon steel | Process parameters — [[Cutting Parameters Index]] |
| Rapid window burn on galv | Splash + Zn deposits + maybe air quality |

## Maintenance interaction

| Item | Galv effect |
| --- | --- |
| Protective window | Faster pitting / haze |
| Nozzle | Beads and bridging → height alarms — [[Height Sensor Alarm Reference]] |
| Ceramic | Contaminated contacts |
| Cartridges | Higher ΔP rise rate — [[Filter Stages and Maintenance]] |

## Related notes

- [[Laser Fume Extraction Overview]]
- [[Dust Collector Sizing]]
- [[Filter Stages and Maintenance]]
- [[Nitrogen Assist Gas]]
- [[Cutting Head Nozzles and Ceramics]]
- [[Fiber Connector Cleaning and Inspection]]

## Sources

- Gweike 3015GAII commissioning zinc-fume callout (local vault)
- General occupational health guidance for zinc oxide fume
- Field practice on coated-sheet filter and window life
