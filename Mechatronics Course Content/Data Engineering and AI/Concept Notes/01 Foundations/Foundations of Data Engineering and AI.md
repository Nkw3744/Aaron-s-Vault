---
aliases:
  - ENGE707 Week 1
  - Week 1 Foundations
week: 1
source_reviewed: 2026-07-22
source_scope: Week 1 introduction, foundations, detailed theory, inspection exercise, and worked example
---

# Foundations of Data Engineering and AI

> [!info] Course navigation
> [[Data Engineering and AI Overview|Subject overview]] · [[Data Engineering and AI Roadmap|Course roadmap]] · [[Data Engineering and AI Practice Index|Practice index]]
>
> [[Week 01 - Course Introduction.pdf|Course introduction]] · [[Week 01 - Foundations of Data Engineering and AI.pdf|Lecture slides]] · [[Week 01 - Detailed Theory Notes.pdf|Detailed theory notes]]
>
> [[Lab 01 - Data Inspection Exercise.pdf|Lab exercise]] · [[Lab 01 - Palmer Penguins Worked Example.pdf|Worked example]]
>
> [[Data Engineering and AI Current Canvas Information|Current Canvas information already stored locally]]

## Core idea

An AI system is an end-to-end data system, not merely a model. Useful results depend on how observations were collected, represented, checked, transformed, served, and monitored. Code running successfully is not evidence that the data or conclusion is meaningful.

## End-to-end feedback loop

1. **Real-world data** — observations from sensors, transactions, forms, logs, text, images, or other sources.
2. **Data engineering** — collecting, storing, validating, cleaning, transforming, and serving the data.
3. **AI or machine learning** — predicting, classifying, clustering, or generating from prepared data.
4. **Application** — delivering the result through an alert, dashboard, report, application, or automation.
5. **Feedback** — measuring outcomes and improving the data, model, or decision process.

A failure can enter at any stage and propagate. Monitoring must therefore cover data and decisions as well as model metrics.

## Data, information, and knowledge

- **Data:** recorded facts or observations.
- **Information:** data organised with context and meaning.
- **Knowledge:** interpreted information that can support action or a decision.

Adding context can make data useful, but it can also add assumptions. Preserve raw-source provenance so interpretations can be checked later.

## Data structures

- **Structured:** fixed rows, columns, and schema, such as a CSV or relational table.
- **Semi-structured:** records with labels or hierarchy but variable fields, such as JSON or XML.
- **Unstructured:** free text, images, audio, and video without a predefined table schema.

Storage format does not determine meaning. A year stored as an integer may be categorical; an identifier made of digits is not a quantity to average.

## The four Vs

- **Volume:** how much data exists.
- **Velocity:** how quickly data arrives and must be processed.
- **Variety:** the range of formats, sources, and structures.
- **Veracity:** trustworthiness, accuracy, consistency, and uncertainty.

The four Vs describe engineering constraints. A small dataset can still have severe veracity problems, and high-volume data can still be unrepresentative.

## AI problem types

- **Classification:** predict a discrete category.
- **Regression:** predict a continuous numerical value.
- **Clustering:** discover groups without supplied labels.
- **Generative AI:** create text, images, audio, code, or other content.

Define the target and decision before choosing an algorithm. A technically valid prediction may still be the wrong output for the operational need.

## Python and tabular data

Week 1 introduces:

- variables, lists, dictionaries, conditionals, loops, and functions;
- Pandas `DataFrame` objects for labelled tables;
- NumPy arrays for numerical operations;
- reading CSV files;
- separating numerical from categorical inspection;
- derived features and simple scaling.

Prefer vectorised column operations to row-by-row loops when the operation naturally applies to a whole column. Keep transformations explicit and reproducible.

## Reproducible working environment

- Python is the language; packages such as Pandas, NumPy, scikit-learn, and Matplotlib provide specialised tools.
- Keep each project in a clear folder with a dedicated virtual environment such as `.venv`.
- Ensure VS Code, the terminal, and a Jupyter notebook use the intended interpreter or kernel; installing a package into one environment does not make it available in every kernel.
- Record package requirements and keep source data separate from generated outputs.
- A notebook is the document containing code and results; the kernel is the Python process that executes it.

## Inspection before trust

### 1. Establish provenance

Record:

- source and access date;
- licence or permission;
- collection method and population;
- unit of observation—what one row represents;
- intended purpose and known limitations;
- target/label definition, if any.

### 2. Inspect structure

Check:

- shape: rows and columns;
- column names and meanings;
- storage dtypes versus semantic types;
- representative first/last/sample rows;
- whether identifiers are unique where expected.

