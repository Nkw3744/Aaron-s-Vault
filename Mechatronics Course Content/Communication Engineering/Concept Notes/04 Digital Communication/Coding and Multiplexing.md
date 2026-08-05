---
aliases:
  - ENEL700 Week 10
  - L10 Coding and Multiplexing
lecture: 10
source: L10 Coding and Multiplexing.pdf
---

# Coding and Multiplexing

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Information Theory]] - Next: [[Introduction to Computer Networks]]
>
> [[L10 Coding and Multiplexing.pdf|Lecture slides]] - [[ENEL700 T10.pdf|Tutorial 10]] - [[ENEL700 T10A.pdf|Tutorial 10 answers]]

## Core idea

Channel coding adds carefully designed redundancy so errors can be detected or corrected. Multiplexing shares a physical channel among many information streams. Duplexing shares resources between the two directions of a link, while line coding and pulse shaping determine how digital bits appear on a baseband medium.

## Shannon's coding result and limit

For a channel of capacity $C$, coding can make error probability arbitrarily small when information rate $R<C$, provided sufficiently long codes and delay are allowed. This is a limit, not a claim that uncoded transmission is error-free.

Simple repetition illustrates the trade-off: repeating each bit three times allows majority logic to correct one error in the triplet, but reduces useful rate to one-third and still fails if multiple bits are wrong. Efficient codes protect blocks or streams instead of treating every bit independently.

For AWGN with infinite bandwidth and noise density $N_0$, Shannon's limit gives the minimum bit-energy ratio for reliable communication:

$$
\left(\frac{E_b}{N_0}\right)_{min}=\ln2\approx0.693=-1.59\ \text{dB}
$$

No real code can support arbitrarily reliable communication below this theoretical limit.

## Channel coding and overhead

Channel encoding transforms $k$ information bits into $n$ transmitted bits, with $n>k$. The code rate is:

$$
R_c=\frac{k}{n}
$$

Lower $R_c$ means more redundancy and usually stronger protection, but also more bandwidth, time, or energy per information bit.

## Error detection

- **Repetition/redundancy:** sends data multiple times; simple but inefficient.
- **Parity:** adds one bit so a word has an even or odd number of 1s. It detects any odd number of bit errors but cannot reliably detect an even number.
- **Longitudinal redundancy check/block check character:** XORs corresponding bit positions across a block to form an additional check word.
- **CRC:** treats the bit sequence as a polynomial and transmits the remainder after division by a generator polynomial. The receiver repeats the division; a non-zero remainder indicates an error. CRCs are especially strong against burst errors.

Detection alone normally requires retransmission through an ARQ protocol. When retransmission is too slow or impossible, forward error correction is used.

## Forward error correction

### Block codes

A block code maps every $k$-bit message to a unique $n$-bit code word. Valid code words are separated in Hamming distance, allowing received errors to be located relative to the valid set.

- Hamming codes add parity bits positioned to identify and correct bit errors.
- Reed-Solomon codes operate on multi-bit symbols and are effective against burst damage.
- Interleaving rearranges symbols before transmission so a physical burst becomes separated errors that a code can correct.

### Convolutional codes

Convolutional encoders process a continuous bit stream through a shift register. Output bits are XOR combinations of the current bit and earlier stored bits, so the output depends on encoder memory. The receiver chooses the most likely path through the encoder state sequence, commonly with a Viterbi-style decoder.

| Block code | Convolutional code |
| --- | --- |
| Operates on fixed $k$-bit blocks | Operates continuously |
| Code word depends on current block | Output depends on present and previous bits |
| Described by $(n,k)$ and distance | Described by rate, memory, and constraint length |

## Multiplexing

Multiplexing combines two or more signals on one cable, fibre, or radio link. It reduces infrastructure cost and increases use of available capacity.

### Frequency-division multiplexing

Each input modulates a different subcarrier. The modulated channels occupy separate frequency bands and are added to form a composite signal.

