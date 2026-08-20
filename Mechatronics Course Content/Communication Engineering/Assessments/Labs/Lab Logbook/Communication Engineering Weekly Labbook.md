---
course: ENEL700 Communication Engineering
assessment: Laboratory Logbook
status: running
student: Aaron Taylor
team_members:
  - Nahil
  - Iyla
  - Amber
  - Aaron Taylor
last_updated: 2026-08-02
---

# ENEL700 Communication Engineering — Weekly Laboratory Logbook

> [!important] Working master and hardcopy requirement
> This is the organised running record used to prepare the laboratory report. Current course guidance also requires a **hardcopy logbook** covering all four labs, including measured data, waveforms, observations, mistakes, and how they were resolved. Keep the hardcopy current unless the lecturer confirms that this digital version can replace it.

[[Mechatronics Course Content/Communication Engineering/Communication Engineering Lab Index|Lab workspace]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Report/Communication Engineering Lab Report - Draft|Running report draft]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Labbook - Answered Questions/Communication Engineering Labbook - Answered Questions.pdf|Answered questions, evidence and graphs (PDF)]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/ENEL700 Lab Book 2026.pdf|2026 laboratory manual]]

## Evidence rule

The group’s **in-class folders are the primary record of what was actually done**. Manual reconstructions, later MATLAB replications, calculations, and classmates’ answers are supporting material only and must not be presented as in-class results.

## Running status

| Week | Laboratory work | Attendance | Primary in-class evidence | Status |
|---:|---|---|---|---|
| 1 | Lab 5 — amplitude modulation | Full group | Initial MATLAB/Simulink work; later-preserved class model and spectra | Recorded; technical details still being refined |
| 2 | Lab 5 — amplitude modulation | Full group | `lab5part2.slx`, `lab5final.mat`, `finalgragh.fig`, MATLAB workspace and spectrum screenshots | Completed in class; final troubleshooting detail needed |
| 3 | Lab 4 — pulse-code modulation | Aaron and Nahil | PCM bench, encoder patching, manual annotations, meter readings, oscilloscope traces and verified graphs | Questions answered; raw uncertainties visibly retained |
| 4 | Lab 4 continued — PCM decoding and reconstruction | Iyla, Amber, Nihil and Aaron | Complete encoder/decoder patching, 16 voltage pairs, periodic-message traces, sample-and-hold/reconstruction and FFT photographs | Completed; data graphed and analysed |
| 5 | Lab 3 — binary phase-shift keying | *** confirm attendance | TIMS BPSK transmitter/receiver patching, phase-transition traces, bandwidth/filter observations and two-scope evidence | Manual questions answered; personal session details still needed |

---

<details open>
<summary><strong>Week 1 — Lab 5: Amplitude modulation</strong> · first attempt</summary>

## Week 1 — Lab 5: Amplitude modulation

### Attendance and roles

Everyone in the group attended. We began by setting up MATLAB and working through Lab 5 from the laboratory book. We rotated the computer role so that everyone had direct time entering and running the work.

While one person operated the computer, the others supported the task by reading the next instructions, checking the code being entered, looking ahead to the next step, or researching enough background to understand what the signals and plots were meant to show. This kept everyone involved rather than leaving the work to one operator.

### Aim and preparation

The practical introduced amplitude modulation using MATLAB and Simulink. The class task involved generating the message signal, multiplying it by a sinusoidal carrier, observing the modulated output, and comparing the message, carrier, and modulated spectra.

### Equipment, software, and setup

- MATLAB
- Simulink
- Lab 5 instructions from the ENEL700 laboratory manual
- Group computer used in class

### What we did

We followed the laboratory instructions in sequence and took turns entering the supplied MATLAB work. We reached the part that required three spectra to be displayed together as vertically stacked plots.

### Measurements and results

The class work produced signal and spectrum data, but the required three-plot arrangement was not completed during this first session.

### Problems, mistakes, and troubleshooting

The main problem was that the code did not produce the required three graphs. We attempted to use Claude to help diagnose the issue, but we did not resolve it before the laboratory ended.

