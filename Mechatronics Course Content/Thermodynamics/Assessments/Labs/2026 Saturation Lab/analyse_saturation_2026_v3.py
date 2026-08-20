#!/usr/bin/env python3
"""Reproduce Aaron Taylor's 2026 TH3 saturation-lab v3 calculations.

The original nine pressure/resistance readings are preserved. Indicated PT100
resistance is corrected with Armfield TH3 Issue 15 Data Sheet 1, then converted
to temperature with Data Sheet 2. Linear interpolation is used between adjacent
tabulated values.
"""

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
P_GAUGE = np.arange(50, 451, 50, dtype=float)
P_ATM = 101.65
R_INDICATED = np.array([142.3, 144.8, 146.9, 148.7, 150.1, 151.1, 152.6, 153.8, 154.6])

# Armfield TH3 Issue 15, Data Sheet 1 (printed p. 22).
R1_INDICATED = np.arange(100, 161, dtype=float)
R1_CORRECTED = np.array([
    100.00,100.83,101.68,102.53,103.38,104.25,105.12,106.00,106.88,107.78,
    108.68,109.59,110.50,111.43,112.36,113.30,114.25,115.21,116.18,117.16,
    118.14,119.13,120.14,121.15,122.17,123.20,124.24,125.29,126.35,127.42,
    128.50,129.59,130.70,131.81,132.93,134.06,135.21,136.36,137.53,138.71,
    139.90,141.10,142.32,143.54,144.78,146.04,147.30,148.58,149.87,151.17,
    152.50,153.83,155.17,156.53,157.91,159.30,160.71,162.13,163.56,165.02,
    166.48,
])

# Armfield TH3 Issue 15, Data Sheet 2 (printed pp. 23-24).
T_REFERENCE = np.arange(0, 201, 2, dtype=float)
R2_CORRECTED = np.array([
    100.00,100.78,101.56,102.34,103.12,103.90,104.68,105.46,106.24,107.02,
    107.79,108.57,109.35,110.12,110.90,111.67,112.45,113.22,113.99,114.90,
    115.54,116.31,117.08,117.85,118.62,119.40,120.16,120.93,121.70,122.47,
    123.24,124.01,124.77,125.54,126.31,127.07,127.84,128.60,129.37,130.13,
    130.89,131.66,132.42,133.18,133.94,134.70,135.46,136.22,136.98,137.74,
    138.50,139.26,140.02,140.77,141.53,142.29,143.04,143.80,144.55,145.31,
    146.06,146.81,147.57,148.32,149.07,149.82,150.57,151.33,152.08,152.83,
    153.58,154.32,155.07,155.82,156.57,157.31,158.06,158.81,159.55,160.30,
    161.04,161.79,162.53,163.27,164.02,164.76,165.50,166.24,166.98,167.72,
    168.46,169.20,169.94,170.68,171.42,172.16,172.90,173.63,174.37,175.10,
    175.84,
])

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
    r_corrected = np.interp(R_INDICATED, R1_INDICATED, R1_CORRECTED)
    t_exp = np.interp(r_corrected, R2_CORRECTED, T_REFERENCE)
    t_th = np.interp(p_abs, P_TABLE, T_TABLE)
    error = (t_exp - t_th) / t_th * 100
    absolute_error = np.abs(error)

    a_exp, n_exp, r2_exp = power_fit(p_abs, t_exp)
    a_table, n_table, r2_table = power_fit(P_TABLE, T_TABLE)

    rows = list(zip(P_GAUGE,p_abs,R_INDICATED,r_corrected,t_exp,t_th,error,absolute_error))
    with (OUT / "Saturation Lab 2026 Calculations v3.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow([
            "Gauge pressure P1 (kPa)", "Absolute pressure Pabs (kPa)",
            "Indicated PT100 resistance Rm (ohm)", "Corrected resistance Rc (ohm)",
            "Experimental temperature Texp (degC)", "Theoretical temperature Tth (degC)",
            "Signed error (%)", "Absolute error (%)",
        ])
        writer.writerows([[f"{value:.5f}" for value in row] for row in rows])

    with (OUT / "Armfield TH3 PT100 conversion v3.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Indicated resistance (ohm)","Corrected resistance (ohm)","Interpolated temperature (degC)"])
        writer.writerows([[f"{a:.5f}",f"{b:.5f}",f"{c:.5f}"] for a,b,c in zip(R_INDICATED,r_corrected,t_exp)])

    plt.style.use("seaborn-v0_8-whitegrid")
    p_exp_line = np.linspace(p_abs.min(), p_abs.max(), 300)
    p_table_line = np.linspace(P_TABLE.min(), P_TABLE.max(), 300)
    fig, ax = plt.subplots(figsize=(8,5.2), dpi=180)
    ax.scatter(p_abs,t_exp,label="Experimental data",color="#1f77b4",s=34,zorder=3)
    ax.plot(p_exp_line,a_exp*p_exp_line**n_exp,color="#1f77b4",lw=1.6,
            label=rf"Experimental fit: $T={a_exp:.3f}P^{{{n_exp:.4f}}}$")
    ax.scatter(P_TABLE,T_TABLE,label="Table A-5 values",color="#d62728",marker="s",s=28,zorder=3)
    ax.plot(p_table_line,a_table*p_table_line**n_table,color="#d62728",lw=1.6,
            label=rf"Table A-5 fit: $T={a_table:.3f}P^{{{n_table:.4f}}}$")
    ax.set_xlabel(r"Absolute pressure, $P_{abs}$ (kPa)")
    ax.set_ylabel(r"Saturation temperature, $T_{sat}$ ($^{\circ}$C)")
    ax.legend(frameon=True,fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "Figure 2 v3 - Experimental and Table A5 values.png",bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8,4.6), dpi=180)
    ax.axhline(0,color="black",lw=0.8)
    ax.plot(p_abs,error,"o-",color="#7b2cbf",lw=1.5)
    ax.set_xlabel(r"Absolute pressure, $P_{abs}$ (kPa)")
    ax.set_ylabel("Signed temperature error (%)")
    ax.grid(True,alpha=0.35)
    fig.tight_layout()
    fig.savefig(OUT / "Figure 3 v3 - Error versus absolute pressure.png",bbox_inches="tight")
    plt.close(fig)

    assert np.allclose(r_corrected,[142.686,145.788,148.452,150.780,152.633,153.964,155.986,157.634,158.744],atol=5e-7)
    assert np.allclose(t_exp,[111.056,119.27466667,126.352,132.55263158,137.47466667,141.03783784,146.44266667,150.864,153.824],atol=5e-7)
    assert abs(error.mean()+1.0316828898) < 1e-9
    assert abs(a_exp-31.2176460386) < 1e-9
    assert abs(n_exp-0.2527486298) < 1e-9
    assert np.all(error < 0)

    print(f"Experimental fit: A={a_exp:.10f}, n={n_exp:.10f}, R2={r2_exp:.10f}")
    print(f"Direct Table A-5 fit: A={a_table:.10f}, n={n_table:.10f}, R2={r2_table:.10f}")
    print(f"Mean signed error: {error.mean():.10f}%")
    print(f"Mean absolute error: {absolute_error.mean():.10f}%")
    print(f"Maximum absolute error: {absolute_error.max():.10f}%")
    print("All numerical assertions passed.")


if __name__ == "__main__":
    main()
