---
aliases:
  - ENME601 Week 1
  - Introduction and Basics Concept
lecture: 1
source: L1 Introduction and Basics Concept.pdf
---

# Thermodynamic Systems and Basic Concepts

> [!info] Course navigation
> [[Thermodynamics Overview|Subject overview]] - [[Thermodynamics Roadmap|Course roadmap]] - [[Thermodynamics Practice Index|Practice index]] - [[Thermodynamics Reference Index|References]] - Next: [[Energy Transfer and the First Law]]
>
> [[L1 Introduction and Basics Concept.pdf|Lecture 1 slides]] - [[Ch 1 INTRODUCTION AND BASIC CONCEPTS.pdf|Textbook Chapter 1]] - [[Ch1 Questions.pdf|Chapter 1 questions]] - [[Ch1 Answers.pdf|answers]]

## Related diagram

- [[Drawing 2026-07-16 14.58.37.excalidraw|Foundations and properties sketch]]

## Core idea

Thermodynamics studies relationships among energy, matter, and the macroscopic properties used to describe equilibrium states. Every analysis starts by choosing a system boundary, identifying mass and energy interactions, specifying the state, and applying consistent units and physical laws.

## Thermodynamics and energy

**Thermodynamics** is the science of energy and energy conversion. Engineering applications include power plants, refrigeration and heat pumps, renewable energy, thermal storage, waste-heat recovery, and intelligent energy systems.

- **Classical thermodynamics:** macroscopic approach used in this course. Matter is treated as a continuum and described through bulk properties such as pressure, temperature, and volume.
- **Statistical thermodynamics:** microscopic approach that explains macroscopic behaviour using molecular states, motion, and probability.
- **Heat transfer:** studies rates and mechanisms of heat transfer once a temperature difference exists. Thermodynamics determines possible end states and energy balances but usually does not determine how fast the process occurs.

### First and second laws

- **First law:** energy quantity is conserved. Energy can change form or cross a boundary, but it cannot be created or destroyed.
- **Second law:** energy has quality and real processes have a preferred direction. Heat flows spontaneously from high to low temperature, and converting heat completely into work in a cycle is impossible.

A proposed process must satisfy both laws.

## Systems, surroundings, and boundaries

- **System:** quantity of matter or region in space selected for study.
- **Surroundings:** everything external to the system.
- **Boundary:** real or imaginary surface separating system and surroundings. It may be fixed or moving.
- **Control surface:** boundary of a control volume.

| System type | Mass crossing boundary? | Energy crossing boundary? | Example |
| --- | --- | --- | --- |
| Closed system/control mass | No | Yes | Sealed piston-cylinder |
| Open system/control volume | Yes | Yes | Turbine, compressor, nozzle |
| Isolated system | No | No | Ideal perfectly sealed, insulated system |

> [!important] Boundary choice matters
> The same physical device can yield different heat and mass interactions under different boundaries. If a heat exchanger control volume encloses both streams, heat transfer between the streams is internal; if it encloses only one stream, that heat crosses the boundary.

## Properties

A **property** is a measurable or calculable macroscopic characteristic of a system.

- **Intensive property:** independent of system size, such as $T$, $P$, density $\rho$, and specific volume $v$.
- **Extensive property:** proportional to system size, such as mass $m$, total volume $V$, total energy $E$, and internal energy $U$.
- **Specific property:** an extensive property divided by mass, for example $u=U/m$, $e=E/m$, and $v=V/m$.

### Density and specific volume

$$
\rho=\frac{m}{V}\quad[\text{kg/m}^3]
$$

$$
v=\frac{V}{m}=\frac{1}{\rho}\quad[\text{m}^3/\text{kg}]
$$

Gases are highly compressible, so their density changes strongly with pressure and temperature. Most liquids and solids can often be treated as incompressible.

### Worked example: density

For $m=800\ \text{g}=0.8\ \text{kg}$ and $V=900\ \text{mL}=9.00\times10^{-4}\ \text{m}^3$:

$$
\rho=\frac{0.8}{9.00\times10^{-4}}=8.89\times10^2\ \text{kg/m}^3
$$

## State and equilibrium

A **state** is the condition of a system described by a set of fixed properties. Thermodynamic property tables describe equilibrium states.

Thermodynamic equilibrium requires all relevant forms of equilibrium simultaneously:

- **Thermal equilibrium:** no temperature difference within the system.
- **Mechanical equilibrium:** no unbalanced pressure force or time-varying pressure distribution.
- **Phase equilibrium:** masses of each phase remain stable.
- **Chemical equilibrium:** composition does not change with time.

### State postulate

> The state of a simple compressible system is completely specified by two independent intensive properties.

A **simple compressible system** has no significant electrical, magnetic, surface-tension, gravitational, or motion effects. If additional effects matter, additional independent properties are needed.

Two properties are independent if one can vary while the other is held fixed. In a saturated liquid-vapour mixture, $P$ and $T$ are not independent because saturation pressure fixes saturation temperature.

## Processes and cycles

A **process** changes a system from state 1 to state 2. A full description includes initial state, final state, and path. Heat and work depend on the path; properties depend only on the end states.

| Process | Constant property |
| --- | --- |
| Isothermal | Temperature, $T$ |
| Isobaric | Pressure, $P$ |
| Isochoric/isometric | Volume, $V$, or specific volume, $v$ |
| Adiabatic | No heat transfer, $Q=0$ |

A **cycle** is a sequence of processes that returns the system to its initial state. Every property has zero net change over a cycle:

$$
\Delta E_{cycle}=\Delta U_{cycle}=0
$$

The net heat and net work over a cycle need not be zero; the first law requires them to be equal in magnitude under the usual sign convention.

## Steady-flow process

A steady-flow control volume has no change with time in its mass or total energy content. Properties may vary from one location to another, but at a fixed inlet or outlet they remain constant with time.

Turbines, compressors, pumps, nozzles, and heat exchangers are often modelled this way after start-up transients have ended.

> [!note] Steady does not mean uniform
> A nozzle can have different inlet and outlet pressures and velocities while still operating steadily. Steady means no time variation at each fixed location.

## Temperature

Temperature measures thermal state and determines the direction of spontaneous heat transfer. Absolute temperature must be used in relations such as the ideal-gas equation and Carnot limits.

$$
T(K)=T(^\circ C)+273.15
$$

$$
T(^\circ F)=1.8T(^\circ C)+32
$$

$$
T(^\circ R)=T(^\circ F)+459.67=1.8T(K)
$$

Temperature differences satisfy:

$$
\Delta T(K)=\Delta T(^\circ C),\qquad \Delta T(^\circ R)=\Delta T(^\circ F)
$$

## Pressure

Pressure is normal force per unit area:

$$
P=\frac{F}{A}
$$

$$
1\ \text{Pa}=1\ \text{N/m}^2,\quad
1\ \text{bar}=100\ \text{kPa},\quad
1\ \text{atm}=101.325\ \text{kPa}
$$

Thermodynamic equations use **absolute pressure**, measured relative to a perfect vacuum. Most gauges display gauge pressure relative to the local atmosphere:

$$
P_{abs}=P_{atm}+P_{gauge}
$$

For a vacuum reading $P_{vac}$:

$$
P_{abs}=P_{atm}-P_{vac}
$$

Pressure and temperature must be absolute in gas equations.

## Thermodynamic problem-solving method

1. Restate the problem and list knowns and unknowns.
2. Draw a schematic with the system/control-volume boundary and label mass, heat, and work interactions.
3. State assumptions: steady, adiabatic, negligible kinetic/potential changes, ideal gas, incompressible, and so on.
4. Write the applicable physical laws before inserting numbers.
5. Determine required properties using tables or equations of state.
6. Substitute using consistent units and show a logical calculation path.
7. Check units, sign, magnitude, assumptions, and physical reasonableness.

Use enough figures during intermediate work, then report a final precision consistent with the input data.

## Quick recall

- Choose the boundary before writing an energy or mass balance.
- Closed systems exclude mass transfer; control volumes allow it.
- Intensive properties do not scale with mass; extensive properties do.
- Two independent intensive properties fix a simple compressible state.
- A process has a path; a cycle returns to the initial state.
- Use Kelvin and absolute pressure in thermodynamic equations.

## Practice prompts

1. Classify a sealed tank, open mug, thermos, compressor, and piston-cylinder.
2. Distinguish properties from heat and work interactions.
3. Identify whether pairs such as $(P,T)$ are independent in single-phase and saturated states.
4. Convert between gauge and absolute pressure and between temperature scales.
5. Draw a fully labelled control volume for a heat exchanger under two different boundary choices.
