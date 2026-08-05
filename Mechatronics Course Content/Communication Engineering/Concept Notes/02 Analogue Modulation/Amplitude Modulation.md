---
aliases:
  - ENEL700 Week 3
  - L3 Amplitude Modulation
lecture: 3
source: L3 Amplitude Modulation.pdf
source_reviewed: 2026-07-22
source_scope: Lecture 3 plus ENEL700 Lab 5 MATLAB and Simulink evidence
---

# Amplitude Modulation

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Fundamentals of Electronics and Signals]] - Next: [[Frequency and Phase Modulation]]
>
> [[L3 Amplitude Modulation.pdf|Lecture slides]] - [[ENEL700 T3.pdf|Tutorial 3]] - [[ENEL700 T3A.pdf|Tutorial 3 answers]]

## Core idea

Amplitude modulation translates a baseband message to a band around a high-frequency carrier by making the carrier amplitude follow the message. The result contains the carrier and two information-bearing sidebands.

## Single-tone AM signal

Let the carrier and message be:

$$
c(t)=V_c\cos(2\pi f_ct),\qquad m(t)=V_m\cos(2\pi f_mt)
$$

The AM waveform in the lecture is:

$$
v_{AM}(t)=[V_c+V_m\cos(2\pi f_mt)]\cos(2\pi f_ct)
$$

Using the modulation index $m=V_m/V_c$:

$$
v_{AM}(t)=V_c[1+m\cos(2\pi f_mt)]\cos(2\pi f_ct)
$$

The outline joining the carrier peaks is the **envelope**. In conventional AM, an envelope detector can recover the message if the envelope is not overmodulated.

## Frequency-domain components

Using $\cos A\cos B=\tfrac12[\cos(A-B)+\cos(A+B)]$:

$$
\begin{aligned}
v_{AM}(t)=&\ V_c\cos(2\pi f_ct)\\
&+\frac{V_m}{2}\cos[2\pi(f_c-f_m)t]\\
&+\frac{V_m}{2}\cos[2\pi(f_c+f_m)t]
\end{aligned}
$$

The spectrum contains:

- Carrier at $f_c$, amplitude $V_c$.
- Lower sideband (LSB) at $f_c-f_m$, amplitude $V_m/2=mV_c/2$.
- Upper sideband (USB) at $f_c+f_m$, amplitude $V_m/2=mV_c/2$.

For a complex message extending to maximum frequency $f_{m,max}$, each message component produces a pair of translated sidebands. The occupied bandwidth is:

$$
BW=(f_c+f_{m,max})-(f_c-f_{m,max})=2f_{m,max}
$$

### Worked example: sidebands and bandwidth

For $f_c=980\ \text{kHz}$ and $f_{m,max}=5\ \text{kHz}$:

$$
f_{USB}=985\ \text{kHz},\qquad f_{LSB}=975\ \text{kHz}
$$

$$
BW=985-975=10\ \text{kHz}
$$

## Modulation index and percentage modulation

$$
m=\frac{V_m}{V_c},\qquad \%\text{ modulation}=100m
$$

For an AM envelope measured on an oscilloscope:

$$
m=\frac{V_{max}-V_{min}}{V_{max}+V_{min}}
$$

The message amplitude itself can be inferred as:

$$
V_m=\frac{V_{max}-V_{min}}{2}
$$

| Condition | Meaning |
| --- | --- |
| $m=0$ | Unmodulated carrier |
| $0<m<1$ | Normal modulation |
| $m=1$ | 100% modulation; envelope just reaches zero |
| $m>1$ | Overmodulation; envelope distortion and unreliable envelope detection |

> [!warning] Common mistake
> Do not use only $(V_{max}-V_{min})/2$ as the modulation index. That expression gives the message amplitude represented by the envelope excursion; the index also requires division by the carrier amplitude.

## AM power

For a resistive load $R$, carrier power is:

$$
P_c=\frac{V_{c,rms}^2}{R}
$$

For single-tone AM, each sideband has power:

$$
P_{USB}=P_{LSB}=\frac{m^2}{4}P_c
$$

Total sideband power and total transmitted power are:

$$
P_{SB}=\frac{m^2}{2}P_c
$$

$$
P_T=P_c+P_{SB}=P_c\left(1+\frac{m^2}{2}\right)
$$

At $m=1$, $P_T=1.5P_c$. The two sidebands together carry $0.5P_c$, so only one-third of total transmitted power contains information; two-thirds remains in the carrier.

If total sideband power is known:

$$
m=\sqrt{\frac{2P_{SB}}{P_c}}
$$

## Suppressed-carrier and single-sideband forms

