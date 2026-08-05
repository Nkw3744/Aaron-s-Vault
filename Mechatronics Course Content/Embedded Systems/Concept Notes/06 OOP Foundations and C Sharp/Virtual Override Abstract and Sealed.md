---
lecture: 17
---

# Virtual, Override, Abstract and Sealed

> [!info] Course navigation
> [[Embedded Systems Overview|Subject overview]] · [[Embedded Systems Roadmap|Course roadmap]] · [[Lecture-17.pdf|Lecture 17 overview]] · Previous: [[Static Inheritance and Polymorphism]] · Next: [[The NET Framework and Memory Management]]

## Core Ideas

- `virtual` methods can be replaced in a derived class with `override`; this enables runtime (dynamic) dispatch.
- `abstract` classes cannot be instantiated and may declare methods with no body that derived classes must implement.
- **Interfaces** define a contract of members with no implementation - the basis of the final project's `IAppBoard` abstraction.
- `sealed` prevents further inheritance or overriding.
- Choosing between abstract classes and interfaces for extensibility.

## Source Material

- [[Lecture-17.pdf|Lecture 17 - OOP Part C: Virtual, Override, Abstract, Sealed]]
