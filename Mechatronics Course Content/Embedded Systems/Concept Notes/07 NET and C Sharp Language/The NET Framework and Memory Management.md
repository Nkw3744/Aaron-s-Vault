---
lecture: 18
---

# The .NET Framework and Memory Management

> [!info] Course navigation
> [[Embedded Systems Overview|Subject overview]] · [[Embedded Systems Roadmap|Course roadmap]] · [[Lecture-18.pdf|Lecture 18 overview]] · [[Lecture-Week-10.pdf|Week 10 consolidation]] · Previous: [[Virtual Override Abstract and Sealed]] · Next: [[C Sharp Fundamentals]]

## Core Ideas

- Process memory layout: code, static data, the **stack** (locals, call frames), and the **heap** (dynamic objects).
- Value types live on the stack; reference types live on the managed heap, with the variable holding a reference.
- The **CLR** and Common Type System; C# compiles to IL, then JIT-compiles to native code.
- **Automatic garbage collection**: roots and reachability, compaction ("free and slide"), and generational collection - no manual `malloc`/`free`.
- Stack overflow, why embedded engineers avoid deep recursion, and the timer-vs-communication threading bug.
- `.NET Framework` vs modern `.NET`, `unsafe`/pinning, and NuGet ("like pip").

## Source Material

- [[Lecture-18.pdf|Lecture 18 - .NET Framework & Automatic Memory Management]]
- [[Lecture-Week-10.pdf|Week 10 - .NET & C# Concepts]]
