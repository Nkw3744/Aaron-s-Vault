---
aliases:
  - ENEL700 Week 2
  - The Fundamentals of Electronics
lecture: 2
source: L2 The Fundamentals of Electronics.pdf
---

# Fundamentals of Electronics and Signals

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Introduction to Electronic Communication]] - Next: [[Amplitude Modulation]]
>
> [[L2 The Fundamentals of Electronics.pdf|Lecture slides]] - [[ENEL700 T2.pdf|Tutorial 2]] - [[ENEL700 T2A.pdf|Tutorial 2 answers]]

## Core idea

Communication circuits shape signals by amplifying, attenuating, selecting, rejecting, and translating frequency components. Gain, decibels, resonance, filters, and Fourier analysis provide the mathematical language for describing those operations.

## Gain and attenuation

Gain is the ratio of output to input. For voltage, current, and power:

$$
A_v=\frac{V_{out}}{V_{in}},\qquad
A_i=\frac{I_{out}}{I_{in}},\qquad
A_p=\frac{P_{out}}{P_{in}}
$$

- $A>1$ represents gain or amplification.
- $0<A<1$ represents attenuation or loss.
- Cascaded linear ratios multiply:

$$
A_{total}=A_1A_2\cdots A_n
$$

### Worked example: cascaded power gain

For stage gains $5$, $2$, and $17$:

$$
A_{p,total}=5\times2\times17=170
$$

With $P_{in}=40\ \text{mW}$:

$$
P_{out}=170(40\times10^{-3})=6.8\ \text{W}
$$

## Decibels

The decibel expresses a ratio logarithmically:

$$
G_{dB}=20\log_{10}\left|\frac{V_{out}}{V_{in}}\right|
$$

$$
G_{dB}=20\log_{10}\left|\frac{I_{out}}{I_{in}}\right|
$$

$$
G_{dB}=10\log_{10}\left(\frac{P_{out}}{P_{in}}\right)
$$

The factor 20 is used for voltage or current only when the compared quantities relate to the same impedance, because power is proportional to the square of voltage or current.

- Positive dB means gain.
- Negative dB means attenuation.
- A zero-dB ratio means output equals input.
- Cascaded dB values add: $G_{total,dB}=G_{1,dB}+G_{2,dB}+\cdots$.

### Inverse conversion

$$
\frac{P_{out}}{P_{in}}=10^{G_{dB}/10},\qquad
\frac{V_{out}}{V_{in}}=10^{G_{dB}/20}
$$

### Referenced decibel units

- **dBm:** power referenced to $1\ \text{mW}$.

$$
P_{dBm}=10\log_{10}\left(\frac{P}{1\ \text{mW}}\right)
$$

- **dBc:** level referenced to a carrier, often used for sidebands, harmonics, or spurious signals.

### Worked examples

An amplifier changes $3\ \text{mV}$ to $5\ \text{V}$:

$$
G_{dB}=20\log_{10}\left(\frac{5}{0.003}\right)\approx64.4\ \text{dB}
$$

A filter changes $50\ \text{mW}$ to $2\ \text{mW}$:

$$
G_{dB}=10\log_{10}\left(\frac{2}{50}\right)\approx-14.0\ \text{dB}
$$

## Tuned circuits and resonance

A tuned or resonant circuit uses inductance and capacitance to respond selectively around a resonant frequency. Resonance occurs when the magnitudes of inductive and capacitive reactance are equal:

$$
X_L=2\pi fL,\qquad X_C=\frac{1}{2\pi fC}
$$

Therefore:

$$
f_r=\frac{1}{2\pi\sqrt{LC}}
$$

### Series resonance

- $R$, $L$, and $C$ are in series.
- At resonance, reactive effects cancel, impedance is minimum, and current is maximum.
- The circuit strongly passes or responds to frequencies near $f_r$.

### Parallel resonance

