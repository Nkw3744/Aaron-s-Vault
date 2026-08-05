---
aliases:
  - laser cutting nozzle
  - ceramic ring cutting head
type: technical-reference
category: cutting-head
applies_to: [fiber-laser]
source_reviewed: 2026-08-05
source_scope: Gweike nozzle guidance, Raytools field practice
status: generic reference — verify against nameplate and project drawing
---

# Cutting Head Nozzles and Ceramics

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Nozzle types, ceramic insulator, selection by material/thickness, maintenance.

## Nozzle role

- Focuses assist gas jet into kerf
- Forms capacitive electrode with sheet
- Must be concentric with beam for cut quality and sensor stability

## Common nozzle families

| Type | Use |
| --- | --- |
| Single layer | N₂/air thin sheet — e.g. 1.5 mm dia for 1–2 mm |
| Double layer | O₂ thick CS; some high-pressure N₂ |
| High speed / coated | OEM specific |

Match **head model** — thread and seat vary (Raytools, Precitec, WSX, etc.).

Example local: 1.5 mm single layer for 1.2 mm galvanized N₂ — [[Gweike 3015GAII 3 kW CypCut Cutting Parameter Setting]].

## Ceramic ring (body)

- Electrical insulator between nozzle and head body
- **~80% of capacitance faults** from cracked ceramic (field estimate)
- May include sealing ring — must seat fully or capacitance drifts

## Inspection schedule

| When | Action |
| --- | --- |
| Daily start | Visual nozzle orifice; slag |
| After crash | Replace ceramic; inspect nozzle |
| Poor edge quality | Check nozzle diameter wear |
| Height alarms | Clean/replace nozzle first |

## Cleaning

- Brass or wire brush on nozzle exterior only
- Do not file orifice — changes gas flow and capacitance
- Replace if orifice bell-mouthed or off-center

## Torque

Under-torque → capacitance drift during blow and cut.  
Over-torque → cracked ceramic.

Use OEM torque spec if available; otherwise firm with proper socket, not pliers on nozzle face.

## Spares kit (recommended truck stock)

- 2× common nozzle sizes per head
- 2× ceramic bodies
- 1× SMA cable
- Protective windows

## Related notes

- [[Height Sensor Alarm Reference]]
- [[Assist Gas Overview]]
- [[Autofocus and Proportional Gas Valves]]

## Sources

- Gweike cutting parameter nozzle selection tables
- Yihai Raytools service practice (ceramic crack prevalence)
