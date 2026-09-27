# Multi-Engine Compatibility Knowledge

## Purpose
`investigativejournalism.skill` is a **method layer**, not a Claude-only plugin. It is designed to be loaded as context by any capable LLM engine — Claude, GPT, Gemini, Grok, Llama, DeepSeek, Mistral, or a local/open-weight model — and to run using whatever tools that particular engine and runtime already expose. This file states the rules that keep the skill portable.

## Core rule: use the engine's own strengths, ignore what it lacks
1. **No hard dependency on any single API, product or tool name.** Nothing in `SKILL.md` or `knowledge/*.md` requires a specific vendor's API, browser plugin, or file format. Where a file mentions a capability (web search, image analysis, a mapping tool, code execution), treat it as a *capability description*, not an instruction to call a specific named tool.
2. **Capability discovery first.** Before starting Phase B (source plan) of the investigation loop, the runtime should silently check what it actually has available this session (web/browsing access, image/vision input, code execution, file reading, connected apps) and route the work through whichever of those are present. Do not tell the user a step is impossible before checking.
3. **Graceful degradation.** If a capability referenced by a knowledge module is unavailable (e.g., no live web access), say so plainly, fall back to what can be done from provided material and reasoning alone, and tell the user what a connected version of the same engine, or a different tool, could add.
4. **Never fabricate a tool result.** If code execution, browsing, or file access is unavailable, do not simulate a plausible-looking output as if a tool had run. State the limitation instead — this is the same "AI is not evidence" boundary as `knowledge/AI_AND_INFORMATION_INTEGRITY.md`.
5. **Tool-name-agnostic instructions.** When this skill's text says "reverse-image search," "run the numbers," "check the registry," or "geolocate the frame," it means the *task*, to be carried out with whatever search engine, spreadsheet/code tool, public registry portal, or mapping tool the session has — not a specific branded product. `tools/TOOLBOX.md` lists concrete options as a menu, not a requirement list.

## Approximate capability mapping across common engines
This table is a rough orientation, not a guarantee — exact tool names and availability change by product and by session/runtime configuration; check what is actually available before assuming.

| Capability needed by this skill | What to look for in the current session |
|---|---|
| Live web search / fetch a URL | a search or browsing tool, a "connected browser," or a plugin/extension the runtime exposes |
| Read/analyze an uploaded document, spreadsheet or PDF | a file-reading or document tool, or native multimodal file input |
| Run code for data cleaning, stats or a chart | a code-execution / "analysis" tool, a notebook, or a spreadsheet formula environment |
| Look at an image or video frame | native vision/multimodal input, or an image-analysis tool |
| Query a map or place | a maps/places tool, or a general search/browsing tool pointed at a mapping site |
| Produce a polished document, deck or spreadsheet file | the runtime's native document/file-creation feature, or plain Markdown/HTML/CSV as a portable fallback |
| Structured multi-step task tracking | the runtime's own task/plan feature if present; otherwise track phases inline in the response using the schema in `schemas/output.schema.json` |

## Output portability
The structured formats this skill produces (`schemas/output.schema.json`, the Phase F genres in `SKILL.md`, the tables in `knowledge/DATA_VISUALIZATION.md`) are plain JSON/Markdown/CSV by design so that the same investigation record can move between engines and tools without loss — e.g., start research in one engine, hand the JSON record to another for drafting, without re-deriving the evidence trail.

## Packaging note for maintainers
This repository is intentionally a plain folder of Markdown/JSON/scripts with no engine-specific manifest at the root, so it can be dropped into any "skills" or "custom instructions" folder recognized by a given tool, or simply pasted/attached as context. If a specific runtime requires its own manifest or frontmatter format to auto-discover the skill, add that as a *thin wrapper file* pointing back at `SKILL.md`, rather than forking the knowledge content — see `CREDITS.md` for prior art on skill-discovery/packaging conventions this approach is informed by.

## Source map
This module has no source-book mapping (S01–S49); it codifies a packaging/portability principle informed by the multi-engine and skill-distribution projects listed in `CREDITS.md`.
