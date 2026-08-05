---
aliases:
  - ENGE707 Week 3 Visualisation and inferential statistics
  - Data Visualisation and Inferential Statistics
week: 3
source_reviewed: 2026-07-30
source_scope: Week 2–3 slides, combined notes, and lab exercises on exploratory visualisation, distribution checking, statistical inference, and interpretation after cleaning
---

# Data Visualisation and Inferential Statistics

> [!info] Course navigation
> [[Data Engineering and AI Overview|Subject overview]] · [[Data Engineering and AI Roadmap|Course roadmap]] · [[Data Engineering and AI Practice Index|Practice index]]
> 
> Available working sources: [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Labs 02 and 03 - Arrhythmia/Labs 2 and 3 - Arrhythmia worked example and Assessment 1 preparation.pdf|worked example and assessment preparation]] · [[Mechatronics Course Content/Data Engineering and AI/Practice/Labs/Labs 02 and 03 - Arrhythmia/Labs 2 and 3 - Annotated Arrhythmia Worked Example.ipynb|annotated notebook]] · [[Data Engineering and AI Lab Index|file-status note]]
> 
> Companion data-preparation note: [[Arrhythmia Data Representation and Quality]]

## Core idea

Week 3 moves from “is the data clean enough to trust?” to “what can we learn from it, and how cautiously can we say it?” The source frames visualisation and inference as a continuation of the Arrhythmia cleaning workflow: first check the representation, then inspect the cleaned data with plots, and only then make a statistical claim that matches the sample and the assumptions.

The important discipline is to keep exploratory plots, descriptive summaries, and inferential tests separate. A plot can reveal structure; it cannot by itself prove a hypothesis. Likewise, a p-value says something about the test under its assumptions, not about every possible explanation for the data.

## Why the source matters

The Arrhythmia dataset is useful here because it contains real-world imperfections: missing values, coded variables, and a mix of demographic and ECG-derived measurements. That means the analysis sequence is not optional. If the schema is wrong, or the cleaning is not documented, then the later visualisation and inference can become misleading even when the code runs.

## Visualisation as evidence gathering

The lecture and lab material use plots to answer practical questions:

- what does the distribution of a variable look like?
- are there unusual values that deserve manual review?
- do the groups look meaningfully different?
- did a cleaning choice distort the shape of the data?

Useful checks include:

1. look at histograms or density plots before and after cleaning;
2. compare groups with box plots, strip plots, or similar summaries;
3. inspect relationships with scatter plots or grouped summaries;
4. check whether apparent structure survives basic cleaning decisions;
5. keep the plotting question narrow enough that the plot answers something concrete.

A neat-looking plot is not proof of a good dataset. The source repeatedly treats plots as prompts for further checking, not as a substitute for documentation or verification.

## Inferential statistics as constrained claims

Inference in the notes is used for limited, well-stated claims. The workflow is:

- identify the variables and the comparison you actually want to make;
- choose a test that matches the variable types and the question;
- state the assumptions that make the test meaningful;
- interpret the output in context, not as a standalone verdict;
- avoid causal language unless the design supports it.

That discipline matters because the Arrhythmia material is observational. Even if two variables are associated, the result does not automatically explain why the association exists.

### Practical interpretation rules

- A non-significant result is not the same as “no relationship exists.”
- A significant result is not the same as “one variable causes the other.”
- Statistical significance does not guarantee practical importance.
- The sample and the cleaning rules are part of the inference, not background noise.

## Common workflow from the lab

1. Start with the cleaned or carefully prepared table.
2. Visualise the variables of interest.
3. Check group structure and obvious imbalance.
4. Choose the test that matches the question.
5. Record the result together with the assumptions and the data preparation that preceded it.
6. Return to the plot if the result seems surprising.

This makes the analysis defensible to a teaching assistant because the reasoning is visible, not just the final statistic.

## Pitfalls to avoid

- treating exploratory plots as proof;
- selecting a test before clarifying the question;
- ignoring missingness or cleaning choices when interpreting output;
- reading causality into an observational association;
- reporting a p-value without the surrounding context;
- confusing a visually large difference with a statistically tested one;
- forgetting that a cleaned dataset is already a transformed object.

## Connections

- [[Arrhythmia Data Representation and Quality]] explains the schema, quality checks, and cleaning discipline that the Week 3 analysis depends on.
- [[Foundations of Data Engineering and AI]] provides the earlier vocabulary for data inspection, data quality, and basic analysis workflow.
- The lab exercises use this topic to turn a cleaned dataset into evidence-led interpretation rather than ad hoc commentary.

## Study cue

If you are revising this topic, rehearse the sequence “clean → plot → compare → test → interpret” and be ready to say which part of the sequence produced each conclusion.
