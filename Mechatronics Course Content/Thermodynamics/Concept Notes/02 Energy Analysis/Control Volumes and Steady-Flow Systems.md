---
aliases:
  - ENME601 Week 5
  - Open Steady Flow Systems
  - Mass and Energy Analysis of Control Volumes
lecture: 5
source: L5 Open, Steady Flow Systems.pdf
source_reviewed: 2026-07-22
source_scope: Lecture 5, Textbook Chapter 5, and current 2026 formula sheet
---

# Control Volumes: Steady and Uniform-Flow Systems

> [!info] Course navigation
> [[Thermodynamics Overview|Subject overview]] - [[Thermodynamics Roadmap|Course roadmap]] - [[Thermodynamics Practice Index|Practice index]] - [[Thermodynamics Reference Index|References]] - Previous: [[Closed-System Energy Analysis]] - Next: [[Second Law of Thermodynamics]]
>
> [[L5 Open, Steady Flow Systems.pdf|Lecture 5 slides]] - [[Ch 5 MASS AND ENERGY ANALYSIS OF CONTROL VOLUMES.pdf|Textbook Chapter 5]] - [[Ch5 Questions.pdf|Chapter 5 questions]]

## Core idea

An open system or control volume allows mass to cross its control surface. Each flowing stream carries enthalpy, kinetic energy, and potential energy. Under steady operation, mass and energy stored inside do not change with time, so inlet and outlet rates balance with heat and work interactions.

## Steady-flow assumptions

A steady-flow process has:

- No time variation of properties at any fixed point.
- Constant mass and total energy inside the control volume.
- Constant inlet and outlet states and flow rates.
- Heat and work rates that do not change with time.

Properties may differ from inlet to outlet and from location to location. Steady does not mean the fluid has uniform pressure, temperature, or velocity.

## Mass and volume flow rates

Volume flow rate through a cross-section is:

$$
\dot V=V_{avg}A\quad[\text{m}^3/\text{s}]
$$

Mass flow rate is:

$$
\dot m=\rho\dot V=\rho V_{avg}A
$$

Using specific volume $v=1/\rho$:

$$
\dot m=\frac{V_{avg}A}{v}
$$

Here $V_{avg}$ denotes average speed and $\dot V$ denotes volume flow rate; distinguish them carefully.

## Conservation of mass

General rate balance:

$$
\sum\dot m_{in}-\sum\dot m_{out}=\frac{dm_{CV}}{dt}
$$

At steady state:

$$
\sum\dot m_{in}=\sum\dot m_{out}
$$

For one inlet and one outlet:

$$
\dot m_1=\dot m_2
$$

$$
\rho_1V_1A_1=\rho_2V_2A_2
$$

For incompressible flow with constant density:

$$
V_1A_1=V_2A_2
$$

## Transient and uniform-flow processes

When mass or energy stored inside the control volume changes with time, the process is transient rather than steady. Integrated over a process interval, mass conservation is

$$
\sum m_{in}-\sum m_{out}=m_2-m_1.
$$

A **uniform-flow process** is a useful transient model in which each inlet and outlet stream has uniform properties while crossing the boundary, and the contents of the control volume are represented by uniform end states. With heat into and work out positive:

$$
Q-W=
\sum_{out}m\left(h+\frac{V^2}{2}+gz\right)
-\sum_{in}m\left(h+\frac{V^2}{2}+gz\right)
+(m_2e_2-m_1e_1)_{CV},
$$

where stored specific energy is

$$
e=u+\frac{V^2}{2}+gz.
$$

If kinetic and potential terms are negligible:

$$
Q-W=\sum_{out}m h-\sum_{in}m h+(m_2u_2-m_1u_1)_{CV}.
$$

Typical applications include filling or emptying a rigid tank. Do not use the steady-flow equation when the control-volume mass or stored energy changes between states.

## Flow work and enthalpy

Pressure forces must push fluid into and out of a control volume. Flow work for a volume $V$ is:

$$
W_{flow}=PV
$$

Per unit mass:

$$
w_{flow}=Pv
$$

A non-flowing unit mass carries:

$$
e_{nonflow}=u+\frac{V^2}{2}+gz
$$

Adding flow work gives the energy of a flowing stream:

$$
e_{flow}=u+Pv+\frac{V^2}{2}+gz
$$

Since $h=u+Pv$:

$$
e_{flow}=h+\frac{V^2}{2}+gz
$$

The energy rate carried by mass is:

$$
\dot E_{mass}=\dot m\left(h+\frac{V^2}{2}+gz\right)
$$

This is why enthalpy, rather than internal energy alone, appears in control-volume balances.

## Steady-flow energy equation

Using heat into the control volume as positive and work out as positive:

$$
\dot Q-\dot W=
\sum_{out}\dot m\left(h+\frac{V^2}{2}+gz\right)
-\sum_{in}\dot m\left(h+\frac{V^2}{2}+gz\right)
$$

For one inlet and one outlet:

$$
\dot Q-\dot W=\dot m\left[(h_2-h_1)+\frac{V_2^2-V_1^2}{2}+g(z_2-z_1)\right]
$$

Or:

$$
\dot Q-\dot W=\dot m(\Delta h+\Delta e_k+\Delta e_p)
$$

If kinetic and potential changes are negligible:

