# Saturation Lab 2026 — Source and Requirements Ledger

## Authoritative sources

| Source | Role | Evidence used |
|---|---|---|
| [[Saturation Lab Instructions 2025 Updated - Current 2026.pdf]] | Current assessment specification | Required sections, calculations, discussion prompts and formatting rules |
| [[TH3 Saturation Pressure Apparatus Manual.pdf]] | Apparatus and measurement physics | 2.4 L boiler, 0–7 bar gauge operating range, PT100 location, air-purge requirement and pressure measurement |
| [[Thermo Tables Reference.pdf]] | Reference saturation data | Table A–5 pressure–temperature values used for interpolation |
| [[Saturation Lab Data 2026]] | Raw 2026 data | $P_{atm}=101.65$ kPa, nine gauge-pressure readings and nine resistance readings |
| [[Figure 4 - Whiteboard data.jpeg]] | Primary photographic data evidence | Whiteboard data, atmospheric pressure and calibration calculation |
| [[Figure 5 - Controller calibration.jpeg]] | Instrument evidence | PT100 resistance display and 138.7 Ω = 100 °C label |
| [[Figure 1 - TH3 apparatus.jpeg]] | Apparatus evidence | Actual boiler, loop, viewing port, gauge, valves and wiring |
| [[Lab Assignment 2025.pdf]] | Prior high-performing structural benchmark | Concise section order and expected reporting scope; numerical results were not reused |

## Requirement coverage

| Current requirement | Report evidence |
|---|---|
| Synopsis of entire report | Synopsis |
| Aim, equipment and method | Sections 1, 3 and 4 |
| Convert gauge to absolute pressure | Equation and worked calculation in Sections 2 and 5.1 |
| Plot experimental temperature versus absolute pressure | Figure 2 |
| Plot steam-table values on same axes | Figure 2 |
| Fit $T=AP^n$ to both datasets and state $A,n$ | Table 2 and Section 6.2 |
| Interpolate $T_{th}$ at every experimental pressure | Table 1 and worked interpolation |
| Calculate point errors and average error | Table 1, Figure 3 and Section 5.2 |
| Compare experimental and theoretical graphs | Section 6.1 |
| Discuss equation accuracy and usefulness | Section 6.2 |
| Discuss trend and average error | Section 6.3 |
| Discuss steam/water equality, thermal lag and heat loss | Section 6.4 |
| Discuss sources of error | Section 6.5 |
| Brief conclusion relative to aim | Section 7 |
| Correct captions, axis labels and units | Figures 1–5 and Tables 1–2 |
| No first-person pronouns | Report checked |
| Include only figures referred to in text | Every included figure is introduced and captioned |

## Evidence boundary

The whiteboard's $T_{exp}$ column was not populated; only pressure and PT100 resistance were recorded. Experimental temperatures in the report are therefore **derived**, not direct temperature observations. The adopted calibration is the photographed two-point relation:

- $R_1=109.0\ \Omega$ at $T_1=15^\circ\mathrm{C}$
- $R_2=138.7\ \Omega$ at $T_2=100^\circ\mathrm{C}$
- $\alpha=(R_2-R_1)/(T_2-T_1)=0.34941\ \Omega/{}^\circ\mathrm{C}$

This assumption is defensible because the controller photograph identifies the display as PT100 resistance and independently labels 138.7 Ω as 100 °C. It should nevertheless be confirmed with the lecturer before final submission if a different instrument calibration was intended.

## Improvements over the 2025 benchmark

- Keeps the concise structure that previously performed well.
- Shows the complete resistance-to-temperature and pressure-to-temperature calculation chain.
- Correctly distinguishes signed mean error from mean absolute error.
- Interprets the error trend rather than relying on a near-zero signed average.
- Links each result to primary photographic or published evidence.
- Avoids the internal table inconsistencies present in the extracted 2025 document.
