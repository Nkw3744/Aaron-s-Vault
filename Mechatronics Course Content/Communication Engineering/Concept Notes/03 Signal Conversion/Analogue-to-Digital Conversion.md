---
aliases:
  - ENEL700 Week 5
  - Analogue to Digital Conversion
lecture: 5
source: L5 Analogue to Digital Conversion.pdf
---

# Analogue-to-Digital Conversion

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Frequency and Phase Modulation]] - Next: [[Pulse Modulation]]
>
> [[L5 Analogue to Digital Conversion.pdf|Lecture slides]] - [[ENEL700 T5.pdf|Tutorial 5]] - [[ENEL700 T5A.pdf|Tutorial 5 answers]]

## Core idea

An analogue-to-digital converter represents a continuous waveform as a sequence of binary numbers. The conversion chain is **sampling -> quantisation -> encoding**. A DAC performs the reverse conversion, producing a stepped analogue approximation that is smoothed by a reconstruction filter.

## ADC signal chain

```text
analogue input -> anti-alias filter -> sample-and-hold -> quantiser -> binary encoder
```

1. **Sampling:** measure the waveform at discrete times.
2. **Quantisation:** map each continuous sample amplitude to one of a finite number of levels.
3. **Encoding:** represent the selected level with a binary word.

Sampling makes time discrete; quantisation makes amplitude discrete. Both are needed before the result is truly digital.

## Sampling theorem

For a signal band-limited to a highest frequency $f_m$, exact reconstruction is possible in the ideal case when uniformly sampled at:

$$
f_s\geq2f_m
$$

The boundary value $2f_m$ is the **Nyquist rate**, while the corresponding maximum interval is:

$$
T_s=\frac{1}{f_s}\leq\frac{1}{2f_m}
$$

- $f_s=2f_m$: critical sampling.
- $f_s<2f_m$: undersampling.
- $f_s>2f_m$: oversampling.

In practice, use $f_s>2f_m$ because real filters do not have an ideal vertical cutoff and sampling phase can make the equality case unreliable for a sinusoid.

## Sampling in the frequency domain

Sampling replicates the baseband spectrum around integer multiples of $f_s$. Correct reconstruction requires neighbouring replicas not to overlap:

$$
f_s-f_m\geq f_m
$$

which gives $f_s\geq2f_m$.

### Aliasing

When spectral replicas overlap, high-frequency components appear as false lower frequencies. For a single tone below $f_s$ but above $f_s/2$, a common alias relation is:

$$
f_a=|f_s-f_h|
$$

Example: sampling $4\ \text{kHz}$ at $6\ \text{kS/s}$ produces an alias at:

$$
f_a=|6-4|=2\ \text{kHz}
$$

Once aliasing has occurred, the original and false components cannot be separated from the samples alone.

### Anti-alias filter

A low-pass anti-alias filter before the ADC limits the input bandwidth to below $f_s/2$. Its transition band must fit between the wanted signal band and the Nyquist frequency. Practical examples in the lecture include telephone speech below roughly $4\ \text{kHz}$ with $8\ \text{kS/s}$ sampling and audio below roughly $20\ \text{kHz}$ with $44.1\ \text{kS/s}$ sampling.

## Sample-and-hold circuit

The S/H or track-and-hold circuit tracks the input during the sampling phase, then stores the instantaneous voltage on a capacitor during conversion. Holding the input constant prevents signal movement during the conversion interval from causing **aperture error**.

## Uniform quantisation

With $K$ bits per sample, the number of available codes or intervals is:

$$
N=2^K
$$

For a full-scale input range from $-C$ to $+C$:

$$
\Delta=\frac{2C}{N}=\frac{2C}{2^K}
$$

where $\Delta$ is one least significant bit (LSB) or quantisation step.

Rounding to the nearest level gives quantisation error:

$$
-\frac{\Delta}{2}\leq e_q<\frac{\Delta}{2}
$$

Smaller steps reduce error but require more bits, which increases storage, bit rate, and transmission bandwidth.

## Quantisation noise

For an ideal uniform quantiser whose error is uniformly distributed:

$$
\text{MSQE}=\sigma_q^2=\frac{\Delta^2}{12}
$$

$$
V_{q,rms}=\frac{\Delta}{\sqrt{12}}
$$

The lecture's dynamic-range estimate is:

$$
DR=\frac{V_{max}}{V_{min}}\approx2^K
$$

$$
DR_{dB}\approx20\log_{10}(2^K)=6.02K\ \text{dB}
$$

Each additional bit therefore adds about $6\ \text{dB}$ of ideal dynamic range.

### Signal-to-quantisation-noise ratio

For a full-scale sine wave in an ideal $K$-bit uniform ADC:

$$
SQNR_{dB}\approx6.02K+1.76\ \text{dB}
$$

For $K=8$:

$$
SQNR\approx6.02(8)+1.76\approx49.9\ \text{dB}
$$

Underloading the converter uses fewer levels and gives a worse SQNR. This motivates non-uniform quantisation or companding for speech, where both quiet and loud talkers should receive useful quality.

## ADC specifications

- **Resolution:** smallest input increment represented, ideally $V_{REF}/2^K$.
- **Input/full-scale range:** minimum-to-maximum voltage accepted.
- **Dynamic range:** ratio between largest usable and smallest resolvable signals.
- **SNR:** signal power relative to total noise.
- **SINAD:** signal relative to noise plus distortion.
- **ENOB:** effective resolution after noise and distortion are included. It is lower than nominal bit count in a non-ideal converter.
- **SFDR:** RMS signal relative to the largest spurious spectral component.

## ADC architectures

| Architecture | Method | Main characteristic |
| --- | --- | --- |
| Successive approximation | Tests reference levels bit by bit | Good general balance of speed and resolution |
| Flash | Many comparators decide in one step | Very fast, but hardware-intensive |
| Pipeline | Multiple stages resolve portions sequentially | High throughput with conversion latency |
| Sigma-delta | Oversampling and noise shaping | High resolution for lower-bandwidth signals |

## Digital-to-analogue conversion

A DAC maps each binary word to a proportional voltage or current. The raw output is a staircase or pulse-shaped approximation. A low-pass **reconstruction filter** removes high-frequency sampling images and smooths the result.

## Design trade-offs

| Change | Benefit | Cost |
| --- | --- | --- |
| Increase $f_s$ | Easier anti-alias filtering, wider signal band | Higher data rate and processing load |
| Increase $K$ | Smaller $\Delta$, lower quantisation noise | More bits, power, storage, and bandwidth |
| Increase full-scale range | Handles larger inputs | Coarser resolution for fixed $K$ |
| Oversample | Spreads quantisation noise, relaxes filtering | Higher internal clock rate |

## Quick recall

- ADC = sample, quantise, encode.
- Nyquist requires $f_s\geq2f_m$ ideally; practical systems leave margin.
- Anti-alias filtering must happen before sampling.
- $N=2^K$ and $\Delta=\text{range}/2^K$.
- Ideal quantisation noise power is $\Delta^2/12$.
- Ideal full-scale sine SQNR is approximately $6.02K+1.76\ \text{dB}$.

## Practice prompts

1. Choose a sampling rate and anti-alias cutoff for a specified message bandwidth.
2. Calculate alias frequencies for undersampled tones.
3. Find $N$, $\Delta$, maximum error, and MSQE for an ADC.
4. Estimate dynamic range and SQNR from bit depth.
5. Explain why a sample-and-hold is needed before a finite-time conversion.
