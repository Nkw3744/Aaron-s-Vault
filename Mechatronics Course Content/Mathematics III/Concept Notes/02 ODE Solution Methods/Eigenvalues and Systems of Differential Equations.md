---
course: ENGE702
type: concept
source_reviewed: 2026-07-22
source_scope: Lectures 12 and 14; no Lecture 13 source present
---

# Eigenvalues and Systems of Differential Equations

> [!info] Course navigation
> [[Mathematics III Overview|Subject overview]] · [[Mathematics III Roadmap|Course roadmap]] · Previous: [[Second-Order Differential Equations and Oscillations]] · Next: [[Laplace Transforms]]
>
> Sources: [[Lecture 12 EigenValues and Eigenvectors.pdf|Lecture 12]] · [[Lecture 14 systems of diff Equ.pdf|Lecture 14]]

> [!warning] Source gap
> No Lecture 13 source is present in the vault. This note does not assign or invent a Lecture 13 topic.

## Core idea

A matrix describes a linear transformation. An eigenvector is a direction that the transformation does not rotate away from itself; the corresponding eigenvalue is its scale factor. In a linear ODE system, eigenvectors identify independent system modes and eigenvalues determine how those modes grow, decay, or oscillate.

## Matrix essentials

- Matrices can be added only when they have the same dimensions.
- A $p\times q$ matrix times a $q\times s$ matrix produces a $p\times s$ matrix.
- Each product entry is a row-column dot product.
- Matrix multiplication is generally not commutative: $AB$ need not equal $BA$.
- $I$ is the identity transformation; $AI=IA=A$ when dimensions agree.
- The transpose $A^T$ interchanges rows and columns.

For

$$
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
$$

$$
\det A=ad-bc,
$$

and, when $\det A\neq0$,

$$
A^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.
$$

A zero determinant means the transformation is singular and no inverse exists.

## Eigenvalues and eigenvectors

An eigenpair satisfies

$$
A\mathbf v=\lambda\mathbf v,
$$

where $\mathbf v\neq\mathbf0$.

### Workflow

1. Find eigenvalues from
   $$\det(A-\lambda I)=0.$$
2. For each eigenvalue, solve
   $$(A-\lambda I)\mathbf v=\mathbf0.$$
3. Choose any convenient non-zero vector from the solution family.
4. Verify directly that $A\mathbf v=\lambda\mathbf v$.

Eigenvectors are not unique: any non-zero scalar multiple represents the same eigen-direction.

## Linear systems of ODEs

A constant-coefficient system can be written

$$
\mathbf y'=A\mathbf y.
$$

If $(\lambda,\mathbf v)$ is an eigenpair, then

$$
\mathbf y(t)=e^{\lambda t}\mathbf v
$$

is a modal solution because

$$
\mathbf y'=\lambda e^{\lambda t}\mathbf v=Ae^{\lambda t}\mathbf v.
$$

With enough linearly independent eigenvectors, combine the modes:

$$
\mathbf y(t)=\sum_i c_i e^{\lambda_i t}\mathbf v_i.
$$

Initial conditions determine the constants. A negative real eigenvalue produces a decaying mode; a positive one produces growth; complex conjugate eigenvalues produce oscillatory modes with exponential envelopes.

## Coupled-tank example pattern

Lecture 14 models two well-mixed 100-L tanks exchanging fluid at 5 L/min. If $y_1,y_2$ are salt masses,

$$
y_1'=-0.05y_1+0.05y_2,
$$

$$
y_2'=0.05y_1-0.05y_2,
$$

or

$$
\mathbf y'=\begin{pmatrix}-0.05&0.05\\0.05&-0.05\end{pmatrix}\mathbf y.
$$

The model comes from **rate in minus rate out** for each tank. Before solving, check conservation: because the exchange is internal, $y_1+y_2$ should remain constant. This physical check is independent of the eigenvalue algebra.

## Converting a second-order ODE to a system

For

$$
y''+by'+cy=0,
$$

set

$$
v_1=y,\qquad v_2=y'.
$$

Then

$$
\begin{pmatrix}v_1'\\v_2'\end{pmatrix}
=
\begin{pmatrix}0&1\\-c&-b\end{pmatrix}
\begin{pmatrix}v_1\\v_2\end{pmatrix}.
$$

Initial conditions map directly:

$$
\mathbf v(0)=\begin{pmatrix}y(0)\\y'(0)\end{pmatrix}.
$$

This state-space form connects the characteristic-root method in [[Second-Order Differential Equations and Oscillations]] to matrix modes. The characteristic polynomial of the state matrix matches the ODE's characteristic equation.

## Coherent solution workflow

1. Define state variables and units.
2. Derive every row from a balance or state definition.
3. Write $\mathbf y'=A\mathbf y$ and the initial vector.
4. Find and verify eigenpairs.
5. Build the modal sum.
6. Apply initial conditions as a vector equation.
7. Check the result against conservation, signs, and long-term behaviour.

## Common mistakes

- Multiplying matrices with incompatible dimensions.
- Forming $\det(A-\lambda I)$ incorrectly by subtracting $\lambda$ from non-diagonal entries.
- Accepting the zero vector as an eigenvector.
- Finding eigenvalues but not their eigenvectors.
- Assuming eigenvectors have a unique magnitude.
- Writing a coupled model without checking units or conserved totals.
- Converting $y''+by'+cy=0$ with the bottom row signs reversed.
