---
aliases:
  - ENEL700 Week 6
  - L6 Pulse Modulation
lecture: 6
source: L6 Pulse Modulation.pdf
---

# Pulse Modulation

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Analogue-to-Digital Conversion]] - Next: [[Digital Modulation]]
>
> [[L6 Pulse Modulation.pdf|Lecture slides]] - [[ENEL700 T6.pdf|Tutorial 6]] - [[ENEL700 T6A.pdf|Tutorial 6 answers]]

## Core idea

Pulse modulation represents information by changing a property of a pulse train. Binary pulse techniques are valuable because a receiver can decide between discrete states and regenerate a clean signal instead of continuously amplifying accumulated distortion and noise.

## Pulse-modulation families

| Method | Pulse property that carries information | Amplitude levels |
| --- | --- | --- |
| PAM | Pulse amplitude | Continuously variable sample values |
| PWM | Pulse width/duration | Usually two amplitude levels |
| PPM | Pulse position in a time window | Usually two amplitude levels |
| PCM | Binary code word representing each quantised sample | Binary |

- **PAM** uses constant-width, constant-position pulses whose heights follow sample amplitudes. It is simple and inexpensive, but amplitude noise directly affects the information.
- **PWM** keeps pulse amplitude fixed and varies pulse width.
- **PPM** keeps amplitude and width fixed and shifts the pulse timing.
- **PCM** samples, quantises, and encodes each amplitude as a binary word. It is the most widely used form for digital transport.

## Traditional PCM

```text
analogue signal -> sample-and-hold -> ADC -> parallel word -> serializer -> channel
channel -> word recovery -> DAC -> reconstruction filter -> analogue signal
```

If each sample is encoded with $K$ bits and samples are taken at $f_s$ samples/s, the raw bit rate is:

$$
R_b=Kf_s
$$

For an 8-bit converter at $8\ \text{kS/s}$:

$$
R_b=8(8000)=64\ \text{kbit/s}
$$

The ADC output must be serialised before the next word is sent, and sampling, conversion, and bit clocks must remain synchronised.

## Companding

Uniform quantisation gives poor relative resolution for small speech signals. **Companding** compresses the input's dynamic range before uniform quantisation and applies the inverse expansion at the receiver.

- Small amplitudes receive finer effective steps.
- Large amplitudes receive coarser effective steps.
- SQNR becomes more consistent over the speech dynamic range.

**A-law** is a telephony companding characteristic. In the lecture's 8-bit coding description:

- Most-significant bit: sign.
- Three bits: segment number.
- Four bits: interval within the segment.

A **codec** integrates coding and decoding functions, while a **vocoder** uses a model of speech parameters to encode speech efficiently.

## Differential PCM

Adjacent audio or video samples are usually similar. DPCM predicts the next sample and transmits the quantised prediction error:

$$
e[n]=x[n]-\hat{x}[n]
$$

The receiver adds the received difference to its matching prediction to reconstruct the sample. Because the difference signal usually spans a smaller range than the original, fewer bits can provide a given quality, or the same bits can provide a higher SQNR.

## Delta modulation

Delta modulation is a one-bit form of DPCM. Each bit reports whether the local reconstructed signal should step up or down:

- `1`: increment estimate by step $\Delta$.
- `0`: decrement estimate by step $\Delta$.

A comparator compares the input sample with the feedback estimate from an up/down counter and DAC. The comparator output is both the transmitted bit and the direction command for the reconstructed staircase.

### Delta-modulation errors

- **Granular noise:** the step is too large for a slowly varying or nearly constant input, so the estimate oscillates above and below the signal.
- **Slope-overload distortion:** the input changes faster than the staircase can follow.

The maximum staircase slope is approximately:

$$
\left|\frac{dx}{dt}\right|_{max,track}\approx\frac{\Delta}{T_s}=\Delta f_s
$$

Avoiding slope overload requires the input's maximum slope to be less than this tracking slope. Increasing $\Delta$ helps track fast changes but worsens granular noise; increasing $f_s$ can improve both at the cost of bit rate.

## Sigma-delta conversion

A sigma-delta ($\Sigma\Delta$) converter combines oversampling, feedback, integration, coarse quantisation, digital filtering, and decimation.

Key ideas from the lecture:

- Sampling occurs far above the minimum Nyquist rate.
- Oversampling spreads quantisation-noise power over a much wider frequency range.
- Feedback **noise shaping** pushes much of that noise toward higher frequencies.
- A low-pass digital filter removes out-of-band noise.
- Decimation reduces the sample rate and produces a high-resolution multi-bit output.

This yields high precision, wide dynamic range, and low in-band noise. Sigma-delta converters are common in digital audio and are available with high nominal word lengths such as 18-24 bits.

> [!note] Oversampling and aliasing
> Oversampling does not remove the need to control out-of-band analogue input energy, but it moves the Nyquist boundary outward and makes the required analogue anti-alias filter much easier to realise.

## Comparing PCM, DPCM, delta, and sigma-delta

| Method | What is encoded | Bits/sample | Main advantage | Main limitation |
| --- | --- | ---: | --- | --- |
| PCM | Absolute sample value | Several | Direct, robust representation | Higher bit rate |
| DPCM | Prediction error | Several | Removes sample-to-sample redundancy | Predictor complexity/error propagation |
| Delta modulation | Sign of change | 1 | Very simple | Granular and slope-overload noise |
| Sigma-delta | Oversampled feedback error, then digitally filtered | Internally often 1/few | High resolution and low in-band noise | High internal sample rate and latency |

## Quick recall

- PAM varies height, PWM varies width, and PPM varies position.
- PCM bit rate is $R_b=Kf_s$.
- Companding improves effective resolution for small speech signals.
- DPCM sends prediction error; delta modulation reduces that to one bit.
- Delta modulation trades granular noise against slope overload.
- Sigma-delta conversion uses oversampling and noise shaping.

## Practice prompts

1. Sketch PAM, PWM, and PPM for the same message waveform.
2. Calculate PCM bit rate from sample rate and word length.
3. Explain how companding improves speech SQNR.
4. Diagnose granular noise versus slope overload and propose a remedy.
5. Explain how oversampling and noise shaping improve sigma-delta performance.
