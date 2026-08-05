---
aliases:
  - ENEL700 Week 8
  - Transmitter, Receiver and Noise
lecture: 8
source: L8 Transmitter, Receiver and Noise.pdf
---

# Transmitters, Receivers, and Noise

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Digital Modulation]] - Next: [[Information Theory]]
>
> [[L8 Transmitter, Receiver and Noise.pdf|Lecture slides]] - [[ENEL700 T8.pdf|Tutorial 8]] - [[ENEL700 T7A,8A.pdf|Tutorial 7-8 answers]]

## Core idea

A transmitter generates, modulates, amplifies, and delivers an RF signal to a channel. A receiver must select a weak desired signal, amplify it with minimal added noise, and recover the message. Noise analysis quantifies how reliably this can be done.

## Transmitter requirements

Every practical radio transmitter must:

1. Generate a stable carrier at the correct allocated frequency.
2. Modulate that carrier with the information.
3. Provide enough RF power for the required path and coverage.
4. Match the power amplifier to the antenna or transmission line for efficient power transfer.

Typical blocks include oscillators, buffers, modulators, mixers, frequency multipliers, drivers, power amplifiers, filters, and impedance-matching networks.

### Example transmitter arrangements

- **CW transmitter:** carrier is keyed on and off to send Morse-code symbols.
- **High-level AM:** modulation occurs at a high-power stage, so the final RF amplifier must preserve the envelope.
- **Low-level FM:** a stable oscillator and phase/frequency modulator are followed by frequency multipliers, driver, and final amplifier. Constant envelope permits efficient non-linear RF stages.
- **SSB:** a balanced modulator creates DSB-SC, a sideband filter selects USB or LSB, a mixer translates it to the final frequency, and linear amplifiers preserve its amplitude information.

## Receiver performance

The received signal is usually weak and contaminated by noise and other transmissions. Two central requirements are:

- **Selectivity:** ability to isolate the desired channel and reject adjacent or unwanted signals.
- **Sensitivity:** ability to recover a usable output from a weak input.

The superheterodyne architecture is widely used because frequency conversion lets most selectivity and gain occur at a fixed intermediate frequency.

### Selectivity

Tuned circuits and filters set receiver bandwidth. The ideal passband is wide enough for the wanted modulation and its sidebands but no wider than necessary.

- Higher resonator $Q$ usually gives narrower bandwidth.
- Response-curve sides are called **skirts**.
- **Shape factor** compares a wide bandwidth measured far down the response, such as the 60-dB bandwidth, with the narrower 6-dB bandwidth:

$$
SF=\frac{BW_{60dB}}{BW_{6dB}}
$$

A shape factor nearer 1 means steeper skirts and better selectivity.

### Sensitivity

Sensitivity depends on receiver gain and noise performance. A common threshold is the **minimum discernible signal (MDS)**, approximately the input level equal to the internally generated receiver noise floor for the stated bandwidth.

More gain alone does not improve SNR, because real amplifiers also add noise. Low-noise performance in the first receiver stage is especially important.

## Signal-to-noise ratio

$$
SNR=\frac{P_S}{P_N}
$$

$$
SNR_{dB}=P_S(dBm)-P_N(dBm)
$$

A larger SNR generally produces fewer decision or demodulation errors. An ideal noiseless amplifier preserves SNR; a real amplifier makes output SNR lower than input SNR.

## Noise sources

### External noise

- Industrial equipment, motors, generators, and switching circuits.
- Atmospheric electrical activity or static.
- Solar and other space noise.

### Internal noise

- Thermal or Johnson noise.
- Semiconductor effects such as shot and flicker noise.
- Intermodulation products from non-linearity.

Noise is random unwanted energy; **interference** is an unwanted but structured signal from another source.

## Thermal noise and AWGN

Thermal noise results from random electron motion and is approximately white over communication bands. The available noise power in bandwidth $B$ is:

$$
P_N=kTB
$$

The open-circuit RMS noise voltage of resistance $R$ is:

$$
v_N=\sqrt{4kTBR}
$$

where $k=1.38\times10^{-23}\ \text{J/K}$ and $T$ is absolute temperature.

The thermal-noise power spectral density is:

$$
N_0=kT\quad\text{W/Hz}
$$

An **additive white Gaussian noise (AWGN)** model assumes noise:

- Adds to the transmitted signal.
- Has flat power spectral density across the band of interest.
- Has Gaussian-distributed instantaneous amplitude.

This model is mathematically tractable and provides a baseline for communication performance.

## Noise factor and noise figure

Noise factor measures how much a device degrades SNR:

$$
F=\frac{SNR_{in}}{SNR_{out}}\geq1
$$

Noise figure is the decibel form:

$$
NF=10\log_{10}F\quad\text{dB}
$$

Always convert $NF$ from dB to linear $F$ before using it in cascade formulas:

$$
F=10^{NF/10}
$$

## Equivalent noise temperature

A noisy device can be modelled as an ideal noiseless device with an equivalent input noise temperature $T_e$:

$$
P_{N,out}=GkT_eB
$$

Using the standard reference temperature $T_0=290\ \text{K}$:

$$
F=1+\frac{T_e}{T_0}
$$

$$
T_e=T_0(F-1)
$$

## Cascaded stages: Friis formula

For linear power gains $G_i$ and linear noise factors $F_i$:

$$
F_{total}=F_1+\frac{F_2-1}{G_1}+\frac{F_3-1}{G_1G_2}+\frac{F_4-1}{G_1G_2G_3}+\cdots
$$

The first stage dominates because later noise contributions are divided by preceding gain. A receiver should therefore put a low-noise, sufficiently high-gain RF amplifier early, while avoiding overload or intermodulation.

For a passive loss $L>1$ at $T_0$:

$$
F=L=\frac{1}{G}
$$

A lossy cable or filter before the first amplifier therefore directly worsens receiver noise factor.

## SINAD and practical tests

**SINAD** compares signal plus noise and distortion with noise plus distortion. It is commonly used to state receiver sensitivity at a specified output quality.

Other practical receiver concerns include blocking, intermodulation, output power, and adjacent-channel selectivity.

## Reducing noise pickup

- Use twisted pairs or transposed conductors.
- Use shielding, coaxial cable, and suitable equipment enclosures.
- Restrict bandwidth to what the signal actually needs.
- Decouple power supplies.
- Keep ground leads short.
- Separate high-level and low-level signal wiring.
- Use optical isolation where appropriate.

## Quick recall

- A transmitter needs frequency generation, modulation, power gain, and matching.
- Selectivity rejects unwanted channels; sensitivity concerns weak wanted signals.
- Thermal noise power is $kTB$.
- $F=SNR_{in}/SNR_{out}$ and $NF=10\log_{10}F$.
- Friis shows why the first receiver stage is critical.
- Narrowing receiver bandwidth reduces integrated noise power.

## Practice prompts

1. Draw suitable block diagrams for AM, FM, and SSB transmitters.
2. Explain the difference between sensitivity, selectivity, MDS, and shape factor.
3. Calculate thermal-noise power and RMS noise voltage.
4. Convert between noise figure, noise factor, and equivalent noise temperature.
5. Apply Friis to a receiver cascade and explain which redesign gives the largest improvement.
