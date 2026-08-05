---
aliases:
  - ENME601 Week 4
  - Energy Analysis of Closed Systems
lecture: 4
source: L4 Energy Analysis of Closed Systems.pdf
---

# Closed-System Energy Analysis

> [!info] Course navigation
> [[Thermodynamics Overview|Subject overview]] - [[Thermodynamics Roadmap|Course roadmap]] - [[Thermodynamics Practice Index|Practice index]] - [[Thermodynamics Reference Index|References]] - Previous: [[Properties and Phase Change of Pure Substances]] - Next: [[Control Volumes and Steady-Flow Systems]]
>
> [[L4 Energy Analysis of Closed Systems.pdf|Lecture 4 slides]] - [[Ch 4 ENERGY ANALYSIS OF CLOSED SYSTEMS.pdf|Textbook Chapter 4]] - [[Ch4 Questions.pdf|Chapter 4 questions]] - [[Ch4 Answers.pdf|answers]]

## Core idea

A closed system contains a fixed mass. Its energy changes through heat and work, not mass flow. Piston-cylinder problems additionally require boundary work, found from the process path on a $P-V$ diagram.

## Closed-system balance

No mass crosses a closed-system boundary. Using $Q>0$ into the system and $W>0$ by the system:

$$
Q-W=\Delta E
$$

$$
Q-W=\Delta U+\Delta KE+\Delta PE
$$

For a stationary system with negligible changes in speed and elevation:

$$
Q-W=\Delta U=m(u_2-u_1)
$$

If work contains moving-boundary and other components:

$$
W=W_b+W_{other}
$$

Always draw heat and work arrows and state the sign convention before substituting values.

## Moving-boundary work

For a quasi-equilibrium piston motion:

$$
\delta W_b=P\,dV
$$

$$
W_b=\int_{V_1}^{V_2}P\,dV
$$

Boundary work is the area under the process curve on a $P-V$ diagram.

- Expansion: $dV>0$, so $W_b>0$; the system does work.
- Compression: $dV<0$, so $W_b<0$; work is done on the system.
- Different paths between the same states give different boundary work.
- Net cyclic boundary work is the area enclosed by the cycle.

The integral uses the pressure at the moving boundary and requires a quasi-equilibrium path so that a meaningful system pressure is defined.

## Common boundary-work processes

### Constant pressure

$$
W_b=P(V_2-V_1)
$$

With $P$ in kPa and $V$ in $\text{m}^3$, $W_b$ is in kJ.

### Constant volume

$$
W_b=0
$$

A rigid tank may still exchange heat or shaft/electrical work; only moving-boundary work is zero.

### Isothermal ideal gas

For fixed $m$, $R$, and $T$:

$$
PV=mRT=\text{constant}
$$

$$
W_b=mRT\ln\left(\frac{V_2}{V_1}\right)
$$

Equivalent forms are:

$$
W_b=P_1V_1\ln\left(\frac{V_2}{V_1}\right)
=P_2V_2\ln\left(\frac{V_2}{V_1}\right)
$$

For an ideal gas, $u$ depends only on temperature, so an isothermal process has $\Delta U=0$. Therefore the energy balance gives $Q=W_b$.

### Polytropic ideal gas

$$
PV^n=\text{constant}
$$

For $n\neq1$:

$$
W_b=\frac{P_2V_2-P_1V_1}{1-n}
=\frac{P_1V_1-P_2V_2}{n-1}
$$

Using the ideal-gas relation:

$$
W_b=\frac{mR(T_2-T_1)}{1-n}
$$

The isothermal result is the limiting $n=1$ case.

### Reversible adiabatic ideal gas

For a quasi-equilibrium, adiabatic ideal-gas process with approximately constant specific heats:

$$
PV^k=\text{constant},\qquad k=\frac{c_p}{c_v}
$$

$$
W_b=\frac{P_2V_2-P_1V_1}{1-k}
$$

Adiabatic alone does not guarantee $PV^k=\text{constant}$; reversibility/quasi-equilibrium assumptions are also needed.

## Constant-pressure closed-system process

For a stationary closed system at constant pressure:

$$
Q-W_b-W_{other}=\Delta U
$$

Since $W_b=P(V_2-V_1)$:

