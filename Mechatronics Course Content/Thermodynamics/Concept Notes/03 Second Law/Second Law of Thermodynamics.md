---
aliases:
  - ENME601 Week 6
  - The Second Law of Thermodynamics
lecture: 6
source: L6 The Second Law of Thermodynamics.pdf
---

# Second Law of Thermodynamics

> [!info] Course navigation
> [[Thermodynamics Overview|Subject overview]] - [[Thermodynamics Roadmap|Course roadmap]] - [[Thermodynamics Practice Index|Practice index]] - [[Thermodynamics Reference Index|References]] - Previous: [[Control Volumes and Steady-Flow Systems]]
>
> [[L6 The Second Law of Thermodynamics.pdf|Lecture 6 slides]] - [[Ch 6 THE SECOND LAW OF THERMODYNAMICS.pdf|Textbook Chapter 6]]

## Core idea

The first law conserves energy but does not determine process direction or the maximum possible performance of a device. The second law establishes direction, distinguishes energy quality, and sets upper limits for heat engines, refrigerators, and heat pumps.

## Why the first law is not enough

The first law alone would not forbid:

- A hot drink becoming hotter in a cooler room without other effects.
- Heat supplied to a wire converting completely to electricity.
- Heat supplied to a paddle wheel causing it to rotate with no other change.

These processes conserve energy but do not occur spontaneously. A valid process must satisfy both the first and second laws.

The second law is used to:

- Determine the possible direction of a process.
- Establish theoretical performance limits.
- Compare energy quality.
- Identify unavoidable losses or irreversibilities.

## Thermal energy reservoirs

A **thermal energy reservoir** has enough thermal capacity to supply or absorb finite heat without an appreciable temperature change.

- High-temperature reservoir supplying heat: **source** at $T_H$.
- Low-temperature reservoir absorbing heat: **sink** at $T_L$.

Atmosphere, oceans, lakes, and large furnaces can often be modelled as reservoirs.

## Heat engines

A heat engine:

1. Receives $Q_H$ from a high-temperature source.
2. Converts part of it to net work $W_{net,out}$.
3. Rejects $Q_L$ to a low-temperature sink.
4. Operates on a cycle.

For a cycle:

$$
W_{net,out}=Q_H-Q_L
$$

Thermal efficiency is desired output divided by required input:

$$
\eta_{th}=\frac{W_{net,out}}{Q_H}
$$

$$
\eta_{th}=1-\frac{Q_L}{Q_H}
$$

Efficiency is dimensionless and always less than 1 for a real cyclic heat engine.

### Rankine-cycle example

A steam power plant illustrates a heat-engine cycle:

```text
pump -> boiler -> turbine -> condenser -> pump
```

- Boiler supplies $Q_H$ and produces high-energy steam.
- Turbine produces shaft work.
- Condenser rejects $Q_L$ and returns steam to liquid.
- Pump consumes work to raise liquid pressure.

$$
W_{net,out}=W_{turbine,out}-W_{pump,in}
$$

Waste heat rejected by the condenser may still be useful for process heating or a lower-temperature cycle, but it cannot all be converted to work within the same heat-engine cycle.

## Kelvin-Planck statement

> No device operating in a cycle can receive heat from a single reservoir and produce an equal amount of net work with no other effect.

Consequences:

- A heat engine must reject some heat: $Q_L>0$.
- A cyclic heat engine cannot be 100% efficient.
- A perpetual-motion machine of the second kind is impossible.

## Refrigerators and heat pumps

Both devices use work input to move heat from a low-temperature region to a high-temperature region:

$$
W_{net,in}=Q_H-Q_L
$$

The cycle is the same; the desired effect differs.

### Refrigerator

Desired output is heat removed from the cold space:

$$
COP_R=\frac{Q_L}{W_{net,in}}
$$

$$
COP_R=\frac{Q_L}{Q_H-Q_L}
$$

### Heat pump

Desired output is heat delivered to the warm space:

$$
COP_{HP}=\frac{Q_H}{W_{net,in}}
$$

$$
COP_{HP}=\frac{Q_H}{Q_H-Q_L}
$$

Because $Q_H=Q_L+W_{net,in}$:

$$
COP_{HP}=COP_R+1
$$

A COP may exceed 1 because the device transfers existing heat in addition to converting work input; COP is not a heat-engine efficiency.

## Vapour-compression refrigeration cycle

```text
compressor -> condenser -> expansion device -> evaporator -> compressor
```

1. Compressor raises refrigerant pressure and temperature using work input.
2. Condenser rejects $Q_H$ and condenses the refrigerant.
3. Capillary tube or valve throttles it to a lower pressure and temperature.
4. Evaporator absorbs $Q_L$ from the refrigerated region and vaporises the refrigerant.

## Clausius statement

> No cyclic device can have as its sole effect the transfer of heat from a colder body to a hotter body.

Thus a refrigerator or heat pump requires work or another energy input. The Clausius and Kelvin-Planck statements are equivalent expressions of the second law.

