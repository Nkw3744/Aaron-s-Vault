# Communication Engineering Lab 4 — Pulse Coded Modulation

[[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Weekly Labbook|Running weekly labbook]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Report/Communication Engineering Lab Report - Draft|Running report draft]]

> [!important] Evidence hierarchy
> The photographs and traces in `Lab 4 Class Documents/` are the primary evidence of what Aaron's group actually used and did in class. This note is a preparation and interpretation aid reconstructed from the manual; it must not replace or overrule the in-class evidence.

> [!success] Manual source confirmed
> These instructions were reconstructed from **ENEL700 Lab Book 2026**, PDF pages 20–29 (file pages 20–29 of 50). The booklet is stored at:
> [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/ENEL700 Lab Book 2026.pdf]]

## Quick purpose

Use the TIMS system to investigate:

1. **PCM encoding** — converting an analogue voltage into a serial digital code;
2. **PCM decoding** — converting the serial code back into a quantised analogue signal;
3. linear and companded quantisation;
4. message reconstruction and distortion.

---

## Source photographs

### Tektronix TDS2012C oscilloscope
![[IMG_2376_Original.jpeg]]

### TIMS-301 modelling system
![[IMG_2377_Original.jpeg]]

### Lab 4 — PCM equipment list
![[IMG_2378_Original.jpeg]]

> [!warning]
> `IMG_2379_Original.jpeg` shows an **ENEL800 Superheterodyne Receiver** manual. It belongs to a different experiment and is not used below.

---

# 1. Essential theory and limits

- The encoder must receive an analogue message constrained in bandwidth and amplitude.
- Maximum permitted encoder input amplitude: **±2.0 V peak**.
- Encoder clock: external **8.333 kHz TTL sample clock** from the TIMS Master Signals module.
- Each PCM frame contains **8 equal clock slots**, numbered 7 through 0.
- Slot 0 is the least-significant-bit position and carries an embedded alternating `1, 0, 1, 0...` pattern for frame synchronisation.
- In **7-bit mode**, slots 7–1 carry seven data bits.
- In **4-bit mode**, slots 4–1 carry four data bits; slots 7–5 remain zero.
- The 4-bit system has $2^4=16$ quantisation levels.
- The 7-bit system has $2^7=128$ quantisation levels.

## Pre-calculations

Using $f_{CLK}=8.333\text{ kHz}$ and eight clock periods per frame:

$$T_b=\frac{1}{8333}=120.005\ \mu\text{s}$$

$$T_{frame}=8T_b=0.960038\ \text{ms}$$

$$f_s=\frac{f_{CLK}}{8}=1041.625\ \text{samples/s}$$

The sampling rate is the same in 4-bit and 7-bit modes because both use an eight-slot frame.

The theoretical Nyquist limit is:

$$B_{message}\leq\frac{f_s}{2}=520.813\ \text{Hz}$$

In practice, the input should be band-limited below this upper boundary.

For the four data-bit slots:

$$T_{4\text{-bit word}}=4T_b=480.019\ \mu\text{s}$$

The same embedded bit value reappears every two frames because slot 0 alternates between one and zero:

$$2T_{frame}=1.920077\ \text{ms}$$

> [!note] Likely booklet typo
> Page 27 says the alternating embedded bits should be “1920 ms apart.” With an 8.333 kHz clock, the consistent value is **1.920 ms** (or 1920 μs), not 1920 ms.

---

# 2. Equipment

- TIMS-301 modelling system
- PCM Encoder module
- PCM Decoder module
- Variable DC module
- Buffer Amplifier module
- Master Signals module
- Oscilloscope: Tektronix TDS2012C
- DC voltmeter: Uni-T UT803 or equivalent
- TIMS patch leads and oscilloscope leads

## Important terminals

### PCM Encoder

- `Vin` — analogue input
- `CLK` — TTL master-clock input
- `FS` — end-of-frame synchronisation output
- `PCM DATA` — serial PCM output
- `SYNC MESSAGE` — clock-synchronised periodic message
- coding switch — `7-bit LINEAR`, `4-bit LINEAR`, or `4-bit COMPAND`

