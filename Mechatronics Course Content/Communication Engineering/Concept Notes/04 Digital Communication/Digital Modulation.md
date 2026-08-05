---
aliases:
  - ENEL700 Week 7
  - L7 Digital Modulation
lecture: 7
source: L7 Digital Modulation.pdf
---

# Digital Modulation

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Pulse Modulation]] - Next: [[Transmitters Receivers and Noise]]
>
> [[L7 Digital Modulation.pdf|Lecture slides]] - [[ENEL700 T7.pdf|Tutorial 7]] - [[ENEL700 T7A,8A.pdf|Tutorial 7-8 answers]]

## Core idea

Digital modulation maps bits to changes in a carrier's amplitude, frequency, phase, or a combination of amplitude and phase. The design trade-off is between data rate, bandwidth, energy per bit, noise tolerance, amplifier linearity, and receiver complexity.

## Modems and passband data

A modem contains a modulator and demodulator. It converts binary baseband data into a passband waveform suitable for telephone, cable, or radio channels, then reconstructs the bits at the receiver. The lecture introduces dial-up, DSL, cable, and wireless modems.

## Bits, symbols, and baud

A **symbol** is one transmitted waveform state. If a modulation has $M$ possible states, each symbol can represent:

$$
k=\log_2M\quad\text{bits/symbol}
$$

Therefore:

$$
R_b=kR_s
$$

where $R_b$ is bit rate and $R_s$ is symbol rate (baud). Increasing $M$ raises the number of bits per symbol but places constellation points closer together for fixed power, making noise errors more likely.

## ASK and OOK

**Amplitude-shift keying (ASK)** assigns different carrier amplitudes to binary states. Rectangular data pulses contain a fundamental and odd harmonics, so abrupt switching produces a broad sideband spectrum.

**On-off keying (OOK)** is the special case where one state transmits the carrier and the other turns it off. Morse-code continuous-wave transmission is an example.

- Advantage: simple generation and detection.
- Disadvantage: amplitude noise and fading directly affect the decision.
- Poor filtering of sharp transitions can create wide harmonic interference or **splatter**.

## FSK

**Frequency-shift keying (FSK)** assigns different frequencies to symbols. Binary FSK uses two tones, historically called:

- **Mark:** binary 1.
- **Space:** binary 0.

FSK has a constant envelope and can tolerate amplitude variation, but the separated tones often require more bandwidth than PSK for the same bit rate.

## PSK

**Binary phase-shift keying (BPSK)** assigns two carrier phases separated by $180^\circ$ to 0 and 1. Its two constellation points are maximally separated for a given carrier amplitude, giving strong power efficiency.

**Quadrature PSK (QPSK)** uses four phases. Each symbol represents a dibit:

$$
\log_2 4=2\ \text{bits/symbol}
$$

A QPSK modulator splits serial data into in-phase ($I$) and quadrature ($Q$) streams, multiplies them by carriers $90^\circ$ apart, and adds the results. For the same bit rate, the QPSK symbol rate is half the BPSK symbol rate.

## QAM

**Quadrature amplitude modulation (QAM)** varies both $I$ and $Q$, which changes carrier amplitude and phase. A constellation diagram shows each allowed complex symbol.

- 8-QAM: $3$ bits/symbol.
- 16-QAM: $4$ bits/symbol.
- 64-QAM: $6$ bits/symbol.

Higher-order QAM improves spectral efficiency but requires higher SNR, better linearity, and more accurate carrier/amplitude recovery.

## Spectral efficiency

$$
\eta_s=\frac{R_b}{B}\quad\text{bits/s/Hz}
$$

The lecture gives representative efficiencies showing the trend from less than $1\ \text{bit/s/Hz}$ for simple FSK to about $1$ for BPSK, $2$ for QPSK, and $4$ for 16-QAM. Exact practical efficiency also depends on pulse shaping, coding, guard intervals, and implementation margins.

## Bit-error rate

$$
BER=\frac{\text{incorrect bits}}{\text{total received bits}}
$$

BER decreases as energy per bit relative to noise density increases. The relationship between carrier-to-noise ratio and bit-energy ratio is:

$$
\frac{E_b}{N_0}=\frac{C}{N}\frac{B}{R_b}
$$

For coherent BPSK in an AWGN channel:

$$
BER=\frac12\operatorname{erfc}\left(\sqrt{\frac{E_b}{N_0}}\right)
$$

This curve falls rapidly as $E_b/N_0$ increases. When comparing modulation schemes, specify whether the horizontal axis is $C/N$, SNR per symbol, or $E_b/N_0$; they are related but not interchangeable.

## Spread spectrum

Spread-spectrum systems deliberately occupy much more bandwidth than the original data. A matching pseudorandom sequence lets the intended receiver despread the signal.

### FHSS

Frequency-hopping spread spectrum changes carrier frequency according to a shared pseudorandom hop sequence.

```text
data -> FSK/modulator -> mixer <- hopping frequency synthesiser <- PN generator
```

- **Dwell time:** time spent on one hop frequency.
- The hop rate may exceed the data rate, so several hops can occur within one data interval.
- Narrowband interference affects only some hops.

### DSSS

Direct-sequence spread spectrum combines each data bit with a faster pseudorandom chip sequence, commonly using XOR, then applies PSK.

- **Chip:** one element of the spreading code.
- **Chipping rate:** chip rate, much higher than data rate.
- The rapid code transitions create a wide spectrum.
- To a narrowband receiver, the waveform resembles noise.
- A receiver with the correct code correlates and despreads the desired signal.

DSSS supports code-division multiple access because different users can share time and frequency while using different codes.

### Benefits and caveat

- Resistance to narrowband interference and jamming.
- Multiple-user band sharing.
- Resistance to fading and multipath.
- Precise timing through code correlation.
- Low probability of casual interception when code details are unknown.

Spread spectrum is not automatically encryption; security still requires cryptographic protection.

## OFDM

Orthogonal frequency-division multiplexing divides a high-rate stream among many lower-rate subcarriers. The subcarriers overlap spectrally but are orthogonal over the symbol interval, so they can be separated without conventional guard bands.

```text
serial bits -> mapping -> serial/parallel -> IFFT -> guard/cyclic prefix -> channel
channel -> remove prefix -> FFT -> symbol decisions -> parallel/serial
```

Benefits:

- Long symbol duration makes multipath delay a smaller fraction of a symbol.
- A cyclic prefix can prevent intersymbol interference when longer than the channel delay spread.
- Frequency-selective equalisation becomes simple: approximately one coefficient per subcarrier.
- Efficient digital generation and separation using IFFT/FFT processing.

Costs include sensitivity to carrier-frequency error, synchronisation demands, and a high peak-to-average power ratio that challenges power-amplifier efficiency.

## Comparison

| Scheme | Changed property | Main strength | Main limitation |
| --- | --- | --- | --- |
| ASK/OOK | Amplitude | Simplicity | Sensitive to amplitude noise/fading |
| FSK | Frequency | Constant envelope and robust detection | More bandwidth |
| BPSK | Phase | Strong power efficiency | 1 bit/symbol |
| QPSK | Phase | 2 bits/symbol | More carrier/symbol complexity |
| QAM | Amplitude + phase | High spectral efficiency | Needs high SNR and linear amplification |
| FHSS/DSSS | Wideband coded waveform | Interference and multipath resistance | Uses more bandwidth and needs code sync |
| OFDM | Many orthogonal carriers | Excellent multipath handling | High PAPR and synchronisation sensitivity |

## Quick recall

- $k=\log_2M$ and $R_b=kR_s$.
- Higher-order modulation sends more bits/symbol but needs better SNR.
- BER is best compared using $E_b/N_0$.
- FHSS changes frequency; DSSS multiplies data by a faster chip code.
- OFDM converts one fast stream into many slower orthogonal subcarriers.

## Practice prompts

1. Convert between $M$, bits/symbol, symbol rate, and bit rate.
2. Sketch constellation diagrams for BPSK, QPSK, and a QAM scheme.
3. Explain the bandwidth/power trade-off between FSK, PSK, and QAM.
4. Use the BPSK BER expression for a specified $E_b/N_0$.
5. Compare how FHSS, DSSS, and OFDM respond to narrowband interference and multipath.