$$
Q-W_{other}=\Delta U+P\Delta V
$$

Using $H=U+PV$:

$$
Q-W_{other}=\Delta H=m(h_2-h_1)
$$

If boundary work is the only work, constant-pressure heat transfer equals enthalpy change:

$$
Q=\Delta H
$$

## Specific heats

- $c_v$: energy required per unit mass per degree at constant volume; related to internal energy.
- $c_p$: energy required per unit mass per degree at constant pressure; related to enthalpy.

Differential definitions are:

$$
c_v=\left(\frac{\partial u}{\partial T}\right)_v
$$

$$
c_p=\left(\frac{\partial h}{\partial T}\right)_p
$$

Units are $\text{kJ/(kg K)}$, numerically the same per degree Celsius difference.

## Ideal-gas internal energy and enthalpy

For an ideal gas, $u$, $h$, $c_v$, and $c_p$ depend only on temperature:

$$
\Delta u=\int_{T_1}^{T_2}c_v(T)\,dT
$$

$$
\Delta h=\int_{T_1}^{T_2}c_p(T)\,dT
$$

With constant or average specific heats:

$$
u_2-u_1\approx c_{v,avg}(T_2-T_1)
$$

$$
h_2-h_1\approx c_{p,avg}(T_2-T_1)
$$

Total changes are:

$$
\Delta U=mc_{v,avg}\Delta T,qquad
\Delta H=mc_{p,avg}\Delta T
$$

These property-change relations are valid for any ideal-gas process; the subscripts indicate how the properties are defined, not that the actual process must be constant volume or pressure.

For improved accuracy over a large temperature range, use tabulated ideal-gas $u(T)$ and $h(T)$ values or integrate variable specific heats.

### Ideal-gas specific-heat relations

$$
c_p-c_v=R
$$

$$
k=\frac{c_p}{c_v}
$$

For a gas, $c_p>c_v$ because constant-pressure heating includes energy associated with expansion.

## Incompressible solids and liquids

For an incompressible substance, $v$ is nearly constant and:

$$
c_p\approx c_v\approx c
$$

$$
\Delta u\approx c_{avg}\Delta T
$$

$$
\Delta U\approx mc_{avg}\Delta T
$$

From $h=u+Pv$:

$$
\Delta h\approx c_{avg}\Delta T+v(P_2-P_1)
$$

- For solids or liquids with a small pressure change, $\Delta h\approx\Delta u\approx c\Delta T$.
- For a nearly isothermal liquid pump, $\Delta h\approx v\Delta P$.

## Problem-solving workflow

1. Identify the fixed mass and draw its boundary.
2. Mark heat and every work mode, including boundary, shaft, electrical, or spring work.
3. Determine whether $\Delta KE$ and $\Delta PE$ matter.
4. Identify the substance model: table-based pure substance, ideal gas, or incompressible material.
5. Determine boundary work from the actual process relation, not merely from end states.
6. Apply $Q-W=\Delta U+\Delta KE+\Delta PE$.
7. Check work and heat signs against expansion/compression and heating/cooling.

## Equation selection table

| Process/model | Boundary work |
| --- | --- |
| Constant $P$ | $P(V_2-V_1)$ |
| Constant $V$ | $0$ |
| Isothermal ideal gas | $mRT\ln(V_2/V_1)$ |
| Polytropic ideal gas, $n\neq1$ | $(P_2V_2-P_1V_1)/(1-n)$ |
| Reversible adiabatic ideal gas | Polytropic result with $n=k$ |

## Quick recall

- Closed system: no mass transfer.
- $W_b=\int P\,dV$ and depends on the process path.
- Expansion work is positive under the classical convention.
- Stationary closed system: $Q-W=\Delta U$.
- Ideal-gas $u$ and $h$ depend only on temperature.
- $c_p-c_v=R$ and $k=c_p/c_v$.

## Practice prompts

1. Calculate boundary work for constant-pressure, isothermal, and polytropic paths.
2. Compare two paths between identical end states and explain why $\Delta U$ matches but $Q$ and $W$ differ.
3. Solve a rigid-tank energy balance.
4. Use property tables versus ideal-gas specific heats for a closed-system process.
5. Analyse an incompressible liquid process with temperature and pressure changes.
