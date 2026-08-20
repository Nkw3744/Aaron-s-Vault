# Saturation Temperature and Pressure

**ENME 601 Thermodynamics**  
**Author:** Aaron  
**Year:** 2026

> [!success] Rebuilt report — v3
> Aaron's original nine gauge-pressure and indicated PT100-resistance readings are unchanged. The temperatures have been rebuilt using the Armfield TH3 Issue 15 correction and PT100 reference tables rather than the earlier two-point interpretation. The previous Markdown report is preserved as [[Saturation Temperature and Pressure Report 2026-v2]].

## Synopsis

The relationship between the saturation temperature and absolute pressure of water was investigated using an Armfield TH3 saturation-pressure apparatus. Nine readings were recorded from 50 to 450 kPa gauge pressure. The measured atmospheric pressure of 101.65 kPa was added to each gauge reading.

The PT100 values were processed in two stages from the Armfield manual:

1. correct the console's indicated resistance using Data Sheet 1; and
2. convert corrected resistance to temperature using Data Sheet 2.

Linear interpolation was used between adjacent entries. Data Sheet 1 explicitly permits interpolation. Data Sheet 2 specifies selection of the closest value; interpolation across its 2 °C intervals was made as a documented processing assumption to preserve the recorded resistance resolution.

The experimental fit was $T=31.218P^{0.2527}$ with $R^2=0.99904$. The direct Table A–5 fit was $T=31.019P^{0.2557}$ with $R^2=0.99983$. All experimental temperatures were slightly below the point-specific reference values. The mean signed error was $-1.03\%$, and the maximum absolute error was $1.89\%$ at 401.65 kPa absolute.

## 1. Aim

To measure the relationship between water's saturation temperature and absolute pressure, obtain an empirical power-law model, and compare the measured values with published saturated-water data.

## 2. Theory and processing

At liquid–vapour equilibrium, saturated liquid water and saturated steam have one saturation temperature for a given absolute pressure. Gauge pressure was converted using

$$
P_{\mathrm{abs}}=P_1+P_{\mathrm{atm}},
\qquad P_{\mathrm{atm}}=101.65\ \text{kPa}.
$$

### Armfield PT100 conversion scope

This is a correction and reference-table conversion, not a new two-point calibration. For an indicated resistance $R_m$ between adjacent Data Sheet 1 entries,

$$
R_c=R_{c,a}+\frac{R_m-R_{m,a}}{R_{m,b}-R_{m,a}}(R_{c,b}-R_{c,a}).
$$

Corrected resistance was then converted to temperature from Data Sheet 2:

$$
T_{\mathrm{exp}}=T_a+\frac{R_c-R_{c,a}}{R_{c,b}-R_{c,a}}(T_b-T_a).
$$

The saturation data were modelled as

$$
T_{\mathrm{sat}}=AP_{\mathrm{sat}}^n.
$$

The point-specific theoretical temperature was linearly interpolated from Table A–5, and signed error was calculated as

$$
\text{Error }(\%)=\frac{T_{\mathrm{exp}}-T_{\mathrm{th}}}{T_{\mathrm{th}}}\times100.
$$

## 3. Equipment

- Armfield TH3 saturation-pressure apparatus with 2.4 L boiler, sight glass, closed pipe loop, filling valve and pressure-relief valve
- Cartridge heaters and Armfield control console
- PT100 platinum resistance thermometer
- Electronic pressure sensor and Bourdon pressure gauge
- Barometer
- De-ionised water

![[Figure 1 - TH3 apparatus.jpeg|750]]

*Figure 1: The Armfield TH3 apparatus used in the 2026 experiment.*

## 4. Method

1. The drain and isolating valves were checked closed and the console power was switched off.
2. The boiler was filled with de-ionised water to approximately halfway up the sight glass while the filling point remained open.
3. Water was heated to vigorous boiling. Steam was vented until the temperature indication stabilised to expel air from the loop.
4. The filling valve was closed. The apparatus was treated as a sealed, approximately constant-volume system containing a saturated water–steam mixture.
5. Heater input was raised for approximately two minutes and reduced.
6. Gauge pressure and indicated PT100 resistance were recorded after stabilisation at nine stages from 50 to 450 kPa gauge pressure.
7. Pressures and resistances were processed as described above. Experimental and direct steam-table values were plotted and fitted separately.
8. After the final reading, heater power was switched off and pressure was released according to the operating instructions. The isolating valve was opened before cooling to prevent a damaging partial vacuum.

## 5. Results

### 5.1 Worked conversion

For $P_1=50.00\ \text{kPa}$ and $R_m=142.3\ \Omega$:

$$
P_{\mathrm{abs}}=50.00+101.65=151.65\ \text{kPa}.
$$

From Data Sheet 1, 142 Ω corresponds to 142.32 Ω corrected and 143 Ω corresponds to 143.54 Ω corrected:

$$
R_c=142.32+\frac{142.3-142}{143-142}(143.54-142.32)
=142.686\ \Omega.
$$

From Data Sheet 2, 142.29 Ω corresponds to 110 °C and 143.04 Ω corresponds to 112 °C:

$$
T_{\mathrm{exp}}=110+\frac{142.686-142.29}{143.04-142.29}(112-110)
=111.056^\circ\text{C}.
$$

The interpolated Table A–5 value is 111.660 °C, giving

$$
\text{Error}=\frac{111.056-111.660}{111.660}\times100=-0.541\%.
$$

