---
course: ENGE702
type: concept
source_reviewed: 2026-07-30
source_scope: Week 3 lecture pack and handwritten notes covering second-order homogeneous ODEs, characteristic roots, initial conditions, damping classification, forced oscillations, resonance, and the mass-spring-damper model
---

# Second-Order Differential Equations and Oscillations

> [!info] Course navigation
> [[Mathematics III Overview|Subject overview]] · [[Mathematics III Roadmap|Course roadmap]] · Previous: [[First-Order Differential Equations]] · Next: [[Eigenvalues and Systems of Differential Equations]]
>
> Sources: [[Lecture 6 Second Order Homogeneous ODEs-2.pdf|Lecture 6]] · [[L6_note.pdf|annotated Lecture 6]] · [[Lecture 7 Second Order Hom ODEs.pdf|Lecture 7]] · [[Lecture 8 Second Order Hom ODEs.pdf|Lecture 8]] · [[Lecture 9 Second Order NonHom ODEs.pdf|Lecture 9]] · [[Lecture 10 Second Order NonHom ODEs.pdf|Lecture 10]] · [[Lecture 11 Second Order NonHom ODEs.pdf|Lecture 11]] · [[Week 3 lecture 3_combined final_Canvas.pdf|Week 3 lecture pack]] · [[L7_note.pdf|L7]] · [[L8_note.pdf|L8]] · [[L9_note.pdf|L9]]
>
> Current practice: [[Tutorial 2 Answers.pdf|official answers]] · [[Tutorial 2 ENGE702 Worked Solutions.pdf|official worked solutions]]

## Core idea

A second-order linear ODE carries two independent pieces of initial information, usually position and velocity. For constant-coefficient homogeneous equations, the characteristic roots determine the solution family. For non-homogeneous equations, the total response is the sum of a transient homogeneous part and a particular forced part. In oscillation problems, damping and forcing frequency control whether the response decays, resonates, or settles to a steady-state amplitude.

## Linear and homogeneous form

A second-order linear equation can be written as

$$
y''+p(x)y'+q(x)y=r(x).
$$

It is **homogeneous** when $r(x)=0$. For a homogeneous linear equation, linear combinations of solutions are also solutions. If $y_1$ and $y_2$ are linearly independent, then

$$
y=c_1y_1+c_2y_2
$$

is the general solution.

> [!important] Superposition boundary
> Superposition applies directly to homogeneous linear equations. For a non-homogeneous equation, add one particular solution to the homogeneous solution; arbitrary sums of particular solutions do not automatically satisfy the same forcing term.

## Constant-coefficient homogeneous equations

For

$$
y''+ay'+by=0,
$$

try $y=e^{\lambda x}$. Substitution gives the characteristic equation

$$
\lambda^2+a\lambda+b=0.
$$

### Root cases

- **Distinct real roots $\lambda_1,\lambda_2$:**
  $$y=c_1e^{\lambda_1x}+c_2e^{\lambda_2x}.$$
- **Repeated real root $\lambda$:**
  $$y=(c_1+c_2x)e^{\lambda x}.$$
- **Complex roots $\alpha\pm i\omega$:**
  $$y=e^{\alpha x}\left(A\cos\omega x+B\sin\omega x\right).$$

Two initial conditions determine the two constants. Always differentiate the general solution before applying a derivative condition.

### Workflow check

1. Put the ODE in standard form first.
2. Solve the characteristic equation.
3. Choose the root-case formula that matches the discriminant.
4. Differentiate the full solution before using derivative data.
5. Use both initial conditions to solve for both arbitrary constants.

## Mass-spring-damper model

With displacement $y$ measured from equilibrium:

- spring force: $F_s=-ky$;
- damping force: $F_d=-cy'$;
- Newton's law: $\sum F=my''$.

The unforced model is

$$
my''+cy'+ky=0,
$$

with $m,k>0$ and $c\geq0$.

### Undamped motion

When $c=0$:

$$
my''+ky=0,
$$

and the natural angular frequency is

$$
\omega_0=\sqrt{\frac{k}{m}}.
$$

The solution is

$$
y=A\cos\omega_0t+B\sin\omega_0t.
$$

Initial conditions change amplitude and phase but not $\omega_0$.

### Damping classification

The characteristic discriminant is $c^2-4mk$.

