---
lecture: 5-6
---

# Embedded Digital Communications

> [!info] Course navigation
> [[Embedded Systems Overview|Subject overview]] · [[Embedded Systems Roadmap|Course roadmap]] · [[Lecture-05.pdf|Lecture 5 overview]] · [[Lecture-06.pdf|Lecture 6 overview]] · Previous: [[Advanced MCUs and Microprocessors]] · Next: [[Embedded Hardware Design]]

## Core Ideas

- Serial versus parallel communication, and synchronous versus asynchronous transfer.
- **UART/USART**: asynchronous framing (start/data/parity/stop bits), baud rate, and no shared clock; used for the PC link in the labs and final project.
- **SPI**: synchronous, full-duplex, master/slave with MOSI/MISO/SCLK/SS; fast and simple but uses a select line per slave.
- **I2C / TWI**: two-wire (SDA/SCL) multi-drop bus with 7-bit addressing; slower but wires many devices on two lines.
- Choosing a bus: distance, speed, number of devices, pin count, and noise immunity.

## Source Material

- [[Lecture-05.pdf|Lecture 5 - Embedded Digital Communications A]]
- [[Lecture-06.pdf|Lecture 6 - Embedded Digital Communications B]]
- Related host side: [[File Handling and Serial Ports]]
