---
lecture: 3
---

# MCU Memory Architecture and Clocking

> [!info] Course navigation
> [[Embedded Systems Overview|Subject overview]] · [[Embedded Systems Roadmap|Course roadmap]] · [[Lecture-03.pdf|Lecture 3 overview]] · Previous: [[Microcontroller Operation and Architecture]] · Next: [[Advanced MCUs and Microprocessors]]

## Core Ideas

- Harvard architecture (separate program and data buses, as in AVR) versus von Neumann (shared bus).
- Memory types: flash for program code, SRAM for variables and the stack, and EEPROM for non-volatile settings.
- Program memory is word-addressed; data memory holds registers, I/O space, and SRAM.
- Clock sources: internal RC oscillator, external crystal, and how the system clock feeds peripherals.
- Prescalers divide the clock for timers, the ADC, and communication baud-rate generators; this sets timing resolution and range.

## Source Material

- [[Lecture-03.pdf|Lecture 3 - MCU Memory Architecture & Clocking]]
