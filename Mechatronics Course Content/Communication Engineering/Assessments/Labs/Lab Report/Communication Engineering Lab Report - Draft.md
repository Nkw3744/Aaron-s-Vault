---
course: ENEL700 Communication Engineering
assessment: Laboratory Report
status: running-candidate-draft
student: Aaron Taylor
selected_labs: pending-comparison
required_labs_in_report: 3
required_labs_in_logbook: 4
due: 2026-10-02 15:00 NZST
last_updated: 2026-08-02
---

# ENEL700 Communication Engineering Laboratory Report — Running Draft

**Student:** Aaron Taylor  
**Team members:** Nahil, Iyla, Amber, and Aaron Taylor  
**Required final selection:** Three laboratories  
**Current candidate sections:** Lab 5 — Amplitude Modulation; Lab 4 — Pulse-Code Modulation  
**Submission:** 2 October 2026, 3:00 pm NZST

> [!important] Evidence hierarchy
> The group’s files in each **Class Documents** folder are the primary record of what was actually completed in class. Aaron’s weekly account is the primary source for the team process. Manual reconstructions and later MATLAB replications may explain or check the results, but they must not be presented as the group’s in-class work.

> [!note] Running-draft purpose
> A candidate section will be drafted for every completed laboratory. The strongest three will be selected only after all four have comparable evidence, analysis, and personal reflection. Dropdowns are for managing this working file and will be flattened for the formal submission.

[[Communication Engineering Lab Report - Draft.html|Open the standalone HTML draft]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Weekly Labbook|Open the running weekly labbook]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/ENEL700 Lab Book 2026.pdf|Laboratory manual]]

## Report development dashboard

| Candidate laboratory | In-class technical evidence | Team/process account | Main unresolved work | Current strength |
|---|---|---|---|---|
| Lab 5 — Amplitude Modulation | Class `.slx`, `.mat`, `.fig`, workspace capture, and four spectrum screenshots | Weeks 1–2 recorded | Identify the decisive plotting fix and confirm final Scope observation | Strong |
| Lab 4 — Pulse-Code Modulation | Two weeks of PCM bench evidence, complete encoder/decoder patching, 16 voltage pairs, verified graphs, periodic-message/reconstruction traces and FFT photograph | Weeks 3–4 recorded | Earlier quantisation transcription still has two unusual values and an incomplete companded sequence; harmonic amplitudes were not recorded | Strong |
| Candidate laboratory 3 | Not yet added | Not yet added | Complete future laboratory | Pending |
| Candidate laboratory 4 | Not yet added | Not yet added | Complete future laboratory | Pending |

## Draft abstract

*Complete after the final three laboratories are selected. The abstract will summarise the shared purpose, actual methods, most important measured results, principal comparison, and overall conclusions in approximately 150–250 words.*

## 1. Introduction

The ENEL700 laboratory programme develops practical understanding of communication signals by combining software modelling, frequency-domain analysis, physical training equipment, and oscilloscope measurements. This running report currently develops two candidate studies. Lab 5 investigates double-sideband suppressed-carrier amplitude modulation using MATLAB and Simulink. Lab 4 investigates pulse-code modulation by relating analogue input voltage to discrete binary code words and oscilloscope frames.

The final report will contain three selected laboratories. Selection will be based on the quality of the group’s in-class evidence, the strength of the connection between theory and observed results, and the completeness of the group’s technical and reflective account.

## 2. Team organisation and working method

The team consisted of Nahil, Iyla, Amber, and Aaron. During the first two sessions, all four members worked on Lab 5 and rotated the computer role so that each person gained direct experience with MATLAB. While one member operated the computer, the others read the next instructions, checked entered code, researched the communication-engineering context, or looked ahead to the next required step.

This arrangement shared participation, but the single-computer environment made troubleshooting difficult. During the second session, several members developed possible fixes for the plotting problem and changes occasionally replaced one another before the earlier code had been fully diagnosed. The group eventually completed the work, but the experience showed the value of preserving a known baseline and making one agreed change at a time.

