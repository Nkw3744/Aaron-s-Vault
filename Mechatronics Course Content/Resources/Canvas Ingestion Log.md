# Canvas Ingestion Log

Return to [[Mechatronics Engineering]].

This log records material read from AUT Canvas through Aaron's authenticated student session. Canvas originals are treated as read-only. Deduplication uses Canvas IDs, exact hashes, sizes, and normalized extracted text rather than filenames alone.

The machine-readable baseline is `/home/aaron/projects/aut-canvas-obsidian/state/canvas-sync-ledger.json`. Future checks should compare Page timestamps/body fingerprints and file IDs/update timestamps/sizes against that ledger, then inspect only new or changed records.

## 2026-07-21 — Mathematics III and Data Engineering and AI

### Imported files

| Course | Canvas file ID | Canvas name | Vault destination |
| --- | ---: | --- | --- |
| Mathematics III | `8149949` | L4_note-1.pdf | [[Mechatronics Course Content/Mathematics III/Source Material/Lecture Notes/L4_note.pdf]] |
| Mathematics III | `8149870` | L5_note-1.pdf | [[Mechatronics Course Content/Mathematics III/Source Material/Lecture Notes/L5_note.pdf]] |
| Mathematics III | `8149929` | L6_note-1.pdf | [[Mechatronics Course Content/Mathematics III/Source Material/Lecture Notes/L6_note.pdf]] |
| Mathematics III | `8366060` | Tutorial_1_ENGE702.pdf | [[Mechatronics Course Content/Mathematics III/Practice/Tutorials/Tutorial 1 ENGE702.pdf]] |
| Mathematics III | `8366061` | Tutorial 1 Answers.pdf | [[Mechatronics Course Content/Mathematics III/Practice/Tutorials/Tutorial 1 Answers.pdf]] |
| Mathematics III | `8148882` | Tutorial_2_ENGE702.pdf | [[Mechatronics Course Content/Mathematics III/Practice/Tutorials/Tutorial 2 ENGE702.pdf]] |
| Data Engineering and AI | `8367841` | 01-IntroCourse-ENGE707.pdf | [[Mechatronics Course Content/Data Engineering and AI/Source Material/Lectures/Week 01 - Course Introduction.pdf]] |

### Duplicate Canvas files skipped

Exact hash matches: `8147865`, `8147894`, `8147952`, `8147958`, `8147985`, `8148001`, `8148729`, `8149308`, and `8149374`. These resolve to existing renamed Mathematics III lecture slides or L1–L3 notes.

Cross-format content matches: `8365454` (Lab 1 exercise), `8365455` (Palmer Penguins worked example), `8365456` (Week 1 theory notes), and `8368519` (Week 1 foundations slides). Their normalized extracted text matched the existing renamed Data Engineering PDFs at 95–99.8% similarity.

### Canvas-only and excluded material