### 3. Inspect quality

Check:

- missing values by column and by pattern;
- exact and near-duplicate rows;
- inconsistent spelling, capitalization, or whitespace in categories;
- impossible or suspicious numeric ranges;
- unexpected units or mixed measurement systems;
- class imbalance and underrepresented groups;
- whether missingness may itself carry operational meaning.

### 4. Summarise by semantic type

For numerical variables, inspect count, centre, spread, quantiles, and range. For categorical variables, inspect distinct values, frequencies, rare classes, and spelling variants. Do not report a numerical mean for an identifier or unordered label merely because Pandas stored it as a number.

### 5. Decide fitness for purpose

A dataset is not simply “clean” or “dirty.” State whether it is sufficiently reliable for the intended question, which limitations remain, and what additional collection or validation is required.

## Missingness, duplicates, and outliers

- Do not delete missing rows automatically; first ask why the values are absent and whether the pattern is biased.
- Exact duplicates can overweight observations, but repeated records may also represent genuine repeated events.
- An outlier can be an error, a rare valid case, or the most important case in the dataset.
- Keep an auditable distinction between raw values, cleaned values, and derived features.

## Feature engineering and scaling

Feature engineering converts available columns into representations suited to the task, such as a ratio, range, flag, or grouped category. Every feature should have a clear definition, unit, and rationale.

Standardisation commonly uses

$$
z=\frac{x-\mu}{\sigma}.
$$

Scaling matters for distance- or magnitude-sensitive methods because a large-unit feature can dominate. Fit transformation parameters on training data only; using future/test information during preprocessing is data leakage.

## Bias and leakage checks

- Ask who or what is missing from the data.
- Check whether collection conditions differ across groups or time periods.
- Ensure the target is not directly or indirectly included in the input features.
- Split data before learning imputations, scales, encodings, or feature-selection rules.
- Use metrics that reflect the real costs of different errors; a high overall accuracy can hide failure on an important minority class.

## Evaluation, clustering, and generated output

### Supervised evaluation

1. Split training and test data before learning preprocessing parameters.
2. Use stratification when class proportions need to be preserved.
3. Compare a classifier with a simple majority-class baseline.
4. Inspect false positives and false negatives, not only total accuracy.
5. Treat the held-out test set as an estimate of performance on unseen data, not another training resource.

### Clustering

Distance-based methods such as K-means require appropriately scaled numerical features. A cluster is a statistical grouping under the selected features, scaling, distance, and number of clusters; it is not automatically a real-world category. Use crosstabs and domain interpretation to understand what the groups represent.

### Generative AI

Writing a prompt is not equivalent to running or validating a model. Generated output should be grounded in the relevant data or source material, checked by a person, and treated as a proposed result rather than authoritative evidence.

## Week 1 lab pattern

The [[Lab 01 - Palmer Penguins Worked Example.pdf|Palmer Penguins example]] demonstrates the workflow. The [[Lab 01 - Data Inspection Exercise.pdf|Student Exam Performance exercise]] asks you to repeat it independently:

1. select and document the dataset;
2. load it from CSV;
3. describe rows, columns, semantic types, and dtypes;
4. inspect missingness, duplicates, categories, ranges, and imbalance;
5. state and test assumptions;
6. create only justified features or transformations;
7. scale the selected features and apply the requested K-means workflow;
8. interpret clusters with a crosstab rather than assigning them unsupported meaning;
9. create a train/test classifier with suitable stratification;
10. compare test accuracy with the majority-class baseline and inspect error types;
11. decide whether the data and result are trustworthy enough for the intended use.

## Engineering connections

- The saturation experiment in [[Properties and Phase Change of Pure Substances#Saturation lab bridge: theory to measurement|Thermodynamics]] requires provenance, units, equilibrium checks, interpolation, and comparison of measured with reference data.
- The FFT evidence in [[Amplitude Modulation#Lab 5 bridge: product modulation and measured spectra|Communication Engineering Lab 5]] uses arrays, vectorised multiplication, scaling, windowing, and visual validation.
- [[Information Theory]] connects compression and coding efficiency to data storage and transmission, while [[Coding and Multiplexing]] distinguishes useful structured redundancy from accidental duplicate records.

These links show the same data-quality habits in different engineering domains without moving their subject-specific theory into this note.

## Quick recall

- Data engineering makes data dependable and usable before modelling.
- Semantic type matters more than storage dtype.
- Inspect provenance, structure, missingness, duplicates, categories, ranges, units, and bias before trust.
- Successful code is not validation.
- Learn preprocessing parameters from training data only.
- Model choice comes after data understanding and fitness-for-purpose decisions.
