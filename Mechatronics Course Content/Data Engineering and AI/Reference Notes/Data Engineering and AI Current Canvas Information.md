---
source: AUT Canvas
canvas_course_id: 23615
course_code: ENGE707_2026_S2
last_checked: 2026-08-20
---

# Data Engineering and AI Current Canvas Information

Return to [[Data Engineering and AI Overview|subject overview]] · Follow the [[Data Engineering and AI Roadmap|course roadmap]] · Open the [[Data Engineering and AI Assessment Index|assessment index]].

## Course structure

ENGE707 treats AI as an end-to-end data system: data collection and preparation feed modelling, deployment, evaluation, and feedback. The published course sequence covers NumPy/Pandas, visualisation and inference, cleaning and quality, machine-learning paradigms and pipelines, bio-inspired learning, deep architectures, feature engineering, data-centric AI, and responsible practice including FAIR, CARE, biculturalism, and Māori data sovereignty.

Recommended tools include Python, NumPy, Pandas, scikit-learn, Git/GitHub, Matplotlib/Seaborn, TensorFlow or PyTorch, and Jupyter or Colab.

- [Canvas homepage](https://canvas.aut.ac.nz/courses/23615/pages/homepage)
- [Course overview](https://canvas.aut.ac.nz/courses/23615/pages/course-overview)
- [Course schedule](https://canvas.aut.ac.nz/courses/23615/pages/course-schedule)
- [Assessment overview](https://canvas.aut.ac.nz/courses/23615/pages/assessment)

## Assessment and project registration

- **Project Phase I — 30%:** the current [live submission](https://canvas.aut.ac.nz/courses/23615/assignments/195248) is due **30 August 2026 at 23:59:59 NZST**. The 9 August announcement says “August 31” without a time; use the live assignment timestamp unless teaching staff clarifies the discrepancy.
- **Final project report, demo, and presentation — 30%:** 11 October 2026 on the overview page.
- **ML/Kaggle competition — 40%:** 18 October 2026 on the overview page.

Project work must be completed in groups of at least two; individual projects are not permitted. Register the team and topic through the [group-registration assignment](https://canvas.aut.ac.nz/courses/23615/assignments/195242) by **31 July 2026 at 23:59:59 NZST**. The 23 and 29 July announcements warn that late registration incurs a **5% deduction from the final project mark**. Team members may come from different lab streams, and marks are based on each student's individual contribution.

The 17 July assessment announcement clarifies that each 30-mark project phase consists of 25 report marks and 5 lab-performance marks. Phase 1 lab marks are earned across Labs 2–6; Phase 2 across Labs 7–11. These marks are based on demonstrated lab performance/results checked by teaching assistants, not merely submitting lab files.

The Week 6 feedback announcement asks every group member to attend the same lab session prepared to explain the approved topic and dataset, problem statement, data structure and quality issues, cleaning and transformation plan, exploratory analysis, and any blockers. Use one shared GitHub repository per group; every member must be a collaborator and make at least two direct commits each week.

## Week 1 and Lab 1

Week 1 presents the `Data → Model → Deployment → Feedback` pipeline, structured/semi-structured/unstructured data, classification/regression/clustering/generative AI, and data-quality risks such as missing values, duplicates, inconsistent categories, class imbalance, and weak assumptions.

The Lab 1 announcement gives this order:

1. Run and understand the code examples on pages 28–43 of the Week 1 slides.
2. Read and run the Palmer Penguins worked example.
3. Complete the Student Exam Performance exercise independently using the same workflow.

The exercise requires documenting the dataset, inspecting its structure and quality, testing assumptions, and applying introductory machine-learning methods. The Canvas Page and announcement both emphasize understanding outputs rather than simply running code.

## Week 2–3 data engineering and laboratory work

The [Data Representation and Data Engineering Page](https://canvas.aut.ac.nz/courses/23615/pages/data-representation-and-data-engineering) and [Data Visualisation and Inferential Statistics Page](https://canvas.aut.ac.nz/courses/23615/pages/data-visualisation-and-inferential-statistics) introduce realistic data extraction, preparation, cleaning, visualisation, and inference. The supplied UCI Arrhythmia material uses 452 patient records with demographic and ECG-derived features. Its main lesson is evidence-led cleaning: inspect documentation and joint plausibility before removing unusual age, height, or weight values; use derived checks such as BMI; handle missing ECG values explicitly; and preserve the untouched raw DataFrame for comparison and reproducibility.

- [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Labs 02 and 03 - Arrhythmia/Labs 2 and 3 - Arrhythmia worked example and Assessment 1 preparation.pdf|Labs 2–3 worked example and Assessment 1 preparation]] — available combined reference
- [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Labs 02 and 03 - Arrhythmia/Labs 2 and 3 - Annotated Arrhythmia Worked Example.ipynb|Annotated Labs 2–3 notebook]] — executable working file
- [[Data Engineering and AI Lab Index|Lab workspace and missing-file note]] — records the three named Week 2–3 teaching originals that are not currently present in the synced vault
- [[Arrhythmia Data Representation and Quality]] — durable concept note for provenance, schema, cleaning, missingness, and plausibility checks
- [[Data Visualisation and Inferential Statistics]] — durable concept note for plots, uncertainty, assumptions, and statistical interpretation after cleaning

## Weeks 4–5 machine learning

- **Week 4:** move from the cleaned Arrhythmia dataset into rule-based and statistical machine-learning approaches, coding along from the prior lecture output. The imported lab, notes, slides, and notebook are retained together under `Practice/Labs/Canvas Source Materials/Week 04` and `Source Material/Lectures/Week 04`.
- **Week 5:** bio-inspired machine learning introduces evolutionary ideas and genetic algorithms for learning, adaptation, optimisation, and decision-making. The current lab and lecture pack are retained under the Week 05 source folders.
- Two PNGs embedded only as Homepage decoration were deliberately excluded.

## Sources

- [[Week 01 - Course Introduction.pdf]] - compact course introduction and expectations imported from the Week 1 Canvas Page
- [[Week 01 - Foundations of Data Engineering and AI.pdf]] - lecture slides; the current Canvas PDF was not imported again because normalized content matched this renamed local copy
- [[Week 01 - Detailed Theory Notes.pdf]] - theory notes; equivalent to the current Canvas DOCX
- [[Lab 01 - Palmer Penguins Worked Example.pdf]] - worked inspection/analysis pattern; equivalent to the Canvas DOCX
- [[Lab 01 - Data Inspection Exercise.pdf]] - independent Student Exam Performance exercise; equivalent to the Canvas DOCX
- [Week 1 Canvas Page](https://canvas.aut.ac.nz/courses/23615/pages/foundations-of-data-engineering-and-ai-data-handling-fundamentals) - current module context and authoritative links

## Provenance

Canvas pages and accessible file metadata were read through Aaron's authenticated student session. Local imports were verified by size and SHA-256; renamed PDF/DOCX equivalents were detected with normalized text-shingle comparison.