### Observations and interpretation

The first session showed that entering code and obtaining an output was not enough: the plots also had to be arranged and checked against the requested signal order. The group needed a more controlled troubleshooting method for the next session.

### What we learned and what we would change

Rotating roles worked well for participation. The weaker part was debugging through one shared screen. In the next session, it would have helped to preserve one known version, change one part at a time, and write down what each change affected.

### Primary evidence

The final in-class folder retained after Week 2 contains the completed class model and output evidence used to continue this work:

- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/lab5part2.slx|Class Simulink model]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/lab5final.mat|Class MATLAB data]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/finalgragh.fig|Editable class MATLAB figure]]

### Report-ready points

- The group used rotating roles so every member gained direct MATLAB experience.
- The unresolved plotting problem provides a genuine example of iterative troubleshooting.
- The session identified the need for controlled code changes and version preservation.

</details>

---

<details open>
<summary><strong>Week 2 — Lab 5: Amplitude modulation</strong> · completed class work</summary>

## Week 2 — Lab 5: Amplitude modulation

### Attendance and roles

The full group continued from the previous week’s plotting problem. The team again divided the immediate work between operating MATLAB, checking the laboratory instructions, understanding the expected spectra, and trying changes to the code.

### What we did

We resumed the code that had failed to display the three required spectra correctly. At first, people worked more individually on possible fixes. Because everyone was trying to understand different parts of the code through one computer, changes sometimes overlapped and parts were deleted or reset before the earlier version had been fully diagnosed.

We eventually completed the laboratory successfully. The in-class folder preserves the Simulink model, MATLAB data, editable MATLAB figure, workspace state, and several versions of the three-spectrum result.

### In-class model evidence

The saved class model contains:

- `Signal From Workspace` using `bumps'`;
- a discrete sine-wave carrier with frequency `2*pi*0.3`, phase `pi/2`, and sample time `1`;
- a Product block multiplying the message and carrier;
- a Scope connected to the product;
- a To Workspace block saving the result as `am`.

[[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/lab5part2.slx|Open the class Simulink model]]

### Results and observations

The clearest preserved class screenshot shows:

1. the **modulating signal**, centred on normalized frequency zero;
2. the **carrier**, with dominant components near normalized frequencies `-0.3` and `+0.3`;
3. the **modulated signal**, with translated spectral content around `-0.3` and `+0.3`.

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/Screenshot 2026-07-23 184430.png|900]]

*In-class three-spectrum result retained in the Lab 5 Class Documents folder. The plots are labelled Modulating signal, carrier, and Modulated signal.*

The other preserved screenshots appear to record intermediate or alternate plotting states and remain useful for tracing the troubleshooting process:

- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/Screenshot 2026-07-23 184310.png|Spectrum screenshot 18:43:10]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/Screenshot 2026-07-23 184343.png|Spectrum screenshot 18:43:43]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/Screenshot 2026-07-23 184421.png|Spectrum screenshot 18:44:21]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/Screenshot 2026-07-23 184430.png|Spectrum screenshot 18:44:30]]

The workspace capture records variables including `am`, `AM`, `bump`, `bumps`, `DB`, `f`, `NFFT`, `out`, `required`, and `v`.

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/image.png|650]]

*In-class MATLAB workspace state. This is useful execution evidence, although it is weaker than the labelled spectra as a main report figure.*

### Problems, mistakes, and troubleshooting

Looking back, the group’s debugging was initially too scattered. Several people proposed and entered changes through the same computer, and some changes overwrote each other. Deleting and resetting code made it harder to identify which part had caused the original problem.

The experience showed why debugging should start from a saved baseline, use one change at a time, and check the output after each change. Despite the inefficient start, the group worked through the issue and completed the required result.

### What we learned and what we would change

- Preserve a known working or starting version before experimenting.
- Assign one person to enter changes while the group agrees on each change.
- Compare every output to the required plot titles, order, frequency range, and expected peaks.
- Save the final model, data, editable figure, and screenshots together—as was done in the class folder.