- **Overdamped:** $c^2>4mk$ — two decaying real modes; no inherent oscillation.
- **Critically damped:** $c^2=4mk$ — repeated root; fastest non-oscillatory return in the ideal model.
- **Underdamped:** $c^2<4mk$ — decaying oscillation:
  $$y=e^{-ct/(2m)}(A\cos\omega_dt+B\sin\omega_dt),$$
  where
  $$\omega_d=\sqrt{\frac{k}{m}-\frac{c^2}{4m^2}}.$$

The lecture notes the phase portrait logic informally: underdamped motion oscillates while the envelope decays, and the root structure explains the response type.

## Non-homogeneous equations

For

$$
y''+ay'+by=r(x),
$$

the general solution is

$$
y=y_h+y_p,
$$

where $y_h$ solves the corresponding homogeneous equation and $y_p$ is one particular solution.

## Undetermined coefficients

For suitable constant-coefficient equations, choose the trial form from the forcing:

- $ke^{\gamma x}$ → $Ke^{\gamma x}$;
- polynomial of degree $n$ → general polynomial of degree $n$;
- $k\cos\omega x$ or $k\sin\omega x$ → $K_1\cos\omega x+K_2\sin\omega x$;
- $ke^{\alpha x}\cos\omega x$ or sine counterpart → $e^{\alpha x}(K_1\cos\omega x+K_2\sin\omega x)$.

### Reusable workflow

1. Solve the homogeneous equation for $y_h$.
2. Choose a trial $y_p$ matching every independent forcing term.
3. If any trial term duplicates a homogeneous mode, multiply that term by $x$; use $x^2$ for a double overlap.
4. Differentiate and substitute.
5. Match coefficients and solve for the unknown constants.
6. Form $y=y_h+y_p$ and then apply initial data.

The overlap correction is essential: without it, substitution cannot determine the particular solution.

## Sinusoidally forced oscillation

With external forcing,

$$
my''+cy'+ky=F_0\cos\omega t.
$$

The homogeneous part is the transient. A sinusoidal particular solution describes the steady-state response after decaying transients become small.

Using $\omega_0=\sqrt{k/m}$, the steady-state amplitude is

$$
C(\omega)=\frac{F_0}{\sqrt{m^2(\omega_0^2-\omega^2)^2+c^2\omega^2}}.
$$

- Increasing damping lowers and broadens the resonance peak.
- In the ideal undamped case, forcing at $\omega=\omega_0$ produces resonance and a response with a growing $t\sin(\omega_0t)$ factor.
- When forcing and natural frequencies are close but unequal, their interference can produce beats.
- Distinguish the **transient** determined by initial conditions from the **steady-state** determined by forcing.

### Quick checks for forced oscillation questions

- Confirm whether the forcing is exactly sinusoidal or a sum of terms that require separate particular guesses.
- Check whether the trial particular solution overlaps the homogeneous basis.
- Read the requested output carefully: some questions ask for the full solution, others only for the steady-state term or amplitude.
- Keep the forcing frequency separate from the natural and damped frequencies.

## Electrical analogy

The same mathematics appears in an RLC circuit. Depending on whether charge or current is used as the state variable, the circuit balance produces a second-order linear ODE with inductance corresponding to inertia, resistance to damping, capacitance to restoring behaviour, and source voltage to forcing. This connection is revisited in [[Laplace Transforms]].

## Connections

- The exponential mode used here grows from [[First-Order Differential Equations]].
- Coupled oscillators lead to eigenvalue methods in [[Eigenvalues and Systems of Differential Equations]].
- General periodic forcing is decomposed into harmonics in [[Fourier Analysis]].
- Resonance, bandwidth, and frequency response connect to [[Fundamentals of Electronics and Signals]] and [[Amplitude Modulation]].

## Common mistakes

- Solving the characteristic equation before putting the ODE in standard form.
- Using only one arbitrary constant for a second-order problem.
- Forgetting the $x$ multiplier when the trial particular solution overlaps $y_h$.
- Applying initial conditions to $y_p$ alone rather than the full $y_h+y_p$.
- Confusing natural frequency, damped frequency, and forcing frequency.
- Calling every large response resonance without checking frequency and damping.
- Treating the steady-state solution as the complete solution when initial transients matter.
- Forgetting that the discriminant tells you the response type before you interpret the motion physically.
