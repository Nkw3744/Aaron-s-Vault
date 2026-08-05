---
aliases:
  - ENEL700 Week 12
  - L12 Modern Telecommunication Systems and Measurements
lecture: 12
source: L12 Modern Telecommunication Systems and Measurements.pdf
---

# Modern Telecommunication Systems and Measurements

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Introduction to Computer Networks]]
>
> [[L12 Modern Telecommunication Systems and Measurements.pdf|Lecture slides]] - [[ENEL700 T12.pdf|Tutorial 12]]

## Core idea

Modern telecommunications combines the course's earlier building blocks - media, antennas, modulation, multiplexing, coding, networks, and measurements - into complete wired, optical, satellite, cellular, and short-range wireless systems. Measurement closes the engineering loop by showing whether a real implementation meets its frequency, power, modulation, noise, and interface requirements.

## Communication hardware

### Transmission lines

Wires, cables, coaxial lines, waveguides, and fibre guide energy between system blocks. At high frequencies, a line must be treated as a distributed system with characteristic impedance. Mismatch causes reflections, standing waves, power loss, and possible transmitter stress.

### Antennas

Antennas convert guided RF energy to electromagnetic waves and back. Forms named in the lecture include dipoles, monopoles, loops, microstrip patches, helices, and aperture antennas. Choice depends on frequency, bandwidth, gain, polarisation, pattern, size, and environment.

### Microwave components

At microwave frequencies, waveguides, resonators, specialised diodes, and historically microwave tubes provide low-loss guiding, filtering, oscillation, amplification, and frequency conversion.

### EMI and EMC

- **Electromagnetic interference (EMI):** unwanted coupling that degrades a device or system.
- **Electromagnetic compatibility (EMC):** ability to operate correctly without causing or suffering unacceptable interference.

Shielding, grounding, filtering, cable routing, controlled impedance, and enclosure design support EMC.

## Internet technologies

Internet connectivity carries email, files, web traffic, e-commerce, images, voice over IP, video, telemedicine, conferencing, and cloud services.

- **Cloud computing:** processing and storage are delivered over networked infrastructure.
- **Internet of Things:** sensors and actuators exchange measurements and commands.
- **Machine-to-machine communication:** devices communicate with limited or no direct human input.
- **Security:** confidentiality, integrity, authentication, availability, and safe device management are system requirements rather than optional additions.

These applications depend on the layered networking ideas in [[Introduction to Computer Networks]] and on the capacity, error control, and signal-quality concepts developed earlier in the course.

## Satellite communication

A satellite link includes a transmitting earth station, uplink, satellite payload/transponder, downlink, and receiving station.

Important system choices include:

- Orbit and coverage footprint.
- Propagation delay and path loss.
- Ground-station antenna gain and pointing.
- Uplink/downlink frequency allocation.
- Power and noise-temperature budget.

Applications include broadcasting, long-distance communications, remote-area coverage, navigation, and the Global Positioning System. Satellite performance is analysed with a link budget, combining transmitter power, antenna gains, propagation losses, receiver noise, and required SNR or $E_b/N_0$.

## Telecommunication services

The lecture connects traditional telephone, facsimile, paging, and Internet telephony systems. VoIP digitises and packetises speech, then transports it over IP networks. It replaces a continuously reserved circuit with packet-based sharing, but must manage delay, jitter, loss, clock recovery, and quality of service.

## Optical communication

Optical fibre confines light by total internal reflection between core and cladding.

```text
electrical data -> LED/laser -> optical fibre -> photodetector -> electrical data
```

- **LED/laser:** optical source; lasers generally support higher power, narrower spectrum, and higher rates.
- **Fibre cable:** low-loss, high-bandwidth medium immune to electromagnetic pickup.
- **Photodetector:** converts received light to current.
- **Wavelength-division multiplexing (WDM):** carries multiple channels on different optical wavelengths.
- **Passive optical network (PON):** shares fibre using passive splitters between provider and users.
- **Photonic integration/all-optical processing:** integrates optical functions and reduces repeated electrical conversion.

### Optical power budget

In dB form:

$$
P_{rx}=P_{tx}+G_{system}-L_{fibre}-L_{connectors}-L_{splices}-L_{splitters}-L_{margin}
$$

The received power must exceed receiver sensitivity with adequate engineering margin.

## Cellular evolution