The first Lab 4 session was completed by Aaron and Nahil because two members were sick. The pair first asked the lecturer and classmates for enough context to understand how to align and decode the PCM frame. They practised the interpretation method, checked it against other students, and then divided the task between finding each result and recording the voltage/code pair. In the second Lab 4 session, Iyla, Amber, Nihil and Aaron attended. Iyla read ahead while Nihil and Aaron set up the encoder/decoder chain and continued data collection. Lecturer assistance resolved uncertainty in the physical patching, after which the group completed all 16 encoder/decoder voltage pairs and the later reconstruction/FFT observations.

---

<details open markdown="1">
<summary><strong>Candidate Lab 5 — Amplitude Modulation</strong> · strong in-class evidence</summary>

## 3. Candidate Lab 5 — Amplitude Modulation

### 3.1 Objective

The objective was to construct a double-sideband suppressed-carrier amplitude-modulation model, inspect the time-domain output, and compare the frequency spectra of the message, carrier, and modulated signal. The practical also introduced the group to entering MATLAB code, constructing a Simulink model, saving the output to the workspace, and arranging multiple spectra in one figure.

### 3.2 Theory

For message signal \(m[n]\) and carrier \(c[n]\), the modulated output is

\[
s[n] = m[n]c[n].
\]

The saved class Simulink model uses a sinusoidal carrier with unit amplitude, normalized frequency \(f_c=0.3\), phase \(\pi/2\), and sample time 1:

\[
c[n] = \sin\!\left(2\pi(0.3)n+\frac{\pi}{2}\right).
\]

Multiplication shifts the message spectrum from baseband to regions around the positive and negative carrier frequencies. For ideal DSB-SC modulation, the translated message spectrum appears around \(f=\pm 0.3\), while a separate unsuppressed carrier line is not expected in the modulated output.

### 3.3 Actual in-class method

The group followed the laboratory instructions collaboratively over two sessions. In the first session, members rotated through the computer role while the others read code and instructions aloud, checked entries, researched the purpose of the signals, and prepared the next step. The group reached the spectrum-comparison task but did not produce the required three vertically stacked plots before the session ended.

In the second session, the group continued from that problem. Early debugging was scattered because different members proposed changes through one shared screen, and code was occasionally deleted or reset before the previous version had been diagnosed. The group eventually completed the laboratory and preserved the class model, data, editable figure, workspace capture, and spectrum screenshots together.

The saved in-class model `lab5part2.slx` directly records the following chain:

1. `Signal From Workspace`, using `bumps'`;
2. a discrete Sine Wave block with frequency `2*pi*0.3`, phase `pi/2`, and sample time `1`;
3. a Product block multiplying the message and carrier;
4. a Scope connected to the Product output;
5. a To Workspace block saving the result as `am`.

This model structure supports the group’s account that the message and carrier were multiplied in Simulink and that the output was both viewed and saved for MATLAB analysis.

### 3.4 Primary in-class results

#### Three-spectrum comparison

The clearest retained class screenshot is labelled **Modulating signal**, **carrier**, and **Modulated signal**. All three horizontal axes show normalized frequency from approximately `-0.5` to `+0.5`, and the vertical axes show magnitude in decibels.

![In-class Lab 5 result: modulating signal, carrier, and modulated signal spectra.](<../Lab 5/Lab 5 Class Documents/Screenshot 2026-07-23 184430.png>)

The modulating signal is centred at zero normalized frequency. The carrier plot has dominant components near `-0.3` and `+0.3`. The modulated-signal plot contains translated spectral content around the same positive and negative carrier frequencies. This visible displacement from baseband is consistent with the expected effect of multiplying the message by the carrier.

The class folder contains three earlier screenshots from the same period. They show alternate or intermediate plotting states and are preserved as troubleshooting evidence rather than treated automatically as additional final results:

- `Screenshot 2026-07-23 184310.png`
- `Screenshot 2026-07-23 184343.png`
- `Screenshot 2026-07-23 184421.png`

#### Workspace state

![In-class MATLAB workspace showing the variables retained during Lab 5.](<../Lab 5/Lab 5 Class Documents/image.png>)

The workspace capture records variables including `am`, `AM`, `bump`, `bumps`, `DB`, `f`, `NFFT`, `out`, `required`, and `v`. It is useful corroborating evidence that the signal and spectrum calculations were present in the class workspace, although the labelled three-spectrum screenshot is the stronger main report figure.

### 3.5 Discussion

The final class spectra show the central principle of DSB-SC modulation. The message begins at baseband, whereas the modulated signal appears around the selected carrier frequency on both sides of the spectrum. The visible symmetry about zero frequency is expected for the spectrum of a real-valued signal.

The practical also demonstrated that validation requires more than obtaining a MATLAB figure. The group had to check the subplot titles, ordering, normalized-frequency range, and expected peak locations. The saved screenshot at 18:44:30 is currently the clearest evidence because all three plots are labelled and their relationships can be compared directly.

The largest process difficulty was collaborative debugging through one computer. Working on several possible fixes at once caused changes to overlap. A better method would have been to save the starting version, agree on one suspected cause, make one change, run the code, and record the effect before proceeding.

### 3.6 Supporting numerical check performed later

A later, separate MATLAB reproduction used the manual’s 5,000-sample message, carrier frequency 0.3, and point-by-point multiplication. It measured an output-spectrum peak at normalized frequency `0.300003` and a sideband/message peak ratio of `0.498366`, close to the theoretical value `0.5`. The measured logarithmic difference was `-3.0245 dB`, close to the expected `-3.01 dB`.

These values strengthen the theoretical interpretation of the class screenshot, but they are **supporting analysis performed later**, not a substitute for the group’s in-class files.

Detailed later evidence: [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Report/Lab 5 - MATLAB Replication Report|Lab 5 MATLAB replication report]].

### 3.7 Personal and team reflection

Rotating the computer role gave every member practical experience and kept the group involved. Reading code aloud and checking entries meant that members away from the keyboard still contributed. The group’s main weakness was allowing several people’s debugging ideas to compete through one shared code state. The eventual completion was useful, but preserving versions and testing one change at a time would have made the process faster and easier to explain.

### 3.8 Provisional conclusion

The in-class Simulink model and labelled spectrum screenshot support successful DSB-SC modulation. The saved model multiplies the workspace message by a sinusoid at normalized frequency 0.3, and the class spectrum shows the message content translated from zero frequency to regions around `±0.3`. The practical met its main technical purpose and also provided a clear lesson in controlled collaborative troubleshooting.

### 3.9 Questions for Aaron

1. What exact code or plotting change finally fixed the three vertically stacked spectra?
2. Did the lecturer or another student identify the decisive fix?
3. What did the final Scope display show, and how did the group use it to check the model?

### 3.10 Selection strength

**Current assessment:** Strong candidate. It has a saved class model, class data, a clear final spectrum screenshot, an editable figure, a workspace capture, two weeks of process narrative, and independent later verification. The main missing element is the precise final troubleshooting step and Scope observation.

</details>

---

<details open markdown="1">
<summary><strong>Candidate Lab 4 — Pulse-Code Modulation</strong> · strong two-session in-class evidence</summary>

## 4. Candidate Lab 4 — Pulse-Code Modulation

### 4.1 Objective

The objective was to use the TIMS PCM equipment to investigate how an analogue input is sampled and represented as a serial binary word. The class work focused on understanding the PCM frame, identifying the four data bits on the oscilloscope, varying the DC input, and recording the voltages at which the code changed.

### 4.2 Relevant theory

