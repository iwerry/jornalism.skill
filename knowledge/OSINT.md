# OSINT Knowledge

## Purpose
A lawful, reproducible workflow for public-source research.

## Search ladder
Start broad, then narrow:

1. exact phrase;
2. entity variants;
3. domain restriction;
4. file type;
5. date range;
6. source-specific search;
7. archived versions;
8. cross-source validation.

Record useful search terms in the research log.

## Passive reconnaissance
Use public metadata and public indexing to understand:
- organizations;
- public documents;
- technology disclosures;
- domains and subdomains already intentionally exposed;
- public-facing records.

Do not cross an authentication boundary.

## Search operators
Search operators can locate:
- public PDFs;
- spreadsheets;
- public directories;
- archived pages;
- exposed metadata.

Use them for discovery and verification, not exploitation.

Do not use search operators to obtain credentials, bypass controls or facilitate unauthorized intrusion.

## Digital evidence
Preserve:
- original URL;
- retrieval timestamp;
- downloaded original where lawful;
- cryptographic hash when appropriate;
- screenshots only as supplementary evidence;
- source context;
- chain of custody.

A screenshot alone is weak provenance.

## Geolocation and chronolocation
For the full tool-level geolocation/chronolocation workflow (imagery, satellite, shadows, landmarks) see `knowledge/GEOLOCATION.md`. In short, use multiple independent anchors — landmarks, road geometry, signage, terrain, shadows, weather — and never publish a precise location when it creates unnecessary risk.

## Ethical OSINT
The fact that information is technically discoverable does not automatically make publication justified.

Apply:
`public interest + necessity + proportionality + harm minimization`.

A concrete tool inventory (search engines, archives, imagery, corporate/financial registries) lives in `tools/TOOLBOX.md`. Listing a tool there is not an endorsement to use it beyond lawful, passive, public-source research — the same boundary as this file.

## Source map
- S38 — advanced search operators and public document discovery.
- S39 — defensive web security testing concepts.
- S40 — passive reconnaissance.
- S42 — search/asset-exposure concepts with defensive framing.
- S46–S47 — structured OSINT search and validation.
- S48 — digital investigation standards.
- S49 — imagery evaluation.
