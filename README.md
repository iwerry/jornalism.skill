# 🔎 Investigative Journalism Skill

> **A modular AI skill for investigative journalism, OSINT, fact-checking, verification, data journalism, corporate research, source protection, and information integrity — built to run on any capable AI engine.**

**Author:** Daniel Rodrigues
**Skill:** `investigativejournalism.skill`
**Version:** `4.0.0`
**Language:** English-first • International by design
**Repository:** [iwerry/jornalism.skill](https://github.com/iwerry/jornalism.skill)

[![Version](https://img.shields.io/badge/version-4.0.0-blue?style=for-the-badge)](https://github.com/iwerry/jornalism.skill)
[![Knowledge Sources](https://img.shields.io/badge/knowledge-49%20sources-purple?style=for-the-badge)](https://github.com/iwerry/jornalism.skill)
[![OSINT](https://img.shields.io/badge/OSINT-supported-success?style=for-the-badge)](https://github.com/iwerry/jornalism.skill)
[![Fact Checking](https://img.shields.io/badge/fact--checking-supported-orange?style=for-the-badge)](https://github.com/iwerry/jornalism.skill)
[![Multi-Engine](https://img.shields.io/badge/engine-agnostic-informational?style=for-the-badge)](knowledge/MULTI_ENGINE.md)
[![License](https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge)](LICENSE)

---

## 🧭 What is this?

**Investigative Journalism Skill** is a reusable knowledge and reasoning layer designed to help AI systems perform **structured journalistic research instead of superficial web searching**.

Created by **Daniel Rodrigues**, the skill combines a curated knowledge base of **49 journalism-related PDF sources** with operational workflows for:

- 🔎 Investigative reporting
- 🌐 OSINT and open-source research
- ✅ Fact-checking and verification
- 🗺️ Geolocation and chronolocation of images/video
- 📊 Data journalism, from cleaning to published dashboards
- 🏢 Corporate and financial investigations
- 🧾 Public records and documentary research
- 🖼️ Image, video and audio verification
- 🧠 AI-assisted journalism
- 🛡️ Source protection, journalist safety and defensive digital security
- ✍️ Editorial structure, reporting and narrative craft
- 🌍 Multilingual and cross-border investigations (with a dedicated Brazilian newsroom annex)
- 🧬 Information integrity and synthetic media analysis

The central idea is simple:

> **The reference library is not decoration. It is a method layer.**

The books are not treated as a bibliography sitting beside the Skill. Their useful concepts are transformed into **workflows, decision gates, evidence models, verification procedures, source-routing rules and reusable research patterns**.

---

## 🤖 Works with any AI engine

This is not a Claude-only plugin. `investigativejournalism.skill` is a plain folder of Markdown, JSON and small scripts — no vendor API, no required plugin format. It is designed to be loaded as context by **Claude, GPT, Gemini, Grok, Llama, DeepSeek, or any other capable engine**, and to use whatever tools that engine's runtime already exposes (web search, file reading, code execution, vision input, connected apps).

See [`knowledge/MULTI_ENGINE.md`](knowledge/MULTI_ENGINE.md) for the compatibility rules and a rough capability-mapping table across common engines. Use only what a given session actually has available — an unavailable capability should degrade gracefully, never be faked.

---

## ⚡ Why this Skill exists

A powerful research assistant should not simply answer:

> "Here are some links."

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
| 🗺️ Geolocation & chronolocation of media | `knowledge/GEOLOCATION.md` |
| 📊 Data & statistics | `knowledge/DATA.md` |
| 📈 Charts, dashboards, maps & publication | `knowledge/DATA_VISUALIZATION.md` |
| 🏢 Companies & money | `knowledge/COMPANIES_AND_MONEY.md` |
| ✍️ Reporting & editorial work | `knowledge/EDITORIAL.md` |
| 🎙️ Narrative craft for verified stories | `knowledge/NARRATIVE_AND_STYLE.md` |
| 🛡️ Ethics & journalist safety | `knowledge/ETHICS_AND_SAFETY.md` |
| 🔐 Defensive digital safety (phishing, leaks, forensics) | `knowledge/DIGITAL_SAFETY.md` |
| 🤖 AI & information integrity | `knowledge/AI_AND_INFORMATION_INTEGRITY.md` |
| 🌍 International & Brazilian newsroom work | `knowledge/INTERNATIONALIZATION.md` |
| 🧰 Concrete tool inventory | `tools/TOOLBOX.md` |
| 🔌 Running on a non-Claude engine | `knowledge/MULTI_ENGINE.md` |

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
Relevant Source Family / Tool
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

Version 3.0 was developed by analyzing the complete journalism reference archive rather than relying on a single reference work. Version 4.0 adds five new knowledge modules (geolocation, defensive digital safety, data visualization, narrative craft, multi-engine compatibility) informed by a separate review of ten external open-source AI-skill projects — see [`CREDITS.md`](CREDITS.md) for exactly what was reviewed and what, if anything, was adapted from each.

The source collection covers multiple disciplines, including:

### Investigative journalism
Research methodology, hypotheses, documentary evidence, narrative construction and investigative workflows.

### Verification & fact-checking
Claim isolation, primary evidence, corroboration, context, UGC verification, geolocation/chronolocation and uncertainty handling.

### OSINT
Public-source research, search strategies, archives, digital traces, provenance and open-source investigations.

### Data journalism
Dataset acquisition, cleaning, statistical reasoning, reproducibility, visualization, dashboards and methodological transparency.

### Corporate & financial research
Company records, ownership structures, financial statements, contracts, procurement, related parties and documentary chains.

### Editorial practice
Accuracy, attribution, structure, headlines, corrections, narrative craft, right of reply and publication discipline.

### Ethics & safety
Source protection, privacy minimization, proportionality, risk assessment, journalist safety and defensive digital security.

### AI & information integrity
AI-assisted newsroom workflows, synthetic media, information disorder, provenance and human verification.

See:

- [`REFERENCES.md`](REFERENCES.md)
- [`sources/manifest.json`](sources/manifest.json)
- [`ANALYSIS_REPORT.md`](ANALYSIS_REPORT.md)
- [`CREDITS.md`](CREDITS.md) — external skill/tooling inspirations for v4.0.0
- [`CHANGELOG.md`](CHANGELOG.md)

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

### Narrative craft never outruns evidence

Version 4.0 adds engagement and storytelling techniques (`knowledge/NARRATIVE_AND_STYLE.md`), but a technique is used only if it can sit on top of an already-verified fact. If a technique would require softening a qualifier or implying more certainty than the reporting supports, it is rejected — no exception for how much it improves the read.

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

A concrete, categorized menu of tools for this ladder (search engines, archives, registries, imagery) lives in [`tools/TOOLBOX.md`](tools/TOOLBOX.md).

---

## 🖼️ Media verification & geolocation

For suspicious images, videos or audio, the workflow may include:

1. Find the earliest discoverable version.
2. Preserve the original when possible.
3. Inspect metadata and provenance.
4. Compare crops, frames and recompressions.
5. Geolocate using multiple landmarks — see [`knowledge/GEOLOCATION.md`](knowledge/GEOLOCATION.md) for the full ladder, including satellite comparison and a privacy/necessity gate before publishing any location finding.
6. Chronolocate using independent temporal evidence.
7. Compare against archival imagery.
8. Inspect possible manipulation or synthesis.
9. Corroborate independently.
10. Treat automated AI detectors — and AI-assisted geolocation reads from tools like Grok's vision, Google Lens or similar — as **indicators, not proof**.

A visual anomaly is a **lead for investigation**, not a verdict.

---

## 📊 Data journalism, visualized

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

When the deliverable is a chart, map, dashboard or interactive piece, [`knowledge/DATA_VISUALIZATION.md`](knowledge/DATA_VISUALIZATION.md) covers choosing the right visual form, accuracy/accessibility checks, and design guidance for a publication-ready result.

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
- draft structure;
- a first-pass geolocation or media-authenticity read.

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

The Skill also includes safeguards around confidential sources, journalist safety, and — new in v4.0 — defensive digital safety: recognizing phishing aimed at a newsroom, authenticating a leaked file's digital packaging, and account/device hygiene ([`knowledge/DIGITAL_SAFETY.md`](knowledge/DIGITAL_SAFETY.md)).

### Security boundary

Security-related knowledge in this skill — passive reconnaissance concepts, digital-forensics-informed verification, defensive threat modeling — is used only for **lawful, passive, defensive and journalistic research involving publicly accessible or properly authorized information**.

The Skill is not intended to facilitate, and explicitly excludes:

- unauthorized access;
- credential theft;
- malware;
- exploitation of systems without authorization;
- bypassing access controls;
- any offensive security technique, however framed;
- exposure of private information merely because it is technically discoverable.

`CREDITS.md` documents a case in point: a large third-party cybersecurity-skill library was reviewed for v4.0, and only its defensive/verification-relevant subset was adapted — its offensive-security content was deliberately left out.

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

New in v4.0: a dedicated **Brazilian newsroom operational annex** inside [`knowledge/INTERNATIONALIZATION.md`](knowledge/INTERNATIONALIZATION.md) — pauta (assignment) format, the exact procedural-stage terms (*investigado → indiciado → denunciado → réu → condenado*), right-of-reply register, style conventions, and an LGPD-aware data-minimization note.

> **Localization must not silently change the legal, statistical or evidentiary meaning of a source.**

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
├── CREDITS.md
├── CHANGELOG.md
├── LICENSE
├── config.yaml
│
├── knowledge/
│   ├── INVESTIGATION.md
│   ├── VERIFICATION.md
│   ├── OSINT.md
│   ├── GEOLOCATION.md
│   ├── DATA.md
│   ├── DATA_VISUALIZATION.md
│   ├── COMPANIES_AND_MONEY.md
│   ├── EDITORIAL.md
│   ├── NARRATIVE_AND_STYLE.md
│   ├── ETHICS_AND_SAFETY.md
│   ├── DIGITAL_SAFETY.md
│   ├── AI_AND_INFORMATION_INTEGRITY.md
│   ├── INTERNATIONALIZATION.md
│   └── MULTI_ENGINE.md
│
├── tools/
│   └── TOOLBOX.md
│
├── sources/
│   └── manifest.json
│
├── schemas/
│   └── output.schema.json
│
└── scripts/
    ├── profile_dataset.py
    └── validate_manifest.py
```

---

## 🚀 Using the Skill

The primary runtime instructions are in:

**[`SKILL.md`](SKILL.md)**

A compatible AI runtime — of any vendor — should:

1. Load the Skill instructions.
2. Check which tools/capabilities this session actually has (`knowledge/MULTI_ENGINE.md`).
3. Classify the user's research task.
4. Route the request to the relevant knowledge module(s) via `SKILL.md`'s task router.
5. Use the source map and `tools/TOOLBOX.md` to identify supporting methodology and concrete tools.
6. Collect and evaluate evidence.
7. Separate fact from inference.
8. Test alternative explanations.
9. Record uncertainty.
10. Apply ethical, safety and (if geolocation is involved) publication-precision gates.
11. Produce a transparent result with a source trail, following `schemas/output.schema.json` when structured output is requested.

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

The repository does **not** attempt to redistribute the 49 reference books, nor any text or code from the third-party skill projects reviewed for v4.0 (see `CREDITS.md`).

Instead, the Skill contains:

- operational summaries;
- methodological abstractions;
- source mappings;
- research procedures;
- decision gates;
- schemas;
- machine-readable metadata;
- a concrete, non-binding tool inventory.

The original works remain the underlying references.

This architecture allows the Skill to benefit from a broad journalism knowledge base — and from the wider open-source AI-skill ecosystem — without turning the repository into a copy of any source library.

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
- AI-assisted newsrooms — on whichever AI engine they use.

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
- newsroom-oriented use cases;
- additional concrete tools for `tools/TOOLBOX.md` (with current-as-of dates);
- credited adaptations from other open-source skill projects, following the accounting format in `CREDITS.md`.

When proposing a methodological change, explain **what evidence or journalism practice supports the change**. When proposing an adaptation from an external project, state clearly what you verified about that project and what, specifically, was adapted versus reviewed-and-set-aside.

---

## 📌 Project philosophy

> **Investigate first. Verify independently. Preserve provenance. Challenge your own hypothesis. Protect people. Publish only what the evidence supports — on any engine, with any tool that actually helps.**

---

## 🔗 Project

**GitHub:** [github.com/iwerry/jornalism.skill](https://github.com/iwerry/jornalism.skill)

Made with research, journalism methodology and a lot of curiosity by **Daniel Rodrigues**.
