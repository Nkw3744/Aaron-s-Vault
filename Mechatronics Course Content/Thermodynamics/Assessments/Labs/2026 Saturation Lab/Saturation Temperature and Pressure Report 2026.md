# Saturation Temperature and Pressure Report 2026

**Author:** Aaron Taylor — 24232594  
**Course:** ENME 601 Thermodynamics  
**Current evidence-reconciled version:** v4

## Current report

- [[SaturationAndPressureLab-AaronTaylor-24232594-v4.pdf|Open the v4 PDF report]]
- [[SaturationAndPressureLab-AaronTaylor-24232594-v4.tex|LaTeX source]]
- [[analyse_saturation_2026_v4.py|Reproducible analysis]]
- [[Saturation Lab 2026 Calculations v4.csv|Processed calculations]]
- [[SaturationAndPressureLab-AaronTaylor-24232594-v4-verification.txt|v4 verification record]]
- [[Saturation Lab Data 2026|Raw evidence and conversion-method reconciliation]]

## Evidence-based processing decision

Aaron's nine recorded gauge-pressure and PT100-resistance readings and the measured atmospheric pressure of 101.65 kPa are unchanged. The photographed whiteboard from the Tuesday 8–10 laboratory session explicitly records the following processing points:

- $R_1=109.0\ \Omega$ at $T_1=15\,{}^\circ\mathrm{C}$
- $R_2=138.7\ \Omega$ at $T_2=100\,{}^\circ\mathrm{C}$
- $\alpha=(R_2-R_1)/(T_2-T_1)=0.34941\ \Omega/{}^\circ\mathrm{C}$
- $T_{exp}=T_1+(R-R_1)/\alpha$

The v4 report uses this session-supplied conversion because it is primary evidence of how Aaron's class was instructed to process these readings. It explicitly discloses that this differs from the manufacturer's general Data Sheet 1 bridge correction followed by the Data Sheet 2 PT100 reference chart. The session method is therefore neither described as fabricated nor represented as the manufacturer's standard calibration.

## Main v4 results

- Experimental fit: $T=37.633P^{0.2146}$, $R^2=0.99895$
- Direct Table A–5 fit: $T=31.019P^{0.2557}$, $R^2=0.99983$
- Mean signed error: $-4.32\%$
- Mean absolute error: $4.32\%$
- Maximum absolute error: $6.47\%$ at 551.65 kPa absolute

The derived experimental temperatures remain below the point-specific steam-table temperatures. The report now gives the calibration uncertainty fuller treatment. All measured resistances ($142.3$–$154.6\ \Omega$) exceed the whiteboard's upper point of $138.7\ \Omega$ at $100\,{}^\circ\mathrm{C}$, meaning the session conversion extrapolates beyond its two supplied points and assumes constant slope above $100\,{}^\circ\mathrm{C}$. The evidence also leaves ambiguity over whether both endpoint values were indicated or bridge-corrected resistance.

Using the same raw readings, the Armfield Data Sheet method produces temperatures approximately $0.75\,{}^\circ\mathrm{C}$ higher at the first point and $8.32\,{}^\circ\mathrm{C}$ higher at the final point. The corresponding mean errors are $-4.32\%$ for the session method and $-1.03\%$ for the manual method. The widening difference demonstrates that conversion choice can create a pressure-dependent error trend. These are method-sensitivity cases rather than statistical uncertainty limits; traceable calibration and repeat measurements would be required for a defensible confidence interval.

## Preserved alternatives

- [[SaturationAndPressureLab-AaronTaylor-24232594-v3.pdf|v3 PDF]] — manufacturer-manual Data Sheet 1 → Data Sheet 2 alternative; mean error $-1.03\%$
- [[Saturation Temperature and Pressure Report 2026-v3|v3 Markdown note]]
- [[SaturationAndPressureLab-AaronTaylor-24232594-v2.pdf|v2 PDF]] — earlier session-method draft; mean error $-4.32\%$
- [[Saturation Temperature and Pressure Report 2026-v2|v2 Markdown note]]

The difference between v3 and v4 is a resistance-to-temperature processing decision, not a change to Aaron's raw experimental readings.