A four-bit encoder can represent

\[
2^4=16
\]

quantisation levels. The analogue input range is divided into regions, and every input within one region is represented by the same four-bit code. As the input voltage passes a transition, the output word changes to the next code.

The TIMS PCM frame contains eight clock slots. In four-bit mode, the four data bits occupy the designated data slots while the remaining frame positions provide unused or synchronization functions. Interpreting the result therefore required the group to align the oscilloscope trace with the frame diagram before reading the code word.

### 4.3 Actual in-class method

Only Aaron and Nahil attended because the other members were sick. The pair did not immediately begin collecting numbers. They first asked the lecturer and classmates about the purpose of the experiment and the correct way to read the PCM frame. They practised decoding examples and checked their interpretation with classmates.

Once they were confident about the relevant bit positions, they divided the work. One person varied the voltage and identified each result while the other recorded the meter reading and bit code. The folder `Lab 4 Class Documents` is the primary record of this work and contains the equipment photographs, PCM Encoder patching, annotated instruction page, meter values, and oscilloscope traces.

#### In-class setup

![TIMS-301 system used during the Lab 4 PCM class.](<../Lab 4/Lab 4 Class Documents/IMG_2377_Original.jpeg>)

![Close in-class view of the PCM Encoder area and patch leads.](<../Lab 4/Lab 4 Class Documents/1FB5A1C1-D1E0-4F62-9F98-16C1D8678FEE.JPG>)

The full bench photograph establishes the TIMS hardware used. The closer photograph records the actual encoder area and patch leads. These are setup evidence; the meter-and-oscilloscope photographs below are stronger evidence for the measured results.

#### Decoding aid used in class

![Annotated Lab 4 instruction page used to identify the PCM frame and four-bit word.](<../Lab 4/Lab 4 Class Documents/341F0719-8146-4629-B6DB-A01E5C1A1658.JPG>)

The annotated page supports Aaron’s account that the pair first learned and practised the decoding method before gathering the voltage/code table.

### 4.4 Primary in-class results

The class photographs provide direct visual evidence for several voltage/code points. The associated code is taken from the companion recorded table where the visible voltage matches the recorded value.

| Photograph | Visible voltage | Recorded four-bit code | Interpretation |
|---|---:|:---:|---|
| `67EAA729-D418-4075-803C-5A2196C63CE8.JPG` | approximately `-2.634 V` | `0000` | negative endpoint |
| `FF32F2C8-BDB9-4C5F-9F25-CADB0F6287D0.JPG` | approximately `-2.240 V` | `0001` | next transition/region |
| `AA06F6D9-ACAF-449A-AC36-30C4613A34A1.JPG` | approximately `-1.911 V` | `0010` | next recorded code |
| `1B4E24ED-F867-4D86-AD97-58DBCAEFD16C.JPG` | approximately `-1.595 V` | `0011` | next recorded code |
| `726424E8-03E2-4DB9-B0B7-DE1336643C03.JPG` | approximately `-2.633 V` | `0000` | matches the negative start of Question 4.2 |

![In-class PCM measurement near −2.634 V with its oscilloscope trace.](<../Lab 4/Lab 4 Class Documents/67EAA729-D418-4075-803C-5A2196C63CE8.JPG>)

![In-class PCM measurement near −1.595 V with its oscilloscope trace.](<../Lab 4/Lab 4 Class Documents/1B4E24ED-F867-4D86-AD97-58DBCAEFD16C.JPG>)

![A second in-class PCM measurement near −2.633 V with a different oscilloscope trace, matching the start of Question 4.2.](<../Lab 4/Lab 4 Class Documents/726424E8-03E2-4DB9-B0B7-DE1336643C03.JPG>)

Together, these photographs show the analogue input being associated with different discrete pulse patterns. The two photographs near `-2.63 V` have different traces and match the negative start values recorded for Questions 4.1 and 4.2. The positive endpoint at `+2.633 V` is present in the companion table but is not currently matched to a class photograph.