At the receiver, a bank of band-pass filters separates the subchannels and individual demodulators recover the sources. Guard bands and filtering prevent adjacent-channel overlap.

Applications in the lecture include telemetry, legacy telephone carrier systems, cable television, and FM stereo broadcasting.

### Time-division multiplexing

Each input uses the full channel bandwidth, but only during its assigned time slot. A frame groups slots for the participating sources.

- Well suited to digital data.
- Requires framing, clocks, and synchronisation.
- Synchronous TDM reserves slots even when a source has nothing to send; statistical multiplexing can allocate slots on demand.

### Code-division multiple access

Users share time and frequency but are separated by codes. A receiver correlates with the desired user's code to despread it while other users appear more noise-like. This links directly to DSSS in [[Digital Modulation]].

## Multiplexing comparison

| Method | Resource divided | Separation mechanism | Main requirement |
| --- | --- | --- | --- |
| FDM | Frequency | Filters and subcarriers | Guard bands/selective filters |
| TDM | Time | Frames and time slots | Accurate synchronisation |
| CDMA | Code | Correlation with spreading code | Code control and power management |

## Duplexing

- **Half duplex:** directions take turns.
- **Full duplex:** directions operate simultaneously.

### FDD

Frequency-division duplexing assigns separate frequency channels to uplink and downlink. It is straightforward and continuous but consumes paired spectrum and needs filtering to isolate simultaneous transmit and receive paths.

### TDD

Time-division duplexing alternates the two directions in different time slots on the same frequency. It saves paired spectrum and can adapt the uplink/downlink ratio, but needs guard times and precise synchronisation to prevent collisions.

> [!important] Do not confuse these terms
> FDM/TDM/CDMA separate multiple users or information streams. FDD/TDD separate the two directions of a bidirectional link.

## Line coding

Line coding maps bits to electrical baseband pulses.

- **NRZ:** level does not return to zero during a bit interval. Variants include unipolar, polar, and bipolar forms.
- **RZ:** pulse returns to zero within each bit interval.
- **AMI:** successive 1s alternate polarity; reduces DC and creates violation-based error checks.
- **Manchester/biphase:** guaranteed mid-bit transition provides self-clocking but uses more bandwidth.
- **Run-length-limited and substitution codes:** prevent long transition-free sequences; examples include BnZS and HDB3.

A useful line code balances bandwidth, timing recovery, DC content, error visibility, and implementation complexity.

## Pulse shaping and intersymbol interference

Rectangular pulses contain large high-frequency components. A band-limited channel spreads each pulse into neighbouring symbol intervals, causing **intersymbol interference (ISI)**.

The Nyquist zero-ISI condition requires the combined pulse response to be non-zero at its own decision instant and zero at all other symbol decision instants.

An ideal sinc pulse satisfies this condition but is non-causal, infinite in time, and highly sensitive to timing error. A practical **raised-cosine filter** introduces a gradual spectral roll-off controlled by roll-off factor $\alpha$:

$$
B=\frac{R_s}{2}(1+\alpha)
$$

for the one-sided baseband bandwidth convention. Larger $\alpha$ uses more bandwidth but shortens and smooths the time-domain pulse, easing implementation and timing.

## Quick recall

- Channel coding trades code rate for reliability.
- Parity/CRC detect; FEC also corrects without retransmission.
- Block codes work on words; convolutional codes have memory.
- FDM separates in frequency, TDM in time, CDMA by code.
- FDD/TDD concern link direction, not multiple data streams.
- Pulse shaping controls bandwidth and ISI.

## Practice prompts

1. Calculate code rate and overhead for an $(n,k)$ block code.
2. Compare parity, CRC, block FEC, and convolutional FEC.
3. Draw transmitter and receiver structures for FDM and TDM.
4. Choose FDD or TDD for symmetric and asymmetric traffic cases.
5. Explain why raised-cosine shaping is preferred to rectangular or ideal sinc pulses.
