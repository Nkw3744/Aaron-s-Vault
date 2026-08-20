# Thermodynamics Half-Semester Exam Pack

> [!important] Recommended v2 pack
> [[Thermodynamics Exam Pack v2|V2 guide]] · [[Thermodynamics-Half-Semester-Resource-v2.pdf|Expanded 12-page theory resource]] · [[Thermodynamics-Tutorial-Booklet-v2.pdf|61 rewritten questions with worked answers]] · [[Thermodynamics-Half-Semester-Resource-v2.tex|Theory v2 source]] · [[Thermodynamics-Tutorial-Booklet-v2.tex|Tutorial v2 source]]

V2 adds fuller explanations, worked mini-examples, explicit system boundaries and assumptions, source-vagueness notes, sequential tutorial working and nine necessary question figures. The original v1 package remains below for comparison and source-page facsimiles.

> [!important] Exam pack
> [[Thermodynamics-Half-Semester-Resource.pdf|Compact Weeks 1–6 theory resource (PDF)]] · [[Thermodynamics-Tutorial-Booklet-Weeks-1-6.pdf|Complete tutorial booklet (PDF)]] · [[Thermodynamics-Half-Semester-Resource.tex|Theory LaTeX source]] · [[Thermodynamics-Tutorial-Booklet-Weeks-1-6.tex|Tutorial LaTeX source]]

## V1 preserved package

### Half-semester theory resource

The seven-page A4 theory resource condenses the first half of ENME601 into an exam-facing sequence:

1. system and model selection;
2. systems, properties, state, pressure and temperature;
3. energy transfer, the first law and ideal gases;
4. pure substances, phase classification, quality and interpolation;
5. closed-system energy analysis and boundary work;
6. control volumes and steady-flow devices;
7. heat engines, refrigeration, heat pumps and Carnot limits.

It includes four visually checked source figures from the current lecture set: phase change, moving-boundary work, steady-flow energy analysis and heat engines. The current [[Property Tables 2026.pdf|property tables]] remain authoritative for numerical state values.

### Tutorial booklet

The 161-page tutorial booklet keeps the complete locally held Weeks 1–6 tutorial pages together. Each week begins with a compact method guide and is followed by the original question and official solution pages, preserving source wording, values, diagrams, tables, highlights and handwritten working.

- **Week 1:** current 14-page solutions/teaching deck. No separate clean 2026 question PDF was found locally, so the booklet does not invent one.
- **Week 2:** all ten question pages plus the expanded worked-solutions package.
- **Week 3:** question list, interpolation method, Q1–Q8 pure-substance solutions and Q9–Q14 ideal-gas solutions.
- **Week 4:** all twelve questions plus Q1–Q4, Q5–Q8 and Q9–Q12 official solutions.
- **Week 5:** all ten questions plus the complete official solution set.
- **Week 6:** Q1–Q5 prompt sheet plus the complete official solution set.

## Fast exam route

1. Start with the model selector on page 2 of the theory PDF.
2. For table problems, use the Week 3 workflow and [[Property Tables 2026.pdf]].
3. For boundary work and closed systems, use Week 4.
4. For nozzles, turbines, compressors, throttles, mixing and heat exchangers, use Week 5.
5. For efficiency, COP and Carnot limits, use Week 6.
6. Use the tutorial booklet when a problem resembles a worked source question.

## Editable package

The self-contained package is stored in `Resources/Exam Pack 2026/`. The theory source uses the four images in `figures/`. The tutorial source uses the preserved local PDFs in `build/tutorial-inputs/`. Both sources compile with Tectonic from the package root:

```bash
tectonic -X compile Thermodynamics-Half-Semester-Resource.tex
tectonic -X compile Thermodynamics-Tutorial-Booklet-Weeks-1-6.tex
```

## Related course material

[[Thermodynamics Overview]] · [[Thermodynamics Roadmap]] · [[Thermodynamics Practice Index]] · [[Thermodynamics Reference Index]] · [[Thermodynamics Assessment Index]]