$$
\dot Q-\dot W=\dot m(h_2-h_1)
$$

> [!warning] Unit conversion
> $V^2/2$ and $gz$ are in J/kg when SI base units are used. Divide them by $1000$ before adding to enthalpy in kJ/kg.

## Nozzles and diffusers

- **Nozzle:** increases velocity at the expense of pressure/enthalpy.
- **Diffuser:** slows the flow and raises pressure/enthalpy.

Typical assumptions: steady, adiabatic, no shaft work, negligible elevation change.

$$
h_1+\frac{V_1^2}{2}=h_2+\frac{V_2^2}{2}
$$

For a nozzle, $V_2>V_1$ usually means $h_2<h_1$.

## Turbines and compressors

### Turbine

A turbine converts a fluid enthalpy drop into shaft work. With adiabatic operation and negligible kinetic/potential changes:

$$
\dot W_{out}=\dot m(h_1-h_2)
$$

### Compressor

A compressor consumes shaft work to increase gas pressure. Under the same simplifying assumptions:

$$
\dot W_{in}=\dot m(h_2-h_1)
$$

Intentional compressor cooling means $\dot Q$ cannot be neglected. A pump is similar but handles a liquid and is often analysed with $w_{pump}\approx v(P_2-P_1)$ for an incompressible fluid.

## Throttling valves

A valve, capillary tube, or porous plug causes a large pressure drop. Typical assumptions are steady, adiabatic, no work, and negligible kinetic/potential changes:

$$
h_1=h_2
$$

Throttling is **isenthalpic**, not generally isothermal or isentropic. Temperature may rise or fall depending on the fluid and starting state.

## Mixing chambers

For an adiabatic chamber with no work and negligible kinetic/potential changes:

$$
\sum\dot m_{in}=\sum\dot m_{out}
$$

$$
\sum_{in}\dot m h=\sum_{out}\dot m h
$$

For two inlets and one outlet:

$$
\dot m_1h_1+\dot m_2h_2=(\dot m_1+\dot m_2)h_3
$$

Both mass and energy balances are required.

## Heat exchangers

Two streams exchange energy while remaining separated.

### Each stream as its own control volume

With no work and negligible kinetic/potential changes:

$$
\dot Q_{stream}=\dot m(h_{out}-h_{in})
$$

### Entire heat exchanger as one control volume

If external heat loss is negligible, transfer between streams is internal:

$$
\dot m_h(h_{h,in}-h_{h,out})
=\dot m_c(h_{c,out}-h_{c,in})
$$

Heat lost by the hot stream equals heat gained by the cold stream.

## Pipe and duct flow

Pipes and ducts may include heat transfer, fans, pumps, heaters, elevation changes, and velocity changes. Start with the full SFEE:

$$
\dot Q-\dot W=\dot m\left[\Delta h+\frac{V_2^2-V_1^2}{2}+g(z_2-z_1)\right]
$$

Simplify only after evaluating the actual geometry and equipment. Elevation can matter in long pipelines, and kinetic energy can matter where diameter changes greatly.

## Device summary

| Device | Usually negligible | Dominant relation |
| --- | --- | --- |
| Nozzle/diffuser | $\dot Q$, $\dot W$, $\Delta PE$ | $\Delta h+\Delta e_k=0$ |
| Turbine | $\dot Q$, $\Delta KE$, $\Delta PE$ | $\dot W_{out}=\dot m(h_1-h_2)$ |
| Compressor | Often $\dot Q$, $\Delta KE$, $\Delta PE$ | $\dot W_{in}=\dot m(h_2-h_1)$ |
| Throttle | $\dot Q$, $\dot W$, $\Delta KE$, $\Delta PE$ | $h_1=h_2$ |
| Mixing chamber | $\dot Q$, $\dot W$, $\Delta KE$, $\Delta PE$ | $\sum\dot m h_{in}=\sum\dot m h_{out}$ |
| Heat exchanger, whole | External $\dot Q$, $\dot W$, $\Delta KE$, $\Delta PE$ | Hot-stream loss = cold-stream gain |
| Pipe/duct | Case-dependent | Start with full SFEE |

## Problem-solving workflow

1. Draw the control volume and label every inlet, outlet, heat transfer, and work interaction.
2. State steady or transient operation.
3. Apply mass conservation first.
4. Determine each inlet/outlet state and obtain $h$, $v$, or other required properties.
5. Write the full SFEE, then cross out terms only with physical justification.
6. Convert velocity/elevation energy units consistently.
7. Check whether the result matches device behaviour: turbine work out, compressor work in, nozzle acceleration, throttle constant $h$.

## Quick recall

- Steady state means no time accumulation inside the control volume.
- $\dot m=\rho V_{avg}A$.
- Flow energy is $h+V^2/2+gz$ because $h=u+Pv$.
- Apply mass balance before energy balance.
- Throttles are isenthalpic.
- Device simplifications are assumptions to justify, not automatic rules.

## Practice prompts

1. Calculate mass flow from area, velocity, and density.
2. Apply the full SFEE to a one-inlet, one-outlet device.
3. Determine nozzle exit speed from an enthalpy drop.
4. Calculate turbine output or compressor input from inlet and outlet enthalpies.
5. Solve a two-stream mixing or heat-exchanger energy balance.
