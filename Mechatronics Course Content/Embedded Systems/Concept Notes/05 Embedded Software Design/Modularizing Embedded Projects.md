---
lecture: 10
---

# Modularizing Embedded Projects

> [!info] Course navigation
> [[Embedded Systems Overview|Subject overview]] · [[Embedded Systems Roadmap|Course roadmap]] · [[Lecture-10.pdf|Lecture 10 overview]] · Previous: [[Architectural Design]] · Next: [[Advanced C Programming Techniques]]

## Core Ideas

- Splitting code into translation units (`.c`) with matching headers (`.h`); the header is the public interface.
- Header guards / `#pragma once` prevent multiple inclusion; keep implementation details out of headers.
- Driver modules wrap a peripheral behind a clean API - exactly what `Labboard.h` does for the board.
- A hardware abstraction layer (HAL) lets application code stay portable across boards.
- The linker combines object files; understand `extern`, internal vs external linkage, and static functions.

## Source Material

- [[Lecture-10.pdf|Lecture 10 - Modularizing Embedded Projects]]
- [[Library Functions Reference|Labboard.h as a module example]]