### 5.2 Processed dataset

| $P_1$ (kPa gauge) | $P_{\mathrm{abs}}$ (kPa) | $R_m$ (Ω) | $R_c$ (Ω) | $T_{\mathrm{exp}}$ (°C) | $T_{\mathrm{th}}$ (°C) | Error (%) |
|---:|---:|---:|---:|---:|---:|---:|
| 50 | 151.65 | 142.3 | 142.686 | 111.06 | 111.66 | -0.54 |
| 100 | 201.65 | 144.8 | 145.788 | 119.27 | 120.46 | -0.98 |
| 150 | 251.65 | 146.9 | 148.452 | 126.35 | 127.62 | -0.99 |
| 200 | 301.65 | 148.7 | 150.780 | 132.55 | 133.70 | -0.86 |
| 250 | 351.65 | 150.1 | 152.633 | 137.47 | 139.02 | -1.11 |
| 300 | 401.65 | 151.1 | 153.964 | 141.04 | 143.75 | -1.89 |
| 350 | 451.65 | 152.6 | 155.986 | 146.44 | 148.03 | -1.07 |
| 400 | 501.65 | 153.8 | 157.634 | 150.86 | 151.95 | -0.71 |
| 450 | 551.65 | 154.6 | 158.744 | 153.82 | 155.57 | -1.12 |

![[Figure 2 v3 - Experimental and Table A5 values.png|700]]

| Dataset | $A$ | $n$ | $R^2$ |
|---|---:|---:|---:|
| Experimental measurements | 31.218 | 0.2527 | 0.99904 |
| Direct Table A–5 values | 31.019 | 0.2557 | 0.99983 |

![[Figure 3 v3 - Error versus absolute pressure.png|650]]

## 6. Discussion

The close exponents and $R^2$ values show that the apparatus reproduced the expected nonlinear relationship. The experimental equation is useful only as a compact description over 151.65–551.65 kPa absolute. It should not replace steam tables or be extrapolated beyond the tested interval.

All signed errors were negative, but the error did not become progressively more negative with pressure. It ranged from $-0.54\%$ to $-1.89\%$, reached its largest magnitude at 401.65 kPa, and then reduced. This supports a small negative bias with point-to-point variation rather than a continuously growing pressure-dependent error.

### Assumptions

The processing and interpretation assume that:

- air was sufficiently purged for total pressure to approximate steam saturation pressure;
- the boiler water, local steam, pressure indication and PT100 had reached equilibrium before each reading;
- atmospheric pressure remained effectively constant during the run;
- linear interpolation was adequate over the small resistance and steam-table intervals; and
- the Armfield bridge-correction table represented the console and sensor used.

These assumptions are reasonable but were not isolated experimentally. Residual air, thermal lag, exposed-pipe heat loss, resistance-table resolution and pressure uncertainty are therefore plausible explanations consistent with the error, not proven mechanisms.

### Improvements

Repeat measurements would make the experiment stronger. Each pressure stage should be repeated after independent stabilisation, allowing a mean and standard deviation to be reported. An increasing-pressure run could also be compared with a decreasing-pressure run to detect hysteresis. Longer purging, a defined pressure-and-resistance stability criterion, and documented instrument resolutions would strengthen the uncertainty assessment.

## 7. Conclusion

The rebuilt analysis preserved Aaron's original dataset and applied the Armfield TH3 resistance correction and PT100 reference tables. The experimental fit, $T=31.218P^{0.2527}$, closely matched the direct steam-table fit, $T=31.019P^{0.2557}$. The mean signed error was $-1.03\%$, and the maximum absolute error was $1.89\%$. The small negative bias is consistent with the stated assumptions and possible thermal or measurement effects. Repeated measurements are recommended to quantify repeatability and determine whether the remaining bias is systematic.

## 8. Evidence and reproducibility

- Final report: [[SaturationAndPressureLab-AaronTaylor-24232594-v3.pdf]]
- LaTeX source: [[SaturationAndPressureLab-AaronTaylor-24232594-v3.tex]]
- Reproduction script: [[analyse_saturation_2026_v3.py]]
- Calculation table: [[Saturation Lab 2026 Calculations v3.csv]]
- PT100 conversion trace: [[Armfield TH3 PT100 conversion v3.csv]]
- Verification record: [[SaturationAndPressureLab-AaronTaylor-24232594-v3-verification.txt]]
- Original readings and evidence: [[Saturation Lab Data 2026]]
- Armfield manual: [[Sources/TH3 Issue 15 Instruction Manual.pdf]]
- Requirements ledger: [[Source and Requirements Ledger]]
- Previous report note: [[Saturation Temperature and Pressure Report 2026-v2]]
- Previous PDF: [[SaturationAndPressureLab-AaronTaylor-24232594-v2.pdf]]

## References

1. Çengel, Y. A., Boles, M. A., & Kanoğlu, M. *Thermodynamics: An Engineering Approach*, 9th SI ed., McGraw-Hill, 2020, Table A–5.
2. Armfield Ltd. [[Sources/TH3 Issue 15 Instruction Manual.pdf|*TH3 Saturation Pressure Apparatus Instruction Manual*]], Issue 15, Data Sheets 1–2, pp. 22–24.
3. Auckland University of Technology. *ENME 601 Saturation Temperature & Pressure Lab Instructions*, 2025 update used for the 2026 laboratory.
