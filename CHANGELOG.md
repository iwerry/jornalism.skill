# Changelog

## 4.0.0

**Theme: multi-engine portability + five new knowledge modules.**

### Added
- `knowledge/MULTI_ENGINE.md` — explicit rules for running this skill on any LLM engine (Claude, GPT, Gemini, Grok, Llama, DeepSeek, etc.), using whatever tools that engine's runtime exposes rather than any single vendor's API.
- `knowledge/GEOLOCATION.md` — full geolocation/chronolocation verification ladder (landmarks, reverse-image search, sun/shadow, satellite comparison), bounded by a privacy/necessity gate before publication.
- `knowledge/DIGITAL_SAFETY.md` — defensive-only digital safety and threat-modeling checklist (phishing recognition, leak/tip authentication, account hygiene, forensic chain-of-custody). Explicitly excludes all offensive security content.
- `knowledge/DATA_VISUALIZATION.md` — production pipeline from cleaned dataset to published chart/map/dashboard, with accuracy, accessibility and design checks.
- `knowledge/NARRATIVE_AND_STYLE.md` — narrative-craft and reader-engagement techniques for verified reporting, with an explicit list of techniques that remain off-limits regardless of engagement value.
- `tools/TOOLBOX.md` — a categorized, non-binding inventory of concrete external tools (geolocation, verification, OSINT/public records, data journalism, companies/money, collaboration).
- `CREDITS.md` — full, honest accounting of the ten external projects reviewed for this version: what each is, what was adapted (pattern-level only, never copied text/code), and what was reviewed and deliberately set aside.
- `CHANGELOG.md` (this file).
- Brazilian newsroom operational annex inside `knowledge/INTERNATIONALIZATION.md` (pauta format, procedural-stage terms, right-of-reply register, LGPD framing note).

### Changed
- `SKILL.md` — task router extended with the five new modules; added an explicit "Engine and tool compatibility" section up top.
- `README.md` — v4.0.0 badges/description, updated module table, new "Works with any AI engine" section, link to `CREDITS.md` and `tools/TOOLBOX.md`.
- `config.yaml` — version bumped to `4.0.0`; five new `knowledge_modules` entries; new `tools_manifest` pointer; added `engine_agnostic: true` and `offensive_security_excluded: true` rules.
- `schemas/output.schema.json` — added optional `tools_used` and `geolocation` fields to `investigation_record` and `verification_record` to capture the new modules' output without breaking v3.0.0 consumers (all new fields optional).
- Existing knowledge modules (`VERIFICATION.md`, `OSINT.md`, `DATA.md`, `EDITORIAL.md`, `ETHICS_AND_SAFETY.md`, `AI_AND_INFORMATION_INTEGRITY.md`, `INVESTIGATION.md`) — added short cross-reference lines pointing to the relevant new module, with no change to their existing rules.
- `SOURCE_ARCHIVE_POLICY.md` — added a short note pointing to `CREDITS.md` for the new, non-PDF external inspirations.

### Explicitly not changed
- The 49-source PDF manifest (`sources/manifest.json`), `REFERENCES.md`'s routing table, and the 10 Golden Rules / `SKILL.md` runtime rules are unchanged in substance. New modules extend the method; they do not relax any existing evidence, ethics or corroboration requirement.

### Not adopted
- `Awesome-Journal-Skills` (academic-journal submission tooling — different domain from news journalism).
- Any offensive-security content from the cybersecurity skills library reviewed for item 5–6 of `CREDITS.md`.
- `skills-jornalismo-br` — could not be independently verified at review time; see `CREDITS.md` item 3 for what was built instead to cover the same need.

## 3.0.0
Prior version — see `ANALYSIS_REPORT.md` for the original 49-source corpus reanalysis this skill was built from.
