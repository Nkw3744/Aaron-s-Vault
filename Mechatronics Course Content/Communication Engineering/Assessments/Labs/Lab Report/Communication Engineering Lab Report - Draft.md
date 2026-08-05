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
| Lab 4 — Pulse-Code Modulation | PCM bench, encoder patching, annotated instructions, meter readings, oscilloscope traces | Week 3 recorded | Check two unusual values, incomplete companded sequence, and photo classification | Promising but incomplete |
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

Lab 4 was completed by Aaron and Nahil because two members were sick. The pair first asked the lecturer and classmates for enough context to understand how to align and decode the PCM frame. They practised the interpretation method, checked it against other students, and then divided the task between finding each result and recording the voltage/code pair. This made the smaller team effective despite the reduced attendance.

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
<summary><strong>Candidate Lab 4 — Pulse-Code Modulation</strong> · direct measurements, data checks pending</summary>

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

### 4.6 Discussion

The in-class photographs support the essential qualitative result: changing the continuous DC input produced discrete binary patterns. This is direct evidence of quantisation. The code does not vary continuously with voltage; it remains in one state over an interval and changes when a threshold is crossed.

The linear run appears to span codes `0000` to `1111` across approximately `-2.63 V` to `+2.63 V`. Most neighbouring recorded values are separated by roughly similar increments, as expected for linear quantisation. However, the two central values identified above prevent a complete quantitative claim until they are checked.

The second sequence appears intended to represent a non-linear or companded response. Its voltage intervals are visibly non-uniform, with narrower regions near small amplitudes and wider regions toward the extremes. That is qualitatively consistent with companding, but the missing codes and questionable ordering mean that the final graph and detailed comparison remain provisional.

The strongest process feature was the pair’s decision to understand the frame before collecting measurements. By practising the decoding method and checking it with the lecturer and classmates, they reduced the risk of recording a complete table from the wrong bit positions.

### 4.7 Limitations and evidence boundary

- The meter-and-oscilloscope photographs are primary in-class evidence.
- `Lab4 Recorded Data.txt` is a companion transcription and contains unresolved values.
- `Communication Engineering Lab 4.md` is a manual-based preparation and interpretation note, not proof of what was completed.
- `Lab 4 answers Kane.pdf` is another student’s work and is not used as Aaron’s report wording or evidence.
- `IMG_2379_Original.jpeg` shows an ENEL800 superheterodyne-receiver sheet and is excluded as irrelevant to this PCM experiment.

### 4.8 Personal and team reflection

Reduced attendance meant that the work could not be divided across the full group. The two attending members compensated by taking time to learn from the lecturer and classmates, confirming the decoding process, and then separating measurement from recording. This worked efficiently once the method was understood. The next improvement is to resolve uncertain entries immediately against the hardcopy record so that a graph is not delayed by ambiguous data.

### 4.9 Provisional conclusion

The in-class equipment, patching, and meter/scope photographs support that the pair completed a PCM voltage-to-code investigation using the TIMS system. The observed code changed in discrete steps as the analogue voltage was varied, demonstrating four-bit quantisation. Raw-data graphs have now been produced without correcting or filling missing values. They support the qualitative linear/companded comparison while keeping the quantitative limitations visible.

### 4.10 Resolved evidence questions

1. Nahil attended Lab 4 with Aaron.
2. `-0.308 V` and `-0.270 V` remain exact raw transcriptions but are not independently verified by the retained photographs; they must not be silently corrected.
3. Only 11 companded points survive in the class-data file; codes 5, 6, 7, 8 and 10 are missing.
4. The visible meter readings confirm `67EAA...`, `FF32...`, `AA06...`, and `1B4E...` for Question 4.1, and `7264...` and `E70F...` for Question 4.2.
5. The full first-person answers, evidence photographs and raw-data graphs are available in [[../Lab Logbook/Communication Engineering Labbook - Answered Questions/Communication Engineering Labbook - Answered Questions.pdf|Communication Engineering Labbook — Answered Questions and Evidence]].

### 4.11 Selection strength

**Current assessment:** Promising candidate. It has strong physical in-class evidence, a useful personal method account, and verified raw-data plots. Resolving the two questionable linear values and recovering the five missing companded codes would strengthen the quantitative analysis further, but the present graphs are defensible because they display the preserved uncertainty explicitly.

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
| Primary in-class evidence | Strong | Strong photographs; table checks pending | — | — |
| Technical result clarity | Strong | Moderate pending data checks | — | — |
| Theory-to-result connection | Strong | Strong qualitatively | — | — |
| Team/process detail | Strong | Good; one name/detail pending | — | — |
| Troubleshooting/reflection | Strong | Moderate | — | — |
| Effort to make submission-ready | Low–moderate | Moderate | — | — |

## 8. Overall discussion

*Complete after the final three laboratories are selected. Compare how modelling, physical measurement, time-domain traces, and frequency-domain plots developed the group’s understanding. Distinguish results obtained in class from later checks.*

## 9. Team reflection

The team’s experience so far shows two different forms of practical collaboration. Lab 5 involved the full group around one computer, creating broad participation but also competing code changes. Lab 4 involved only two members, making communication simpler but reducing available roles. In both cases, progress improved when the team agreed on the interpretation method before gathering or presenting results.

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
- companion `Lab4 Recorded Data.txt`, retained without invented corrections.

### Appendix D — Pending evidence checklist

- [x] Full-group role-rotation account for Lab 5
- [x] Saved Lab 5 in-class Simulink model
- [x] Saved Lab 5 in-class spectrum screenshots
- [x] Lab 4 setup and oscilloscope photographs
- [x] Week 1–3 running logbook entries
- [ ] Exact Lab 5 plotting fix and final Scope observation
- [ ] Name of Aaron’s Week 3 Lab 4 teammate
- [ ] Check Lab 4 values around `-0.960`, `-0.308`, and `-0.270 V`
- [ ] Recover or confirm missing Lab 4 companded points
- [ ] Classify remaining Lab 4 photographs by linear/companded run
- [ ] Add candidate sections for the remaining laboratories
- [ ] Select the strongest three laboratories
- [ ] Complete final abstract, comparison, conclusion, and reference formatting
