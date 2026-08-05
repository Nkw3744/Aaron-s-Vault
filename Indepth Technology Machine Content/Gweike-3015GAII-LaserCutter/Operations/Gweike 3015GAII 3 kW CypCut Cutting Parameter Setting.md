---
aliases:
  - Gweike 3015GAII cutting parameters
  - 3 kW CypCut parameter setting
machine: Gweike 3015GAII
controller: CypCut
laser_power: 3 kW
source_reviewed: 2026-07-31
source_scope: Official BOCHU CypCut V6.5 guidance, official Gweike process guidance, the local 3015GAII-family installation manual, and a third-party 3000 W speed-and-gas reference table
status: commissioning reference — local recipes require coupon validation
---

# Gweike 3015GAII — 3 kW CypCut Cutting Parameter Setting

> [!danger] Starting references, not production recipes
> Do **not** load an internet table into CypCut and run a full sheet. A transferable recipe depends on the installed laser-source model, cutting head, collimating/focusing optics, nozzle type and diameter, focus calibration, gas purity and delivered pressure, material grade/surface/actual thickness, and machine condition. Confirm the installed hardware, preserve the Gweike factory material library, and prove each recipe on a witnessed test coupon.

Return to [[Gweike 3015GAII]].

## Purpose

This document gives a controlled method for creating and validating cutting recipes on the **3 kW Gweike 3015GAII with CypCut**. It explains what CypCut's layer fields mean, provides internet reference speeds and gas pressures for comparison, and defines the evidence to save before a setting is released for production.

The machine's stated 3 kW configuration comes from the local machine record and Aaron's instruction. The available local installation PDF is for a **6 kW 3015GAII-family machine**; it is relevant to the family architecture and mentions CypCut, BCS100 height control, and autofocus wiring, but it is **not proof of the exact 3 kW source, cutting head, optics, or recipe values installed here**.

## Establish the exact machine configuration first

Record these items from labels, CypCut, and the factory handover documents before approving numerical recipes:

| Item | Installed value | Evidence |
| --- | --- | --- |
| Laser source manufacturer and model | Raycus brand stated by Aaron and supported by a branded shipping crate photo; exact installed model still to verify | Installed source nameplate / Gweike handover |
| Rated continuous output | 3 kW stated; nameplate confirmation required | Installed source nameplate |
| Cutting-head manufacturer and model | _To verify_ | Head nameplate |
| Collimating and focusing lens configuration | _To verify_ | Head documentation / Gweike |
| Focus zero and sign convention | _To calibrate_ | Head and CypCut commissioning record |
| Height controller and calibration status | BCS100 appears in the family manual; installed unit to verify | Controller / calibration screen |
| Nozzle type and diameter | _To record per recipe_ | Nozzle marking |
| Assist-gas specification and purity | _To verify_ | Gas certificate / supply specification |
| Pressure available under flow | _To measure_ | Dynamic pressure test |
| CypCut/FSCUT version | _To record_ | About/system screen |
| Factory material-library backup | _Required before editing_ | Exported library and dated checksum |

The supplied photograph shows a **Raycus-branded shipping crate** and the visible number `300747`. It does not show the installed source nameplate, model number, serial number, or rated output, so it supports the manufacturer identification but not the exact source configuration. The photograph itself has not been imported into Obsidian.

## Current application — 1.2 mm galvanized sheet

**Known:** galvanized carbon-steel sheet, approximately 1.2 mm thick; Raycus source brand; machine described as 3 kW; CypCut control. **Still unknown:** HDG versus electro-galvanized coating, coating weight, exact Raycus model, cutting-head model and optics, nozzle inventory, focus-zero convention, gas supply, and factory recipe.

> [!danger] Zinc-fume control is mandatory
> Zinc vaporizes before the steel melts and can generate zinc-containing fume and fine deposits. Run only with the enclosure closed and effective local extraction/filtration operating. Verify airflow and filter condition, control exposure during filter replacement, and follow the sheet SDS and workplace risk assessment. The zinc coating is removed at the kerf, so exposed edges may need specified corrosion protection.

### Preferred process direction