### 4.5 Companion recorded data

The following values are preserved exactly as written in `Lab4 Recorded Data.txt`. They are included as a working transcription, not silently corrected.

#### Question 4.1 — recorded sequence

| No. | Voltage (V) | Bit code | Status |
|---:|---:|:---:|---|
| 1 | -2.635 | 0000 | supported by class photograph near -2.634 V |
| 2 | -2.239 | 0001 | supported by class photograph near -2.240 V |
| 3 | -1.911 | 0010 | supported by class photograph |
| 4 | -1.595 | 0011 | supported by class photograph |
| 5 | -1.277 | 0100 | recorded; photo mapping not yet established |
| 6 | -0.960 | 0101 | recorded; photo mapping not yet established |
| 7 | -0.308 | 0110 | **check against hardcopy** |
| 8 | -0.270 | 0111 | **check against hardcopy** |
| 9 | -0.020 | 1000 | recorded; photo mapping not yet established |
| 10 | 0.296 | 1001 | recorded; photo mapping not yet established |
| 11 | 0.645 | 1010 | recorded; photo mapping not yet established |
| 12 | 0.840 | 1011 | recorded; photo mapping not yet established |
| 13 | 1.314 | 1100 | recorded; photo mapping not yet established |
| 14 | 1.608 | 1101 | recorded; photo mapping not yet established |
| 15 | 2.062 | 1110 | recorded; photo mapping not yet established |
| 16 | 2.633 | 1111 | recorded; positive-end photo mapping not yet established |

The jump from `-0.960 V` to `-0.308 V`, followed by only `0.038 V` to `-0.270 V`, is inconsistent with the approximate spacing visible elsewhere in the sequence. This may be a real recording issue or a transcription mistake. It must be checked rather than corrected by assumption.

#### Question 4.2 — recorded sequence

| No. | Voltage (V) | Bit code | Status |
|---:|---:|:---:|---|
| 1 | -2.632 | 0000 | supported by class photograph near -2.633 V |
| 2 | -1.100 | 0001 | supported by class photograph near -1.100 V |
| 3 | -0.522 | 0010 | recorded |
| 4 | -0.291 | 0011 | recorded |
| 5 | -0.154 | 0100 | recorded |
| 6 | -0.003 | 1001 | missing intermediate codes; check |
| 7 | -0.072 | 1011 | order/value should be checked |
| 8 | 0.217 | 1100 | recorded |
| 9 | 0.308 | 1101 | recorded |
| 10 | 0.809 | 1110 | recorded |
| 11 | 1.272 | 1111 | recorded |

This sequence contains only 11 rows and omits several code words. A final companding plot and numerical comparison will not be certified until the hardcopy notes or additional class evidence confirms whether the sequence is complete.

### 4.6 Second in-class session — decoder and reconstruction

The group returned for a second Lab 4 session with Iyla, Amber, Nihil and Aaron present. Iyla read ahead through the next tasks while Nihil and Aaron set up the PCM Encoder and PCM Decoder and continued collecting data. The group initially had difficulty translating the instructions into the complete physical patching. Lecturer assistance helped them correct the clock, frame-synchronisation, PCM-data and measurement connections. Understanding the full system and collecting the complete dataset took the remainder of the session.

The second-week folder is primary in-class evidence and contains 16 photographs of the TIMS patching, meter and scope readings, periodic-message/PCM traces, sample-and-hold or reconstruction traces, and FFT mode.

![Second-week TIMS PCM Encoder and Decoder patching.](<../Lab 4/Lab 4 Class Documents/second week evidence/report-ready/21E33F07-6AAB-465A-80C7-BD6228867B93-normalized.jpg>)

#### Encoder/decoder data

The measured decoder error is defined as **e = Vdecoder − Vencoder**.

| No. | Venc (V) | Vdec (V) | Code | Error (V) |
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

