---
course: ENEL700 Communication Engineering
source_type: assessment-lab evidence supplement
source_reviewed: 2026-08-10
source_scope: answered questions, Lab 4 raw measurements, Lab 4 manual answers, and Lab 5 spectrum answers from the preserved PDF
status: evidence-backed-summary
---

# Communication Engineering Labbook — Answered Questions

Return to the [[Communication Engineering Lab Index|lab index]] · Open the [[Communication Engineering Lab Report - Draft|running report draft]] · Read the [[Communication Engineering Weekly Labbook|weekly labbook]].

This note is a concise, searchable companion to [[Communication Engineering Labbook - Answered Questions.pdf|the preserved answered-questions PDF]]. It records the useful conclusions without replacing the PDF's first-person answers, figures, or evidence register.

## Evidence boundary

The in-class photographs, screenshots, Simulink/MATLAB files, and raw measurement transcription are the primary evidence of what the group completed. Later calculations and MATLAB replication are supporting analysis only. Missing evidence is not filled by assumption.

## Lab 5 — amplitude modulation

- The retained plotting workflow selected each axis with `subplot(3,1,k)` before calling `sigspec` for the modulating signal, carrier, and modulated signal. The preserved files do not identify one decisive final edit or attribute it to a particular lecturer/classmate.
- The saved model routes the message and a carrier at normalized frequency `0.3` through a Product block to a Scope and a To Workspace block. The expected Scope interpretation is a DSB-SC waveform with a carrier-frequency oscillation whose envelope follows the message, but no identifiable in-class Scope capture survives.
- The final class spectrum shows baseband message energy near zero, carrier components near `±0.3`, and translated modulated content near those carrier regions. This is the primary visual result; the later numerical replication remains secondary.
- The completed `sigspec` answer standardises vector orientation, applies a Hamming window, uses a zero-padded FFT with `fftshift`, and supports linear or decibel magnitude plots.

## Lab 4 — pulse-code modulation

Nahil attended with Aaron. They first learned the four data-bit positions in the PCM frame, checked the interpretation with the lecturer and nearby classmates, and then divided voltage adjustment and recording.

### Evidence-supported points

- Question 4.1 photographs support the first four recorded pairs: approximately `−2.634 V → 0000`, `−2.240 V → 0001`, `−1.911 V → 0010`, and `−1.595 V → 0011`.
- Question 4.2 photographs support approximately `−2.633 V → 0000` and `−1.100 V → 0001`.
- The Question 4.1 table contains all 16 codes, but `−0.308 V` and `−0.270 V` are not independently confirmed by photographs and produce an anomalously small adjacent spacing. Preserve them as recorded until checked against the hardcopy.
- The Question 4.2 record has only 11 points and omits decimal codes `5, 6, 7, 8, and 10`; the preserved code-9/code-11 pair is not monotonic. The companded comparison is therefore qualitative and partial, not a certified complete law.

### Manual-derived checks

Using the preserved manual parameters, the eight-slot frame and `8.333 kHz` clock give a sampling rate of approximately `1041.625 samples/s`, a theoretical Nyquist boundary of approximately `520.8125 Hz`, a frame width of approximately `0.960038 ms`, a data-bit width of approximately `120.005 µs`, and a four-bit word width of approximately `480.019 µs`.

In four-bit mode, slots 7–5 are zero, slots 4–1 carry the data bits, and slot 0 carries the alternating frame-synchronisation bit. A reconstruction filter should pass the wanted message band with low ripple while attenuating sampling images; the required specification depends on passband, stopband, attenuation, transition width, phase/group delay, levels, and whether harmonics must remain measurable. Sampling distortion can be reduced with higher sampling rate and suitable anti-alias/reconstruction filtering; quantisation distortion with more bits, proper scaling, or companding. More levels cost bits, frame capacity or channel rate, storage, complexity, and power.

## Related evidence

- [[Communication Engineering Labbook - Answered Questions.pdf|Preserved PDF supplement]] — full first-person answers, figures, raw tables, and evidence limitations.
- [[Communication Engineering Labbook - Answered Questions.tex|LaTeX source]] — source for the PDF.
- [[Communication Engineering Lab Report - Draft|Running laboratory report]] — report-facing synthesis that keeps class evidence separate from later checks.

**Evidence boundary:** This summary is grounded in the preserved PDF and existing lab workspace links. It does not certify unresolved Lab 4 values or missing companded measurements.