- Use **nitrogen** when a bright, low-oxidation edge and minimum coating damage are important.
- **Clean, dry, oil-free compressed air** is a reasonable lower-cost alternative for suitable thin-sheet work, but expect some oxidation and confirm that the compressor, dryer, filters, pressure, and flow are approved for the machine.
- Do not choose oxygen as the first process for this 1.2 mm application unless an oxidized edge and a wider zinc-damage zone are acceptable.
- For nitrogen or air on thin galvanized carbon steel, Gweike's nozzle guide gives a **1.5 mm single-layer nozzle** as the common 1–2 mm starting specification. The physical nozzle must match the installed cutting-head model.

### Nitrogen commissioning card

The closest Gweike published examples are 1.0 mm galvanized sheet at 45–55 m/min, 14 bar and −0.5 mm focus, and 2.0 mm sheet at 18–24 m/min, 16 bar and −1.0 mm focus. A straight-line interpolation at 1.2 mm gives approximately 39.6–48.8 m/min, 14.4 bar and −0.6 mm. This interpolation is **a test-plan calculation, not a Gweike or Raycus production recipe**.

| CypCut item | First controlled trial | Evidence and constraint |
| --- | --- | --- |
| Material | Actual 1.2 mm galvanized production offcut | Record grade, HDG/EG, coating weight and surface condition |
| Gas | Nitrogen | Use verified purity and dynamic delivery pressure |
| Nozzle | 1.5 mm single layer | Gweike 1–2 mm N₂/air starting selection; confirm head compatibility |
| Pressure | Begin around 14 bar under flow | Gweike 1.0 mm example; do not exceed system ratings |
| Speed ladder | 40, 44 and 48 m/min | Covers the rounded 1.2 mm interpolation band |
| Focus ladder | −0.4, −0.6 and −0.8 mm | Only after confirming the installed head's zero and sign convention |
| Cut height | Retain the known-good factory thin-sheet value | Gweike's general guide band is 0.5–1.0 mm, but the installed head controls the final value |
| Peak power, duty and frequency | Copy the factory Raycus thin-carbon-steel N₂ layer | No verified source-specific values found; do not invent them |
| Pierce stages and delay | Copy the factory 1.0–1.5 mm recipe, then prove on coupons | Zinc vapor can disturb piercing and contaminate the protective window |
| Lead-in and compensation | Use the factory thin-sheet strategy; inspect kerf before changing compensation | Final value depends on optics, focus and measured kerf |

Run the **speed ladder first** while holding all other settings constant. Select the best complete cut, then run the focus ladder at that speed. Label each coupon and inspect penetration, bottom dross, top-edge coating damage, striations, corner heat, dimensional result and protective-window/nozzle contamination. Repeat the selected combination at least three times before releasing a sheet.

If compressed air will be used instead, keep a separate CypCut layer and validation record. Do not silently substitute air for nitrogen in a proven recipe because gas chemistry, delivered pressure/flow and edge oxidation change.

## What the CypCut fields mean

The official BOCHU **CypCut User Manual V6.5**, section 3.13, states that CypCut provides 16 process layers. Each layer can carry its own speed, laser, gas, pressure, cut-height, focus, piercing, and related settings. BOCHU explicitly warns that available options vary with the laser source and gas configuration and that values shown in the manual are references only; the operator must use the display and configuration of the actual machine.

### Basic and machining fields

- **Cutting speed:** target linear speed. Actual speed falls below the set value at corners and during acceleration/deceleration.
- **Lift height:** Z height used when moving between contours and when machining is paused.
- **Cut height:** nozzle-to-sheet following distance during the cut.
- **Gas type:** selected assist gas.
- **Gas pressure:** commanded cutting pressure where a proportional valve is fitted. Check pressure under real flow, not only regulator static pressure.
- **Peak power:** percentage of the source's available peak power. The CypCut manual illustrates that 80% on a 3,000 W source limits maximum power to 2,400 W.
- **Cut pwr:** PWM duty cycle.
- **Cut Freq:** PWM firing frequency.
- **Cut Focus:** focus position relative to the nozzle tip. The machine/head convention and calibrated zero must be confirmed before copying values.
- **Delay Time:** laser-on dwell used to establish penetration at the start.
- **Laser-off delay:** delay before the laser turns off.
- **Step time:** transition time from pierce height to cut height.
- **Extra puffing:** gas-only cooling after piercing.

### Thick-plate and corner controls

- **Pre-pierce:** performs piercing at start points before normal cutting.
- **Slow lead:** uses a controlled low-speed starting length to make sure thick plate is fully established before normal speed.
- **Lead-line technique:** after piercing thick stainless, the head can rise to clear plasma, return to cut height, travel a stable distance at lead speed, then enter normal cutting.
- **Real-time power/frequency regulation:** varies duty/frequency with actual speed. This can reduce corner overburn, but it must be tuned on the real source and cannot be copied blindly.

