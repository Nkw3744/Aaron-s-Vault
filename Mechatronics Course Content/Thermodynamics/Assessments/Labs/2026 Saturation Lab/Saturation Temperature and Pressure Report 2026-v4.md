# Saturation Temperature and Pressure Report 2026 — v4

**Author:** Aaron Taylor — 24232594  
**Course:** ENME 601 Thermodynamics

## Deliverables

- [[SaturationAndPressureLab-AaronTaylor-24232594-v4.pdf|PDF report]]
- [[SaturationAndPressureLab-AaronTaylor-24232594-v4.tex|LaTeX source]]
- [[analyse_saturation_2026_v4.py|Analysis script]]
- [[Saturation Lab 2026 Calculations v4.csv|Calculation CSV]]

## Method selection

The original nine pressure/resistance readings are preserved. Experimental temperatures use the two-point relationship photographed on the laboratory whiteboard for Aaron's Tuesday 8–10 session:

$$
\alpha=\frac{138.7-109.0}{100-15}=0.34941\ \Omega/{}^\circ\mathrm{C},
\qquad
T_{exp}=15+\frac{R-109.0}{0.34941}.
$$

This is reported as a **session-supplied processing method**, not as the Armfield manufacturer's standard calibration. The report discloses that the manual instead specifies Data Sheet 1 bridge correction followed by Data Sheet 2 temperature conversion.

## Results

- Experimental power fit: $T=37.633P^{0.2146}$, $R^2=0.99895$
- Direct Table A–5 fit: $T=31.019P^{0.2557}$, $R^2=0.99983$
- Mean signed and absolute error magnitude: $4.32\%$
- Maximum absolute error: $6.47\%$

The discussion now treats calibration as a substantial source of method uncertainty rather than a single generic error term. Every recorded resistance ($142.3$–$154.6\ \Omega$) exceeds the whiteboard's upper point of $138.7\ \Omega$ at $100\,{}^\circ\mathrm{C}$, so the session method extrapolates beyond its two supplied points and assumes a constant slope above $100\,{}^\circ\mathrm{C}$. The evidence does not establish whether both endpoint resistances were indicated or bridge-corrected values, while the Armfield manual distinguishes between them. Endpoint rounding, display resolution and uncertainty in the $15\,{}^\circ\mathrm{C}$ reference consequently affect every derived temperature.

The report also quantifies method sensitivity. Relative to the session method, the Armfield Data Sheet 1 → Data Sheet 2 temperatures are approximately $0.75\,{}^\circ\mathrm{C}$ higher at the first point and $8.32\,{}^\circ\mathrm{C}$ higher at the final point. This produces mean signed errors of $-4.32\%$ and $-1.03\%$, respectively, and shows that conversion choice can create a pressure-dependent trend. These are sensitivity cases, not statistical confidence limits; a traceable calibration and repeated measurements would be needed to assign a defensible uncertainty interval.
