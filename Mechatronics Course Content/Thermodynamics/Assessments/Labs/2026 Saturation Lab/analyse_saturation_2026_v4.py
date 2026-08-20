#!/usr/bin/env python3
"""Reproduce Aaron Taylor's 2026 TH3 saturation-lab v4 calculations.

The original nine pressure/resistance readings are preserved. Experimental
temperatures use the two-point resistance conversion explicitly recorded on the
laboratory whiteboard for this session: 109.0 ohm at 15 degC and 138.7 ohm at
100 degC. This differs from the manufacturer's Data Sheet 1 -> Data Sheet 2
workflow and is therefore reported as a session-supplied method and limitation.
"""

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
P_GAUGE = np.arange(50, 451, 50, dtype=float)
P_ATM = 101.65
R_INDICATED = np.array([142.3, 144.8, 146.9, 148.7, 150.1, 151.1, 152.6, 153.8, 154.6])

# Session-specific values photographed on the laboratory whiteboard/controller.
T1 = 15.0
R1 = 109.0
T2 = 100.0
R2 = 138.7
ALPHA = (R2 - R1) / (T2 - T1)

P_TABLE = np.array([150,175,200,225,250,275,300,325,350,375,400,450,500,550,600], dtype=float)
T_TABLE = np.array([111.35,116.04,120.21,123.97,127.41,130.58,133.52,136.27,138.86,141.30,143.61,147.90,151.83,155.46,158.83])


def power_fit(x, y):
    """Return A, n and R-squared for y=A*x**n using log-space OLS."""
    n, ln_a = np.polyfit(np.log(x), np.log(y), 1)
    a = np.exp(ln_a)
    prediction = a * x**n
    r_squared = 1 - np.sum((y - prediction)**2) / np.sum((y - y.mean())**2)
    return a, n, r_squared


def main():
    p_abs = P_GAUGE + P_ATM
    t_exp = T1 + (R_INDICATED - R1) / ALPHA
    t_th = np.interp(p_abs, P_TABLE, T_TABLE)
    error = (t_exp - t_th) / t_th * 100
    absolute_error = np.abs(error)

    a_exp, n_exp, r2_exp = power_fit(p_abs, t_exp)
    a_table, n_table, r2_table = power_fit(P_TABLE, T_TABLE)

    rows = list(zip(P_GAUGE, p_abs, R_INDICATED, t_exp, t_th, error, absolute_error))
    with (OUT / "Saturation Lab 2026 Calculations v4.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "Gauge pressure P1 (kPa)", "Absolute pressure Pabs (kPa)",
            "Recorded PT100 resistance R (ohm)", "Experimental temperature Texp (degC)",
            "Theoretical temperature Tth (degC)", "Signed error (%)", "Absolute error (%)",
        ])
        writer.writerows([[f"{value:.5f}" for value in row] for row in rows])

    plt.style.use("seaborn-v0_8-whitegrid")
    p_exp_line = np.linspace(p_abs.min(), p_abs.max(), 300)
    p_table_line = np.linspace(P_TABLE.min(), P_TABLE.max(), 300)
    fig, ax = plt.subplots(figsize=(8, 5.2), dpi=180)
    ax.scatter(p_abs, t_exp, label="Experimental data", color="#1f77b4", s=34, zorder=3)
    ax.plot(p_exp_line, a_exp * p_exp_line**n_exp, color="#1f77b4", lw=1.6,
            label=rf"Experimental fit: $T={a_exp:.3f}P^{{{n_exp:.4f}}}$")
    ax.scatter(P_TABLE, T_TABLE, label="Table A-5 values", color="#d62728", marker="s", s=28, zorder=3)
    ax.plot(p_table_line, a_table * p_table_line**n_table, color="#d62728", lw=1.6,
            label=rf"Table A-5 fit: $T={a_table:.3f}P^{{{n_table:.4f}}}$")
    ax.set_xlabel(r"Absolute pressure, $P_{abs}$ (kPa)")
    ax.set_ylabel(r"Saturation temperature, $T_{sat}$ ($^{\circ}$C)")
    ax.legend(frameon=True, fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "Figure 2 v4 - Experimental and Table A5 values.png", bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.6), dpi=180)
    ax.axhline(0, color="black", lw=0.8)
    ax.plot(p_abs, error, "o-", color="#7b2cbf", lw=1.5)
    ax.set_xlabel(r"Absolute pressure, $P_{abs}$ (kPa)")
    ax.set_ylabel("Signed temperature error (%)")
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    fig.savefig(OUT / "Figure 3 v4 - Error versus absolute pressure.png", bbox_inches="tight")
    plt.close(fig)

    assert abs(ALPHA - 0.34941176470588237) < 1e-12
    assert np.allclose(t_exp, [110.30303,117.45791,123.46801,128.61953,132.62626,135.48822,139.78114,143.21549,145.50505], atol=5e-6)
    assert abs(error.mean() + 4.3220438343) < 1e-9
    assert abs(np.max(absolute_error) - 6.4704513740) < 1e-9
    assert abs(a_exp - 37.6330592462) < 1e-9
    assert abs(n_exp - 0.2145733100) < 1e-9
    assert np.all(error < 0)

    print(f"Session coefficient alpha: {ALPHA:.10f} ohm/degC")
    print(f"Experimental fit: A={a_exp:.10f}, n={n_exp:.10f}, R2={r2_exp:.10f}")
    print(f"Direct Table A-5 fit: A={a_table:.10f}, n={n_table:.10f}, R2={r2_table:.10f}")
    print(f"Mean signed error: {error.mean():.10f}%")
    print(f"Mean absolute error: {absolute_error.mean():.10f}%")
    print(f"Maximum absolute error: {absolute_error.max():.10f}%")
    print("All numerical assertions passed.")


if __name__ == "__main__":
    main()
