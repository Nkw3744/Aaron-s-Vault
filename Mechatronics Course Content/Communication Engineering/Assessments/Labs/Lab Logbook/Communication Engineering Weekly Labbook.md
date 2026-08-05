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
| 4 | To be recorded | — | — | Ready for entry |

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

<details>
<summary><strong>Week 4 — Ready for the next laboratory</strong></summary>

## Week 4 — Laboratory entry

### Attendance and roles

*Add after the session.*

### Aim and preparation

*What were we trying to investigate or demonstrate?*

### Equipment, software, and setup

*Record the actual setup used in class.*

### What we did

*Write the sequence while it is still fresh.*

### Measurements and results

*Add tables, code, screenshots, photographs, and oscilloscope settings.*

### Observations and interpretation

*What changed, and what did the result mean?*

### Problems, mistakes, and troubleshooting

*What went wrong, what was changed, and how was the result checked?*

### Lecturer or classmate guidance

*Record specific guidance without presenting another person’s work as ours.*

### What we learned and what we would change

*Add a short personal and team reflection.*

### Primary in-class evidence

*Link the new in-class folder here.*

### Report-ready points

*Promote the strongest technical result, method detail, and reflection into the report draft.*

</details>

---

## Source preservation

The original raw note remains at [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab Logbook/Weekly Logbook for Communications Labs.txt|Weekly Logbook for Communications Labs.txt]]. This Markdown file is the organised running version; the raw note should remain preserved for comparison.
