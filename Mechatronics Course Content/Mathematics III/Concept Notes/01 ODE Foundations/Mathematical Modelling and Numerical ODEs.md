---
course: ENGE702
type: concept
source_reviewed: 2026-07-22
source_scope: Lectures 1-3, annotated notes L1-L3, Tutorials 1-2
---

# Mathematical Modelling and Numerical ODEs

> [!info] Course navigation
> [[Mathematics III Overview|Subject overview]] · [[Mathematics III Roadmap|Course roadmap]] · [[Mathematics III Practice Index|Practice index]] · Next: [[First-Order Differential Equations]]
>
> Sources: [[Lecture 1 Slides Math Modelling and ODEs.pdf|Lecture 1]] · [[L1_note.pdf|annotated Lecture 1]] · [[ODE 1|Lecture 1 transcript]] · [[Lecture 2 Slides Math Modelling and ODEs.pdf|Lecture 2]] · [[L2_note.pdf|annotated Lecture 2]] · [[ODE 2|Lecture 2 transcript]] · [[Lecture 3 Slides Numerical Methods and Direction Fields.pdf|Lecture 3]] · [[L3_note.pdf|annotated Lecture 3]] · [[Tutorial 1 ENGE702.pdf|Tutorial 1]] · [[Tutorial 2 ENGE702.pdf|Tutorial 2]]

## Core idea

A mathematical model translates physical assumptions into equations, solves or approximates those equations, and then interprets the result in the physical system. The equation is never the whole model: variables, units, sign conventions, initial conditions, parameter assumptions, and the range where the model is credible all matter.

## Modelling cycle

1. **Define the system and question.** State what is being predicted and choose dependent and independent variables.
2. **State assumptions.** Examples include constant parameters, negligible drag, perfect mixing, small displacement, or no heat loss.
3. **Apply physical principles.** Typical starting points are force balance, conservation of mass, conservation of energy, or an electrical circuit law.
4. **Form the differential equation.** Include initial or boundary conditions and check dimensions.
5. **Solve or approximate.** Use an analytic, numerical, or qualitative method appropriate to the equation.
6. **Interpret and validate.** Check units, signs, limiting behaviour, initial conditions, and whether the answer remains physically plausible.
7. **Refine if necessary.** A model can be mathematically correct under its assumptions and still be unsuitable for the real system.

> [!important] A model is conditional
> A solution belongs to the assumptions used to derive it. Changing drag, damping, heat loss, forcing, or boundary behaviour can change both the equation and its solution.

## Differential-equation language

An ordinary differential equation (ODE) relates an unknown function to one or more derivatives with respect to a single independent variable.

- **Order:** the highest derivative present.
- **Linear ODE:** the unknown function and its derivatives occur to the first power and are not multiplied together.
- **General solution:** contains arbitrary constants.
- **Particular solution:** constants have been fixed, commonly by initial conditions.
- **Initial-value problem (IVP):** an ODE plus data at a starting point, such as $y(x_0)=y_0$.

### Checking a proposed solution

1. Differentiate the proposed function as required.
2. Substitute the function and derivatives into the ODE.
3. Simplify both sides.
4. Check every initial or boundary condition separately.
5. Confirm the function is defined on the interval being discussed.

## Three kinds of solution information

- **Analytic:** an exact formula, available for suitable equations.
- **Numerical:** approximate values or a computed trajectory.
- **Qualitative:** information such as increase/decrease, equilibrium, long-term behaviour, or oscillation without a closed formula.

These approaches complement one another. A direction field can expose implausible behaviour in an algebraic answer, while an analytic solution can be used to assess a numerical approximation.

## Direction or slope fields

For an ODE written as

$$
y'=f(x,y),
$$

the number $f(x,y)$ is the slope of a solution curve passing through $(x,y)$. A direction field draws a short line segment with that slope at each sampled point.

### Workflow

1. Rearrange the ODE into $y'=f(x,y)$.
2. Choose an $(x,y)$ grid.
3. Evaluate $f(x,y)$ at each grid point.
4. Draw short slope segments.
5. Trace a curve from the specified initial condition, always following the local field.

Direction fields help identify equilibrium curves, regions of growth or decay, and whether different initial conditions converge or diverge. They do not by themselves provide an exact formula.

### MATLAB pattern from Lecture 3

- Use `meshgrid` to construct sample points.
- Use horizontal component $U=1$ and vertical component $V=f(X,Y)$.
- Plot with `quiver(X,Y,U,V)`.
- Plot selected trajectories with an ODE solver such as `ode23`.

## Euler's method

Euler's method approximates the IVP

$$
y'=f(x,y), \qquad y(x_0)=y_0
$$

by following the current tangent for one step at a time:

$$
x_{n+1}=x_n+h,
$$

$$
y_{n+1}=y_n+h f(x_n,y_n).
$$

### Table workflow

For each row record:

1. $n$;
2. $x_n$;
3. $y_n$;
4. the slope $f(x_n,y_n)$;
5. the next value $y_{n+1}=y_n+h f(x_n,y_n)$.

Lecture 3 applies this to

$$
y'+2y=x, \qquad y(0)=1,
$$

so the update function is $f(x,y)=x-2y$. Tutorial 2 combines the same skills: draw a slope field, trace an IVP, and then compute Euler estimates.

### Accuracy and checks

- A smaller step $h$ generally improves the approximation but increases the number of calculations.
- Euler's method is a first-order method and accumulates local approximation error.
- Decreasing $h$ is useful only if the values begin to stabilise; it is not proof that the model itself is valid.
- Compare the numerical path with the direction field and, when available, an analytic solution or a higher-quality solver.
- Keep signs and the evaluation point straight: the slope is evaluated at $(x_n,y_n)$, not at the unknown next point.

## Engineering modelling connections

- A falling body begins with a force balance and leads to a second-order equation for position; adding drag changes the model.
- A mass-spring-damper system leads to [[Second-Order Differential Equations and Oscillations]].
- A circuit balance can lead to the first-order RL model in [[First-Order Differential Equations]] or the second-order RLC model in [[Laplace Transforms]].
- An energy balance supplies the physical principle in [[Energy Transfer and the First Law]], while an ODE can describe how temperature or stored energy changes with time.

## Common mistakes

- Starting algebra before defining variables and signs.
- Treating a general solution as an IVP solution without applying the initial data.
- Accepting a formula because it looks plausible without substituting it back.
- Reading a direction field as a set of disconnected arrows rather than local tangent information.
- Applying Euler's update with the wrong slope or inconsistent step size.
- Reporting numerical precision that the model assumptions do not justify.

## Practice sequence

1. [[Tutorial 1 ENGE702.pdf|Tutorial 1]] — integration-based ODEs, IVPs, verification, and introductory models.
2. [[Tutorial 2 ENGE702.pdf|Tutorial 2]] — slope fields, Euler's method, separable equations, integrating factors, and an RL circuit.
3. Continue to [[First-Order Differential Equations]] for exact first-order solution methods.