![Measured encoder-to-decoder transfer and ideal one-to-one line.](<../Lab 4/Lab 4 Class Documents/second week evidence/analysis/lab4_week2_encoder_decoder_transfer.png>)

![Encoder and decoder voltage levels for each four-bit code.](<../Lab 4/Lab 4 Class Documents/second week evidence/analysis/lab4_week2_levels_by_code.png>)

![Decoder error calculated for each four-bit code.](<../Lab 4/Lab 4 Class Documents/second week evidence/analysis/lab4_week2_decoder_error.png>)

The mean absolute error was `0.0436 V`, the RMSE was `0.0585 V`, and the mean signed error was `-0.0248 V`. The maximum absolute error was `0.138 V` at code `0000`. Linear regression gave

\[
V_{decoder}=0.9886V_{encoder}-0.0265\text{ V},\qquad R^2=0.99879.
\]

This close-to-unity slope and high coefficient of determination show that the decoder tracked the encoder input closely over the measured range. The small negative intercept and predominantly negative errors show a slight downward bias, while the two largest discrepancies occurred at the negative end.

#### Periodic message, reconstruction and FFT evidence

![Periodic analogue message and PCM data; the scope reports approximately 259.1 Hz and 3.52 V peak-to-peak for the analogue waveform.](<../Lab 4/Lab 4 Class Documents/second week evidence/report-ready/039C2806-340B-44CC-B954-6D36F873DAF4-normalized.jpg>)

![Periodic message and quantised/decoded output.](<../Lab 4/Lab 4 Class Documents/second week evidence/report-ready/71F277D7-828B-4647-A938-C01A4409C042-normalized.jpg>)

![FFT-mode evidence from the reconstruction/distortion stage.](<../Lab 4/Lab 4 Class Documents/second week evidence/report-ready/966FE682-7AF7-4B6B-983C-4C8790D9CEF3-normalized.jpg>)

The FFT photograph contains visible spectral peaks but no written harmonic-amplitude readings. It supports that the FFT stage was reached, but it does not justify invented second- or third-harmonic distortion values.

Full-resolution checks found direct photographic support for the encoder readings near `-1.498 V` and `+1.592 V`. Other visible meter readings near `-0.629 V`, `-0.330 V`, `-2.628 V`, and `-0.473 V` are retained as setup or operating evidence where they do not exactly match a typed row. The supplied 16-row dataset remains unchanged.

### 4.7 Discussion

The first session demonstrated encoder quantisation and established a method for reading four-bit PCM words. The second session extended this evidence to the complete encoder-to-decoder chain. The decoder produced discrete output levels corresponding closely to the encoder input regions, confirming that the binary PCM words could be converted back into proportional analogue levels. The remaining voltage errors are consistent with finite quantisation, endpoint behaviour and practical module/measurement offsets.

The second-week periodic-message photographs make the sample-and-hold behaviour more visible than the DC measurements. A continuously varying input is represented by a stepped or held decoder output. The reconstruction and FFT photographs show that the group progressed to filtering and frequency-domain inspection, although the available evidence is qualitative for harmonic distortion.

The strongest process feature across both sessions was the group's willingness to pause and understand the signal path rather than record unexplained numbers. In the first session Aaron and Nahil learned how to read the PCM frame. In the second session Iyla, Amber, Nihil and Aaron worked through the larger encoder/decoder system, using lecturer assistance when the physical patching was unclear.

### 4.8 Limitations and evidence boundary

