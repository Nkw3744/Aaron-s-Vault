---
aliases:
  - ENME601 Week 2
  - Energy, Energy Transfer, and General Energy Analysis
lecture: 2
source: L2 Energy, Energy Transfer, and General Energy Analysis.pdf
source_reviewed: 2026-07-30
source_scope: Lecture 2, Tutorial Week 2 questions, and current ideal-gas practice covering pressure conversion, absolute temperature, gas constants, two-state fixed-mass relations, connected tanks, and constant-pressure energy balances
---

# Energy Transfer and the First Law

> [!info] Course navigation
> [[Thermodynamics Overview|Subject overview]] - [[Thermodynamics Roadmap|Course roadmap]] - [[Thermodynamics Practice Index|Practice index]] - Previous: [[Thermodynamic Systems and Basic Concepts]] - Next: [[Properties and Phase Change of Pure Substances]]
>
> [[L2 Energy, Energy Transfer, and General Energy Analysis.pdf|Lecture 2 slides]] - [[Week 2 slides 1-2.pptx|current Week 2 slides]] - [[Ch 2 ENERGY, ENERGY TRANSFER, AND GENERAL ENERGY ANALYSIS.pdf|Textbook Chapter 2]] - [[Ch2 Questions.pdf|Chapter 2 questions]] - [[Ch2 Answers.pdf|answers]] - [[Tutorial Week 2 Questions 2026.pdf|Tutorial Week 2]] - [[Thermodynamics Tutorial 2 2.pptx|current Tutorial 2 slides]]
>
> Current ideal-gas practice: [[Tutorial Week 3 Question list.pdf|questions 9–14]] · [[Q9-Q14 Ideal gas.pdf|worked solutions]]

## Core idea

Energy is stored in a system as internal, kinetic, and potential energy and crosses a boundary by heat, work, or mass flow. The first law is an accounting rule: net energy entering a system equals the increase in energy stored within it.

## Forms of energy

For a simple system with electrical, magnetic, and surface effects neglected:

$$
E=U+KE+PE
$$

$$
E=U+m\frac{V^2}{2}+mgz
$$

On a per-unit-mass basis:

$$
e=u+\frac{V^2}{2}+gz
$$

where $V$ is speed, not volume, and $z$ is elevation relative to a chosen datum.

### Internal energy

Internal energy $U$ is microscopic energy stored within matter:

- **Sensible energy:** molecular translation, rotation, and vibration; closely related to temperature.
- **Latent energy:** molecular arrangement associated with phase.
- **Chemical energy:** energy of chemical bonds.
- **Nuclear energy:** energy within atomic nuclei.

Thermal energy commonly refers to sensible plus latent internal energy.

## Stored energy versus energy transfer

- Internal, kinetic, and potential energy are **stored** in the system and are properties.
- Heat and work are **energy interactions** recognised only while crossing the boundary.
- A system contains energy; it does not contain heat or work.

## Heat transfer

Heat $Q$ is energy transferred solely because of a temperature difference.

- Heat into the system is positive under the classical sign convention.
- Heat out is negative.
- An **adiabatic process** has $Q=0$; it is not necessarily isothermal.

Specific heat transfer:

$$
q=\frac{Q}{m}\quad[\text{kJ/kg}]
$$

Heat transfer over time:

$$
Q_{1-2}=\int_{t_1}^{t_2}\dot Q\,dt
$$

For constant $\dot Q$:

$$
Q=\dot Q\Delta t
$$

### Heat-transfer example

A $2\ \text{kg}$ object receives $30\ \text{kJ}$ in $5\ \text{s}$:

$$
\dot Q=\frac{30}{5}=6\ \text{kW}
$$

$$
q=\frac{30}{2}=15\ \text{kJ/kg}
$$

## Work transfer

Work is energy transfer associated with a generalised force acting through a displacement. Examples include moving-boundary work, shaft work, spring work, electrical work, lifting, and acceleration.

Under the classical sign convention:

