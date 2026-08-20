# Thermodynamics Past Exam Booklet — Weeks 1–6

> [!important] Main document
> [[Thermodynamics-Past-Exam-Booklet-Weeks-1-6.pdf|Open the 30-page past-exam booklet]]

This booklet follows the question-and-answer format of the v2 tutorial booklet. It collects **22 rewritten past-exam questions** relevant to the first six weeks:

| Source | Questions | Main coverage |
|---|---:|---|
| Test 1 (2016) | 4 | phase diagrams, R-134a piston-cylinder, rigid tank and water tables |
| Test 2 (2018) | 4 | ideal-gas validity, R-134a tables, piston stops and electrical/paddle work |
| Test 3 (2019) | 4 | phase/table work, electrical heating and ideal-gas process cycle |
| Test 4 (2017 alternative) | 4 | phase diagram, steam piston, room heating and R-134a tables |
| 2025 test | 3 | sensible heat, spring-loaded piston and condenser heat exchanger |
| Selected end-of-year problems | 3 | refrigeration balances and COP as Week 5–6 stretch applications |

Every answer includes the rewritten question, source page, system and boundary, assumptions, Given/Find information, the governing model, property values where required, sequential calculations, boxed answers and a common-trap check. **Fourteen source diagrams or official worked figures** are embedded.

## Scope boundary

The end-of-year selection includes only questions that directly extend first-six-week steady-flow, heat-exchanger, refrigeration and COP ideas. Otto, Diesel, detailed Brayton-regenerator and Rankine-cycle problems were excluded because they require later cycle theory.

The 2025 spring-loaded-piston question contains a likely source inconsistency: its printed final state produces net compression although the prompt asks for “work produced.” The booklet preserves the literal calculation and flags the conflict rather than silently changing the data.

## Source and rebuild files

- Editable master: [[Thermodynamics-Past-Exam-Booklet-Weeks-1-6.tex]]
- Chapter source files: `chapters/`
- Embedded source figures: `question-images/`
- Verification report: `verification/verification-report.json`

From this `past-exams` folder:

```bash
tectonic -X compile Thermodynamics-Past-Exam-Booklet-Weeks-1-6.tex
```

## Verification

- 30 A4 pages; unencrypted.
- 22 rewritten questions, 22 system/boundary statements and 22 assumption sets.
- 14 image references, with all dependencies present.
- Representative arithmetic was independently recalculated.
- Every page was rendered and visually checked for clipping, overflow, blank pages and broken figures.
- Installed PDF hash matches the verified build artifact.

Return to [[Thermodynamics Exam Pack v2]].