### PCM Decoder

- `PCM DATA` — serial PCM input
- `CLK` — TTL master-clock input
- `EXT FS` — external frame-sync input
- `EMBED FS` — internally recovered frame-sync output
- `Vout` — decoded sample-and-hold output
- `FS SELECT` — `EXT FS` or `EMBED`
- coding switch — must match the encoder

---

# 3. Part A — PCM encoder

## A1. Initial 4-bit linear setup

> [!danger]
> Build or change patching with the TIMS system switched off. Never connect an output directly to another output.

1. Insert the **PCM Encoder** module into the TIMS frame.
2. Set its coding switch to **4-bit LINEAR**.
3. Connect:

| From | To | Purpose |
|---|---|---|
| Master Signals `8.333 kHz TTL SAMPLE CLOCK` | Encoder `CLK` | Encoder master clock |
| Variable DC `GND` | Encoder `Vin` | Initial 0 V message |
| Encoder `FS` | Oscilloscope `EXT TRIG` | Stable frame triggering |
| Encoder `FS` | Oscilloscope CH1 | Display frame markers |
| Master Signals `8.333 kHz TTL` | Oscilloscope CH2 | Display clock initially |

4. Set the oscilloscope to show approximately **three frame markers**.
5. Trigger externally from encoder `FS`.
6. Record the number of clock periods in one frame. Expected result: **8 periods**.

### Initial oscilloscope arrangement

- CH1: encoder `FS`
- CH2 initially: `CLK`
- external trigger: encoder `FS`
- use DC coupling
- adjust timebase near **0.5 ms/div** and refine until two or three frames are clear

## A2. PCM output for a zero-volt input

Before looking at the result, sketch the expected PCM frame.

1. Keep encoder `Vin` grounded at 0 V.
2. Move oscilloscope CH2 from `CLK` to encoder `PCM DATA`.
3. Display approximately two or three frames.
4. Identify slots 7 through 0.
5. Identify the four-bit word in slots **4, 3, 2, and 1**.
6. Record the alternating embedded frame-sync bit in slot 0.

### Four-bit frame layout

```text
Slot:       7     6     5     4     3     2     1     0
Purpose:    0     0     0    D3    D2    D1    D0    FS
                                                   alternates
                                                   1,0,1,0...
```

Do not assume that 0 V must encode as binary `0000`; identify the actual code from the trace.

## A3. Determine the 4-bit linear quantisation levels

1. Disconnect `Vin` from ground.
2. Connect **Variable DC output → Encoder `Vin`**.
3. Connect the DC voltmeter across the encoder input/reference so it measures the actual `Vin`.
4. Slowly sweep Variable DC through its complete range.
5. Observe that the PCM code changes in discrete jumps.
6. Set `Vin` to its maximum negative value.
7. Record:
   - the measured input voltage;
   - the four-bit binary word in slots 4–1;
   - its decimal value.
8. Slowly increase `Vin` until the PCM word changes.
9. Record the transition voltage and the new word.
10. Continue across the full DC range until all 16 quantisation regions/transitions are mapped.
11. Plot:
   - horizontal axis: input/transition voltage;
   - vertical axis: decimal equivalent of the four-bit code.

### 4-bit linear data table

| Region / transition | Measured $V_{in}$ (V) | Binary slots 4–1 | Decimal code | Notes |
|---:|---:|:---:|---:|---|
| 1 | | | | maximum negative end |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |
| 11 | | | | |
| 12 | | | | |
| 13 | | | | |
| 14 | | | | |
| 15 | | | | |
| 16 | | | | maximum positive end |

## A4. Determine the 4-bit companding law

1. Keep the Variable DC and voltmeter connected to encoder `Vin`.
2. Change the encoder switch to **4-bit COMPAND**.
3. Repeat the transition-voltage measurements over the full input range.
4. Record the spacing between adjacent transitions.
5. Plot decimal code against input voltage.
6. Compare the transition spacing with the 4-bit linear result.