- Work done **by** the system is positive.
- Work done **on** the system is negative.

An alternative bookkeeping method uses only positive magnitudes with explicit `in` and `out` subscripts. Do not mix conventions within one balance.

Specific work and power are:

$$
w=\frac{W}{m}\quad[\text{kJ/kg}]
$$

$$
\dot W=\frac{dW}{dt}\quad[\text{kW}]
$$

For constant electrical voltage and current:

$$
\dot W_{elec}=VI
$$

$$
W_{elec}=VI\Delta t
$$

For time-varying voltage or current:

$$
W_{elec}=\int_{t_1}^{t_2}V(t)I(t)\,dt
$$

### Work-transfer example

If $30\ \text{kJ}$ of work enters a $2\ \text{kg}$ system over $5\ \text{s}$:

$$
\dot W_{in}=6\ \text{kW},\qquad w_{in}=15\ \text{kJ/kg}
$$

The second value means $15\ \text{kJ}$ is transferred per kilogram of system mass over the process.

### Mechanical work and power patterns

The current [[Tutorial Week 2 Questions 2026.pdf|Tutorial 2]] extends the general work definition into several engineering forms.

For lifting through a height change:

$$
W=mg(z_2-z_1),\qquad \dot W=mg\frac{dz}{dt}.
$$

For rotational shaft work and power:

$$
W_{shaft}=\int_{\theta_1}^{\theta_2}\tau\,d\theta,
$$

$$
\dot W_{shaft}=\tau\omega=2\pi N\tau,
$$

where $N$ is rotational speed in revolutions per second. Convert rpm before using the second form.

For a linear spring with $F=kx$, the work magnitude between two deflections is

$$
W_{spring}=\frac12k(x_2^2-x_1^2).
$$

Assign the sign from the selected system boundary and whether work is done by or on the system.

Power required for a kinetic-energy change over a time interval is based on

$$
\dot W=\frac{\Delta KE}{\Delta t}
=\frac{m(V_2^2-V_1^2)}{2\Delta t}
$$

when other energy transfers are absent or separately accounted for.

> [!warning] Do not use $Q=mc\Delta T$ automatically
> It describes sensible heating under an appropriate property model and no phase change. For ideal-gas internal-energy changes use $c_v$; for ideal-gas enthalpy changes use $c_p$. Phase change and real-fluid states normally require property tables.

### Tutorial 2 coverage map

[[Tutorial Week 2 Questions 2026.pdf|Tutorial 2]] applies this note to kinetic energy, energy rate versus time, sensible heating, spring work, shaft torque and power, lifting power, a closed piston-cylinder energy balance, room-energy accumulation, vehicle acceleration, and river hydro-energy potential. Keep the full question statements in the practice source; this note owns the reusable equations and system-boundary decisions.

## Path and point functions

Properties such as $U$, $T$, $P$, and $V$ are **point functions**: their changes depend only on end states. Their differentials are exact, written $dU$, $dT$, and so on.

Heat and work are **path functions**: their values depend on how the process occurs. Their differentials are inexact, written $\delta Q$ and $\delta W$.

For the same state 1 and state 2, different paths can produce different $Q$ and $W$, but the same $\Delta E$.

## First law and general energy balance

$$
E_{in}-E_{out}=\Delta E_{system}
$$

In words:

> Net energy transfer into the system by heat, work, and mass equals the change in internal, kinetic, potential, and other stored energies.

For a closed system, no energy crosses with mass:

$$
Q_{in}-Q_{out}+W_{in}-W_{out}=\Delta E
$$

Using the classical signs $Q>0$ into the system and $W>0$ out of the system:

$$
Q-W=\Delta E
$$

$$
Q-W=\Delta U+\Delta KE+\Delta PE
$$

For a stationary closed system with negligible kinetic and potential changes:

$$
Q-W=\Delta U
$$

### Rate form

$$
\dot E_{in}-\dot E_{out}=\frac{dE_{system}}{dt}
$$

