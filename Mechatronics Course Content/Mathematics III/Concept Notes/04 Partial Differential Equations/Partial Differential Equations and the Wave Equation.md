---
course: ENGE702
type: concept
source_reviewed: 2026-07-22
source_scope: Lectures 21-22
---

# Partial Differential Equations and the Wave Equation

> [!info] Course navigation
> [[Mathematics III Overview|Subject overview]] · [[Mathematics III Roadmap|Course roadmap]] · Previous: [[Fourier Analysis]]
>
> Sources: [[Lecture 21 Introduction to PDEs.pdf|Lecture 21]] · [[Lecture 22 The Wave Equation Derivation.pdf|Lecture 22]]

## Core idea

A partial differential equation (PDE) relates a function of several independent variables to its partial derivatives. The equation describes local behaviour; initial and boundary conditions select the physical solution over the region of interest.

## Partial derivatives

For $u(x,y,t)$, a partial derivative changes one variable while treating the others as constants. Common notation includes

$$
\frac{\partial u}{\partial x},\quad
\frac{\partial^2u}{\partial x^2},\quad
\frac{\partial^2u}{\partial x\partial y}.
$$

When the relevant second derivatives are continuous, mixed derivatives can be interchanged:

$$
u_{xy}=u_{yx}.
$$

## Common PDE models in Lecture 21

- **One-dimensional heat equation:**
  $$u_t=c^2u_{xx}.$$
- **One-dimensional wave equation:**
  $$u_{tt}=c^2u_{xx}.$$
- **Two-dimensional Laplace equation:**
  $$u_{xx}+u_{yy}=0.$$

The derivative pattern reflects the physics: diffusion is first order in time, wave motion is second order in time, and the Laplace equation describes a steady spatial field.

## Verifying a PDE solution

1. Compute every required partial derivative.
2. Substitute into the PDE.
3. Check the equation over the stated domain.
4. Check each initial condition.
5. Check each boundary condition.

A function that satisfies the PDE but violates a boundary condition is not a solution to the full boundary-value problem.

## Initial and boundary conditions

- **Initial conditions** specify the state, and sometimes its time derivative, at an initial time.
- **Boundary conditions** specify behaviour at spatial boundaries.
- The PDE plus its conditions forms the complete problem.

For a string fixed at $x=0$ and $x=L$:

$$
u(0,t)=0,\qquad u(L,t)=0.
$$

A second-order time equation also requires two time conditions, commonly initial displacement $u(x,0)$ and initial velocity $u_t(x,0)$.

## Solving PDEs like ODEs when variables are absent

If a PDE contains derivatives in only one independent variable, treat the others as parameters. For example,

$$
u_{xx}-u=0
$$

has

$$
u(x,y)=A(y)e^x+B(y)e^{-x},
$$

because the integration “constants” may depend on the variables not used in the differentiation. Forgetting this dependence discards valid solutions.

## Deriving the one-dimensional wave equation

Let $u(x,t)$ be the transverse displacement of a string with fixed endpoints. Lecture 22 assumes:

1. uniform mass per unit length $\rho$;
2. a perfectly flexible string with no bending resistance;
3. gravity negligible relative to tension;
4. small transverse displacements and slopes;
5. horizontal tension component $T$ approximately constant.

For a short element from $x$ to $x+\Delta x$, the vertical force balance is

$$
T_2\sin\beta-T_1\sin\alpha
=\rho\Delta x\,u_{tt}.
$$

Using the constant horizontal component and small-slope relation $\tan\theta\approx u_x$, divide by $\Delta x$ and take the limit $\Delta x\to0$. This gives

$$
u_{tt}=c^2u_{xx},
$$

where

$$
c^2=\frac{T}{\rho}.
$$

Thus higher tension raises wave speed and greater mass per unit length lowers it.

> [!important] The PDE remembers its assumptions
> Large slopes, non-uniform density, bending stiffness, damping, or external forcing require a different model. The derivation is as important as the final equation because it defines when the result applies.

## Mode connection

Fixed-end boundary conditions are naturally satisfied by spatial sine modes such as

$$
\sin\left(\frac{n\pi x}{L}\right).
$$

Each spatial mode has a corresponding time oscillation. This is why [[Fourier Analysis]] comes before PDEs: Fourier sine series express a general initial string shape as a sum of boundary-compatible modes.

The time behaviour of each mode follows a second-order oscillator equation, linking back to [[Second-Order Differential Equations and Oscillations]].

## Visualisation workflow

Lecture 21 uses a surface plot to show $u(x,t)$ over position and time. Useful checks are:

- inspect the full surface;
- inspect fixed-time spatial profiles;
- inspect fixed-position time traces;
- confirm boundary lines remain at their prescribed values;
- label both independent variables and the dependent variable with units.

## Common mistakes

- Differentiating every variable instead of holding the others constant.
- Treating integration constants as true constants when they may be functions of other variables.
- Verifying the PDE but not the initial/boundary conditions.
- Swapping the roles of $u_{tt}$ and $u_{xx}$.
- Omitting units from $c$, $T$, or $\rho$.
- Quoting the wave equation without the small-motion and uniform-string assumptions.
- Jumping to Fourier modes before identifying the boundary conditions they must satisfy.
