# Data Engineering and AI Practice Index

Return to the [[Data Engineering and AI Overview|subject overview]] · Follow the [[Data Engineering and AI Roadmap|course roadmap]] · Open the [[Data Engineering and AI Lab Index|lab workspace]].

## Week 1 - Data Inspection

- [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Lab 01 - Student Exam Performance/Lab 01 - Data Inspection Exercise.pdf|Data inspection exercise]] - apply the Week 1 workflow to a new dataset
- [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Lab 01 - Student Exam Performance/Lab 01 - Palmer Penguins Worked Example.pdf|Palmer Penguins worked example]] - model answer and reusable inspection pattern
- [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Lab 01 - Student Exam Performance/Lab 1 - Annotated Student Exam Performance.ipynb|Annotated Student Exam Performance notebook]] — executable analysis kept beside its source dataset
- [[Data Engineering and AI Lab Index|Lab workspace]] — direct access to notebooks, datasets, handouts and the Arrhythmia material
- Related concept: [[Foundations of Data Engineering and AI]]

The current Lab 1 folder keeps the exercise, worked example, executed notebook and `StudentsPerformance.csv` together. Use the [[Data Engineering and AI Lab Index|lab workspace]] as the stable entry point rather than browsing the implementation folders directly.

The current Canvas announcement asks students to first run the code on pages 28–43 of the Week 1 slides, then work through the Palmer Penguins example, and only then complete the Student Exam Performance exercise independently. Teaching assistants assess understanding and results during scheduled lab sessions; see [[Data Engineering and AI Current Canvas Information]].

## Weeks 2–3 — Arrhythmia sequence

- [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Labs 02 and 03 - Arrhythmia/Labs 2 and 3 - Arrhythmia worked example and Assessment 1 preparation.pdf|Labs 2–3 worked example and Assessment 1 preparation]]
- [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Labs 02 and 03 - Arrhythmia/Labs 2 and 3 - Annotated Arrhythmia Worked Example.ipynb|Annotated Arrhythmia notebook]] — executable combined workflow for Labs 2 and 3
- [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Labs 02 and 03 - Arrhythmia/arrhythmia/arrhythmia.names|Dataset description]] · [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Labs 02 and 03 - Arrhythmia/arrhythmia/arrhythmia.data|raw Arrhythmia data]]
- [[Data Engineering and AI Lab Index|Lab workspace and file-status note]]

The verified worked example loads 452 × 280 raw records and produces 448 × 281 cleaned records after removing four internally unreliable combinations. It retains unusual but plausible patients, keeps the untouched raw table available, and demonstrates why outlier flags and sensitivity capping are analytical checks rather than automatic deletion rules. The heart-rate t-test is not significant (`p = 0.1441`), while sex and arrhythmia status are associated in this sample (`χ² = 21.73`, `p ≈ 0.000003`); neither result supports a causal claim.

For revision, pair the Arrhythmia cleaning note with [[Data Visualisation and Inferential Statistics]] so the source-driven analysis sequence stays clear: inspect representation, clean conservatively, visualise the cleaned data, then interpret any test result in context.

## Week 4 — Machine learning techniques

- [[ENGE707 Lab4_AMK.docx|Lab 4 exercise]] · [[ENGE707_Week4_Notes.docx|Week 4 notes]] · [[lecture4.ipynb|lecture notebook]]
- [[ENGE707 lecture slides-1.pdf|Week 4 lecture slides]]

Run and understand the prior lecture code before continuing. Use the lab and notebook to move from cleaned data into explicit modelling choices rather than treating model fitting as a black box.

## Week 5 — Bio-inspired machine learning

- [[ENGE707-Lab05.pdf|Lab 5 exercise]]
- [[05-Bio-Inspired Machine Learning-ENGE707-3.pdf|Bio-inspired machine-learning lecture pack]]

The lecture introduces evolutionary ideas and genetic algorithms as optimisation and decision-making methods inspired by natural systems.
