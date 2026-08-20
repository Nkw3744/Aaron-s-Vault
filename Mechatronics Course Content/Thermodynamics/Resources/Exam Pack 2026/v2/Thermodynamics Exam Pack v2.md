# Thermodynamics Exam Pack v2

> [!important] Recommended exam resources
> [[Thermodynamics-Half-Semester-Resource-v2.pdf|Expanded half-semester theory resource v2]] · [[Thermodynamics-Tutorial-Booklet-v2.pdf|Rewritten tutorial booklet v2]]

## What changed from v1

### Theory resource v2

The expanded 12-page resource explains why each model and equation applies rather than presenting formulas alone. It includes:

- a seven-line exam setup and system-selection table;
- distinctions between closed systems, control volumes, steady and transient processes;
- pressure, state, equilibrium, heat, work and ideal-gas explanations;
- phase classification, quality, interpolation and compressed-liquid guidance;
- boundary-work path selection and closed-system energy models;
- mass balance, the full steady-flow energy equation and device templates;
- heat-engine, refrigerator, heat-pump and Carnot explanations;
- worked mini-examples, common traps and final answer templates;
- visually checked lecture figures.

Editable source: [[Thermodynamics-Half-Semester-Resource-v2.tex]]

### Tutorial booklet v2

The 47-page tutorial booklet rewrites all **61 recoverable questions** and places the expanded solution directly with each question:

| Week | Questions | Main topics |
|---|---:|---|
| 1 | 10 | properties, pressure and hydrostatics |
| 2 | 10 | energy, work and power |
| 3 | 14 | pure substances, tables, interpolation and ideal gases |
| 4 | 12 | boundary work and closed-system energy |
| 5 | 10 | control volumes and steady-flow devices |
| 6 | 5 | second law, engines and refrigeration |

Every question includes the available source wording, any vagueness or data warning, system type and boundary, assumptions, Given/Find, governing model, sequential working with units, a boxed result and a common-trap check. Nine source figures are embedded where geometry or a process path is needed.

Editable master: [[Thermodynamics-Tutorial-Booklet-v2.tex]]  
Chapter sources: `chapters/`  
Question figures: `question-images/`

## Source and evidence boundary

This package uses the latest authorised local 2026 Thermodynamics files already pulled from Canvas, plus the current formula sheet, property tables and course notes. It did not require a new live Canvas session. Ambiguous or defective source data are identified rather than silently replaced.

## Verification

- Both `.tex` masters compile from this `v2` folder with Tectonic.
- Theory PDF: 12 A4 pages.
- Tutorial PDF: 47 A4 pages.
- Automated coverage checks passed for 61 questions, 61 system/boundary statements, 61 assumption sets and 61 or more boxed answers.
- All display-math delimiters and question-image dependencies passed.
- Every PDF page was rendered and inspected for clipping, blank pages, overflow and broken figures.
- Machine-readable report: `verification/verification-report.json`.

## Rebuild

From this folder:

```bash
tectonic -X compile Thermodynamics-Half-Semester-Resource-v2.tex
tectonic -X compile Thermodynamics-Tutorial-Booklet-v2.tex
```

V1 remains in the parent folder and has not been overwritten.
