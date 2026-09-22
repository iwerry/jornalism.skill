# Library Reanalysis Report

## Scope

The supplied archive was inspected as a corpus rather than as a single reference work.

**Total PDF files analyzed: 49.**

The PDFs were grouped by operational function and their extracted text was inspected for title, table-of-contents structure, chapters/sections and recurring methodological themes. The resulting skill deliberately synthesizes methods rather than copying source text.

## Corpus distribution

- Data journalism / verification: 5
- Investigative journalism / narrative: 3
- AI and journalism: 8
- Fact-checking/editorial standards: 1
- Creator/science/press-safety resources: 4
- Editorial manuals and ethics: 12
- Cyber/platform/information integrity: 4
- Search, data mining and defensive security: 6
- Journalism assignment/reference material: 2
- OSINT: 2
- Berkeley digital investigations: 2

## Major cross-source knowledge domains

### Investigation
The corpus converges on hypothesis-driven investigation, documentary trails, source triangulation, narrative construction and adversarial verification.

### Verification
The verification books and Berkeley materials emphasize provenance, context, source lineage, independent corroboration and careful treatment of uncertainty.

### Data
The data-journalism and data-mining sources contribute a complete workflow from question formulation through acquisition, cleaning, analysis, visualization and reproducibility.

### Corporate and financial reporting
The company-accounts reference contributes a specialized documentary approach for reading accounts and following ownership, transactions and corporate records.

### Editorial practice
Brazilian and international editorial manuals contribute clarity, attribution, headline discipline, corrections, ethics and institutional style.

### Safety and ethics
The corpus includes professional ethics, press safety, digital-investigation security and harm-minimization principles.

### AI and information integrity
The AI resources add AI literacy, newsroom governance, synthetic-media verification, information disorder and election/information-integrity considerations.

### OSINT and search
The OSINT, search-operator and defensive-security materials contribute repeatable public-source discovery techniques. Offensive material is intentionally constrained to lawful passive/defensive use.

## Important design decision

The skill should not attempt to place the full 49-book corpus into every model context.

Instead, the repository uses:

`task routing → knowledge module → source map → evidence procedure → structured output`.

This is the mechanism that turns the library into usable knowledge rather than a bibliography.

## Copyright-aware implementation

The repository contains original summaries, routing information and operational abstractions. It does not redistribute the supplied books or reproduce long passages from them.

The `sources/manifest.json` file identifies the source files used during the reanalysis so that a deployment can maintain a separate licensed/private reference library when appropriate.
