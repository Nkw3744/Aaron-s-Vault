# Saturation Temperature and Pressure

**ENME 601 Thermodynamics**  
**Author:** Aaron  
**Year:** 2026

> [!note] Draft status
> This report is calculated from the recorded 2026 gauge-pressure and PT100-resistance readings. The experimental temperatures were derived using the calibration written on the laboratory whiteboard: $R_1=109.0\ \Omega$ at $T_1=15^\circ\text{C}$ and $R_2=138.7\ \Omega$ at $T_2=100^\circ\text{C}$.

## Synopsis

The relationship between the saturation temperature and absolute pressure of water was investigated using an Armfield TH3 saturation-pressure apparatus. Nine equilibrium-stage readings were recorded from 50 to 450 kPa gauge pressure. Gauge pressures were converted to absolute pressure using the measured atmospheric pressure of 101.65 kPa, while PT100 resistance readings were converted to temperature using the laboratory calibration. Experimental temperatures were compared with linearly interpolated values from the saturated-water pressure table.

Both datasets followed a smooth power relationship of the form $T=AP^n$. The experimental fit was $T=37.633P^{0.2146}$, compared with $T=30.899P^{0.2563}$ for the steam-table data. Experimental temperatures were below the theoretical values at every point; signed error changed from $-1.21\%$ at 151.65 kPa absolute to $-6.47\%$ at 551.65 kPa absolute, with a mean signed error of $-4.32\%$. The increasing negative deviation indicates a systematic effect rather than random scatter, most plausibly incomplete thermal equilibrium, heat loss and probe lag, residual non-condensable air, or uncertainty in the two-point resistance calibration.

## 1. Aim

To measure the relationship between the saturation temperature and absolute pressure of water, model the relationship with a power law, and assess the accuracy of the apparatus by comparison with published saturated-water data.

## 2. Theory

At liquid–vapour equilibrium, water and saturated steam coexist at one saturation temperature for a given absolute pressure. Increasing pressure raises the saturation temperature, producing a smooth saturation curve in temperature–pressure space.

The pressure sensor records gauge pressure, so atmospheric pressure must be added:

$$
P_{\mathrm{abs}}=P_1+P_{\mathrm{atm}}.
$$

The measured atmospheric pressure was

$$
P_{\mathrm{atm}}=101.65\ \text{kPa}.
$$

The PT100 conversion used the two calibration points visible in the laboratory evidence:

$$
\alpha=\frac{R_2-R_1}{T_2-T_1}
=\frac{138.7-109.0}{100-15}
=0.34941\ \Omega/{}^\circ\text{C},
$$

and therefore

$$
T_{\mathrm{exp}}=T_1+\frac{R-R_1}{\alpha}
=15+\frac{R-109.0}{0.34941}.
$$

Over the measured range, the saturation relationship was represented by

$$
T_{\mathrm{sat}}=AP_{\mathrm{sat}}^n,
$$

where $A$ and $n$ were determined separately for the experimental and steam-table datasets.

The theoretical temperature at each experimental pressure was found by linear interpolation:

$$
T_{\mathrm{th}}=T_a+\frac{P_{\mathrm{abs}}-P_a}{P_b-P_a}(T_b-T_a).
$$

Signed percentage error was calculated as specified in the lab instructions:

$$
\text{Error }(\%)=\frac{T_{\mathrm{exp}}-T_{\mathrm{th}}}{T_{\mathrm{th}}}\times100.
$$

## 3. Equipment

- Armfield TH3 saturation-pressure apparatus, including the 2.4 L boiler, sight glass, closed pipe loop, filling valve and pressure-relief valve
- Cartridge heaters and Armfield control console
- PT100 platinum resistance thermometer at the saturated-steam measurement point
- Electronic pressure sensor and Bourdon pressure gauge
- Barometer
- Purified or de-ionised water

![[Figure 1 - TH3 apparatus.jpeg|750]]

*Figure 1: Armfield TH3 boiler and pipe loop used to produce and measure saturated steam. The photograph records the actual apparatus, pressure gauge, boiler viewing port, valves and sensor wiring used in the 2026 experiment.*

## 4. Method