### DSB-SC / DSSC

A balanced modulator suppresses the carrier and leaves both sidebands. This avoids carrier-power waste, but coherent carrier recovery is required at the receiver.

### SSB-SC / SSSC

The carrier and one sideband are suppressed. Because either sideband contains the complete message information, SSB provides:

- Half the bandwidth of conventional AM.
- No carrier power and no duplicated sideband power.
- More useful transmitted power for a given transmitter rating.
- Less received noise because the receiver bandwidth is narrower.
- Reduced selective-fading effects.

The cost is more difficult generation, tuning, and coherent demodulation. A small pilot carrier may be transmitted to assist recovery.

### Lab 5 bridge: product modulation and measured spectra

[[Lab 5 - Amplitude Modulation Using Simulink|Lab 5 working note]] and the [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Report/Lab 5 - MATLAB Replication Report|completed MATLAB replication report]] provide experimental/computational evidence for DSB-SC without repeating the lab procedure here.

For sampled message $m[n]$ and carrier $\cos(2\pi f_cn/f_s+\phi)$:

$$
s[n]=m[n]\cos\left(2\pi\frac{f_c}{f_s}n+\phi\right).
$$

The product translates the message spectrum to both sides of the carrier:

$$
S(f)=\frac12M(f-f_c)+\frac12M(f+f_c).
$$

For a single message tone at $f_m$, this produces lines at $f_c-f_m$ and $f_c+f_m$ with no independent carrier line in ideal DSB-SC. The absence of a carrier term is the practical distinction from conventional AM's $[1+m\cos(2\pi f_mt)]\cos(2\pi f_ct)$ form.

### Interpreting the FFT evidence

- The time-domain product verifies that the message controls the rapid carrier oscillation.
- The spectrum verifies translation to upper and lower sidebands.
- A finite data record can spread energy between bins; windowing reduces leakage but changes amplitude scaling and main-lobe width.
- Sample rate sets the Nyquist limit, while record duration sets frequency-bin spacing.
- Compare relative peak locations first; compare amplitudes only after the FFT/window normalization is defined.

The verified MATLAB replication measured:

- average shifted-sideband/message peak ratio: `0.498366330964`, close to the theoretical $0.5$;
- carrier peak: normalized frequency `0.299987792969`, close to the configured $0.3$;
- logarithmic difference under the lab function: `-3.0245 dB`.

> [!warning] Lab-specific logarithmic convention
> Question 1's `sigspec` uses $10\log_{10}$ of **magnitude**, so a factor of $1/2$ appears as about $-3.01$ dB. The conventional amplitude-ratio definition uses $20\log_{10}$ and would give about $-6.02$ dB. Preserve the lab's convention when reproducing its output, but do not treat the conventions as interchangeable.

The report verifies a MATLAB signal-domain replication. The equivalent Simulink GUI model, block-diagram capture, and Scope evidence remain pending and must not be described as completed.

The mathematics connects directly to [[Fourier Analysis]]. The lab files own MATLAB code, exact parameters, screenshots, and report evidence; this concept note owns the reusable modulation and spectrum interpretation.

### VSB

Vestigial-sideband modulation transmits one complete sideband and a small part of the other. It provides a practical compromise for signals whose low-frequency components make ideal SSB filtering difficult, and is associated with television transmission.

## Comparing AM variants

| Scheme | Carrier | Sidebands | Bandwidth for message bandwidth $B_m$ | Main trade-off |
| --- | --- | --- | ---: | --- |
| Conventional AM | Full | Both | $2B_m$ | Simple receiver, poor power efficiency |
| DSB-SC | Suppressed | Both | $2B_m$ | Better power use, coherent detection |
| SSB-SC | Suppressed | One | $B_m$ | Best spectrum/power use, greater complexity |
| VSB | Usually present/reduced | One plus vestige | Slightly above $B_m$ | Practical filtering compromise |

## Quick recall

- AM changes carrier amplitude; carrier frequency and phase remain fixed.
- $m=V_m/V_c$ and overmodulation occurs for $m>1$.
- Sidebands appear at $f_c\pm f_m$.
- Conventional AM bandwidth is twice the highest message frequency.
- $P_T=P_c(1+m^2/2)$ for a single tone.
- The carrier consumes power but conveys no message information.

## Practice prompts

1. Expand the AM waveform into carrier, LSB, and USB terms.
2. Find sideband frequencies and bandwidth for a specified carrier and message range.
3. Calculate $m$ from $V_{max}$ and $V_{min}$.
4. Determine carrier, sideband, and total power.
5. Explain when SSB is worth its extra receiver complexity.