### Answers to the remaining evidence questions

- The surviving files do not identify one decisive plotting line. The verified final arrangement selects each axis with `subplot(3,1,k)` before calling `sigspec` for the message, carrier and modulated signals.
- The evidence does not support attributing the final fix to a named lecturer or classmate.
- The model routes the Product output to a Scope, but no clearly identified in-class Scope capture survives. The saved three-spectrum screenshot is the strongest final class result.
- The full first-person answers, evidence boundaries and Lab 5 scaling graph are in [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Labbook - Answered Questions/Communication Engineering Labbook - Answered Questions.pdf|the answered-questions PDF]].

### Report-ready points

- The class files directly support that the group built and saved the Simulink modulation chain.
- The final class screenshot visibly supports the expected spectral translation around normalized frequency `±0.3`.
- The troubleshooting process supports a useful reflection on controlled changes and collaborative work through one shared computer.

</details>

---

<details open>
<summary><strong>Week 3 — Lab 4: Pulse-code modulation</strong> · in-class measurements</summary>

## Week 3 — Lab 4: Pulse-code modulation

### Attendance and roles

Two group members attended because the other teammates were sick. Nahil and I worked on Lab 4.

### Aim and preparation

The practical used the TIMS PCM equipment to relate analogue input voltage to a four-bit code and oscilloscope frame. Before gathering the table, we took time to understand the context of the task and the general shape of the encoded signal.

### Equipment and setup

The in-class folder confirms use of:

- TIMS-301 training system;
- PCM Encoder module;
- Tektronix TDS2012C oscilloscope;
- digital multimeter;
- patch leads and the Lab 4 PCM instruction sheet.

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/IMG_2377_Original.jpeg|700]]

*TIMS-301 laboratory system photographed during the class.*

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/1FB5A1C1-D1E0-4F62-9F98-16C1D8678FEE.JPG|650]]

*Close in-class photograph of the PCM Encoder area and patch leads.*

### What we did

We learned from the lecturer and other classmates how to align and interpret the PCM frames. We practised identifying the data positions and checked our method with classmates before relying on it for the measurements.

After establishing the decoding process, we divided the work: one person concentrated on finding each transition/result and the other recorded the voltage and bit code. This allowed the pair to gather the required data efficiently.

### In-class decoding reference

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/341F0719-8146-4629-B6DB-A01E5C1A1658.JPG|650]]

*The annotated in-class instruction page used while identifying the frame and four-bit word.*

### Measurements and oscilloscope evidence

The primary evidence is the meter-and-oscilloscope photography in `Lab 4 Class Documents`. The companion text table is a transcription of the measured sequence and remains subject to checking where its spacing is unusual.

| In-class photograph | Visible meter value | Companion recorded code | Evidence note |
|---|---:|:---:|---|
| `67EAA729-D418-4075-803C-5A2196C63CE8.JPG` | approximately `-2.634 V` | `0000` | negative endpoint |
| `FF32F2C8-BDB9-4C5F-9F25-CADB0F6287D0.JPG` | approximately `-2.240 V` | `0001` | next recorded level |
| `AA06F6D9-ACAF-449A-AC36-30C4613A34A1.JPG` | approximately `-1.911 V` | `0010` | recorded level |
| `1B4E24ED-F867-4D86-AD97-58DBCAEFD16C.JPG` | approximately `-1.595 V` | `0011` | recorded level |
| `E70FA75B-6375-42E7-AC26-0F273758E105.JPG` | approximately `-1.100 V` | `0001` | matches Question 4.2 |
| `726424E8-03E2-4DB9-B0B7-DE1336643C03.JPG` | approximately `-2.633 V` | `0000` | matches the negative start of Question 4.2 |

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/67EAA729-D418-4075-803C-5A2196C63CE8.JPG|650]]

*In-class negative-end measurement: approximately −2.634 V with the corresponding oscilloscope trace.*

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/1B4E24ED-F867-4D86-AD97-58DBCAEFD16C.JPG|650]]