- Both weeks' original meter-and-oscilloscope photographs are primary in-class evidence.
- The new 16-row encoder/decoder dataset is complete and has been graphed exactly as supplied.
- The first-week `Lab4 Recorded Data.txt` still contains unresolved linear and companded entries; the second-week decoder table does not silently correct that earlier table.
- Several second-week meter photographs are operating snapshots rather than exact matches to a typed row and have not been forced into the table.
- FFT mode is photographed, but exact harmonic amplitudes were not recorded; only a qualitative distortion discussion is justified.
- `Communication Engineering Lab 4.md` remains a manual-based preparation and interpretation note.
- `Lab 4 answers Kane.pdf` remains peer comparison material and is not Aaron's evidence or wording.
- `IMG_2379_Original.jpeg` remains excluded because it is unrelated ENEL800 material.

### 4.9 Personal and team reflection

In the first Lab 4 session, reduced attendance meant Aaron and Nahil had to learn the decoding method and divide the measurement roles carefully. In the second session, Iyla read ahead while Nihil and Aaron concentrated on the setup and data collection, with Amber present to support the group. The larger setup was still difficult because the encoder and decoder required several coordinated connections. Lecturer assistance was important in moving the group past that blocker.

The key improvement for future work is to draw and label the entire signal path before patching: source, encoder input, shared clock, frame synchronisation, PCM-data link, decoder output, filter and oscilloscope channels. Verifying one signal at a time would reduce the time spent diagnosing several simultaneous connections. Recording the purpose and scope settings beside each photograph would also make the later evidence mapping faster and more precise.

### 4.10 Provisional conclusion

Across two in-class sessions, the group completed both encoder quantisation and encoder-to-decoder transmission work. The first-week photographs show voltage-dependent four-bit PCM patterns. The second-week data show that all 16 decoded levels tracked the encoder input closely, with a fitted slope of `0.9886`, an intercept of `-0.0265 V`, and R² = `0.99879`. Periodic-message, stepped-output, reconstruction and FFT photographs provide further evidence that the complete PCM chain was operated. The remaining limitations are confined to the earlier ambiguous quantisation transcription and the lack of numerical harmonic readings.

### 4.11 Selection strength

**Current assessment:** Strong candidate. Lab 4 now has evidence from two sessions, complete encoder/decoder voltage data, verified graphs, physical patching photographs, periodic-message and reconstruction traces, FFT-stage evidence, and a clear first-person troubleshooting narrative. Its remaining uncertainties are explicitly separated from the verified second-week dataset.

</details>

---

<details markdown="1">
<summary><strong>Candidate Laboratory 3</strong> · ready for the next completed lab</summary>

## 5. Candidate Laboratory 3 — To be added

### Objective

*Add from the actual class task.*

### Actual team method

*Build from the weekly logbook and the in-class folder.*

### Results and selected figures

*Use the class measurements, traces, screenshots, data, or code first.*

### Discussion and reflection

*Explain what the group observed, how the result was checked, what went wrong, and what was learned.*

### Evidence boundary

*Separate class evidence from later calculations or replications.*

</details>

<details markdown="1">
<summary><strong>Candidate Laboratory 4</strong> · ready for the final completed lab</summary>

## 6. Candidate Laboratory 4 — To be added

### Objective

*Add from the actual class task.*

### Actual team method

*Build from the weekly logbook and the in-class folder.*

### Results and selected figures

*Use the class measurements, traces, screenshots, data, or code first.*

### Discussion and reflection

*Explain what the group observed, how the result was checked, what went wrong, and what was learned.*

### Evidence boundary

*Separate class evidence from later calculations or replications.*

</details>

## 7. Laboratory selection matrix

The final three should not be selected until all four candidate sections are drafted to a similar depth.

| Criterion | Lab 5 | Lab 4 | Candidate 3 | Candidate 4 |
|---|---:|---:|---:|---:|
| Primary in-class evidence | Strong | Strong: two sessions, complete decoder table, setup/scope photographs and FFT evidence | — | — |
| Technical result clarity | Strong | Strong for the second-week encoder/decoder run; earlier companding data still limited | — | — |
| Theory-to-result connection | Strong | Strong | — | — |
| Team/process detail | Strong | Strong: attendance, roles and lecturer assistance recorded | — | — |
| Troubleshooting/reflection | Strong | Strong | — | — |
| Effort to make submission-ready | Low–moderate | Low–moderate | — | — |

