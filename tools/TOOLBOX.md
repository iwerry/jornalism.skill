# Investigative Journalism Toolbox

## Purpose
A concrete, categorized menu of external tools an investigative journalist (or an AI engine assisting one) may reach for. This file is a **reference list, not a recommendation to use any specific tool for any specific task**, and not an integration spec — see `knowledge/MULTI_ENGINE.md` for how to treat these as capability categories rather than hard dependencies.

Every tool here is used subject to `knowledge/ETHICS_AND_SAFETY.md` and `knowledge/OSINT.md`: lawful, passive, publicly-accessible or properly authorized access only. Listing a tool is not permission to use it to identify a private individual, a minor, a confidential source, or to cross an authentication boundary. Availability, pricing, and terms of service change over time and by jurisdiction — verify current terms before relying on a tool for a specific investigation.

## Geolocation and imagery verification (see `knowledge/GEOLOCATION.md`)
- General mapping/satellite: Google Maps, Google Earth (Pro), Bing Maps, OpenStreetMap, Yandex Maps.
- Specialized satellite/aerial imagery: Sentinel Hub / Copernicus Browser, NASA Worldview, Planet (commercial), historical aerial archives held by national mapping agencies.
- Reverse image search: Google Images / Google Lens, Yandex Images, TinEye, Bing Visual Search.
- Sun position / shadow analysis for chronolocation: SunCalc, Suncalc.org-style solar-position calculators.
- Weather history for chronolocation: national meteorological archives, Wolfram Alpha historical weather.
- Frame-by-frame / metadata inspection: InVID-WeVerify browser extension, ExifTool, FotoForensics, Forensically.
- Archived web/media snapshots: Internet Archive Wayback Machine, Archive.today.
- Multimodal AI assistance for describing/locating a scene (Grok vision, Google Lens, GPT-4V-class tools, Claude's own vision input): treat output as a **lead to verify with the ladder in `knowledge/GEOLOCATION.md`**, never as confirmation by itself — same "AI is not evidence" rule as `knowledge/AI_AND_INFORMATION_INTEGRITY.md`.
- Facial or biometric identification services (e.g., PimEyes-style reverse face search): high privacy risk; consult `knowledge/ETHICS_AND_SAFETY.md`'s vulnerable-people gate before any use, and avoid entirely for identifying private individuals or minors.

## Verification and fact-checking
- Claim/fact-check aggregators: International Fact-Checking Network (IFCN) signatory databases, Google Fact Check Explorer.
- UGC and social monitoring: CrowdTangle-style monitoring tools (where access permits), platform-native search and advanced search operators.
- Video/image authenticity: InVID-WeVerify, Amnesty International's YouTube DataViewer.
- Document authenticity cross-checks: issuer's own public registry or verification portal, when one exists.

## OSINT and public records
- Corporate/beneficial-ownership registries: OpenCorporates, national company registries (e.g., Brazil's Receita Federal/CNPJ lookup, Portugal's Portal da Empresa, UK Companies House, US SEC EDGAR), OCCRP Aleph.
- Sanctions/PEP and litigation screening: national court-record portals, OFAC/EU/UN sanctions lists, OpenSanctions.
- Cross-border leak/document archives: ICIJ Offshore Leaks Database, OCCRP Aleph, DocumentCloud for organizing and annotating primary documents.
- Domain/infrastructure lookups (passive, defensive use only per `knowledge/DIGITAL_SAFETY.md`): WHOIS lookups, Wayback Machine for historical site states, `crt.sh` for certificate transparency logs.
- Aircraft/vessel tracking (public transponder data): Flightradar24, ADS-B Exchange, MarineTraffic.
- People/network mapping from public records: LittleSis, public court and property records portals.

## Data journalism and visualization (see `knowledge/DATA.md`, `knowledge/DATA_VISUALIZATION.md`)
- Spreadsheet/cleaning: any spreadsheet tool, OpenRefine for messy data.
- Statistical/code environment: Python (pandas, matplotlib/plotly) or R, run via whatever code-execution capability the session provides.
- Charting/publishing: Datawrapper, Flourish, or hand-built charts in the runtime's own code-execution/artifact capability.
- Mapping for publication: a GIS tool (QGIS) for analysis, paired with a lightweight web map (Leaflet/Mapbox-style) for the published piece.
- Public statistical sources: national statistics institutes (e.g., IBGE), World Bank Open Data, Eurostat, UN Data.

## Companies and money
- See the OSINT/public-records list above (OpenCorporates, OCCRP Aleph, national registries, court portals).
- Procurement/contract portals: national transparency portals (e.g., Brazil's Portal da Transparência), the World Bank's debarred-firms list, national audit-court (Tribunal de Contas) databases where public.

## Collaboration and case management
- Document organization/annotation: DocumentCloud.
- Secure source communication (protective use, see `knowledge/DIGITAL_SAFETY.md`): end-to-end encrypted messaging apps, SecureDrop-style whistleblower submission systems for newsrooms that operate one.

## Cross-checking this list
Tools go stale. Before an investigation depends on a specific tool's continued existence, terms of service, or accuracy, verify it is still operating as described — the same source-precedence rule as `REFERENCES.md`: prefer the tool's own current documentation over this static list for anything time-sensitive.

## Provenance
This inventory is original compilation, informed at a principle level (categories, not verbatim tool descriptions) by the OSINT/cybersecurity/data-journalism material already in `sources/manifest.json` (S38–S43, S46–S49) and by the external projects credited in `CREDITS.md`.