*In-class measurement: approximately −1.595 V with its PCM trace.*

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/726424E8-03E2-4DB9-B0B7-DE1336643C03.JPG|650]]

*A second in-class negative-end measurement: approximately −2.633 V with a different trace, matching the start of Question 4.2.*

### Observations and interpretation

The code changed in discrete steps as the analogue voltage was varied. This is the practical behaviour expected from quantisation: a continuous input range is represented by a finite set of code words.

The pair’s most important process step was not simply recording meter values; it was first learning how to identify the relevant four-bit word reliably from the oscilloscope frame.

### Problems and uncertainties

- The companion linear table contains the sequence `-0.960`, `-0.308`, and `-0.270 V`, whose spacing is inconsistent with the neighbouring values and may contain a transcription error.
- The companion companded table contains only 11 rows and skips several code words.
- The exact linear/companded classification of every photograph has not yet been confirmed.

No corrected values will be invented. The hardcopy notes and Aaron’s recollection must be checked before graphs are treated as final evidence.

### What we learned and what we would change

The reduced attendance did not prevent progress because the pair took time to understand the decoding method, checked it with other people, and then separated measurement from recording. For the next session, the unresolved table entries and the laboratory-book questions should be checked while the equipment and process are still familiar.

### Answers to the remaining evidence questions

- **Attendance:** Nahil attended with me; the other two group members were sick.
- **Questionable linear values:** `-0.308 V` and `-0.270 V` are preserved exactly as typed, but no retained meter photograph verifies them. I have highlighted rather than altered them.
- **Companded record:** only 11 points survive. Codes 5, 6, 7, 8 and 10 are absent from the preserved class-data file.
- **Photograph grouping:** the meter readings confirm `67EAA...`, `FF32...`, `AA06...`, and `1B4E...` as Question 4.1 evidence; `7264...` and `E70F...` match Question 4.2. Both photographs near `-2.63 V` visibly include a minus sign.
- **Graphs and full answers:** [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Labbook - Answered Questions/Communication Engineering Labbook - Answered Questions.pdf|open the first-person answered-questions PDF]].

### Report-ready points

- The in-class photographs provide direct setup, voltage, and oscilloscope evidence.
- The method combined instruction checking, practice decoding, peer/lecturer confirmation, and divided measurement roles.
- The practical demonstrated discrete quantisation levels and code changes as the analogue input varied.

</details>

---

<details open>
<summary><strong>Week 4 — Lab 4 continued: PCM decoding and reconstruction</strong> · encoder/decoder data complete</summary>

## Week 4 — Lab 4 continued: PCM decoding and reconstruction

### Attendance and roles

Iyla, Amber, Nihil and I attended the second Lab 4 session. Iyla read ahead through the next tasks while Nihil and I connected the TIMS modules and continued the data collection. Amber was also present and supported the group as we worked through the experiment.

### Aim and preparation

Our aim was to continue from the PCM encoder work and connect the PCM Decoder so that we could compare the encoder input voltage with the decoder output for all 16 four-bit codes. We also observed the periodic message, decoded sample-and-hold output, reconstruction behaviour and FFT evidence.

### Equipment and setup

We used the TIMS-301 system with the PCM Encoder and PCM Decoder modules, Variable DC source, Master Signals clock, buffer/filter modules, Tektronix TDS2012C oscilloscope, digital multimeter and patch leads. Both PCM modules were operated in the four-bit linear mode. The decoder required the encoder PCM data, a matching clock and frame synchronisation before its output could be compared with the encoder input.

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/second week evidence/drive-download-20260813T032343Z-1-001/21E33F07-6AAB-465A-80C7-BD6228867B93.JPG|700]]

*Our second-week encoder/decoder setup after the additional connections had been made.*

### What we did

We initially had difficulty working out how the encoder and decoder should be connected. The number of clock, frame-sync, PCM-data, input, output and oscilloscope connections made it difficult to determine which leads belonged at each stage. We asked the lecturer for assistance, corrected the patching and then continued carefully through the remaining tasks.

