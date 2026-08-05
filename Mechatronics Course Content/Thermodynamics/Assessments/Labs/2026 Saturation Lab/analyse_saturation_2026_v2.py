#!/usr/bin/env python3
"""Create the corrected 2026 saturation-lab comparison graph.

The comparison graph uses direct Table A-5 pressure/temperature pairs. Linear
interpolation is used separately only for the point-by-point error table.
"""

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent

P_GAUGE = np.arange(50, 451, 50, dtype=float)
P_ATM = 101.65
RESISTANCE = np.array([142.3, 144.8, 146.9, 148.7, 150.1, 151.1, 152.6, 153.8, 154.6])
R1, T1 = 109.0, 15.0
R2, T2 = 138.7, 100.0

# Direct pressure-temperature pairs from Cengel Table A-5, spanning the
# experimental absolute-pressure range. These are the points plotted for the
# theoretical dataset; they are not interpolated to experimental pressures.
P_TABLE = np.array([150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 550, 600], dtype=float)
T_TABLE = np.array([111.35, 116.04, 120.21, 123.97, 127.41, 130.58, 133.52, 136.27, 138.86, 141.30, 143.61, 147.90, 151.83, 155.46, 158.83])


def power_fit(x, y):
    """Return A, n, R² and predictions for y=A*x**n using log-space OLS."""
    n, ln_a = np.polyfit(np.log(x), np.log(y), 1)
    a = np.exp(ln_a)
    predicted = a * x**n
    r_squared = 1 - np.sum((y - predicted) ** 2) / np.sum((y - y.mean()) ** 2)
    return a, n, r_squared, predicted


def main():
    p_abs = P_GAUGE + P_ATM
    alpha = (R2 - R1) / (T2 - T1)
    t_exp = T1 + (RESISTANCE - R1) / alpha

    # Interpolated values belong only to the later error calculation.
    t_th_interpolated = np.interp(p_abs, P_TABLE, T_TABLE)
    error = (t_exp - t_th_interpolated) / t_th_interpolated * 100

    a_exp, n_exp, r2_exp, _ = power_fit(p_abs, t_exp)
    a_table, n_table, r2_table, _ = power_fit(P_TABLE, T_TABLE)

    p_exp_line = np.linspace(p_abs.min(), p_abs.max(), 300)
    p_table_line = np.linspace(P_TABLE.min(), P_TABLE.max(), 300)

    with (OUT / "Saturation Table A5 Plot Data.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Table A-5 pressure (kPa)", "Table A-5 saturation temperature (degC)"])
        writer.writerows(zip(P_TABLE.astype(int), T_TABLE))

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(8, 5.2), dpi=180)
    ax.scatter(p_abs, t_exp, label="Experimental data", color="#1f77b4", s=34, zorder=3)
    ax.plot(p_exp_line, a_exp * p_exp_line**n_exp, color="#1f77b4", lw=1.6,
            label=rf"Experimental fit: $T={a_exp:.3f}P^{{{n_exp:.4f}}}$")
    ax.scatter(P_TABLE, T_TABLE, label="Table A-5 values", color="#d62728", marker="s", s=28, zorder=3)
    ax.plot(p_table_line, a_table * p_table_line**n_table, color="#d62728", lw=1.6,
            label=rf"Table A-5 fit: $T={a_table:.3f}P^{{{n_table:.4f}}}$")
    ax.set_xlabel(r"Absolute pressure, $P_{abs}$ (kPa)")
    ax.set_ylabel(r"Saturation temperature, $T_{sat}$ (°C)")
    ax.legend(frameon=True, fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "Figure 2 v2 - Experimental and Table A5 values.png", bbox_inches="tight")
    plt.close(fig)

    assert len(P_TABLE) == 15
    assert np.all(np.diff(P_TABLE) > 0)
    assert np.all(np.diff(T_TABLE) > 0)
    assert np.allclose(t_th_interpolated, [111.65954, 120.45816, 127.61922, 133.70150, 139.02104, 143.75157, 148.02969, 151.94979, 155.57121], atol=5e-6)
    assert np.all(error < 0)

    print(f"Experimental fit: A={a_exp:.8f}, n={n_exp:.8f}, R2={r2_exp:.8f}")
    print(f"Direct Table A-5 fit: A={a_table:.8f}, n={n_table:.8f}, R2={r2_table:.8f}")
    print(f"Direct table points plotted: {len(P_TABLE)}")
    print("Interpolation is retained only for the nine error-table Tth values.")
    print("All numerical assertions passed.")


if __name__ == "__main__":
    main()
