---
aliases:
  - ENEL700 Week 1
  - L1 Introduction to Electronic Communication
lecture: 1
source: L1 Introduction to Electronic Communication.pdf
---

# Introduction to Electronic Communication

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Next: [[Fundamentals of Electronics and Signals]]
>
> [[L1 Introduction to Electronic Communication.pdf|Lecture slides]] - [[ENEL700 T1.pdf|Tutorial 1]] - [[Tut1.excalidraw]] -[[ENEL700 T1A.pdf|Tutorial 1 answers]]

## Core idea

Electronic communication transfers information from a source to a destination by converting it into a signal, adapting that signal to a transmission medium, and recovering the information at the far end. The same model applies to radio, telephony, fiber links, computer networks, radar, sonar, and many other systems.

## General communication-system model

```text
information source -> transmitter -> channel/medium -> receiver -> destination
                                      + noise
```

- **Transmitter:** converts the original electrical information signal into a form suitable for the chosen medium. Typical stages include oscillators, amplifiers, tuned circuits, filters, modulators, mixers, and frequency synthesisers.
- **Channel or medium:** carries the signal. Examples include twisted pair, coaxial cable, optical fibre, free space, and specialised media such as water for sonar.
- **Receiver:** selects the desired signal, amplifies it, demodulates or detects it, and reconstructs the information in a usable form.
- **Noise:** unwanted random electrical energy added to the wanted signal. Noise makes accurate recovery harder.
- **Attenuation:** reduction in signal level as it propagates. The receiver must still recover the signal after channel loss and noise have degraded it.
- **Transceiver:** combines transmitting and receiving functions in one unit, as in phones, radios, and modems.

> [!important] System-design viewpoint
> A communication system is successful when the receiver can distinguish the wanted information from attenuation, noise, interference, and distortion.

## Direction of communication

| Mode | Direction | Example |
| --- | --- | --- |
| **Simplex** | One way only | Broadcast radio, television, pager |
| **Half duplex** | Both ways, but only one party transmits at a time | Two-way or push-to-talk radio |
| **Full duplex** | Both ways simultaneously | Telephone call |

Duplexing describes the direction and timing of communication; it is different from multiplexing, which is about sharing a channel among multiple signals.

## Analogue and digital signals

- An **analogue signal** varies continuously in time and amplitude. Examples include an audio voltage, a sine wave, and an analogue video waveform.
- A **digital signal** uses discrete levels or symbols, commonly binary 0 and 1.
- A signal can change form during transmission. Digital data may modulate an analogue carrier, while an analogue source may first be digitised by an ADC and then transported as bits.

The origin of the information does not determine the form used on the channel. The transmission medium and system requirements determine the most suitable signalling method.

## Baseband and broadband transmission

### Baseband

The original information signal is sent directly, without shifting it onto a carrier. Examples include voice on a simple intercom wire and binary pulses on some wired networks.

### Broadband or passband

The information changes a higher-frequency **carrier**, producing a modulated signal suitable for radio transmission or a band-limited channel. Common analogue methods are:

- **AM:** information changes carrier amplitude.
- **FM:** information changes carrier frequency.
- **PM:** information changes carrier phase.

At the receiver, **demodulation** or **detection** extracts the original baseband information. A **modem** performs modulation and demodulation for data transmission.

 
%% $f(t) = Acos(\omega t+\phi)$
$w = 2\pi f$
$F(t) = a/2(cos)$

Cover above equations relations to topic  %%

## Why modulation is used

Modulation makes the information signal compatible with the medium and allocated frequency band. It enables practical antennas, frequency translation, channel sharing, selective reception, and in some schemes improved resistance to noise.

For digital data, examples include frequency-shift keying, where binary symbols select different carrier frequencies, and phase-shift keying, where they select different carrier phases.

## Multiplexing

**Multiplexing** combines multiple independent signals so they can share one physical medium. A multiplexer combines them at the transmitter and a demultiplexer separates them at the receiver.

The principal forms introduced in this course are:

- **Frequency-division multiplexing (FDM):** each signal occupies a different frequency band.
- **Time-division multiplexing (TDM):** each signal uses a different time slot.
- **Code-division multiplexing/multiple access (CDM/CDMA):** signals share time and frequency but use distinguishable codes.

## Frequency, wavelength, and propagation

**Frequency** is the number of cycles per second and is measured in hertz. **Wavelength** is the distance travelled during one cycle.

$$
\lambda = \frac{v}{f}
$$

For an electromagnetic wave in free space, $v \approx c = 3\times10^8\ \text{m/s}$, so:

$$
\lambda = \frac{3\times10^8}{f}
$$

### Worked example

For $f=4\ \text{MHz}$:

$$
\lambda=\frac{3\times10^8}{4\times10^6}=75\ \text{m}
$$

Higher frequency therefore means shorter wavelength. Frequency and wavelength influence antenna size, propagation, component design, and the available bandwidth.

## Electromagnetic spectrum

| Region | Approximate range | Typical uses from the lecture |
| --- | ---: | --- |
| ELF/VF | 30 Hz-3 kHz | Very low-frequency and voice-frequency signals |
| VLF/LF | 3-300 kHz | Long-wave services |
| MF | 300 kHz-3 MHz | AM broadcasting |
| HF | 3-30 MHz | Short-wave, amateur, government, and military links |
| VHF | 30-300 MHz | FM broadcasting and television |
| UHF | 300 MHz-3 GHz | Television, cellular, and other radio services |
| SHF/microwave | 3-30 GHz | Satellite, radar, wireless LANs |
| EHF | 30-300 GHz | Millimetre-wave links, radar, satellite |
| Optical | Above radio/millimetre waves | Infrared, visible light, fibre optics |

Spectrum is a shared and finite resource. Regulatory agencies allocate frequency bands, while technical standards ensure transmitters and receivers are compatible.

## Bandwidth

- **Signal bandwidth:** the portion of the frequency spectrum occupied by a signal.
- **Channel bandwidth:** the frequency range a channel can pass or that is allocated to a service.

A channel must be wide enough for the wanted signal spectrum. More information rate, sharper pulses, or more complex modulation often requires more bandwidth, creating a central engineering trade-off between capacity, signal quality, spectrum use, power, and complexity.

## Applications

The same communication principles appear in broadcasting, telephone systems, two-way radio, radar, sonar, navigation, telemetry, remote control, satellite links, LANs, MANs, WANs, and the Internet.

## Quick recall

- Every system contains a transmitter, channel, receiver, and some noise.
- Simplex is one-way; half duplex alternates; full duplex is simultaneous.
- Modulation adapts information to a carrier and medium.
- Multiplexing lets several signals share one channel.
- $\lambda=c/f$, so increasing frequency decreases wavelength.
- Bandwidth measures occupied or usable frequency range.

## Practice prompts

1. Draw the general communication-system model and state the function of each block.
2. Distinguish modulation, multiplexing, and duplexing.
3. Classify a broadcast, push-to-talk radio, and telephone call by direction.
4. Calculate wavelength from frequency and explain why the result matters physically.
5. Explain why digital information may still need an analogue carrier.
