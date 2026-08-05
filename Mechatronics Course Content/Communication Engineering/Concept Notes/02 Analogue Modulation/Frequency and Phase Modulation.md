---
aliases:
  - ENEL700 Week 4
  - Frequency Modulation
lecture: 4
source: L4 Frequency Modulation.pdf
---

# Frequency and Phase Modulation

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Amplitude Modulation]] - Next: [[Analogue-to-Digital Conversion]]
>
> [[L4 Frequency Modulation.pdf|Lecture slides]] - [[ENEL700 T4.pdf|Tutorial 4]] - [[ENEL700 T4A.pdf|Tutorial 4 answers]]

## Core idea

Frequency modulation (FM) and phase modulation (PM) are angle-modulation methods. They keep the carrier amplitude constant and place information in the carrier's instantaneous angle. This improves amplitude-noise immunity but usually requires more bandwidth than AM.

## Frequency modulation

For FM, the instantaneous frequency is:

$$
f_i(t)=f_c+k_fv_m(t)
$$

where:

- $f_c$ is the unmodulated carrier frequency.
- $v_m(t)$ is the message voltage.
- $k_f$ is frequency sensitivity in hertz per volt.

The carrier frequency moves above and below $f_c$ in proportion to message amplitude, while carrier amplitude stays constant.

### Frequency deviation and swing

- **Peak frequency deviation:**

$$
\Delta f=f_d=\max|f_i(t)-f_c|
$$

- **Peak-to-peak frequency swing:**

$$
f_{p-p}=f_{i,max}-f_{i,min}=2\Delta f
$$

Rated deviation limits occupied bandwidth. Lecture examples include approximately $75\ \text{kHz}$ for FM broadcasting, $25\ \text{kHz}$ for television sound, and $5\ \text{kHz}$ for two-way radio.

## Phase modulation

In PM, message amplitude controls carrier phase displacement:

$$
s_{PM}(t)=A_c\cos[2\pi f_ct+k_pv_m(t)]
$$

The maximum leading or lagging phase shift occurs at message peaks. Instantaneous frequency is the time derivative of phase, so PM creates frequency deviation only while the message is changing. Consequently:

- PM phase deviation is proportional to message amplitude.
- PM frequency deviation is proportional to both message amplitude and message frequency.
- A faster-changing message causes greater instantaneous frequency shift.

FM can be generated indirectly with a phase modulator by first passing the message through an integrating or $1/f$ frequency-correcting network. This attenuates high message frequencies so the resulting frequency deviation is independent of message frequency.

## FM modulation index

For a single sinusoidal message of frequency $f_m$:

$$
\beta=m_f=\frac{\Delta f}{f_m}
$$

For speech or music, message frequency and amplitude vary continuously, so a **deviation ratio** is often used:

$$
D=\frac{\Delta f_{max}}{f_{m,max}}
$$

### Narrowband and wideband FM

- **NBFM:** $\beta\leq0.25$ in the lecture convention. Its spectrum is approximated by the carrier plus one significant sideband pair, resembling AM in occupied bandwidth.
- **WBFM:** $\beta>0.25$. It produces many significant sidebands.

Unlike AM, sinusoidal FM theoretically has an infinite number of sidebands at:

$$
f_c\pm nf_m,\qquad n=1,2,3,\ldots
$$

Their amplitudes are set by Bessel coefficients $J_n(\beta)$. As $\beta$ changes, power moves among the carrier and sidebands, but total FM power stays constant because carrier amplitude stays constant.

## FM power

For load resistance $R$ and carrier peak amplitude $V_c$:

$$
P_{FM}=\frac{V_c^2}{2R}
$$

The total equals the sum of the carrier and all sideband-component powers. Modulation redistributes power; it does not change total power for an ideal constant-envelope FM signal.

## FM bandwidth

### Significant-sideband method

If $N$ significant sideband pairs are retained from a Bessel table:

$$
BW\approx2Nf_m
$$

The lecture treats components greater than about 1% of unmodulated carrier amplitude as significant.

### Carson's rule

The practical estimate containing about 98% of FM power is:

$$
BW_C=2(\Delta f+f_{m,max})
$$

Since $\beta=\Delta f/f_m$ for a single tone:

$$
BW_C=2(\beta+1)f_m
$$

### Worked example

For $f_{m,max}=3\ \text{kHz}$ and $\Delta f=6\ \text{kHz}$:

$$
\beta=\frac{6}{3}=2
$$

Carson's rule gives:

$$
BW_C=2(6+3)=18\ \text{kHz}
$$

If a Bessel table indicates four significant sideband pairs, the 1%-component method gives:

$$
BW\approx2(4)(3)=24\ \text{kHz}
$$

The answers differ because the methods use different significance criteria.

## FM noise performance

FM offers several practical advantages:

- **Amplitude limiting:** receiver limiter stages remove much amplitude noise before demodulation.
- **Capture effect:** when two FM signals share a frequency, a sufficiently stronger one tends to dominate the receiver output.
- **Constant envelope:** efficient non-linear power amplifiers can be used without distorting the modulation.
- **Improved noise immunity:** information is carried in instantaneous frequency rather than amplitude.

Its disadvantages are greater occupied bandwidth and more complex modulation/demodulation circuitry, although integrated circuits reduce the implementation burden.

## FM versus AM

| Property | AM | FM |
| --- | --- | --- |
| Varied carrier property | Amplitude | Frequency |
| Envelope | Varies | Constant |
| Typical bandwidth | $2f_{m,max}$ | $2(\Delta f+f_{m,max})$ by Carson |
| Amplitude-noise immunity | Lower | Higher with limiting |
| Power amplifier | Must preserve amplitude linearity | Efficient non-linear stages possible |
| Circuit/spectrum cost | Simpler/narrower | More complex/wider |

## Quick recall

- FM deviation follows message amplitude.
- PM phase follows message amplitude, while its frequency deviation also depends on how fast the message changes.
- $\beta=\Delta f/f_m$.
- FM has theoretically infinite sidebands, with Bessel coefficients setting their amplitudes.
- Carson bandwidth is $2(\Delta f+f_{m,max})$.
- FM total power is constant for constant carrier amplitude.

## Practice prompts

1. Calculate instantaneous frequency, peak deviation, and frequency swing.
2. Explain the difference between FM and PM using message amplitude and slope.
3. Calculate $\beta$ and classify the signal as narrowband or wideband.
4. Estimate bandwidth using both Carson's rule and significant sidebands.
5. Explain why FM can use a non-linear RF power amplifier while AM generally cannot.
