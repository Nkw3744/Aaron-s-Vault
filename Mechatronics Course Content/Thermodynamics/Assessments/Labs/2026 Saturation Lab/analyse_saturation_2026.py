#!/usr/bin/env python3
"""Reproduce the 2026 saturation-lab calculations and report figures."""

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
P_GAUGE = np.arange(50, 451, 50, dtype=float)
RESISTANCE = np.array([142.3, 144.8, 146.9, 148.7, 150.1, 151.1, 152.6, 153.8, 154.6])
P_ATM = 101.65
R1, T1 = 109.0, 15.0
R2, T2 = 138.7, 100.0

# Cengel Table A-5 values enclosing the experimental pressure range.
P_TABLE = np.array([150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 550, 600], dtype=float)
T_TABLE = np.array([111.35, 116.04, 120.21, 123.97, 127.41, 130.58, 133.52, 136.27, 138.86, 141.30, 143.61, 147.90, 151.83, 155.46, 158.83])


def power_fit(x, y):
    """Return A, n, R² and predictions for y = A*x**n (log-space OLS)."""
    n, ln_a = np.polyfit(np.log(x), np.log(y), 1)
    a = np.exp(ln_a)
    predicted = a * x**n
    r_squared = 1 - np.sum((y - predicted) ** 2) / np.sum((y - y.mean()) ** 2)
    return a, n, r_squared, predicted


def main():
    p_abs = P_GAUGE + P_ATM
    alpha = (R2 - R1) / (T2 - T1)
    t_exp = T1 + (RESISTANCE - R1) / alpha
    t_th = np.interp(p_abs, P_TABLE, T_TABLE)
    error = (t_exp - t_th) / t_th * 100
    absolute_error = np.abs(error)

    a_exp, n_exp, r2_exp, fit_exp = power_fit(p_abs, t_exp)
    a_th, n_th, r2_th, fit_th = power_fit(p_abs, t_th)

    rows = list(zip(P_GAUGE, p_abs, RESISTANCE, t_exp, t_th, error, absolute_error))
    headers = [
        "Gauge pressure, P1 (kPa)",
        "Absolute pressure, Pabs (kPa)",
        "PT100 resistance, R (ohm)",
        "Experimental temperature, Texp (degC)",
        "Theoretical temperature, Tth (degC)",
        "Signed error (%)",
        "Absolute error (%)",
    ]
    with (OUT / "Saturation Lab 2026 Calculations.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows([[f"{value:.5f}" for value in row] for row in rows])

    plt.style.use("seaborn-v0_8-whitegrid")
    figure, axis = plt.subplots(figsize=(8, 5.2), dpi=180)
    axis.scatter(p_abs, t_exp, label="Experimental (PT100-derived)", color="#1f77b4", s=34, zorder=3)
    axis.plot(p_abs, fit_exp, color="#1f77b4", lw=1.6, label=f"Experimental fit: T = {a_exp:.3f}P$^{{{n_exp:.4f}}}$")
    axis.scatter(p_abs, t_th, label="Steam-table interpolation", color="#d62728", marker="s", s=28, zorder=3)
    axis.plot(p_abs, fit_th, color="#d62728", lw=1.6, label=f"Theoretical fit: T = {a_th:.3f}P$^{{{n_th:.4f}}}$")
    axis.set_xlabel("Absolute pressure, $P_{abs}$ (kPa)")
    axis.set_ylabel("Saturation temperature, $T_{sat}$ (°C)")
    axis.legend(frameon=True, fontsize=8)
    figure.tight_layout()
    figure.savefig(OUT / "Figure 2 - Temperature versus absolute pressure.png", bbox_inches="tight")
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(8, 4.6), dpi=180)
    axis.axhline(0, color="black", lw=0.8)
    axis.plot(p_abs, error, "o-", color="#7b2cbf", lw=1.5)
    axis.set_xlabel("Absolute pressure, $P_{abs}$ (kPa)")
    axis.set_ylabel("Signed temperature error (%)")
    axis.grid(True, alpha=0.35)
    figure.tight_layout()
    figure.savefig(OUT / "Figure 3 - Error versus absolute pressure.png", bbox_inches="tight")
    plt.close(figure)

    assert len(rows) == 9
    assert np.all(np.diff(p_abs) > 0)
    assert np.all(np.diff(t_exp) > 0)
    assert np.all(error < 0)
    assert abs(error.mean() - (-4.322044)) < 1e-5
    assert abs(a_exp - 37.63305925) < 1e-7
    assert abs(n_exp - 0.21457331) < 1e-7

    print(f"Calibration slope: {alpha:.8f} ohm/degC")
    print(f"Experimental fit: A={a_exp:.8f}, n={n_exp:.8f}, R2={r2_exp:.8f}")
    print(f"Theoretical fit: A={a_th:.8f}, n={n_th:.8f}, R2={r2_th:.8f}")
    print(f"Mean signed error: {error.mean():.6f}%")
    print(f"Mean absolute error: {absolute_error.mean():.6f}%")
    print(f"Maximum absolute error: {absolute_error.max():.6f}%")
    print("All numerical assertions passed.")


if __name__ == "__main__":
    main()
