# Data Visualization and Interactive Storytelling Knowledge

## Purpose
Extends `knowledge/DATA.md` from analysis into production: building the chart, map, dashboard or interactive piece a reader actually sees, and doing it to a publication-ready standard.

This module is engine- and tool-agnostic. Build the visual with whatever the runtime has available — a native charting tool, a code-execution environment (Python/JS charting libraries), a spreadsheet tool, or a hand-written page — following the principles below rather than any one product's syntax.

## Pipeline
`journalistic question → cleaned dataset (knowledge/DATA.md) → chart/visual type selection → draft → accuracy check → accessibility and design pass → caption and sourcing → publish`.

## Choosing a visual form
Match the form to the question, not to what looks impressive:
- change over time → line chart (bar chart only for a handful of discrete periods);
- comparison across categories → bar chart, sorted meaningfully rather than alphabetically unless alphabetical order is the point;
- part-to-whole → stacked bar or a simple share table; use pie/donut sparingly and only for a small number of categories;
- geographic distribution → a choropleth or point map, with a clear statement of whether it shows a count or a rate (a population-weighted rate map, not raw counts, when comparing places of different size);
- relationship between two variables → scatter plot, with a stated correlation caveat per `knowledge/DATA.md` §4;
- a large, explorable dataset → a searchable/filterable table or dashboard, always paired with a written finding — a dashboard is a supplement to the story, not a substitute for one.

## Accuracy and integrity checks before publishing a visual
Re-apply `knowledge/DATA.md` §6 explicitly:
- axis starts at zero for bar charts, or the truncation is clearly and prominently flagged;
- consistent scale and bin size across any small-multiples or compared panels;
- color encodes one consistent meaning and includes a legend; avoid red/green-only encoding for accessibility;
- every number in the visual traces back to a cell in the reviewed, reproducible dataset — no manually retyped figures that bypass the pipeline;
- a caption states the source, the date range, and any material exclusion or estimate.

## Dashboards and interactive pieces
For an interactive or dashboard-style piece:
- default view should answer the single most important question first; exploration is progressive, not a wall of controls;
- filters and toggles must not make it possible to construct a misleading view (e.g., a cherry-picked date range) without that range being visible on screen;
- provide a static fallback (image or table) for accessibility and for readers on limited connectivity;
- log which underlying dataset version powers the published interactive, per `knowledge/DATA.md` §8 reproducibility.

## Design and layout for a published data piece
Applies whether the output is a static image, a web page, or a slide:
- lead with the finding, not the dataset — a headline chart, then supporting detail;
- generous whitespace and a restrained color palette; avoid decorative 3D and unnecessary gridlines;
- typography and contrast should meet basic accessibility standards (legible size, sufficient contrast ratio);
- mobile and desktop layouts both need to be checked when the piece is a web page — wide tables and dense charts often break on narrow screens and need a responsive or simplified alternative.

## Maps specifically
- state the projection/basemap source;
- avoid choropleths at a jurisdiction level too coarse to answer the actual question (e.g., country-level color when the story is about specific cities);
- for sensitive locations (victims, sources, vulnerable groups), apply the same precision-vs-necessity test as `knowledge/GEOLOCATION.md`'s ethics gate — a jittered or regional point may be more responsible than an exact pin.

## Source map
- S01–S02 — data journalism visualization practice.
- S41/S43 — analytical methods feeding the visual.
- This module's production/dashboard framing is adapted at a principle level from general end-to-end data-journalism tooling patterns (data → narrative → production-quality frontend); see `CREDITS.md`.