Expected qualitative observation: companded quantisation levels are closer together for small input amplitudes and farther apart for larger amplitudes. Record measured evidence rather than relying on this expectation.

### 4-bit companded data table

| Region / transition | Measured $V_{in}$ (V) | Binary slots 4–1 | Decimal code | Adjacent spacing (V) |
|---:|---:|:---:|---:|---:|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |
| 11 | | | | |
| 12 | | | | |
| 13 | | | | |
| 14 | | | | |
| 15 | | | | |
| 16 | | | | |

## A5. Periodic message

1. Take the periodic message from encoder `SYNC MESSAGE`.
2. Display the synchronised message on the oscilloscope.
3. Record its frequency and waveform shape.
4. Check that its frequency is compatible with the Nyquist limit calculated above.
5. If needed, pass the message through a **Buffer Amplifier** to keep its amplitude within the encoder input limit.
6. Display:
   - CH1: encoder `FS`;
   - CH2: encoder `PCM DATA`.
7. Trigger from `FS` and display two or three frames.
8. Record the trace.

The data may appear as several overlaid code words because the sinusoidal message produces different samples in successive frames.

---

# 4. Part B — PCM decoder

## B1. Prepare the encoder as the transmitter

1. Use the Master Signals **8.333 kHz TTL** for encoder `CLK`.
2. Select encoder **4-bit LINEAR**.
3. Trigger the oscilloscope externally from encoder `FS`.
4. Start near **0.5 ms/div** so a few frames are visible.
5. Connect oscilloscope CH1 through the Scope Selector, if used, to encoder `PCM DATA`.
6. Apply a large negative DC message from Variable DC to encoder `Vin`.
7. Adjust it to the region which produces code word `0000`.
8. Confirm that only the alternating embedded slot-0 bits remain visible.
9. Confirm the same-state embedded pulses are approximately **1.920 ms apart** by measurement and calculation.
10. Vary the DC signal and observe the new code patterns.
11. Return Variable DC to maximum negative, fully anticlockwise.

## B2. Connect the decoder as the receiver

Set decoder coding to **4-bit LINEAR**.

### Exact decoder connections

| From | To | Purpose |
|---|---|---|
| Encoder `PCM DATA` | Decoder `PCM DATA` | Serial coded signal |
| Master Signals `8.333 kHz TTL` / branched encoder clock | Decoder `CLK` | Stolen/synchronised clock |
| Encoder `FS` | Decoder `EXT FS` | Stolen frame synchronisation |
| Decoder `Vout` | Oscilloscope CH2 | Quantised sample-and-hold output |

Set decoder `FS SELECT` to **EXT FS**.

## B3. Set the oscilloscope for input/output measurements

1. Set both channels to **DC coupling**.
2. Set both channels to **1 V/div**.
3. Temporarily ground both channel inputs.
4. Position each zero trace in the centre of its own half of the screen.
5. Remove the grounding connections.
6. Use:
   - CH1: encoder input `Vin` / Variable DC;
   - CH2: decoder `Vout`.

## B4. DC transmission and quantisation staircase

1. Confirm encoder `PCM DATA → Decoder PCM DATA` is connected.
2. Slowly sweep Variable DC over its full range.
3. Observe:
   - CH1 input changes continuously;
   - CH2 decoder output changes in 16 discrete levels.
4. Record paired input and output voltages.
5. Compare these decoder levels with the encoder transition levels measured in Part A.

### Encoder-input/decoder-output data

| Point | Encoder $V_{in}$ (V) | Decoder $V_{out}$ (V) | Binary code | Error $V_{out}-V_{in}$ (V) |
|---:|---:|---:|:---:|---:|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |
| 11 | | | | |
| 12 | | | | |
| 13 | | | | |
| 14 | | | | |
| 15 | | | | |
| 16 | | | | |

## B5. Periodic message

