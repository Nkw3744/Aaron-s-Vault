---
lecture: 9
---

# Architectural Design

> [!info] Course navigation
> [[Embedded Systems Overview|Subject overview]] · [[Embedded Systems Roadmap|Course roadmap]] · [[Lecture-09.pdf|Lecture 9 overview]] · Previous: [[Software Engineering for Embedded Systems]] · Next: [[Modularizing Embedded Projects]]

## Core Ideas

- The **superloop** (`while(1)`) architecture: simple, but timing depends on the longest path through the loop.
- **Interrupt-driven** designs: ISRs handle time-critical events; keep them short and communicate via flags/buffers.
- **Finite state machines** model system behaviour cleanly - the final-project startup sequence is a state machine.
- **Cooperative** schedulers run tasks to completion; **pre-emptive** schedulers/RTOS can interrupt tasks for higher-priority work.
- Event-driven design and the priority event scheduler used on the lab board.

## Source Material

- [[Lecture-09.pdf|Lecture 9 - Embedded Software Design B: Architectural Design]]
- Applied in [[Final Project Overview|the laser simulator firmware]]