For the DC transmission measurements, we varied the encoder input through all 16 four-bit code regions and recorded the encoder voltage and corresponding decoder voltage. We then observed the periodic-message waveforms and captured supporting oscilloscope and FFT photographs. Because we were still learning how the complete encoder/decoder chain worked, collecting and checking the data took the rest of the session.

### Encoder/decoder measurements

I calculated the error as

$$e=V_{decoder}-V_{encoder}.$$

| No. | $V_{encoder}$ (V) | $V_{decoder}$ (V) | Bit code | Error (V) |
|---:|---:|---:|:---:|---:|
| 1 | -2.668 | -2.530 | 0000 | +0.138 |
| 2 | -2.095 | -2.216 | 0001 | -0.121 |
| 3 | -1.913 | -1.902 | 0010 | +0.011 |
| 4 | -1.498 | -1.589 | 0011 | -0.091 |
| 5 | -1.275 | -1.273 | 0100 | +0.002 |
| 6 | -0.933 | -0.959 | 0101 | -0.026 |
| 7 | -0.639 | -0.646 | 0110 | -0.007 |
| 8 | -0.289 | -0.332 | 0111 | -0.043 |
| 9 | -0.008 | -0.016 | 1000 | -0.008 |
| 10 | 0.325 | 0.297 | 1001 | -0.028 |
| 11 | 0.625 | 0.611 | 1010 | -0.014 |
| 12 | 0.955 | 0.924 | 1011 | -0.031 |
| 13 | 1.275 | 1.240 | 1100 | -0.035 |
| 14 | 1.592 | 1.553 | 1101 | -0.039 |
| 15 | 1.919 | 1.867 | 1110 | -0.052 |
| 16 | 2.233 | 2.181 | 1111 | -0.052 |

The mean absolute error was **0.0436 V**, the RMSE was **0.0585 V**, and the mean signed error was **−0.0248 V**. The largest absolute difference was **0.138 V** at code `0000`. A linear fit gave

$$V_{decoder}=0.9886V_{encoder}-0.0265\text{ V},\qquad R^2=0.99879.$$

The high $R^2$ and slope close to one show that the decoder output followed the encoder input closely across the measured range, although the decoder generally had a small negative offset and the largest endpoint errors occurred at the negative end.

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/second week evidence/analysis/lab4_week2_encoder_decoder_transfer.png|760]]

*Measured encoder-to-decoder transfer compared with the ideal one-to-one relationship.*

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/second week evidence/analysis/lab4_week2_levels_by_code.png|760]]

*Encoder and decoder voltage levels for all 16 four-bit codes.*

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/second week evidence/analysis/lab4_week2_decoder_error.png|760]]

*Decoder error for each code, calculated without changing the collected values.*

### Oscilloscope evidence and observations

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/second week evidence/drive-download-20260813T032343Z-1-001/039C2806-340B-44CC-B954-6D36F873DAF4.JPG|700]]

*Periodic analogue message and PCM data. The scope reports approximately 259.1 Hz for the analogue waveform and about 3.52 V peak-to-peak.*

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/second week evidence/drive-download-20260813T032343Z-1-001/71F277D7-828B-4647-A938-C01A4409C042.JPG|700]]

*Periodic message and the quantised/decoded waveform, showing how the continuously varying message was represented by discrete output levels.*

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 4/Lab 4 Class Documents/second week evidence/drive-download-20260813T032343Z-1-001/966FE682-7AF7-4B6B-983C-4C8790D9CEF3.JPG|700]]

*FFT-mode evidence retained from the reconstruction/distortion part of the session. A small set of spectral peaks is visible, but exact harmonic amplitudes were not written down, so I have not invented numerical distortion values.*

The photographs also include sample-and-hold and reconstruction traces at several time scales. Together they support that we progressed beyond the encoder-only measurements and operated the encoder, decoder and filtering stages as a connected system.

### Photograph-to-result notes