1. Disconnect the DC message.
2. Connect encoder `SYNC MESSAGE → Buffer Amplifier → Encoder Vin`.
3. Adjust message amplitude to **2 Vpp**.
4. Slow the oscilloscope timebase to approximately **1 ms/div**. The booklet says 1 ms/cm; on the digital oscilloscope use the division grid.
5. Observe and record decoder `Vout` on CH2.
6. Capture both the original message and the quantised sample-and-hold output where possible.

## B6. Reconstruction and FFT

The decoder output is a quantised, flat-top sample-and-hold waveform. Reconstruct the message using the low-pass filtering arrangement directed by the lecturer/manual diagram.

1. Apply decoder `Vout` to the appropriate low-pass-filter input.
2. Display the reconstructed output.
3. Compare it with the original periodic message.
4. Put the oscilloscope in FFT mode.
5. Look for second- and third-order message harmonics.
6. Record whether distortion components are visible and their relative levels.

> [!warning]
> The text specifies low-pass reconstruction but does not provide an unambiguous socket-by-socket filter patch in the extracted Lab 4 pages. Confirm the intended TIMS filter module and output socket with the lecturer before patching this final stage.

---

# 5. Complete connection checklist

## Encoder-only stage

- [ ] Encoder switch: `4-bit LINEAR`
- [ ] `8.333 kHz TTL → Encoder CLK`
- [ ] `Variable DC GND → Encoder Vin` initially
- [ ] `Encoder FS → Oscilloscope EXT TRIG`
- [ ] `Encoder FS → CH1`
- [ ] `CLK`, then `PCM DATA → CH2`

## Encoder and decoder stage

- [ ] Encoder switch: `4-bit LINEAR`
- [ ] Decoder switch: `4-bit LINEAR`
- [ ] Decoder `FS SELECT`: `EXT FS`
- [ ] `8.333 kHz TTL → Encoder CLK`
- [ ] same/stolen `8.333 kHz TTL → Decoder CLK`
- [ ] `Encoder FS → Decoder EXT FS`
- [ ] `Encoder PCM DATA → Decoder PCM DATA`
- [ ] `Encoder Vin/reference → CH1`
- [ ] `Decoder Vout → CH2`
- [ ] both scope channels: DC coupling, 1 V/div for the DC comparison

---

# 6. Booklet questions and answer framework

## Question 1 — sampling rate and message bandwidth

Calculated above:

- sampling rate: **1041.625 samples/s**;
- same for 4-bit and 7-bit because both frames contain eight clock slots;
- theoretical maximum message bandwidth: **520.813 Hz** by Nyquist.

## Question 2 — 4-bit timing and levels

- sampling rate: **1041.625 samples/s**;
- frame width: **0.960038 ms**;
- bit width: **120.005 μs**;
- four-bit data-word width: **480.019 μs**;
- quantisation levels: **16**;
- linear-mode levels should be uniformly spaced; verify this from measured transition voltages.

## Question 3 — define the PCM frame

A frame is the eight-clock-slot interval used to transmit one quantised sample. In 4-bit mode, slots 7–5 are zero, slots 4–1 contain the data code, and slot 0 contains the alternating embedded frame-sync bit.

## Question 4 — transmitting frames more slowly

Discuss buffering/storing completed frames and transmitting them later at a lower serial rate, provided the receiver recovers the clock/frame timing and the average channel rate can carry all generated information. Consider when delay is acceptable and when reduced transmission bandwidth or time-division sharing is beneficial.

## Question 5 — stable and unstable PCM displays

A DC input repeatedly produces the same quantised code, so each triggered frame overlays the previous one. A sinusoid usually produces a different code from frame to frame, creating many overlaid words unless acquisition is synchronised over the entire repeating message/code sequence or a single frame is captured.

## Question 6 — quantisation graph

Use the measured transition table. Draw voltage horizontally and binary/decimal code vertically. Explain that each transition was found by slowly changing `Vin` until the displayed four-bit word changed.

## Question 7 — reconstruction-filter characteristic