- $L$ and $C$ are connected in parallel.
- Ideally at resonance, input impedance is very high and source current is very low.
- Large circulating current transfers stored energy between the inductor and capacitor.
- The circuit is often called a **tank circuit**.

### Bandwidth, half-power points, and quality factor

The half-power frequencies $f_1$ and $f_2$ occur where power is half its resonant value. For a voltage or current response, that corresponds to $0.707$ of the peak.

$$
BW=f_2-f_1
$$

The quality factor measures sharpness of resonance:

$$
Q\approx\frac{f_r}{BW}
$$

For a series RLC circuit:

$$
Q=\frac{X_L}{R}=\frac{2\pi f_rL}{R}
$$

Higher $Q$ means narrower bandwidth and better selectivity. Lower $Q$ means a broader response.

## Filters

A filter passes selected frequencies and attenuates others.

| Filter | Passed region | Rejected region |
| --- | --- | --- |
| Low-pass | Below cutoff | Above cutoff |
| High-pass | Above cutoff | Below cutoff |
| Band-pass | Between lower and upper cutoffs | Outside that band |
| Band-reject/notch | Outside a rejected band | Within the rejected band |
| All-pass | All frequencies in the design range | Alters phase rather than magnitude |

- **Passive filters** use $R$, $L$, and $C$ and provide no gain.
- **Active filters** combine RC networks with amplifiers and feedback. Advantages include gain, isolation, easier tuning and impedance matching, and no inductors.
- LC filters are common at radio frequencies.

### Filter vocabulary

- **Passband:** wanted frequency range.
- **Stopband:** strongly attenuated frequency range.
- **Insertion loss:** loss introduced in the passband.
- **Ripple:** amplitude variation within a band.
- **Roll-off:** rate at which attenuation changes with frequency.
- **Shape factor:** ratio of a wider stopband bandwidth to the passband bandwidth; it describes skirt steepness.
- **Envelope delay:** time taken for a feature of the waveform to pass through the filter.
- **Pole/zero:** frequencies associated with very high or zero response in the network model.

### Common response families

| Family | Main property | Trade-off |
| --- | --- | --- |
| Butterworth | Maximally flat passband | Moderate selectivity and phase response |
| Chebyshev | Steeper transition | Passband ripple |
| Elliptic/Cauer | Very sharp transition | Ripple in passband and stopband |
| Bessel/Thomson | Nearly constant group delay | Gentler magnitude roll-off |

The correct filter depends on whether amplitude flatness, selectivity, or waveform shape is most important.

## Fourier theory

Fourier analysis represents a non-sinusoidal periodic waveform as a sum of harmonically related sine and cosine components. A square wave, for example, contains a fundamental and an infinite series of odd harmonics.

This provides two complementary descriptions:

- **Time domain:** signal amplitude versus time.
- **Frequency domain:** amplitude or power versus frequency.

A waveform with sharp edges requires high-frequency harmonics. Passing it through a channel that removes those harmonics rounds the edges and distorts the waveform. Fourier analysis therefore connects waveform shape, channel bandwidth, and filtering.

A **spectrum analyser** displays signal content in the frequency domain and is central to communication-system design and troubleshooting.

## Quick recall

- Linear gains multiply; dB gains add.
- Use $10\log$ for power ratios and $20\log$ for voltage/current ratios at equal impedance.
- $f_r=1/(2\pi\sqrt{LC})$.
- High $Q$ gives a narrow bandwidth and strong selectivity.
- Filters trade amplitude flatness, transition steepness, phase response, and delay.
- Fourier analysis explains which frequencies make up a waveform.

## Practice prompts

1. Convert a cascade of gains and losses between linear and dB form.
2. Calculate $f_r$, $BW$, and $Q$ for a resonant circuit.
3. Choose a suitable filter type for anti-aliasing, channel selection, and notch rejection.
4. Explain why a square wave is distorted by a narrow-band channel.
5. Distinguish time-domain and frequency-domain measurements.