1. The drain and isolating valves were checked closed and the console power was switched off.
2. The boiler was filled with de-ionised water to approximately halfway up the sight glass while the filling-point valve remained open.
3. The water was heated to vigorous boiling. Steam was allowed to escape until the temperature became steady so that air was expelled from the loop.
4. The filling-point valve was closed, creating a closed, constant-volume system containing a saturated water mixture.
5. Heater input was raised for approximately two minutes and then reduced. A reading was recorded only after the PT100 indication had stabilised, limiting thermal-lag error.
6. Gauge pressure and PT100 resistance were recorded at nine stages from 50 to 450 kPa gauge pressure.
7. Gauge pressure was converted to absolute pressure, resistance was converted to temperature, and theoretical saturation temperatures were interpolated from Table A–5.
8. Power-law fits were obtained by linear regression of $\ln T$ against $\ln P$. Temperature errors were then calculated for all nine points.

## 5. Results

### 5.1 Worked calculation

For the first reading, $P_1=50.00\ \text{kPa}$ and $R=142.3\ \Omega$:

$$
P_{\mathrm{abs}}=50.00+101.65=151.65\ \text{kPa},
$$

$$
T_{\mathrm{exp}}=15+\frac{142.3-109.0}{0.34941}=110.30^\circ\text{C}.
$$

The pressure-table values enclosing 151.65 kPa are 111.35 °C at 150 kPa and 116.04 °C at 175 kPa. Therefore,

$$
T_{\mathrm{th}}=111.35+\frac{151.65-150}{175-150}(116.04-111.35)
=111.66^\circ\text{C},
$$

$$
\text{Error}=\frac{110.30-111.66}{111.66}\times100=-1.21\%.
$$

### 5.2 Processed results

**Table 1: Experimental readings, processed temperatures and comparison with saturated-water data**

| $P_1$ (kPa gauge) | $P_{\mathrm{abs}}$ (kPa) | $R$ (Ω) | $T_{\mathrm{exp}}$ (°C) | $T_{\mathrm{th}}$ (°C) | Error (%) |
|---:|---:|---:|---:|---:|---:|
| 50 | 151.65 | 142.3 | 110.30 | 111.66 | -1.21 |
| 100 | 201.65 | 144.8 | 117.46 | 120.46 | -2.49 |
| 150 | 251.65 | 146.9 | 123.47 | 127.62 | -3.25 |
| 200 | 301.65 | 148.7 | 128.62 | 133.70 | -3.80 |
| 250 | 351.65 | 150.1 | 132.63 | 139.02 | -4.60 |
| 300 | 401.65 | 151.1 | 135.49 | 143.75 | -5.75 |
| 350 | 451.65 | 152.6 | 139.78 | 148.03 | -5.57 |
| 400 | 501.65 | 153.8 | 143.22 | 151.95 | -5.75 |
| 450 | 551.65 | 154.6 | 145.51 | 155.57 | -6.47 |

![[Figure 2 - Temperature versus absolute pressure.png|700]]

*Figure 2: Experimental PT100-derived temperature and interpolated steam-table saturation temperature plotted against absolute pressure, with power-law trendlines.*

**Table 2: Power-law fit parameters for $T=AP^n$**

| Dataset | $A$ | $n$ | $R^2$ |
|---|---:|---:|---:|
| Experimental | 37.633 | 0.2146 | 0.99895 |
| Steam-table interpolation | 30.899 | 0.2563 | 0.99984 |

![[Figure 3 - Error versus absolute pressure.png|700]]

*Figure 3: Signed experimental temperature error relative to the interpolated saturated-water values.*

The mean signed error and mean absolute error were both $4.32\%$ in magnitude because every experimental value was below the theoretical value. The maximum absolute error was $6.47\%$ at 551.65 kPa absolute.

## 6. Discussion

### 6.1 Comparison of the saturation curves

Both curves increased smoothly with absolute pressure and both power-law fits had $R^2>0.998$, confirming that the measurements captured the expected form of the saturation relationship. However, the experimental curve became progressively lower than the steam-table curve as pressure increased. The mismatch was therefore systematic rather than the result of scattered readings.

### 6.2 Accuracy and usefulness of the fitted equation

The experimental exponent, $n=0.2146$, was lower than the theoretical value of $0.2563$. Consequently, the experimental equation predicts too little temperature rise as pressure increases. It is useful as an empirical description only within the measured range and for this apparatus calibration. It should not replace the steam tables for design calculations or extrapolation. The theoretical fit follows the reference data more closely and is the more reliable compact approximation over this pressure interval.

