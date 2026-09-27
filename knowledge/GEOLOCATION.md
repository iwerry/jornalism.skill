# Geolocation and Chronolocation Knowledge

## Purpose
Operational workflow for establishing **where** and **when** a piece of visual evidence (photo, video, satellite frame, livestream still) was made — a core step in `knowledge/VERIFICATION.md`'s image/video layer and in `knowledge/OSINT.md`.

This module is engine-agnostic: it describes the *method*, not a specific product. Whatever mapping/imagery/reverse-image tool is available to the runtime (a connected map/Places tool, a browsing tool, or the user's own apps — Google Maps, Google Earth, Grok/X vision, Google Lens, Yandex, Bing Maps, OpenStreetMap, Sentinel Hub, etc.) should be used through that tool's normal interface; this file exists so the reasoning stays the same regardless of which tool executes it. A concrete, versioned list of candidate tools lives in `tools/TOOLBOX.md`.

## Geolocation ladder

1. **Extract anchors from the media itself** — visible text/signage language and alphabet, license-plate format (not the plate number itself — see Ethics below), vehicle models sold in-region, driving side, architecture style, vegetation/climate, terrain shape.
2. **Narrow by claimed location** — take whatever place name, region or route is claimed (by the uploader, a caption, or the assignment) as a *hypothesis*, not a fact.
3. **Cross-reference fixed landmarks** — mountains, skylines, distinctive buildings, bridges, water bodies, road/rail geometry — against satellite and street-level imagery.
4. **Reverse-image search stills** — check whether the same frame (or an earlier/higher-resolution version) already exists online, which can reveal the true origin, an older event, or a prior publication.
5. **Confirm with a second independent anchor** — never geolocate on a single landmark alone if a second is available (a skyline alone can recur in many similar cities).
6. **Record the confidence level** — "confirmed" (two-plus independent anchors matched to current imagery), "probable" (one strong anchor), or "unresolved."

## Chronolocation ladder

1. Sun position and shadow length/direction (cross-checked against date + latitude/longitude).
2. Weather visible in the frame vs. historical weather records for the candidate date/place.
3. Vegetation state (leaf cover, snow) for the season.
4. Construction/demolition state of a landmark, compared against known timelines (satellite history, permits, news coverage).
5. Scheduled public events (matches, ceremonies, elections) visible in banners, dress or context.
6. Upload metadata and platform-reported timestamps — treated as a lead, since these can be edited, stripped, or reflect a re-upload rather than the capture time.

Always distinguish **event time** from **upload time**; do not conflate them in the write-up.

## Satellite and aerial comparison

When lawfully available, compare the scene against dated satellite/aerial imagery to:
- confirm or rule out a candidate location by matching structures, roads and vegetation;
- establish a "not-before" or "not-after" date bound from a visible construction or damage state;
- detect changes over time relevant to the story (deforestation, construction, damage, crowd size).

Record the imagery provider and capture date for every comparison frame used as evidence.

## Ethics and safety gate (applies before publication)

Geolocation is a verification technique, not license to publish a precise address. Before publishing a location finding, run the same test as `knowledge/ETHICS_AND_SAFETY.md`:
- Is the precise location necessary to the public-interest fact, or does a general area (city/region) suffice?
- Could publishing exact coordinates enable harassment, retaliation against a vulnerable person, or expose an ongoing security-sensitive situation (active conflict, a protected witness, a minor's home or school)?
- Never geolocate to identify a private individual's home or a confidential source's location.
- Never attempt to defeat a platform's authentication or access controls to obtain higher-resolution imagery — use only lawfully, publicly accessible sources.

## Source map
- S48 — Berkeley Protocol digital open-source investigation standards.
- S49 — evaluating digital open-source imagery.
- S03–S05 — verification handbooks (UGC, image/video verification).