For continuous-wave cutting, the delivered average power follows the source output, peak-power percentage, duty cycle, and—when enabled—the dynamic power curve. Do not treat `Peak power`, `Cut pwr`, and the displayed source rating as interchangeable.

## Assist-gas selection

### Carbon or mild steel

Oxygen is commonly used for thicker carbon steel because the oxidation reaction contributes heat. It uses much lower pressure than inert-gas cutting but leaves an oxidised edge. Excess oxygen pressure, wrong focus, or an unsuitable nozzle can make the kerf unstable and reduce edge quality.

### Stainless steel

Nitrogen is normally used where an oxidation-free edge is required. It demands high gas flow and pressure, so the nozzle, delivery line, purity, and dynamic pressure strongly affect results. Air can reduce gas cost but changes edge chemistry and colour; use it only where the process and final use permit it.

### Aluminium and brass

Nitrogen is a common reference gas. These reflective alloys require confirmation that the installed source/head combination and protection system support the material and thickness. Use clean material, correct extraction, and a verified nozzle/focus setup. Gweike's own power-selection guidance describes brass/copper as highly application-dependent and says they require a proven process configuration and sample validation; it does not present 3 kW as a universal brass/copper recommendation.

### Gas safety

- Oxygen substantially increases fire and combustion risk: keep fittings and lines oxygen-clean and free from oil or grease.
- Nitrogen can displace oxygen: ensure extraction and ventilation are operating and respond to oxygen-deficiency alarms.
- High-pressure gas and compressed air require rated regulators, hoses, valves, and fittings.
- Air used for cutting must meet the machine supplier's cleanliness, dryness, and oil-free requirements.
- Never defeat doors, interlocks, fume extraction, height control, collision protection, or back-reflection protections to obtain a cut.

## Internet 3 kW speed/pressure reference

> [!warning] Evidence boundary
> The following numbers are transcribed from MachineMFG's **“3000W Fiber Laser Cutting Machine Parameter Tables”**. MachineMFG is not Gweike, BOCHU, the installed source manufacturer, or the cutting-head manufacturer. The chart does not define the installed nozzle, source, focus-zero convention, pierce sequence, or all optical details. Treat it as a **comparison range for coupon planning only**, not an approved Gweike recipe.

### Carbon steel with oxygen

The source chart gives the same speed for its `100 × 125` and `100 × 150` focal-length columns.

| Thickness (mm) | O₂ pressure (bar) | Reference speed (m/min) | Reported edge |
| ---: | ---: | ---: | --- |
| 1 | 1.00 | 10–16 | Bright |
| 2 | 1.00 | 5.0–8.0 | Bright |
| 3 | 0.85 | 4.0–4.5 | Bright |
| 5 | 0.75 | 3.0–3.5 | Bright |
| 6 | 0.75 | 1.8–2.2 | Bright |
| 8 | 0.70 | 1.8–2.2 | Bright |
| 10 | 0.70 | 1.1–1.3 | Semi-bright |
| 12 | 0.70 | 0.8–1.0 | Frosted |
| 14 | 0.70 | 0.6–0.8 | Frosted |
| 16 | 0.70 | 0.5–0.8 | Frosted |
| 18 | 0.70 | 0.5–0.7 | Frosted |
| 20 | 0.70 | 0.4–0.6 | Frosted |

The table is **not a verified 3015GAII capacity rating**. Confirm the factory-rated maximum thickness and pierce capability for the installed source/head before attempting thick plate.

### Stainless steel with nitrogen

The source publishes two optics columns. The large difference on thin sheet demonstrates why the installed optical configuration must be confirmed.

| Thickness (mm) | N₂ pressure (bar) | Speed for chart `100 × 150` (m/min) | Speed for chart `100 × 190` (m/min) |
| ---: | ---: | ---: | ---: |
| 1 | 12 | 35–45 | 12–20 |
| 2 | 14 | 14–16 | 8–12 |
| 3 | 16 | 8–9 | 8–9 |
| 4 | 16 | 4–5 | 4–5 |
| 5 | 18 | 2.5–3.3 | 2.5–3.3 |
| 6 | 20 | 1.6–2.1 | 1.6–2.1 |
| 8 | 20 | 0.9–1.2 | 0.9–1.2 |
| 10 | 20 | 0.6–0.8 | 0.6–0.8 |

