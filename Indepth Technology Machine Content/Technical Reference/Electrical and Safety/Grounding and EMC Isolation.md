---
aliases:
  - laser grounding
  - EMC laser installation
  - capacitive sensor ground
type: technical-reference
category: electrical
applies_to: [fiber-laser, co2-laser]
source_reviewed: 2026-08-05
source_scope: Arcus environmental guide, capacitive sensing field guides, power-quality practice
status: generic reference — verify against nameplate and project drawing
---

# Grounding and EMC Isolation

Return to [[Technical Reference Index]]

> [!info] When to open this note
> Protective earth (PE), ground-resistance targets, bonding of bed/slats/duct, and EMC/EMI issues that show up as height-sensor chaos, encoder faults, or random CNC resets.

> [!warning] Licensed work
> Driving earth electrodes and altering MEN/PE arrangements is electrical work under local rules (NZ: AS/NZS 3000 and HSWA). This note is equipment-oriented guidance for techs coordinating with the electrician.

## Why grounding matters on a laser

Two separate problems share the word "ground":

1. **Safety PE** — fault current path so breakers trip and metalwork stays near earth potential
2. **Signal reference** — capacitive height sensing and encoder electronics need a stable zero relative to the workpiece and bed

A machine can pass a casual "there's a green wire" check and still have floating slats, painted contact points, or EMI that makes [[Capacitive Height Sensing BCS100]] unusable.

## Protective grounding (PE) — typical OEM asks

Arcus/GWK-style targets (always verify project drawing and OEM):

| Item | Typical requirement | Why |
| --- | --- | --- |
| Ground electrode | Independent copper rod ≥2.4 m | Low impedance to true earth |
| Ground resistance | <4 Ω at installation | Measurable acceptance test |
| PE conductor | ≥16 mm² copper to machine PE bar | Fault capacity and stiffness |
| Bonding | Bed, slats (where specified), dust collector duct, cable trays | Single reference plane |

Record measured Ω on the machine hub at commissioning and after any relocation.

## Machine ground bar practice

| Do | Don't |
| --- | --- |
| Bring laser PE, chiller PE, extractor PE to a defined star or OEM bar | Rely on random building steel alone |
| Bond gas panels and cable trays if OEM shows them | Create long daisy-chain PE through paint |
| Re-measure after move | Assume "it was fine before" |

## Height-sensing ground path (critical)

Capacitive follow measures nozzle vs **grounded workpiece**:

```
Nozzle (electrode) → sheet → slats → bed frame → PE bar → earth
```

Anything that breaks that chain raises noise and false capacitance:

| Break | Symptom | Fix |
| --- | --- | --- |
| Rusty / painted slats | Unstable height, "sensor not stable" | Clean contact; bare metal cal plate |
| Plastic / rubber pads under sheet | Floating sheet | Metal contact or grounding strap |
| Isolated scrap on table | Random jumps | Clear scrap; ground bed |
| Loose bed–frame bond | Intermittent alarms | Bonding strap; star washers |
| Poor PE to building | Site-wide noise | Electrician — electrode / MEN check |

See [[Height Sensor Alarm Reference]].

## EMC / electrical noise sources

| Source | Typical effect | Mitigation |
| --- | --- | --- |
| Arc welding nearby | Height jumps, network timeouts | Separate circuit; ≥10 m class separation where possible |
| VFD compressors / extractors | Encoder glitches, BCS100 drops | Line filters; separate feeder; cable segregation |
| Welding on slats while sensing | Capacitance chaos | Sequence work — no weld during follow |
| RF/SMA cable parallel to 380 V | Noisy capacitance | Separate tray; cross at 90° |
| Poor shield termination | Intermittent | Bond shields per OEM (one-end vs both-end) |

Symptoms often blamed on "bad ceramic" or "bad BCS100" when the root is EMI or ground.

## Cable segregation rules of thumb

1. Power (380 V / motor) in one tray; signal/Ethernet/RF in another
2. If trays must meet, cross at 90°, not run parallel for metres
3. Keep QBH fiber and RF height cable away from VFD output leads — [[Fiber Cable Bend Radius and Routing]]
4. Ethernet to BCS100: industrial cable, snug connectors, correct IP subnet

## Measurement methods

| Test | Method | Pass hint |
| --- | --- | --- |
| Earth resistance | Fall-of-potential or clamp meter per electrician practice | <4 Ω typical OEM ask |
| Continuity bed→PE | Low-Ω meter, paint scraped | Milliohms class, not open |
| Capacitance stability | Watch live C value with fans/VFDs on then off | No large steps when VFD starts |
| Wiggle RF cable | Watch C value | No spikes — else replace SMA cable |

## Lightning and surge

Outdoor extraction stacks, long duct, and long Ethernet runs pick up surges. Consider:

- Surge protection on CNC/network supplies per local practice
- Bond outdoor metal duct to the equipotential system
- After storms: check PE connections and unexplained sensor drift

## Commissioning / service checklist

1. Inspect PE conductor size and termination torque
2. Measure earth resistance — log value and date
3. Bond check: bed, source cabinet, chiller, extractor
4. Clean slat contact areas; verify sheet grounds during cal
5. Power-on with nearby welder **off**; note height stability
6. Start VFD compressor; confirm no height/network alarms
7. Document any temporary bonding straps added

## Troubleshooting map

| Symptom | First ground/EMC checks |
| --- | --- |
| Random height alarms only when compressor runs | VFD EMI; cable routing; filters |
| Alarms only on rusty sheet | Sheet–slat contact |
| BCS100 network timeout | Cable, IP, and also PE/EMI |
| Encoder following error with no mechanical bind | Shielding / PE / VFD |
| Shock tingle on panels | Dangerous PE fault — stop; electrician |

## Related notes

- [[Height Sensor Alarm Reference]]
- [[Capacitive Height Sensing BCS100]]
- [[Laser Electrical Supply Requirements]]
- [[Fiber Cable Bend Radius and Routing]]
- [[Fiber Laser Site Requirements]]

## Sources

- Arcus CNC environmental setup (grounding table)
- Arcus capacitive sensor troubleshooting (grounding section)
- Field practice on VFD/EMI interaction with BCS100-class controllers
