---
course: ENGE702
type: concept
source_reviewed: 2026-07-22
source_scope: Lectures 15-17
---

# Laplace Transforms

> [!info] Course navigation
> [[Mathematics III Overview|Subject overview]] · [[Mathematics III Roadmap|Course roadmap]] · Previous: [[Eigenvalues and Systems of Differential Equations]] · Next: [[Fourier Analysis]]
>
> Sources: [[Lecture 15 Lapice Transforms.pdf|Lecture 15]] · [[Lecture 16 Laplace Transforms.pdf|Lecture 16]] · [[Lecture 17 Laplace Transforms.pdf|Lecture 17]]

## Core idea

The Laplace transform converts a time-domain initial-value problem into an algebraic equation in $s$. It is especially useful when initial conditions and switched, pulsed, or piecewise inputs must be handled together.

## Definition and notation

$$
F(s)=\mathcal L\{f(t)\}=\int_0^\infty e^{-st}f(t)\,dt.
$$

Lower-case $f(t)$ denotes the time-domain function; upper-case $F(s)$ denotes its Laplace-domain transform. The defining integral also reminds us that a transform exists only where the improper integral converges.

## Core transform pairs

$$
\mathcal L\{1\}=\frac1s,
$$

$$
\mathcal L\{t^n\}=\frac{n!}{s^{n+1}},
$$

$$
\mathcal L\{e^{at}\}=\frac1{s-a},
$$

$$
\mathcal L\{\cos\omega t\}=\frac{s}{s^2+\omega^2},
$$

$$
\mathcal L\{\sin\omega t\}=\frac{\omega}{s^2+\omega^2}.
$$

Use a transform table as a set of patterns, not isolated formulas.

## Linearity and shifting

$$
\mathcal L\{af+bg\}=aF+bG.
$$

In general, the transform of a product is **not** the product of the transforms.

The $s$-shift rule is

$$
\mathcal L\{e^{at}f(t)\}=F(s-a).
$$

Complete the square or rewrite the denominator so the shifted table pattern is visible before applying the inverse transform.

## Inverse transforms

$$
\mathcal L^{-1}\{F(s)\}=f(t).
$$

A reliable workflow is:

1. simplify algebraically;
2. split sums using linearity;
3. use partial fractions for rational functions;
4. complete squares for shifted sine/cosine forms;
5. match table entries, including scale factors;
6. verify by transforming the result back when practical.

## Heaviside functions and switched inputs

The unit-step function is

$$
u(t-a)=\begin{cases}0,&t<a,\\1,&t\ge a.\end{cases}
$$

It switches a term on at $t=a$. A pulse active between $a$ and $b$ can be represented with

$$
u(t-a)-u(t-b).
$$

The time-shift theorem is

$$
\mathcal L\{f(t-a)u(t-a)\}=e^{-as}F(s).
$$

### Rewriting a piecewise function

1. Start with the expression valid before the first switch.
2. At each switch time, add `new expression − old expression` multiplied by the relevant step.
3. Rewrite each switched term in the form $f(t-a)u(t-a)$.
4. Transform using $e^{-as}F(s)$.

The argument shift matters: $f(t)u(t-a)$ is not automatically in the theorem's required form.

## Transforms of derivatives

If $F(s)=\mathcal L\{f(t)\}$,

$$
\mathcal L\{f'(t)\}=sF(s)-f(0),
$$

$$
\mathcal L\{f''(t)\}=s^2F(s)-sf(0)-f'(0).
$$

Initial data are built directly into these formulas, which is why Laplace methods are effective for IVPs.

## Solving an IVP

1. Transform both sides of the ODE.
2. Insert the initial conditions immediately in derivative transforms.
3. Collect all terms involving $Y(s)$.
4. Solve algebraically for $Y(s)$.
5. Decompose $Y(s)$ into invertible patterns.
6. Take the inverse transform.
7. Verify the initial conditions and, where smooth, substitute back into the ODE.
8. For step inputs, check the solution on each time interval and at switching times.

## RLC connection

A series RLC circuit can be modelled in charge $Q(t)$ as

$$
LQ''+RQ'+\frac1C Q=E(t).
$$

Laplace transforms handle the initial charge and current together with a switched or pulsed source voltage. This extends the RL model in [[First-Order Differential Equations]] and the second-order modes in [[Second-Order Differential Equations and Oscillations]].

## When to use which method

- Use direct ODE methods for simple smooth forcing when they are shorter.
- Use Laplace methods when initial data, discontinuities, delayed inputs, or impulses make a time-domain trial awkward.
- Use [[Fourier Analysis]] when the main objective is frequency content or decomposition over a periodic/whole-domain signal rather than a one-sided IVP.

## Common mistakes

- Omitting an initial-condition term from a derivative transform.
- Treating the transform of a product as a product.
- Using the wrong sign in $F(s-a)$ or $e^{-as}$.
- Applying the time-shift theorem without rewriting the function as $f(t-a)$.
- Losing constants during partial fractions.
- Stopping at $Y(s)$ when the requested answer is $y(t)$.
- Forgetting that step-driven solutions may need interval-by-interval interpretation.