### Aluminium alloy with nitrogen

| Thickness (mm) | N₂ pressure (bar) | Speed for chart `100 × 125` (m/min) | Speed for chart `100 × 150` (m/min) |
| ---: | ---: | ---: | ---: |
| 1 | 12 | 30–35 | 12–20 |
| 2 | 14 | 12–14 | 8–12 |
| 3 | 14 | 7.0–7.5 | 7.0–7.5 |
| 4 | 14 | 5.0–6.5 | 5.0–6.5 |
| 5 | 18 | 3.0–3.5 | 3.0–3.5 |
| 6 | 20 | 1.8–2.0 | 1.8–2.0 |
| 8 | 20 | 0.9–1.0 | 0.9–1.0 |

One source cell appears as `18-2`, which is evidently malformed; this note records the matching companion value **1.8–2.0 m/min** while flagging that the chart itself contains a transcription-quality problem. Verify independently before use.

### Brass with nitrogen

| Thickness (mm) | N₂ pressure (bar) | Reference speed (m/min) |
| ---: | ---: | ---: |
| 1 | 12 | 20–30 |
| 2 | 12 | 10–14.5 |
| 3 | 14 | 6.2–7.0 |
| 4 | 16 | 3.0–4.5 |
| 5 | 18 | 2.0–2.8 |
| 6 | 20 | 1.2–1.5 |

## Controlled parameter-setting workflow

### 1. Preserve the known-good state

1. Export or copy the Gweike factory material library.
2. Record CypCut/FSCUT version and the source/head configuration.
3. Save a dated copy of any recipe being changed.
4. Create a new commissioning recipe; never overwrite the only known-good recipe.

### 2. Prove machine condition before tuning

- Confirm extraction, chiller, source, gas system, lubrication, interlocks, and alarms are normal.
- Inspect the protective window and optics according to the head/manufacturer procedure.
- Fit an undamaged nozzle of the specified type and diameter.
- Check nozzle centring/coaxiality.
- Calibrate height following and verify stable capacitance on the actual material.
- Confirm focus zero and sign convention.
- Measure assist-gas pressure while flowing through the selected nozzle.
- Verify sheet material, grade, actual thickness, coating, flatness, and surface condition.

A recipe cannot compensate reliably for dirty optics, a damaged/off-centre nozzle, incorrect focus zero, poor gas delivery, or unstable height following.

### 3. Build a representative coupon

Use scrap from the same sheet batch. Include:

- a pierce away from the final part;
- a straight cut long enough to reach target speed;
- inside and outside corners;
- a small hole and a larger contour;
- a lead-in and lead-out;
- enough spacing that one failed test does not damage the next.

### 4. Tune one system at a time

1. **Pierce first:** achieve repeatable penetration without excessive crater, spatter, or protective-window contamination. Keep pierce height, gas, power/duty/frequency stages, dwell, and step-down sequence recorded separately from cut settings.
2. **Cut speed next:** hold focus, gas, nozzle, height, and laser settings constant. Test a small speed ladder around the best available factory or supplier value.
3. **Focus next:** hold the chosen speed and other variables constant. Move through small, controlled focus increments permitted by the installed head documentation.
4. **Gas pressure next:** verify dynamic pressure and tune in controlled increments. More pressure is not automatically better; flow quality and nozzle geometry matter.
5. **Cut height/nozzle:** change only with a reason supported by the head/nozzle documentation and collision margin.
6. **Corners and small features:** after straight cuts are sound, tune CypCut's dynamic power/frequency curve, corner behaviour, lead, and small-contour strategy.
7. **Repeat:** make at least three coupons at the selected recipe before release.

### 5. Judge the cut with evidence

Record:

- complete penetration and pierce reliability;
- top and bottom kerf condition;
- dross amount, type, and removal effort;
- striation angle and consistency;
- edge oxidation/colour where relevant;
- corner overburn and small-feature accuracy;
- dimensional result and kerf/compensation;
- heat distortion;
- nozzle/protective-window condition after the test;
- gas consumption and pressure stability.

Do not diagnose from dross alone. Similar-looking defects can arise from speed, focus, gas delivery, nozzle centring, height, optics, material condition, or source instability. Change one variable, label the coupon, and compare.