| Photograph | Visible evidence | Interpretation |
|---|---|---|
| `17F30...JPG` | TIMS encoder/decoder patching; meter appears near `-0.629 V` | setup evidence; near the code `0110` region but not an exact match to the typed pair |
| `20FE...JPG` | alternate patching view; meter appears near `-0.330 V` | setup evidence; close to the recorded decoder value `-0.332 V` for code `0111` |
| `4880...JPG` | meter approximately `-2.628 V` with digital traces | negative-end operating evidence; not an exact match to either typed endpoint value |
| `56CE...JPG` | meter approximately `-1.498 V` with digital traces | directly supports the encoder value for code `0011` |
| `B2F3...JPG` | meter approximately `-0.473 V` with filter/sample trace | another experiment stage; not forced into the 16-row table |
| `BBA3...JPG` | meter approximately `+1.592 V` with digital traces | directly supports the encoder value for code `1101` |

The original full-resolution photographs remain the primary evidence. Meter values in the table above were read from the photographs individually; where a photograph did not match a collected row exactly, I kept it as setup or operating evidence rather than changing the supplied data.

### Problems, troubleshooting and lecturer guidance

The main difficulty was understanding the complete connection path between the PCM Encoder and PCM Decoder. We knew the individual signals existed, but translating the instructions into the correct physical patching was not immediate. Assistance from the lecturer helped us correct the encoder/decoder connections and continue. The session reinforced that checking the coding mode, shared clock, frame synchronisation, PCM-data path and measurement points in a fixed order is more reliable than moving several leads at once.

### What I learned and what I would change

I learned that the decoder output closely follows the encoder input but remains quantised and includes small measurement/reconstruction errors. I also learned that understanding the signal path takes time when several modules are connected. If I repeated the work, I would draw the required connection chain before patching, label each lead by function, verify one signal at a time with the oscilloscope, and record the purpose and settings beside every photograph while the equipment was still connected.

### Primary in-class evidence

The 16 original second-week photographs are preserved in:

`Lab 4 Class Documents/second week evidence/drive-download-20260813T032343Z-1-001/`

They include:

- two complete TIMS patching views (`17F30...`, `20FE...`, `21E33...`);
- meter-and-scope operating photographs (`4880...`, `56CE...`, `B2F3...`, `BBA3...`);
- periodic-message and PCM traces (`039C...`, `6E8F...`, `71F2...`, `84A6...`, `95CE...`);
- sample-and-hold/reconstruction traces (`5C87...`, `C5EA...`, `CE4D...`);
- FFT evidence (`966F...`).

### Report-ready points

- Our second Lab 4 session completed the 16 encoder/decoder voltage pairs.
- The measured transfer was close to one-to-one: slope `0.9886`, intercept `−0.0265 V`, and $R^2=0.99879$.
- The mean absolute encoder/decoder difference was `0.0436 V`.
- We needed lecturer assistance to resolve the encoder/decoder patching, and understanding the full system took most of the session.
- The photographs provide direct evidence of the complete patching, PCM/digital waveforms, periodic message, quantised reconstruction and FFT stage.

</details>

---

<details open>
<summary><strong>Week 5 — Lab 3: Binary phase-shift keying</strong> · evidence and questions added</summary>

## Week 5 — Lab 3: Binary phase-shift keying

### Attendance and roles

*** Confirm who attended, how the work was divided, and whether the oscilloscope date of 13 August 2026 matches the class session date.

### Aim and setup

We used the TIMS equipment to generate and recover a BPSK signal. The visible setup contains the Audio Oscillator, Sequence Generator, Line-Code Encoder, transmitter Multiplier, Phase Shifter, receiver Multiplier, Tuneable LPF, Decision Maker and Line-Code Decoder. The carrier was multiplied by bipolar NRZ-L data, so a data-polarity change produced a carrier phase reversal. The receiver used a synchronous carrier, low-pass filtering and a decision stage to recover data-related signals.

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Labbook - Labs 1-5/figures/lab3_full_setup.jpg|760]]