### 6.3 Error trend

Error became generally more negative as pressure rose, changing from $-1.21\%$ to $-6.47\%$. A small improvement occurred at 451.65 kPa, but it did not alter the overall trend. This pattern indicates a pressure-dependent bias. Reporting only the mean error would conceal this important behaviour; Figure 3 therefore provides stronger evidence than a single average.

### 6.4 Steam temperature, water temperature and thermal lag

Liquid water and steam have the same saturation temperature only when both phases are in thermodynamic equilibrium at the measured pressure. The PT100 measured steam in the upper pipework rather than liquid in the boiler. During heating, energy must conduct through the fluid, metalwork and probe sheath before the sensor reaches the steam temperature. Heat loss from the exposed loop can also make the local probe temperature lower than the bulk saturation temperature. If readings are taken before full stabilisation, both effects produce a negative temperature error, particularly at higher heater input and pressure.

### 6.5 Likely sources of error

- **Residual air:** air remaining when the filling valve was closed contributes partial pressure. The pressure sensor then measures steam pressure plus air pressure, while saturation temperature depends on the steam partial pressure. This produces a measured temperature below the value expected from total pressure.
- **Thermal lag and insufficient stabilisation:** the increasingly negative error is consistent with the PT100 lagging the changing steam temperature.
- **Heat loss and temperature gradients:** the upper loop and sensor fittings lose heat to the room, so the local steam/probe temperature can be below the boiler saturation temperature.
- **Calibration uncertainty:** experimental temperatures depend on the two-point linear conversion recorded on the whiteboard. Any uncertainty in $R_1$, $T_1$, $R_2$ or sensor linearity affects every result systematically.
- **Pressure measurement:** pressure-sensor calibration, gauge resolution and the atmospheric-pressure reading affect every calculated absolute pressure.
- **Interpolation and rounding:** linear interpolation and recorded precision introduce smaller numerical errors, though these are insufficient to explain the observed trend.

The strongest improvements would be to purge the loop for longer, record only after both resistance and pressure remain stable, use the PT100’s certified resistance–temperature relation or a traceable calibration, and repeat each pressure point to quantify repeatability.

## 7. Conclusion

The experiment reproduced the expected increase in water saturation temperature with absolute pressure. The experimental data were smooth and fitted a power law with $R^2=0.99895$, but they did not match the reference curve as closely as their smoothness alone might suggest. Experimental temperatures were lower than the interpolated steam-table values at all nine points, with a mean signed error of $-4.32\%$ and a maximum absolute error of $6.47\%$. The increasing negative error and lower experimental exponent identify a systematic measurement effect, most likely associated with thermal lag, heat loss, residual air, or resistance-calibration uncertainty. The steam-table data remain the appropriate source for accurate saturation values, while the apparatus successfully demonstrates the qualitative pressure–temperature relationship.

## 8. Evidence and reproducibility

![[Figure 4 - Whiteboard data.jpeg|750]]

*Figure 4: Laboratory whiteboard recording the 2026 gauge-pressure and PT100-resistance series, atmospheric pressure, and the two-point resistance–temperature calibration used in this report.*

![[Figure 5 - Controller calibration.jpeg|650]]

*Figure 5: Armfield TH3 control console showing the PT100 resistance display and the apparatus label stating that 138.7 Ω corresponds to 100 °C. This confirms that the recorded values are resistance readings rather than direct displayed temperatures.*

Calculation source: [[Saturation Lab 2026 Calculations.csv]]  
LaTeX source: [[SaturationAndPressureLab-AaronTaylor-24232594-v2.tex]]
Rendered PDF: [[SaturationAndPressureLab-AaronTaylor-24232594-v2.pdf]]
PDF verification: [[lab1.v2-verification.txt]]  
Reproduction script: [[analyse_saturation_2026.py]]  
Verification output: [[analysis-verification.txt]]  
Requirement ledger: [[Source and Requirements Ledger]]  
Working data note: [[Saturation Lab Data 2026]]

## Reference

1. Çengel, Y. A., Boles, M. A., & Kanoğlu, M. *Thermodynamics: An Engineering Approach*, 9th SI ed. McGraw-Hill, 2020, Table A–5.
2. Armfield Ltd. *TH3 Saturation Pressure Apparatus Instruction Manual*.