The reconstruction filter requires a flat passband across the wanted message band and sufficient attenuation of sampling components above it. It must not remove in-band message harmonics that are being measured as distortion; otherwise the experiment would under-report distortion.

## Question 8 — specifying the reconstruction filter

Base the specification on:

- maximum wanted message bandwidth;
- sampling rate;
- separation between the wanted spectrum and the first sampling images;
- allowable passband ripple/amplitude error;
- required stopband attenuation;
- acceptable phase/group-delay distortion;
- the distortion components that must remain observable.

## Question 9 — reducing sampling and quantisation distortion

- Sampling distortion: raise the sampling rate relative to message bandwidth, use suitable anti-alias and reconstruction filters, and compensate the sample-and-hold aperture/droop when necessary.
- Quantisation distortion: increase bit depth/number of levels, optimise signal amplitude to use the available input range, or use suitable non-uniform quantisation/companding.

## Question 10 — cost of more quantisation levels

More levels require more bits per sample. This increases converter complexity, serial bit rate, required channel bandwidth/storage, and potentially clocking/power demands. In this TIMS experiment, the eight-slot frame remains fixed, so moving from four to seven data bits changes the occupied frame slots and resolution but does not change the sample rate.

---

# 7. Evidence to collect

- [ ] Photograph of completed encoder patching
- [ ] Photograph of completed decoder patching
- [ ] FS and clock trace showing eight clock periods per frame
- [ ] Zero-input PCM trace with slots labelled
- [ ] Complete 4-bit linear transition table
- [ ] Linear quantisation graph
- [ ] Complete 4-bit companding transition table
- [ ] Companding graph and comparison
- [ ] Periodic message frequency, shape, and amplitude
- [ ] Periodic-message PCM trace
- [ ] Decoder input/output staircase data
- [ ] Input and sample-and-hold output screenshot
- [ ] Reconstructed output screenshot
- [ ] FFT showing second and third harmonics
- [ ] All oscilloscope scales and probe factors recorded

# 8. Troubleshooting order

1. Check that both modules have the same coding mode.
2. Check `8.333 kHz TTL` at both clock inputs.
3. Check encoder `FS` and eight clock periods per frame.
4. Check encoder `PCM DATA` before troubleshooting the decoder.
5. Check decoder `FS SELECT = EXT FS` when using stolen FS.
6. Check `Encoder FS → Decoder EXT FS`.
7. Check `Encoder PCM DATA → Decoder PCM DATA`.
8. Confirm scope channels are DC-coupled and referenced correctly.
9. Keep encoder input within ±2 V peak.
10. Ask the tutor to verify patching before moving unrelated controls.

> [!note]- Supporting Lab 4 photographs and raw files
> These files remain beside the lab note so the main course Overview does not become a photo gallery.
> - [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab4 Recorded Data.txt|Recorded data]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 answers Kane.pdf|answer reference]]
> - [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/IMG_2376_Original.jpeg|Photo 1]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/IMG_2377_Original.jpeg|Photo 2]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/IMG_2378_Original.jpeg|Photo 3]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/IMG_2379_Original.jpeg|Photo 4]]
> - [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/341F0719-8146-4629-B6DB-A01E5C1A1658.JPG|Photo 5]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/AA06F6D9-ACAF-449A-AC36-30C4613A34A1.JPG|Photo 6]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/726424E8-03E2-4DB9-B0B7-DE1336643C03.JPG|Photo 7]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/E70FA75B-6375-42E7-AC26-0F273758E105.JPG|Photo 8]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/FF32F2C8-BDB9-4C5F-9F25-CADB0F6287D0.JPG|Photo 9]]
> - [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/1FB5A1C1-D1E0-4F62-9F98-16C1D8678FEE.JPG|Photo 10]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/67EAA729-D418-4075-803C-5A2196C63CE8.JPG|Photo 11]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/1B4E24ED-F867-4D86-AD97-58DBCAEFD16C.JPG|Photo 12]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/7488FDFA-EB7F-44F4-A17A-2B586A7C2375.JPG|Photo 13]]
