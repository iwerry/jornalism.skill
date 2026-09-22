# 🔎 Investigative Journalism Skill

> **A modular AI skill for investigative journalism, OSINT, fact-checking, verification, data journalism, corporate research, source protection, and information integrity.**

**Author:** Daniel Rodrigues  
**Skill:** `investigativejournalism.skill`  
**Version:** `3.0.0`  
**Language:** English-first • International by design  
**Repository:** [iwerry/jornalism.skill](https://github.com/iwerry/jornalism.skill)

[![Version](https://img.shields.io/badge/version-3.0.0-blue?style=for-the-badge)](https://github.com/iwerry/jornalism.skill)
[![Knowledge Sources](https://img.shields.io/badge/knowledge-49%20sources-purple?style=for-the-badge)](https://github.com/iwerry/jornalism.skill)
[![OSINT](https://img.shields.io/badge/OSINT-supported-success?style=for-the-badge)](https://github.com/iwerry/jornalism.skill)
[![Fact Checking](https://img.shields.io/badge/fact--checking-supported-orange?style=for-the-badge)](https://github.com/iwerry/jornalism.skill)
[![License](https://img.shields.io/badge/license-see%20repository-lightgrey?style=for-the-badge)](https://github.com/iwerry/jornalism.skill)

---

## 🧭 What is this?

**Investigative Journalism Skill** is a reusable knowledge and reasoning layer designed to help AI systems perform **structured journalistic research instead of superficial web searching**.

Created by **Daniel Rodrigues**, the skill combines a curated knowledge base of **49 journalism-related PDF sources** with operational workflows for:

- 🔎 Investigative reporting
- 🌐 OSINT and open-source research
- ✅ Fact-checking and verification
- 📊 Data journalism
- 🏢 Corporate and financial investigations
- 🧾 Public records and documentary research
- 🖼️ Image, video and audio verification
- 🧠 AI-assisted journalism
- 🛡️ Source protection and journalist safety
- ✍️ Editorial structure and reporting
- 🌍 Multilingual and cross-border investigations
- 🧬 Information integrity and synthetic media analysis

The central idea is simple:

> **The reference library is not decoration. It is a method layer.**

The books are not treated as a bibliography sitting beside the Skill. Their useful concepts are transformed into **workflows, decision gates, evidence models, verification procedures, source-routing rules and reusable research patterns**.

---

## ⚡ Why this Skill exists

A powerful research assistant should not simply answer:

> “Here are some links.”

It should be able to ask:

> **What exactly are we trying to establish?**

Then:

```text
Question
   ↓
Hypothesis
   ↓
Research Plan
   ↓
Source Discovery
   ↓
Evidence Collection
   ↓
Authentication
   ↓
Corroboration
   ↓
Adversarial Testing
   ↓
Right of Reply
   ↓
Editorial Review
   ↓
Report
```

This architecture is designed to reduce:

- confirmation bias;
- unsupported conclusions;
- source duplication;
- false certainty;
- citation hallucination;
- context collapse;
- misleading statistics;
- unverified social-media claims;
- AI-generated misinformation being treated as evidence.

---

## 🧠 Knowledge Architecture

The Skill routes a task to the smallest relevant knowledge module instead of loading the entire reference library into every interaction.

| Research task | Operational module |
|---|---|
| 🔎 Investigations & wrongdoing | `knowledge/INVESTIGATION.md` |
| ✅ Fact-checking & claims | `knowledge/VERIFICATION.md` |
| 🌐 OSINT & digital investigation | `knowledge/OSINT.md` |
| 📊 Data & statistics | `knowledge/DATA.md` |
| 🏢 Companies & money | `knowledge/COMPANIES_AND_MONEY.md` |
| ✍️ Reporting & editorial work | `knowledge/EDITORIAL.md` |
| 🛡️ Ethics & journalist safety | `knowledge/ETHICS_AND_SAFETY.md` |
| 🤖 AI & information integrity | `knowledge/AI_AND_INFORMATION_INTEGRITY.md` |
| 🌍 International investigations | `knowledge/INTERNATIONALIZATION.md` |

### The routing principle

```text
User Request
     │
     ▼
Task Classification
     │
     ▼
Relevant Knowledge Module
     │
     ▼
Relevant Source Family
     │
     ▼
Investigation / Verification Procedure
     │
     ▼
Evidence + Provenance
     │
     ▼
Adversarial Check
     │
     ▼
Structured Result
```

---

## 📚 The 49-source knowledge base

Version 3.0 was developed by analyzing the complete journalism reference archive rather than relying on a single reference work.

The source collection covers multiple disciplines, including:

### Investigative journalism
Research methodology, hypotheses, documentary evidence, narrative construction and investigative workflows.

### Verification & fact-checking
Claim isolation, primary evidence, corroboration, context, UGC verification and uncertainty handling.

### OSINT
Public-source research, search strategies, archives, digital traces, provenance and open-source investigations.

### Data journalism
Dataset acquisition, cleaning, statistical reasoning, reproducibility, visualization and methodological transparency.

### Corporate & financial research
Company records, ownership structures, financial statements, contracts, procurement, related parties and documentary chains.

### Editorial practice
Accuracy, attribution, structure, headlines, corrections, right of reply and publication discipline.

### Ethics & safety
Source protection, privacy minimization, proportionality, risk assessment and journalist safety.

### AI & information integrity
AI-assisted newsroom workflows, synthetic media, information disorder, provenance and human verification.

See:

- [`REFERENCES.md`](REFERENCES.md)
- [`sources/manifest.json`](sources/manifest.json)
- [`ANALYSIS_REPORT.md`](ANALYSIS_REPORT.md)

---

## 🔬 Evidence-first methodology

The Skill follows a strict distinction between:

| Category | Meaning |
|---|---|
| **Verified fact** | Supported by sufficient evidence |
| **Attributed claim** | Statement assigned to a named source |
| **Inference** | Reasoned interpretation derived from evidence |
| **Unresolved** | Evidence is incomplete or contradictory |
| **Not verified** | The available material does not establish the claim |

### Evidence is not the same as confidence

The Skill can internally classify evidence by evidentiary role, but **no confidence label replaces corroboration**.

A social-media post can be an excellent lead.

It is not automatically excellent evidence.

---

## 🌐 OSINT philosophy

OSINT is treated as **lawful research using publicly accessible or authorized information**.

A typical search ladder:

```text
Exact phrase
   ↓
Domain restriction
   ↓
File/document search
   ↓
Temporal narrowing
   ↓
Entity variants
   ↓
Source-specific search
   ↓
Archive comparison
   ↓
Cross-source corroboration
```

The Skill emphasizes:

- provenance;
- preservation;
- reproducibility;
- source independence;
- contextual interpretation;
- privacy minimization.

---

## 🖼️ Media verification

For suspicious images, videos or audio, the workflow may include:

1. Find the earliest discoverable version.
2. Preserve the original when possible.
3. Inspect metadata and provenance.
4. Compare crops, frames and recompressions.
5. Geolocate using multiple landmarks.
6. Chronolocate using independent temporal evidence.
7. Compare against archival imagery.
8. Inspect possible manipulation or synthesis.
9. Corroborate independently.
10. Treat automated AI detectors as **indicators, not proof**.

A visual anomaly is a **lead for investigation**, not a verdict.

---

## 📊 Data journalism

The Skill starts with the **journalistic question**, not the spreadsheet.

For important datasets it encourages:

- preserving the original;
- recording acquisition dates;
- defining the population and time period;
- distinguishing zero, missing and suppressed values;
- checking duplicates;
- investigating outliers;
- documenting transformations;
- distinguishing counts from rates;
- distinguishing mean from median;
- distinguishing nominal from real monetary values;
- avoiding unsupported causal claims;
- documenting uncertainty;
- making analysis reproducible.

> **Every important number should be traceable to its source and definition.**

---

## 🏢 Corporate & financial investigations

A corporate investigation can be modeled as a documentary chain:

```text
Entity
  ↓
Ownership
  ↓
Directors / Officers
  ↓
Incorporation
  ↓
Financial Accounts
  ↓
Contracts
  ↓
Procurement
  ↓
Payments
  ↓
Related Parties
  ↓
Litigation / Regulation
  ↓
Beneficial Ownership
```

The Skill explicitly avoids treating relationships as proof of wrongdoing.

Relationships are classified as:

- documented;
- attributed;
- inferred;
- unresolved.

---

## 🤖 AI is not evidence

AI can assist with:

- transcription;
- translation;
- classification;
- search-query generation;
- data-cleaning suggestions;
- document comparison;
- research organization;
- draft structure.

But:

> **AI-generated information must not silently become factual evidence.**

A generated claim must be checked against external evidence.

For synthetic or manipulated media:

```text
Provenance
   ↓
Original / earliest source
   ↓
Contextual verification
   ↓
Technical inspection
   ↓
Independent corroboration
   ↓
Human editorial judgment
```

---

## 🛡️ Ethics, safety & privacy

The Skill uses proportionality and data minimization.

Before publishing sensitive information, ask:

- Is publication necessary?
- Is the information meaningfully public?
- Could publication enable harassment, stalking, fraud or physical harm?
- Can the public-interest fact be established without publishing the sensitive detail?
- Does the person have a legitimate expectation of privacy?

The Skill also includes safeguards around confidential sources and journalist safety.

### Security boundary

Security and penetration-testing references included in the knowledge archive are used only for **lawful, passive, defensive and journalistic research involving publicly accessible information**.

The Skill is not intended to facilitate:

- unauthorized access;
- credential theft;
- malware;
- exploitation of systems without authorization;
- bypassing access controls;
- exposure of private information merely because it is technically discoverable.

---

## 🌍 International by design

The underlying research methodology is **language-neutral**.

The user-facing response can adapt to:

- English;
- Portuguese;
- Spanish;
- French;
- Italian;
- Catalan;
- other languages supported by the runtime.

Internationalization should preserve the underlying meaning while adapting:

- legal terminology;
- jurisdiction;
- access-to-information mechanisms;
- date and time conventions;
- currencies;
- decimal separators;
- newsroom style;
- names and titles.

> **Localization must not silently change the legal, statistical or evidentiary meaning of a source.**

See [`knowledge/INTERNATIONALIZATION.md`](knowledge/INTERNATIONALIZATION.md).

---

## 🗂️ Repository structure

```text
jornalism.skill/
│
├── SKILL.md
├── README.md
├── REFERENCES.md
├── ANALYSIS_REPORT.md
├── SOURCE_ARCHIVE_POLICY.md
│
├── knowledge/
│   ├── INVESTIGATION.md
│   ├── VERIFICATION.md
│   ├── OSINT.md
│   ├── DATA.md
│   ├── COMPANIES_AND_MONEY.md
│   ├── EDITORIAL.md
│   ├── ETHICS_AND_SAFETY.md
│   ├── AI_AND_INFORMATION_INTEGRITY.md
│   └── INTERNATIONALIZATION.md
│
├── sources/
│   └── manifest.json
│
├── schemas/
│   └── output.schema.json
│
└── scripts/
    └── ...
```

---

## 🚀 Using the Skill

The primary runtime instructions are in:

**[`SKILL.md`](SKILL.md)**

A compatible AI runtime should:

1. Load the Skill instructions.
2. Classify the user's research task.
3. Route the request to the relevant knowledge module.
4. Use the source map to identify supporting methodology.
5. Collect and evaluate evidence.
6. Separate fact from inference.
7. Test alternative explanations.
8. Record uncertainty.
9. Apply ethical and safety gates.
10. Produce a transparent result with a source trail.

---

## 🧪 Recommended research output

For substantial investigations, the Skill prefers:

```text
Research Question
        ↓
What Is Established
        ↓
What Is Disputed
        ↓
Evidence
        ↓
Verification Method
        ↓
Alternative Explanation
        ↓
What Remains Unverified
        ↓
Right-of-Reply Status
        ↓
Sources
        ↓
Next Checks
```

This makes the investigation easier to audit, reproduce and update.

---

## 📖 Copyright-aware knowledge design

The repository does **not** attempt to redistribute the 49 reference books.

Instead, the Skill contains:

- operational summaries;
- methodological abstractions;
- source mappings;
- research procedures;
- decision gates;
- schemas;
- machine-readable metadata.

The original works remain the underlying references.

This architecture allows the Skill to benefit from a broad journalism knowledge base without turning the repository into a copy of the source library.

---

## 👤 Author

### Daniel Rodrigues

**Daniel Rodrigues — Photographer, Filmmaker & AI / Creative Technology Researcher**

Creator and maintainer of the `investigativejournalism.skill` project.

The Skill is designed as a modular foundation for:

- investigative journalists;
- reporters;
- fact-checkers;
- researchers;
- editors;
- OSINT practitioners;
- data journalists;
- journalism students;
- AI-assisted newsrooms.

---

## ⭐ Contributing

Contributions are welcome.

Useful contributions include:

- new verification workflows;
- improvements to source provenance;
- internationalization;
- documentation;
- reproducibility improvements;
- data-journalism methodology;
- ethical safeguards;
- newsroom-oriented use cases.

When proposing a methodological change, explain **what evidence or journalism practice supports the change**.

---

## 📌 Project philosophy

> **Investigate first. Verify independently. Preserve provenance. Challenge your own hypothesis. Protect people. Publish only what the evidence supports.**

---

## 🔗 Project

**GitHub:** [github.com/iwerry/jornalism.skill](https://github.com/iwerry/jornalism.skill)

Made with research, journalism methodology and a lot of curiosity by **Daniel Rodrigues**.