## Reversible and irreversible processes

A **reversible process** can be reversed with no net change to the system or surroundings. It is an ideal limit, not a process achieved exactly in practice.

Common irreversibilities include:

- Friction.
- Unrestrained expansion.
- Mixing.
- Heat transfer through a finite temperature difference.
- Electrical resistance.
- Combustion and chemical reaction.
- Shock, turbulence, and other dissipative effects.

Reversible processes:

- Produce the maximum possible work for a given expansion.
- Require the minimum possible work for a given compression.
- Establish upper performance limits for real devices.

### Internal, external, and total reversibility

- **Internally reversible:** no irreversibility inside the system boundary.
- **Externally reversible:** no irreversibility in the surroundings or at the system-surroundings interaction.
- **Totally reversible:** both internally and externally reversible.
- **Quasi-equilibrium:** the system remains infinitesimally close to equilibrium; necessary for reversibility but not sufficient if friction or finite temperature differences remain.

## Carnot cycle

The Carnot heat-engine cycle consists of four internally reversible processes between $T_H$ and $T_L$:

1. Isothermal heat addition at $T_H$ with expansion.
2. Adiabatic reversible expansion from $T_H$ to $T_L$.
3. Isothermal heat rejection at $T_L$ with compression.
4. Adiabatic reversible compression from $T_L$ to $T_H$.

Reversing these processes gives a Carnot refrigerator or heat pump.

## Carnot principles

1. An irreversible heat engine is less efficient than a reversible engine operating between the same reservoirs.
2. All reversible heat engines operating between the same two reservoirs have the same efficiency.

Therefore performance limits depend only on reservoir temperatures, not the working fluid or device design.

## Carnot heat-engine efficiency

For a reversible engine:

$$
\left(\frac{Q_L}{Q_H}\right)_{rev}=\frac{T_L}{T_H}
$$

$$
\eta_{th,rev}=1-\frac{T_L}{T_H}
$$

Temperatures must be absolute, in kelvin or rankine.

For any real engine operating between these reservoirs:

$$
\eta_{th}<\eta_{th,rev}
$$

### Worked example

For $T_H=600\ \text{K}$ and $T_L=300\ \text{K}$:

$$
\eta_{max}=1-\frac{300}{600}=0.50=50\%
$$

A claimed engine above 50% between these reservoirs is impossible.

## Carnot refrigerator and heat pump

Maximum refrigerator COP:

$$
COP_{R,rev}=\frac{T_L}{T_H-T_L}
=\frac{1}{T_H/T_L-1}
$$

Maximum heat-pump COP:

$$
COP_{HP,rev}=\frac{T_H}{T_H-T_L}
=\frac{1}{1-T_L/T_H}
$$

For real devices:

$$
COP_R<COP_{R,rev},\qquad COP_{HP}<COP_{HP,rev}
$$

Reducing the temperature lift $T_H-T_L$ raises COP. This is why heat exchangers with small approach-temperature differences and moderate supply temperatures improve heat-pump performance.

### Worked example

For $T_L=270\ \text{K}$ and $T_H=300\ \text{K}$:

$$
COP_{R,max}=\frac{270}{300-270}=9
$$

$$
COP_{HP,max}=\frac{300}{300-270}=10
$$

and $COP_{HP}=COP_R+1$ as expected.

## Energy quality

Work can be completely converted to heat, but heat cannot be completely converted to work in a cycle. Heat at a higher temperature has greater ability to produce work relative to the same environment, so it is higher-quality energy.

The Carnot expression shows that raising $T_H$ or lowering $T_L$ increases the fraction of heat that could ideally become work. Practical designs nevertheless face material, safety, environmental, and cost limits.

## Performance decision table

| Device | Desired output | Required input | Performance measure |
| --- | --- | --- | --- |
| Heat engine | $W_{net,out}$ | $Q_H$ | $\eta_{th}=W_{net,out}/Q_H$ |
| Refrigerator | $Q_L$ | $W_{net,in}$ | $COP_R=Q_L/W_{net,in}$ |
| Heat pump | $Q_H$ | $W_{net,in}$ | $COP_{HP}=Q_H/W_{net,in}$ |

## Quick recall

- The second law sets direction and upper performance limits.
- Heat engines must reject heat; $\eta_{th}<1$.
- Refrigerators and heat pumps require work input.
- $COP_{HP}=COP_R+1$.
- Reversible devices define best possible performance.
- Carnot formulas require absolute temperatures.

## Practice prompts

1. Calculate $W_{net}$, $\eta_{th}$, $COP_R$, and $COP_{HP}$ from heat transfers.
2. Test a claimed device against Kelvin-Planck or Clausius.
3. Identify irreversibilities in an actual power or refrigeration cycle.
4. Calculate Carnot limits from reservoir temperatures.
5. Explain why reducing temperature lift improves refrigeration and heat-pump COP.
