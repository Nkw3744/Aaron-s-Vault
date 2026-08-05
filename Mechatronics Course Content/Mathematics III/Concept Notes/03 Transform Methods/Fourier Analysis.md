---
course: ENGE702
type: concept
source_reviewed: 2026-07-22
source_scope: Lectures 18-20
---

# Fourier Analysis

> [!info] Course navigation
> [[Mathematics III Overview|Subject overview]] · [[Mathematics III Roadmap|Course roadmap]] · Previous: [[Laplace Transforms]] · Next: [[Partial Differential Equations and the Wave Equation]]
>
> Sources: [[Lecture 18 Slides Fourier Series.pdf|Lecture 18]] · [[Lecture 19 Fourier Series Applications.pdf|Lecture 19]] · [[Lecture 19 Fourier Series Applications Exercises.pdf|Lecture 19 exercises]] · [[Lecture 20 Fourier Integrals and Transforms.pdf|Lecture 20]]

## Core idea

Fourier analysis represents a function as a collection of sinusoidal components. A periodic function produces a discrete harmonic series; a suitable non-periodic function produces a continuous frequency representation. This makes frequency content visible and lets linear systems respond to one sinusoid at a time.

## Periodic functions

A function is periodic if

$$
f(x+T)=f(x)
$$

for some positive period $T$. The smallest such value is the fundamental period. For a period $2L$, the lecture convention is

$$
f(x)=a_0+\sum_{n=1}^{\infty}\left[a_n\cos\left(\frac{n\pi x}{L}\right)+b_n\sin\left(\frac{n\pi x}{L}\right)\right],
$$

with

$$
a_0=\frac1{2L}\int_{-L}^{L}f(x)\,dx,
$$

$$
a_n=\frac1L\int_{-L}^{L}f(x)\cos\left(\frac{n\pi x}{L}\right)\,dx,
$$

$$
b_n=\frac1L\int_{-L}^{L}f(x)\sin\left(\frac{n\pi x}{L}\right)\,dx.
$$

> [!warning] Coefficient conventions vary
> Some books write the constant term as $a_0/2$ and define $a_0$ differently. Use one convention consistently and check the source formula before comparing coefficients.

## Coefficient workflow

1. Identify one full period and set $L=T/2$.
2. Inspect symmetry before integrating.
3. Calculate the mean term $a_0$.
4. Calculate $a_n$ and $b_n$ over the same interval.
5. Check units and signs.
6. Plot partial sums to confirm the shape and discontinuity behaviour.

### Symmetry shortcuts

- If $f$ is even, all $b_n=0$; only cosine terms remain.
- If $f$ is odd, $a_0=0$ and all $a_n=0$; only sine terms remain.
- A function defined only on $[0,L]$ can be extended evenly for a cosine series or oddly for a sine series.

Do not claim symmetry until the chosen interval and periodic extension have been checked.

## Convergence at jumps

At a point of continuity, the Fourier representation approaches the function under the lecture's regularity assumptions. At a jump, it approaches the average of the left- and right-hand limits. Partial sums can overshoot near a jump; adding terms narrows the affected region but does not simply remove the local overshoot.

## Square-wave and sawtooth lessons

The Lecture 18 square wave is odd, so only odd sine harmonics remain. The sawtooth example has a non-zero average plus sine terms. These examples show how:

- symmetry predicts zero coefficients;
- sharper transitions require more high-frequency content;
- coefficient decay controls how quickly partial sums improve.

## Periodic forcing of a linear oscillator

For a linear system

$$
my''+cy'+ky=r(t),
$$

a periodic forcing $r(t)$ can be expanded into Fourier harmonics. Because the ODE is linear:

1. find the Fourier series of $r(t)$;
2. solve for the response to each sine/cosine harmonic;
3. add the harmonic responses;
4. separate decaying transients from the steady-state sum.

Each harmonic is filtered by the system's frequency response. Harmonics near resonance can contribute disproportionately. The underlying damping and resonance model is owned by [[Second-Order Differential Equations and Oscillations]] rather than repeated here.

## From Fourier series to Fourier integrals

A Fourier series uses discrete frequencies because the signal repeats. For a suitable non-periodic function on the whole real line, the frequency variable becomes continuous:

$$
f(x)=\int_0^\infty\left[A(\omega)\cos(\omega x)+B(\omega)\sin(\omega x)\right]d\omega,
$$

where, in the lecture convention,

$$
A(\omega)=\frac1\pi\int_{-\infty}^{\infty}f(\nu)\cos(\omega\nu)\,d\nu,
$$

$$
B(\omega)=\frac1\pi\int_{-\infty}^{\infty}f(\nu)\sin(\omega\nu)\,d\nu.
$$

At a discontinuity, the integral representation gives the midpoint of the one-sided limits.

## Sine and cosine transforms

For an even extension, Lecture 20 uses the cosine-transform pair

$$
\hat f_c(\omega)=\sqrt{\frac2\pi}\int_0^\infty f(x)\cos(\omega x)\,dx,
$$

$$
f(x)=\sqrt{\frac2\pi}\int_0^\infty \hat f_c(\omega)\cos(\omega x)\,d\omega.
$$

For an odd extension, replace cosine with sine to obtain $\hat f_s$. Any function can be decomposed into even and odd parts:

$$
f_e(x)=\frac{f(x)+f(-x)}2,
$$

$$
f_o(x)=\frac{f(x)-f(-x)}2.
$$

## Engineering connections

- [[Amplitude Modulation]] shifts message spectra around a carrier; the Lab 5 FFT evidence is a discrete computational example of this Fourier viewpoint.
- [[Fundamentals of Electronics and Signals]] uses spectra to distinguish time-domain shape from frequency-domain content.
- [[Partial Differential Equations and the Wave Equation]] uses sine/cosine modes to satisfy spatial boundaries.
- FFT algorithms compute discrete Fourier transforms for sampled data, supporting signal processing, communications, imaging, audio, and spectral feature extraction.

## Common mistakes

- Using $L$ as the full period instead of half the period in this convention.
- Mixing $a_0$ and $a_0/2$ conventions.
- Ignoring symmetry and doing unnecessary integrals.
- Applying odd/even shortcuts on a non-symmetric interval.
- Expecting a Fourier series to equal one side of a jump rather than the midpoint.
- Confusing discrete Fourier-series harmonics with a continuous Fourier-transform spectrum.
- Interpreting an FFT without accounting for sample rate, finite record length, scaling, and windowing.