*Selected full setup photograph. The duplicate and poorly framed photographs remain preserved in Downloads but are not repeated as independent evidence.*

### What we examined

- the BPSK carrier relationship to a binary sequence and the shape of phase transitions;
- the effect of transmitter low-pass-filter bandwidth on transition shape and amplitude;
- the demodulator low-pass-filter output relative to the transmitted sequence;
- receiver carrier-phase ambiguity and the purpose of the 180-degree phase switch;
- the Decision Maker and digital/line-code-related outputs.

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Labbook - Labs 1-5/figures/lab3_bpsk_phase_transitions.jpg|620]]

*High-frequency carrier-like waveform against the binary sequence. The display shows 20.0 V/div and 50.0 V/div, 10.0 ms/div, and a selected-channel frequency readout near 18.99 Hz.*

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Labbook - Labs 1-5/figures/lab3_recovered_bandlimited_waveform.jpg|620]]

*A smooth filtered/recovered analogue waveform compared with the rectangular binary sequence. The exact probe point was not recorded, so the caption remains conservative.*

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Labbook - Labs 1-5/figures/lab3_bandlimited_transition.jpg|620]]

*Band-limited transition evidence: the rectangular sequence is accompanied by a rounded, ringing analogue trace. The photograph supports the visible transition shape, but not an exact filter setting or probe-point assignment.*

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Labbook - Labs 1-5/figures/lab3_digital_comparison.jpg|620]]

*Two-channel digital comparison on a Tektronix TDS 2012C: a slower rectangular trace is shown above a denser digital-related trace. The visible display reports 5.00 V/div on both channels and 50.0 ms/div; channel identity and precise probe mapping are not treated as established beyond the labels shown.*

### Manual questions and answers

1. **Is BPSK analogue?** The transmitted signal is a continuous-time analogue carrier whose phase is selected by digital data. It is a digitally modulated analogue waveform.
2. **Why set the transmitter multiplier to DC?** DC coupling preserves the bipolar NRZ levels and long constant runs. AC coupling would introduce droop and distort the phase-selection signal.
3. **Does the receiver phase shifter change the transmitted spectrum?** No. It changes coherent-demodulator polarity/amplitude, not the magnitude spectrum of the signal already transmitted.
4. **Does a sub-multiple bit rate remove bandwidth?** No. The harmonic relationship makes transitions repeat at predictable carrier phases, but occupied bandwidth is still governed mainly by bit rate and pulse shaping.
5. **Why use the demodulator LPF?** It retains the baseband data term while rejecting the product near twice the carrier frequency and excess noise. Its bandwidth balances transition fidelity, intersymbol interference and rejection.
6. **Why can narrower transmitter bandwidth increase a measured peak?** Filtering changes the phase and cancellation of spectral components and can create ringing or overshoot. A single instantaneous peak can therefore grow even when total passed bandwidth falls.

### Evidence boundary

Sixteen images were supplied. Exact duplicates were found for `Image.jpeg`/`Image(1).jpeg` and `Image(3).jpeg`/`Image(4).jpeg`. Five representative images were normalized for the PDF without modifying the originals. The exact probe mapping for some filtered and digital traces was not written down, so those images are used only for the features they visibly demonstrate.

### Weekly note

- **What we achieved:** built and observed the BPSK transmitter/receiver chain and examined filtering, phase-related and digital-related signals.
- **What was difficult:** ***
- **What I learned:** BPSK carries bits through carrier phase, while coherent recovery depends on receiver phase, filtering and the decision threshold.
- **What I would change:** label every probe point and write the scope settings beside each photograph during the session.

The ordered, presentable Labs 1–5 PDF is [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Labbook - Labs 1-5/Communication Engineering Labbook - Labs 1-5.pdf|Communication Engineering Labbook — Labs 1–5]].

</details>

---

## Source preservation

The original raw note remains at [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Weekly Logbook for Communications Labs.txt|Weekly Logbook for Communications Labs.txt]]. This Markdown file is the organised running version; the raw note should remain preserved for comparison.
