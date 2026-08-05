---
course: ENGE702
type: concept
source_reviewed: 2026-07-22
source_scope: Lectures 4-5, annotated notes L4-L5, Tutorial 2
---

# First-Order Differential Equations

> [!info] Course navigation
> [[Mathematics III Overview|Subject overview]] · [[Mathematics III Roadmap|Course roadmap]] · [[Mathematics III Practice Index|Practice index]] · Previous: [[Mathematical Modelling and Numerical ODEs]] · Next: [[Second-Order Differential Equations and Oscillations]]
>
> Sources: [[Lecture 4 Solving Separable First Order ODEs.pdf|Lecture 4]] · [[L4_note.pdf|annotated Lecture 4]] · [[Lecture 5 Solving linear first order differential equations.pdf|Lecture 5]] · [[L5_note.pdf|annotated Lecture 5]] · [[Tutorial 2 ENGE702.pdf|Tutorial 2]]

## Core idea

The first task is classification. A first-order ODE may be separable, linear, both, or neither. The form determines the method; trying to force every equation into the same workflow creates unnecessary algebra and can discard solutions.

## Decision workflow

1. Rearrange enough to see the structure.
2. Test for **separability**: can it be written as $g(y)y'=f(x)$ or $dy/dx=F(x)G(y)$?
3. Test for **linearity**: can it be written as
   $$y'+p(x)y=r(x)?$$
4. Choose the simplest valid method.
5. Integrate and include the arbitrary constant.
6. Apply initial data if supplied.
7. Substitute the result back and state its valid interval.

## Separable equations

A separable equation can be rearranged into

$$
g(y)\,dy=f(x)\,dx.
$$

Integrating gives

$$
\int g(y)\,dy=\int f(x)\,dx+C.
$$

The answer may be left implicit if solving for $y$ is difficult or would obscure the domain.

### Workflow

1. Isolate the $y$-dependent factors with $dy$ and the $x$-dependent factors with $dx$.
2. Before dividing by a factor involving $y$, check whether setting that factor to zero gives an equilibrium solution.
3. Integrate both sides.
4. Combine constants into one $C$.
5. Solve for $y$ if useful.
6. Apply the initial condition and check the interval.

> [!warning] Division can lose solutions
> Dividing by $y$, $G(y)$, or another expression that may be zero can remove a constant solution. Test the zero-factor cases separately before dividing.

### Exponential growth and decay pattern

The equation

$$
y'=ky
$$

is separable and has

$$
y=Ce^{kx}.
$$

The sign of $k$ determines growth or decay. This pattern reappears in cooling, charging/discharging, mixing, population models, and damped transients.

## Linear first-order equations

A linear equation has standard form

$$
y'+p(x)y=r(x).
$$

If the coefficient of $y'$ is not one, divide the entire equation by that coefficient first, while recording where that division is valid.

### Integrating factor

Define

$$
\mu(x)=e^{\int p(x)\,dx}.
$$

Multiplication by $\mu$ makes the left side a product derivative:

$$
(\mu y)'=\mu r.
$$

Therefore

$$
\mu y=\int \mu r\,dx+C,
$$

and

$$
y=\frac{1}{\mu(x)}\left(\int \mu(x)r(x)\,dx+C\right).
$$

### Reliable workflow

1. Put the equation in standard form.
2. Identify $p(x)$ and $r(x)$ explicitly.
3. Compute $\mu=e^{\int p(x)dx}$.
4. Multiply **every term** by $\mu$.
5. Verify that the left side is $(\mu y)'$.
6. Integrate once.
7. Solve for $y$ and apply initial data.
8. Substitute back and check the interval.

> [!note] Constant inside the integrating factor
> An additive integration constant inside $\int p(x)dx$ only multiplies $\mu$ by a non-zero constant, which cancels from the method. It can be set to zero there; retain the constant produced when integrating $(\mu y)'$.

## RL-circuit model

Kirchhoff's voltage law for a series resistor-inductor circuit gives

$$
L I'(t)+R I(t)=E(t),
$$

or

$$
I'+\frac{R}{L}I=\frac{E(t)}{L}.
$$

This is a linear first-order ODE. For constant input $E$,

$$
I(t)=\frac{E}{R}+Ce^{-Rt/L}.
$$

The constant is fixed by the initial current. The exponential term is the transient; $E/R$ is the long-term steady value. Tutorial 2 extends this model to a time-varying input, so identifying $p(t)$ and $r(t)$ correctly is more important than memorising the constant-input answer.

## Method comparison

- **Separable:** rearrange variables and integrate both sides.
- **Linear:** construct an integrating factor and turn the left side into a product derivative.
- **Both:** either method may work; choose the clearer path.
- **Neither:** use another analytic method, a qualitative approach, or a numerical method such as [[Mathematical Modelling and Numerical ODEs#Euler's method|Euler's method]].

## Verification and domain checks

- Substitute into the original equation, not only the rearranged form.
- Check initial data.
- Record restrictions introduced by division, logarithms, roots, or coefficients such as $1/x$.
- An IVP may select a solution only on an interval that does not cross a singular point.
- Keep units consistent in engineering models; the exponent of an exponential must be dimensionless.

## Connections

- The exponential trial function motivates characteristic roots in [[Second-Order Differential Equations and Oscillations]].
- First-order temperature models combine ODE methods with the physical balances in [[Energy Transfer and the First Law]].
- RL transients lead naturally to switched-input and RLC problems in [[Laplace Transforms]].

## Common mistakes

- Separating variables when $x$ and $y$ are still mixed in a non-factorable way.
- Losing equilibrium solutions by dividing before checking zero factors.
- Forgetting to put a linear ODE in standard form.
- Using $e^{p(x)}$ instead of $e^{\int p(x)dx}$.
- Multiplying only part of the equation by the integrating factor.
- Applying an initial condition before the general integration constant appears.
- Ignoring the interval on which the algebra is valid.

## Practice

Use [[Tutorial 2 ENGE702.pdf|Tutorial 2]] to practise classification, separable equations, integrating factors, the relationship between slope fields and exact solutions, and the RL-circuit model.