- Mathematics file `8147881` is a revised/overlapping Lecture 1 variant; the current Canvas Page is linked instead of creating a near-duplicate.
- Mathematics file `8147579` is a combined 2025 Week 2 pack overlapping existing Lecture 4–6 material; it remains on the [Week 2 Canvas Page](https://canvas.aut.ac.nz/courses/23164/pages/week-2-overview-s2-2026).
- Two editable PowerPoints and two old 2024 transcript/promotional documents remain on Canvas as awkward or low-value binaries.
- Twenty-seven embedded image assets were not copied separately; they remain part of their Canvas Pages.
- Three legacy embedded file IDs returned HTTP 403 and remain inaccessible through the student session.

### Page and announcement coverage

Seven Mathematics III Pages and six Data Engineering and AI Pages were read successfully. Important current announcements were incorporated into [[Mathematics III Overview]], [[Data Engineering and AI Overview]], and the two current Canvas information notes.

## 2026-07-21 — Thermodynamics and Communication Engineering

### Imported files

| Course | Canvas file ID | Canvas name | Vault destination |
| --- | ---: | --- | --- |
| Thermodynamics | `8147543` | Property Tables.pdf | [[Mechatronics Course Content/Thermodynamics/Resources/Property Tables 2026.pdf]] |
| Thermodynamics | `8147694` | Chapter 1.pdf | [[Mechatronics Course Content/Thermodynamics/Source Material/Textbook Chapters/Ch 1 INTRODUCTION AND BASIC CONCEPTS.pdf]] |
| Thermodynamics | `8147984` | Saturation Lab Instructions 2025-updated.pdf | [[Mechatronics Course Content/Thermodynamics/Assessments/Labs/Current/Saturation Lab Instructions 2025 Updated - Current 2026.pdf]] |
| Thermodynamics | `8148292` | ENME601 - Previous Test and Exam Problems.pdf | [[Mechatronics Course Content/Thermodynamics/Assessments/Practice Exams/Previous Test and Exam Problems.pdf]] |
| Thermodynamics | `8148467` | ENME601 - Formulae Sheet.pdf | [[Mechatronics Course Content/Thermodynamics/Resources/ENME601 Formula Sheet 2026.pdf]] |
| Thermodynamics | `8148515` | ENME601 - Previous Test and Exam Problems - Solution.pdf | [[Mechatronics Course Content/Thermodynamics/Assessments/Practice Exams/Previous Test and Exam Problems - Solutions.pdf]] |
| Thermodynamics | `8369728` | Week 1 Tutorial-1.pdf | [[Mechatronics Course Content/Thermodynamics/Practice/Tutorials/Tutorial Week 1 Solutions 2026.pdf]] |
| Thermodynamics | `8370198` | Tute 2 questions.pdf | [[Mechatronics Course Content/Thermodynamics/Practice/Tutorials/Tutorial Week 2 Questions 2026.pdf]] |
| Thermodynamics | `8148185` | TH3 Issue 15 Instruction Manual.pdf | [[Mechatronics Course Content/Thermodynamics/Assessments/Labs/Current/TH3 Saturation Pressure Apparatus Manual.pdf]] |
| Communication Engineering | `8140284` | Maths-formulae-tables-for-ENEL700.pdf | [[Mechatronics Course Content/Communication Engineering/Resources/ENEL700 Maths Formulae Tables.pdf]] |
| Communication Engineering | `8140382` | frequency-deviation of FM and PM.pdf | [[Mechatronics Course Content/Communication Engineering/Resources/FM and PM Frequency Deviation.pdf]] |
| Communication Engineering | `8347949` | ENEL700-Lab-Book-2026.pdf | [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/ENEL700 Lab Book 2026.pdf]] |

### Duplicate Canvas files skipped

Fifty-one PDFs were exact SHA-256 duplicates of existing renamed lecture, chapter, or tutorial files. Three more were strong extracted-content duplicates: Communication `8140409` and Thermodynamics `8352131` and `8369921`. Canvas file `8147705` was an exact second upload of imported Chapter 1 file `8147694`.

Three Communication combined tutorial packs (`8140325`, `8140335`, and `8140415`) remain on their Lecture Resources Pages because the corresponding individual questions/answers already exist locally.

### Canvas-only and excluded material

- Forty embedded image assets remain part of their Pages rather than detached vault files.
- Two PowerPoints and three Word documents remain on Canvas as editable/awkward formats.
- The 36.4 MiB Thermodynamics SI property-table appendix remains on the Week 1 Page because it exceeds the 20 MiB ingestion ceiling.
- All 115 Page-linked file IDs and the additional TH3 module file were accessible; no download permissions failed.

### Page and announcement coverage

Nine Thermodynamics Pages and 30 Communication Engineering Pages were read successfully. The current ENEL700 Test 1 announcement, assessment inconsistencies, ENME601 live saturation-lab deadline, and relevant course guidance were incorporated into both course overviews and current Canvas information notes.

## 2026-08-20 — Current S2 course pull

The deterministic pull inspected 60 published Pages across the four active courses and found five new Pages, eight changed Pages, nine new/changed assignment records, ten new announcements, and six new Thermodynamics course-file records.

- **56 substantive files imported:** Communication Engineering 3; Data Engineering and AI 13; Mathematics III 18; Thermodynamics 22.
- **Duplicates skipped:** nine exact vault duplicates, two repeated staged uploads, and one normalized-text vault duplicate.
- **Other classifications:** 45 ledger-unchanged files, five unavailable/review-only records, and two decorative Data Engineering Homepage images excluded.
- [[Canvas Pull 2026-08-20 Import Manifest]] records every imported Canvas file ID, Page context, and final vault destination.
- Important current changes were incorporated into course overview, assessment, practice, and Current Canvas Information notes. No Calendar or Drive writes were made.
- All 70 staged files passed expected-size, signature, and SHA-256 verification; the 56 final destinations were collision-free and verified after placement.