| Generation | Representative systems in the lecture | Main direction |
| --- | --- | --- |
| 1G | AMPS | Analogue cellular voice |
| 2G | GSM, IS-95 | Digital voice, messaging, improved capacity |
| 3G | WCDMA, CDMA2000, TD-SCDMA | Packet data and mobile Internet |
| 4G | LTE, LTE-Advanced | All-IP mobile broadband |
| Later evolution | 5G | Higher capacity, lower latency, diverse devices/services |

Cellular systems reuse frequencies across geographically separated cells. Mobility requires registration, resource scheduling, power control, and handover between cells.

## Other wireless technologies

- **Wireless LAN:** local high-rate networking.
- **Bluetooth/PAN:** short-range personal-area connectivity.
- **Zigbee and mesh:** low-power devices and multi-hop coverage.
- **WiMAX/MAN:** metropolitan-area broadband concept.
- **Infrared:** short-range optical wireless links.
- **RFID:** identifies or senses tagged objects using radio coupling.
- **NFC:** very-short-range communication and identification.
- **Ultrawideband:** very wide occupied bandwidth for short-range data, ranging, or positioning.

Technology selection depends on range, rate, latency, energy, topology, interference, licensing, security, and cost.

## SCADA in smart grids

A supervisory control and data acquisition (SCADA) system connects field sensors, meters, relays, remote terminal units, and programmable controllers to a supervisory control centre.

```text
field measurements/control -> RTU or PLC -> communication network -> master station/HMI
```

In a smart grid it supports remote measurement, alarms, equipment status, and control actions. The communication design must prioritise availability, deterministic or bounded delay for critical functions, redundant paths, time synchronisation, authentication, and protection against unauthorised commands.

## Communication measurements

### General-purpose instruments

- **Multimeter:** DC/low-frequency voltage, current, resistance, and continuity.
- **Oscilloscope:** waveform amplitude versus time, timing, pulse shape, distortion, and modulation envelope.
- **Signal/function generator:** known stimulus for testing gain, response, and demodulation.
- **Frequency counter:** precise carrier or clock frequency.

### RF-specific instruments

- **RF voltmeter/probe:** high-frequency voltage with controlled loading.
- **Power meter/dummy load:** transmitter output power without radiating.
- **SWR meter:** standing-wave ratio and impedance-match quality.
- **Spectrum analyser:** power versus frequency, occupied bandwidth, harmonics, spurs, and sidebands.
- **Network analyser:** frequency-dependent magnitude and phase of transmission/reflection; commonly expressed through S-parameters.
- **Field-strength meter:** radiated signal level at a location.
- **Sweep generator:** stimulus across a frequency range for response measurements.

### Transmitter tests

- Carrier-frequency accuracy and stability.
- Output power.
- Modulation depth/deviation and occupied bandwidth.
- Harmonics, spurious emissions, and spectral mask.
- Antenna/transmission-line match.

### Receiver tests

- Sensitivity or MDS at a specified SINAD/BER.
- Noise figure/noise floor.
- Selectivity and adjacent-channel rejection.
- Blocking and strong-signal behaviour.
- Intermodulation and third-order intercept.
- Recovered output power and distortion.

> [!important] Measurement rule
> A result is meaningful only when its conditions are stated: frequency, bandwidth, impedance, detector mode, reference level, modulation, termination, and required output quality.

## System-level checklist

When analysing a modern communication system, ask:

1. What information and rate must be transported?
2. Which medium and frequency band are used?
3. Which modulation, multiplexing, and coding schemes are used?
4. What power, bandwidth, latency, and error-rate targets apply?
5. What are the dominant losses, noise sources, and interference paths?
6. How are addressing, access, mobility, and security handled?
7. Which measurements prove compliance and performance?

## Quick recall

- Modern systems are combinations of the same transmitter-channel-receiver principles.
- Link and power budgets add gains and subtract losses in dB.
- WDM separates optical channels by wavelength.
- Cellular generations progressed from analogue voice to all-IP broadband.
- A spectrum analyser measures frequency content; a network analyser measures transfer/reflection versus frequency.
- Receiver sensitivity must always be quoted with a quality criterion such as SINAD or BER.

## Practice prompts

1. Build a block diagram and link budget for a satellite or optical link.
2. Compare fibre, cellular, WLAN, Bluetooth, Zigbee, and satellite for a given application.
3. Choose instruments to measure carrier accuracy, occupied bandwidth, antenna match, and receiver sensitivity.
4. Explain how WDM and cellular frequency reuse increase capacity in different domains.
5. Write a complete test condition for a receiver-sensitivity measurement.
