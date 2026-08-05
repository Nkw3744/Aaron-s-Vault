---
lecture: 2
---

# Microcontroller Operation and Architecture

> [!info] Course navigation
> [[Embedded Systems Overview|Subject overview]] · [[Embedded Systems Roadmap|Course roadmap]] · [[Lecture-02.pdf|Lecture 2 overview]] · Previous: [[Embedded Systems Foundations]] · Next: [[MCU Memory Architecture and Clocking]]

## Core Ideas

- A microcontroller integrates CPU, memory, and peripherals on one chip; a microprocessor is the CPU only.
- The CPU executes the fetch-decode-execute cycle, driven by the program counter and instruction register.
- Registers, the ALU, and the status register (flags) form the datapath; buses (address, data, control) move information.
- On-chip peripherals - timers/counters, ADC, USART, SPI/TWI, PWM, and GPIO ports - are memory-mapped and configured through special-function registers.
- The AT90USB1287 is an 8-bit AVR: ports A-F, and peripheral registers are accessed by name from `Labboard.h`.

## Source Material

- [[Lecture-02.pdf|Lecture 2 - Microcontroller Operation & Architecture]]
- [[Lab Board Knowledge|Board pin maps and peripheral registers]]
