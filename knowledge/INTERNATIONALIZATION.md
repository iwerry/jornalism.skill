# Internationalization Knowledge

## Principle

The investigative method should remain stable while the presentation layer adapts to language, jurisdiction and newsroom convention.

## Runtime localization

Select:
1. user language;
2. requested publication language;
3. jurisdiction;
4. publication style;
5. date/time convention;
6. currency and measurement convention.

## Legal language

Never translate a legal concept only by lexical similarity.

Store:
- original term;
- jurisdiction;
- translated explanation;
- procedural stage when relevant.

## Source language

Keep source titles and quotations in their original language in the evidence record. Provide a translation separately when useful.

## Numbers

Localize:
- decimal separators;
- thousands separators;
- currencies;
- units;
- dates;
- time zones.

Preserve machine-readable values separately from formatted display values.

## Cross-border investigations

Create a jurisdiction matrix containing:
- country;
- relevant records;
- access mechanism;
- applicable privacy rules;
- right-of-reply expectations;
- legal terminology;
- source-risk considerations.

Do not assume a rule from one country applies to another.

## Multilingual source triangulation

A source translated from another language is still the same source lineage.

Independent corroboration requires independence of origin, not merely different languages.

## Brazilian newsroom operational annex

For a `pt-BR` request, the presentation layer defaults to:

- **Pauta (assignment brief):** question, hypothesis, sources to contact, documents to request, expected difficulty — same fields as `schemas/output.schema.json`'s `investigation_record`, in the format used by `S44` (Modelo de Pauta Padrão).
- **Fases processuais (right-of-reply and legal status terms):** use the exact stage — *investigado → indiciado → denunciado → réu → condenado* — never collapse these into a generic "acusado" when the file specifies a stage.
- **Direito de resposta:** frame right-of-reply requests in the register used by Brazilian editorial manuals (S23, S24, S26, S29, S32) — neutral, specific, time-bound, and never presuming guilt (Art. 5º, LXXIV and the press-ethics code S33).
- **Style conventions:** decimal comma, DD/MM/AAAA dates, R$ currency formatting, and Estadão/Poder360/EBC-style numeral and title conventions (S24, S26, S32) unless the newsroom specifies otherwise.
- **LGPD:** treat personal-data minimization questions in `knowledge/ETHICS_AND_SAFETY.md` as also satisfying Lei Geral de Proteção de Dados (Lei 13.709/2018) proportionality expectations — this is operational guidance, not legal advice; confirm with counsel for a specific publication.

## Source map

- S20–S21 — Latin American press and safety context.
- S24/S26/S27/S29/S30/S32/S33 — Brazilian editorial conventions.
- S34–S37 — international/platform context.
- S48–S49 — international digital investigation standards.
- S09/S15 — Spanish/Portuguese information and AI resources.