The form chosen must match the system type and whether the process is transient or steady.

## Kinetic and potential energy changes

$$
\Delta KE=m\frac{V_2^2-V_1^2}{2}
$$

$$
\Delta PE=mg(z_2-z_1)
$$

When using SI values, these expressions give joules. Divide by $1000$ for kilojoules. Do not neglect either term until its scale has been checked against heat, work, or enthalpy changes.

## Ideal-gas equation of state

An equation of state relates equilibrium properties. For an ideal gas:

$$
Pv=RT
$$

Equivalent forms are:

$$
PV=mRT
$$

$$
PV=NR_uT
$$

where:

- $P$ is absolute pressure.
- $T$ is absolute temperature.
- $v=V/m$ is specific volume.
- $R$ is the gas-specific constant.
- $R_u=8.31447\ \text{kJ/(kmol K)}$.
- $M$ is molar mass in $\text{kg/kmol}$.

$$
R=\frac{R_u}{M}
$$

For a fixed mass between two states:

$$
\frac{P_1V_1}{T_1}=\frac{P_2V_2}{T_2}
$$

An ideal-gas approximation is best at relatively low pressure and high temperature, away from saturation. Dense steam in power cycles and refrigerant vapour in refrigeration cycles often requires real-fluid tables instead.

> [!warning] Unit rule
> With $P$ in kPa and $V$ in $\text{m}^3$, $PV$ is in kJ because $1\ \text{kPa m}^3=1\ \text{kJ}$.

## Analysis workflow

1. Define the system boundary.
2. List energy interactions and choose a sign convention.
3. Write $E_{in}-E_{out}=\Delta E$ before simplifying.
4. State justified assumptions such as stationary, adiabatic, or negligible $\Delta KE$ and $\Delta PE$.
5. Use an equation of state or property tables to connect the end states.
6. Check the final sign: does it match the physical direction of heat and work?

### Ideal-gas practice checks from Week 2

- Convert gauge pressure to absolute pressure before using $PV=mRT$.
- Convert Celsius to Kelvin before combining temperature with the gas law.
- Use the correct gas-specific constant or compute it from molar mass.
- For two-state fixed-mass problems, keep the mass constant and relate the end states by $P_1V_1/T_1=P_2V_2/T_2$.
- For connected tanks, compute the mass in each tank from absolute pressure, volume, and temperature before enforcing a final common equilibrium state.
- For constant-pressure energy balances, separate property change from energy transfer and do not silently replace the balance with a heating formula.

## Quick recall

### Exam device map

| Problem cue | First energy term to inspect |
| --- | --- |
| Closed piston-cylinder | moving-boundary work and $\Delta U$ |
| Shaft, pump, compressor, stirrer | shaft-work direction and power |
| Speed change | $\Delta KE=m(V_2^2-V_1^2)/2$ |
| Elevation change | $\Delta PE=mg(z_2-z_1)$ |
| Spring | $W_{spring}=\tfrac12k(x_2^2-x_1^2)$ |

Start from the complete first-law balance. Use $Q=mc\Delta T$ only after justifying a sensible-heating property model with no phase change.

- $E=U+KE+PE$.
- Heat is caused by temperature difference; work is every other energy transfer not carried by mass.
- Heat and work are path functions, not properties.
- General balance: $E_{in}-E_{out}=\Delta E$.
- Closed-system classical form: $Q-W=\Delta E$.
- Ideal gas: $Pv=RT$ with absolute $P$ and $T$.

## Practice prompts

1. Identify all stored energy and transfer terms for a heated, stirred tank.
2. Convert between total, specific, and rate quantities.
3. Apply the closed-system energy balance with both sign-convention styles.
4. Calculate kinetic and potential energy changes and justify whether they are negligible.
5. Use $PV=mRT$ to solve a two-state fixed-mass gas problem.
6. Resolve a connected-tanks problem using absolute pressure and a final common equilibrium state.