## 8. Overall discussion

*Complete after the final three laboratories are selected. Compare how modelling, physical measurement, time-domain traces, and frequency-domain plots developed the group’s understanding. Distinguish results obtained in class from later checks.*

## 9. Team reflection

The team’s experience so far shows different forms of practical collaboration. Lab 5 involved the full group around one computer, creating broad participation but also competing code changes. The first Lab 4 session involved Aaron and Nahil, making communication simpler but reducing available roles. The second Lab 4 session included Iyla, Amber, Nihil and Aaron; Iyla read ahead while Nihil and Aaron concentrated on setup and data collection. In every case, progress improved when the team agreed on the interpretation or signal path before gathering or presenting results.

The strongest improvement for future sessions is to preserve a starting version or raw record, make one change at a time, and label evidence immediately. This reduces the risk of overwriting code, losing measurement context, or reaching the report stage with photographs that cannot be mapped confidently to a result.

## 10. Conclusion

*Complete after all candidate sections are drafted and the final three are selected. Summarise the principal technical findings and the most important development in the group’s experimental and troubleshooting process.*

## References

1. Auckland University of Technology, *ENEL700 Communication Engineering Laboratory Manual*, 2026.
2. Lab 5 in-class files, `Assessments/Labs/Lab 5/Lab 5 Class Documents/`, created 23 July 2026.
3. Lab 4 in-class photographs, `Assessments/Labs/Lab 4/Lab 4 Class Documents/`, 2026.
4. Aaron Taylor, *ENEL700 Communication Engineering — Weekly Laboratory Logbook*, running 2026 record.
5. Supporting later analysis: [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Report/Lab 5 - MATLAB Replication Report|Lab 5 MATLAB Replication Report]].

## Appendices and evidence register

### Appendix A — Running weekly logbook

See [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Communication Engineering Weekly Labbook|Communication Engineering Weekly Labbook]]. The hardcopy requirement remains in force unless confirmed otherwise by the lecturer.

### Appendix B — Lab 5 primary class files

- `lab5part2.slx`
- `lab5final.mat`
- `finalgragh.fig`
- `image.png`
- `Screenshot 2026-07-23 184310.png`
- `Screenshot 2026-07-23 184343.png`
- `Screenshot 2026-07-23 184421.png`
- `Screenshot 2026-07-23 184430.png`

### Appendix C — Lab 4 primary class files

- full TIMS bench and PCM Encoder photographs;
- annotated frame-decoding instruction photograph;
- meter-and-oscilloscope photographs across the measured voltage range;
- companion `Lab4 Recorded Data.txt`, retained without invented corrections;
- second-week PCM Encoder/Decoder patching and 16 original photographs;
- `Lab 4 Week 2 Encoder Decoder Data.csv` with all 16 measured pairs;
- three verified second-week analysis graphs and deterministic status JSON.

### Appendix D — Pending evidence checklist

- [x] Full-group role-rotation account for Lab 5
- [x] Saved Lab 5 in-class Simulink model
- [x] Saved Lab 5 in-class spectrum screenshots
- [x] Lab 4 setup and oscilloscope photographs
- [x] Week 1–4 running logbook entries
- [ ] Exact Lab 5 plotting fix and final Scope observation
- [x] Aaron’s Lab 4 attendance and teammate details recorded for both weeks
- [ ] Check Lab 4 values around `-0.960`, `-0.308`, and `-0.270 V`
- [ ] Recover or confirm missing Lab 4 companded points
- [x] Classify the 16 second-week Lab 4 photographs by setup, meter/scope, reconstruction and FFT evidence
- [ ] Add candidate sections for the remaining laboratories
- [ ] Select the strongest three laboratories
- [ ] Complete final abstract, comparison, conclusion, and reference formatting