## Recipe record

| Field | Validated value |
| --- | --- |
| Recipe ID / revision | |
| Date and operator | |
| Material specification and batch | |
| Actual measured thickness | |
| Laser source / head / optics | |
| Nozzle type and diameter | |
| Gas, purity, static and dynamic pressure | |
| Cut speed | |
| Peak power / cut duty / frequency | |
| Focus position and calibrated zero | |
| Cut height | |
| Pierce stages and dwell | |
| Lead-in / lead technique | |
| Dynamic power/frequency curve | |
| Kerf compensation | |
| Coupon identifiers | |
| Inspection result | |
| Approved by | |

## Settings still required from Gweike or the installed hardware

The reviewed public sources do **not** provide a trustworthy, exact 3 kW 3015GAII recipe for:

- source-specific peak power, duty cycle, and frequency;
- autofocus numerical positions and sign convention;
- nozzle type/diameter by material and thickness;
- pierce stages, heights, dwell times, and cooling cycles;
- cut height;
- lead-in dimensions and slow-lead settings;
- dynamic corner power/frequency curves;
- factory-approved maximum thickness.

Obtain these from the machine's factory material library, Gweike commissioning engineer, installed laser-source manual, and installed cutting-head manual. Record them in this document only after they are tied to the exact hardware and proved by coupons.

## Sources

### Primary controller source

- [BOCHU — CypCut product and official downloads](https://www.bochu.com/en/soft/cypcut/) — official software page; describes integrated CAD/Nest/CAM operation and graphical cutting-technique settings.
- [BOCHU — CypCut User Manual V6.5 (official PDF)](https://d.fscut.com/wordpress-fscut/2020/09/CypCut-user-manual-V6.5.pdf) — section 3.13 defines layer parameters, piercing-related controls, slow lead, lead-line technique, and real-time power/frequency regulation. The manual explicitly says parameter options vary by source/gas configuration and must follow the actual machine.

### Machine and process sources

- [[Indepth Technology Machine Content/Gweike-3015GAII-LaserCutter/Manuals/Gweike-LF3015GAII-InstallationManual-6kW-2026.pdf|Local 3015GAII-family 6 kW installation manual]] — evidence for the local machine family documentation and references to CypCut, BCS100 height control, and autofocus architecture; not an exact 3 kW cutting recipe.
- [Gweike — GA Series Fiber Laser Cutter Selection & Configuration Guide](https://www.gwklaser.com/about/technical/ga-series-fiber-laser-cutter-selection-configuration-guide.html) — Gweike series context; no exact 3 kW recipe was available in the reviewed page content.
- [Gweike — How to Choose Fiber Laser Cutting Power](https://www.gwklaser.com/about/technical/fiber-laser-cutting-power-selection.html) — official system-level guidance: power selection depends on material mix, thickness distribution, gas strategy and edge requirement; optics, nozzle, gas delivery, source/head configuration and sample validation still control the result.
- [Gweike — How to Laser Cut Stainless Steel](https://www.gwklaser.com/about/technical/Laser-Cutting-Stainless-Steel.html) — official qualitative guidance for nitrogen/air selection, nozzle and focus checks, one-variable-at-a-time coupon development, defect diagnosis and recipe records. The page intentionally avoids inventing universal wattage/speed recipes.
- [Gweike — How to Laser Cut Galvanized Steel: Gas, Settings & Safety](https://www.gwklaser.com/how-to-cut-galvanized-sheet-metal.html) — official galvanized-sheet guidance and the closest published 3 kW numerical examples: 1.0 mm and 2.0 mm nitrogen settings, gas-selection trade-offs, coating effects, zinc-fume controls and coupon validation.
- [Gweike — Fiber Laser Cutting Nozzle Selection Guide](https://www.gwklaser.com/fiber-laser-cutting-nozzle-selection-guide.html) — official general nozzle-selection reference; for 1–4 kW thin carbon steel with nitrogen/air it lists single-layer nozzles, including 1.5 mm for 1–2 mm sheet, while requiring confirmation against the installed head.

### Secondary numerical reference

- [MachineMFG — 3000W Fiber Laser Cutting Machine Parameter Tables](https://www.machinemfg.com/3000w-fiber-laser-cutting-machine-parameter-tables/) — third-party gas-pressure and speed tables for carbon steel, stainless steel, aluminium alloy, and brass. Use only as a comparison source for coupon planning.
