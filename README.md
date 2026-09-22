# Investigative Journalism Skill — International Knowledge Edition

**Author:** Daniel Rodrigues  
**Skill name:** `investigativejournalism.skill`  
**Version:** 3.0.0  
**Language:** English-first, internationalized architecture  
**Purpose:** turn a large journalism reference library into an operational research, verification, investigation, data, OSINT, editorial and AI-assistance system.

## What changed in v3

This edition was rebuilt after re-analyzing the full reference archive rather than treating one book as the sole authority.

The archive contains **49 PDF sources** across:

- investigative journalism and narrative construction;
- data journalism and data mining;
- verification and fact-checking;
- OSINT and digital open-source investigations;
- company and financial records;
- editorial standards and newsroom style;
- journalist safety and source protection;
- social platforms, information disorder and platform transparency;
- AI literacy, AI in newsrooms and AI-assisted journalism;
- Brazilian, Latin American, European and international perspectives;
- passive search and defensive cybersecurity references.

The skill does **not** copy the books. Instead, it converts their useful ideas into short, reusable procedures, decision gates, schemas, source-routing rules and research prompts. The original works remain the underlying references.

## Core principle

> **The skill should use the library as a method layer, not as a bibliography decoration.**

When a user asks a journalism question, the skill should identify the task, route it to the relevant knowledge module, apply the appropriate procedure, and cite the source family that supports the procedure.

## Knowledge architecture

```text
User request
   │
   ├── Investigation / reporting
   │       └── investigative workflow + hypothesis testing + evidence matrix
   │
   ├── Verification / fact-checking
   │       └── claim isolation + primary source + independent corroboration
   │
   ├── OSINT / digital investigation
   │       └── passive search + provenance + preservation + validation
   │
   ├── Data
   │       └── question → acquisition → cleaning → analysis → visualization → reproducibility
   │
   ├── Documents / companies / money
   │       └── records → entities → timeline → transaction chain → contradictions
   │
   ├── Editorial / writing
   │       └── accuracy + attribution + clarity + structure + right of reply
   │
   ├── Safety / ethics
   │       └── source protection + threat model + minimization of harm
   │
   └── AI / synthetic media
           └── provenance → verification → human review → disclosure
```

## Files

- `SKILL.md` — main runtime instructions and routing logic.
- `knowledge/INVESTIGATION.md` — investigative workflow and hypothesis testing.
- `knowledge/VERIFICATION.md` — fact-checking, UGC, media and provenance verification.
- `knowledge/OSINT.md` — public-source research and digital investigation.
- `knowledge/DATA.md` — data journalism, statistical discipline and reproducibility.
- `knowledge/COMPANIES_AND_MONEY.md` — corporate records and financial investigation.
- `knowledge/EDITORIAL.md` — reporting, editing, attribution, headlines and corrections.
- `knowledge/ETHICS_AND_SAFETY.md` — ethics, source protection and reporter safety.
- `knowledge/AI_AND_INFORMATION_INTEGRITY.md` — AI-assisted journalism, information disorder and synthetic media.
- `knowledge/INTERNATIONALIZATION.md` — language, jurisdiction and localization layer.
- `sources/manifest.json` — machine-readable inventory of all 49 analyzed PDFs.
- `REFERENCES.md` — human-readable source map and how each source family contributes.
- `schemas/output.schema.json` — structured output contracts.
- `scripts/` — local utilities for inspecting datasets and validating source files.

## How the knowledge is used

A good implementation should **not** load every book into every prompt.

Instead:

1. classify the user's task;
2. select the smallest relevant knowledge module;
3. retrieve the relevant source cards;
4. perform the procedure;
5. record uncertainty and missing evidence;
6. produce the requested output;
7. preserve a source trail.

This keeps the skill practical and reduces context waste.

## Internationalization

The internal method is language-neutral. User-facing language should be selected at runtime.

The skill should preserve:

- the same investigation logic across languages;
- local legal terminology;
- local date, number and currency conventions;
- local newsroom style;
- jurisdiction-specific access-to-information procedures;
- the original source language in the evidence record.

Translation should never silently change the meaning of a legal, statistical or evidentiary term.

See `knowledge/INTERNATIONALIZATION.md`.

## Important security boundary

The archive includes offensive-security and penetration-testing references. In this skill they are used only for **lawful, passive, defensive and journalistic verification of publicly accessible information**.

Do not use the skill to:

- obtain passwords or authentication secrets;
- bypass access controls;
- exploit systems without authorization;
- deploy malware;
- evade monitoring for unauthorized access;
- expose private personal data merely because it can be found.

Search operators may be used to discover public documents, exposed metadata or publicly indexed material, followed by ethical validation and minimization.

## Copyright-aware knowledge extraction

The repository stores **operational summaries and source mappings**, not wholesale copies of copyrighted books.

When a source is needed, the implementation should:

- identify the source by `Sxx`;
- summarize the relevant principle;
- cite the source;
- avoid reproducing long passages;
- preserve the distinction between source guidance and the skill's own synthesis.

## Recommended runtime behavior

For every substantial investigation:

```text
Question
→ Hypothesis
→ Search plan
→ Source map
→ Evidence collection
→ Authentication / provenance
→ Corroboration
→ Adversarial test
→ Right of reply
→ Draft
→ Editorial gates
→ Publication / correction plan
→ Follow-up
```

The final answer should clearly distinguish:

- verified fact;
- attributed claim;
- inference;
- unresolved question;
- unavailable evidence;
- editorial recommendation.

## Author

Created and maintained by **Daniel Rodrigues**.

The skill is designed as a modular foundation for investigative journalists, fact-checkers, researchers, editors, OSINT practitioners and journalism students.
