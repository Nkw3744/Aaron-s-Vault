---
aliases:
  - ENGE707 Week 2–3 Arrhythmia workflow
  - Data Representation and Quality
week: 2-3
source_reviewed: 2026-07-30
source_scope: Week 2–3 Arrhythmia lecture notes and lab exercises covering the UCI Arrhythmia dataset, provenance, schema, semantic types, missingness, plausibility checks, BMI consistency checks, reproducible cleaning, visualisation, inference boundaries, and lab preparation
---

# Arrhythmia Data Representation and Quality

> [!info] Course navigation
> [[Data Engineering and AI Overview|Subject overview]] · [[Data Engineering and AI Roadmap|Course roadmap]] · [[Data Engineering and AI Practice Index|Practice index]]
> 
> Available working sources: [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Labs 02 and 03 - Arrhythmia/Labs 2 and 3 - Arrhythmia worked example and Assessment 1 preparation.pdf|worked example and assessment preparation]] · [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Labs 02 and 03 - Arrhythmia/Labs 2 and 3 - Annotated Arrhythmia Worked Example.ipynb|annotated notebook]] · [[Data Engineering and AI Lab Index|file-status note]]
> 
> Companion foundation note: [[Foundations of Data Engineering and AI]]
> 
> Companion interpretation note: [[Data Visualisation and Inferential Statistics]]

## Core idea

The Week 2–3 Arrhythmia work turns raw medical records into an auditable analysis workflow. The important question is not only whether code runs, but whether the chosen columns, units, missingness handling, and cleaning decisions preserve the meaning of the patient record and support a defensible interpretation.

The dataset used throughout the notes is the UCI Arrhythmia dataset: 452 patient records, 279 input features, and one class column. It contains demographic and ECG-derived measurements and has confirmed missing values, so it is well suited to realistic data-quality checks rather than toy-perfect preprocessing.

## Why the source matters

The notes emphasise that the dataset documentation defines age in years, height in centimetres, and weight in kilograms, but the raw file also contains a class label in the final column and many coded ECG attributes. That means schema work is not just a technical convenience: a missing header or a misread column changes the analysis itself.

## Provenance and schema first

Before cleaning, record:

- the original source and dataset page;
- what the raw file contains;
- the unit of observation;
- which columns are inputs and which column is the diagnosis label;
- the semantic meaning of columns even when the storage dtype is numeric;
- any dataset-level caveats about missingness or coding.

A column can be numeric in storage and still be categorical or coded. The notes repeatedly warn that the last column is the class label and that forgetting to name it causes later key errors and downstream confusion.

### Practical schema rule

Treat the schema as a contract:

1. load the raw file without discarding columns;
2. assign the diagnosis label explicitly;
3. inspect shapes, headers, dtypes, and sample rows;
4. map storage dtype to semantic type before running statistics.

## Semantic types and the BMI consistency check

The lecture uses age, height, and weight as a concrete example of semantic typing. These fields are numeric, but their meaning matters: height must be in metres before a BMI calculation, and weight is not interchangeable with a diagnosis code or ECG code simply because the storage type is numeric.

The BMI check is a consistency check, not a diagnosis.

$$
\text{BMI} = \frac{\text{weight}}{\text{height}_m^2}
$$

The source uses it to catch internal contradictions such as implausible unit mix-ups or records whose height/weight pair does not agree with the declared units. It is not a general health rule and it does not justify deleting valid extreme records on its own.

### What the BMI rule can and cannot do

- It can flag impossible or suspicious unit combinations.
- It can reveal records that need manual review.
- It cannot tell you whether an extreme but real patient should be removed.
- It should be applied after checking that height is converted to metres and that the record still makes sense in context.

## Missingness handling

The dataset has confirmed missing values, so missingness is part of the analysis rather than an edge case.

Key habits from the source:

- inspect which columns contain missing values and how much is missing;
- keep the raw dataset intact;
- make the cleaning step explicit and reproducible;
- check whether missingness follows a pattern that could affect later analysis rather than assuming every blank is interchangeable;
- do not treat every blank as a simple deletion candidate.

If the cleaning strategy removes or imputes values, record the rule and keep the raw source available so another threshold or rule can be tested later.

## Plausibility checks, not blind filtering

The Arrhythmia workflow repeatedly contrasts cautious plausibility checks with over-aggressive filtering.

Use checks such as:

- impossible age/height/weight combinations;
- values that contradict the units stated in the documentation;
- duplicate or nearly duplicate records that might be repeated observations;
- suspicious class or category values;
- rows that are unusual but still physically possible.

Do not automatically remove a record just because it is extreme. The notes explicitly show that a very low BMI rule may flag an implausible adult record, while a very high BMI record can still be real and should remain if it is internally consistent.

## Reproducible cleaning workflow

1. Preserve the raw file unchanged.
2. Create a separate clean working copy.
3. Rename or map columns explicitly.
4. Convert semantic units deliberately.
5. Log missingness and plausibility rules.
6. Keep the cleaned result reproducible from the raw source and the written rules.
7. Keep raw, cleaned, and derived outputs distinguishable.

This is the main lesson for later labs: a new plausibility rule should be easy to re-run without losing the original data.

## Visualisation handoff

The source uses plots for inspection, not for unsupported proof. Once the data are represented well enough to trust, the cleaned table can be passed to [[Data Visualisation and Inferential Statistics]] for exploratory plots and limited statistical tests.

## Lab-performance preparation

The lab materials frame this as a workflow you can repeat under time pressure:

1. identify the dataset and its purpose;
2. inspect headers, missingness, and data types;
3. document the diagnosis label and the input features;
4. run consistency checks such as BMI only when the units are correct;
5. keep a conservative cleaning strategy;
6. separate raw data, cleaned data, and plotted summaries;
7. be ready to explain why each row was kept, adjusted, or flagged.

This is useful for lab performance because it reduces ad hoc decisions. The same check can be defended, repeated, and adjusted later if the threshold changes.

## Connections

- [[Foundations of Data Engineering and AI]] owns the Week 1 general pipeline, data types, data quality vocabulary, and baseline inspection workflow.
- [[Data Visualisation and Inferential Statistics]] owns the Week 3 plots and inferential claims that build on these cleaning decisions.
- Later machine-learning work depends on these choices because model quality cannot recover from a broken schema or unjustified cleaning.

## Common mistakes

- Treating the last column as an unnamed numeric field instead of the diagnosis label.
- Forgetting that semantic type can differ from storage dtype.
- Deleting outliers before checking whether they are plausible real records.
- Losing the raw data after making a cleaned copy.
- Applying BMI before converting height to metres.
- Using visualisations as proof instead of as evidence for further checking.
- Mixing exploratory cleaning with later inferential claims.
