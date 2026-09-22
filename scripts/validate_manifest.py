#!/usr/bin/env python3
"""validate_manifest.py — validate sources/manifest.json (read-only).

Checks ID format and uniqueness, required fields, types, empty values,
language codes, tag hygiene and suspicious source paths. Optionally checks
that every Sxx referenced in the docs exists in the manifest (and vice versa).

Usage:
    python3 scripts/validate_manifest.py
    python3 scripts/validate_manifest.py --json
    python3 scripts/validate_manifest.py --scan-docs        # cross-check Sxx refs in *.md
    python3 scripts/validate_manifest.py --check-files ../archive

Exit codes: 0 = valid (warnings allowed) · 1 = validation errors · 2 = unreadable input.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "sources" / "manifest.json"

# Update this constant when the archive legitimately grows past 49 sources.
EXPECTED_SOURCES = 49

REQUIRED = {"id", "title", "source_path", "language", "pages", "tags"}
ID_PADRAO = re.compile(r"^S\d{2,3}$")
IDIOMA_PADRAO = re.compile(r"^[A-Z]{2}$")
REF_PADRAO = re.compile(r"\bS\d{2,3}\b")
EXTENSAO_DUPLA = re.compile(r"(\.\w{2,4})\1$", re.I)


def checar(dados) -> tuple[list[str], list[str]]:
    erros: list[str] = []
    avisos: list[str] = []

    if not isinstance(dados, list):
        return ["manifest must be a JSON array of source objects"], avisos
    if len(dados) != EXPECTED_SOURCES:
        erros.append(f"expected {EXPECTED_SOURCES} sources, found {len(dados)} "
                     f"(if the archive grew on purpose, update EXPECTED_SOURCES in this script)")

    vistos_id: set[str] = set()
    vistos_caminho: set[str] = set()
    tags_por_forma: dict[str, set[str]] = {}

    for i, item in enumerate(dados):
        onde = f"entry #{i}"
        if not isinstance(item, dict):
            erros.append(f"{onde}: not an object")
            continue
        sid = item.get("id", "")
        onde = f"entry #{i} ({sid or 'no id'})"

        faltando = REQUIRED - item.keys()
        if faltando:
            erros.append(f"{onde}: missing fields {sorted(faltando)}")
        for campo in REQUIRED & item.keys():
            if not isinstance(item[campo], (str, int, list)) or (
                isinstance(item[campo], str) and not item[campo].strip()
            ):
                erros.append(f"{onde}: empty or invalid '{campo}'")

        if not ID_PADRAO.match(str(sid)):
            erros.append(f"{onde}: id must match S01..S999 (got {sid!r})")
        if sid in vistos_id:
            erros.append(f"{onde}: duplicated id")
        vistos_id.add(str(sid))

        idioma = str(item.get("language", ""))
        if idioma and not IDIOMA_PADRAO.match(idioma):
            erros.append(f"{onde}: language must be a 2-letter uppercase code (got {idioma!r})")

        paginas = item.get("pages")
        if not isinstance(paginas, int) or paginas <= 0:
            erros.append(f"{onde}: pages must be a positive integer (got {paginas!r})")

        tags = item.get("tags", [])
        if isinstance(tags, list):
            if not tags:
                avisos.append(f"{onde}: empty tags list")
            for t in tags:
                if not isinstance(t, str) or not t.strip():
                    erros.append(f"{onde}: invalid tag {t!r}")
                else:
                    tags_por_forma.setdefault(t.strip().lower(), set()).add(t)

        caminho = str(item.get("source_path", ""))
        if caminho in vistos_caminho:
            avisos.append(f"{onde}: source_path already used by another entry ({caminho})")
        vistos_caminho.add(caminho)
        if caminho.startswith("/") or ".." in caminho or re.match(r"^[A-Za-z]:\\", caminho):
            erros.append(f"{onde}: suspicious source_path (absolute or traversal): {caminho}")
        if EXTENSAO_DUPLA.search(caminho):
            avisos.append(f"{onde}: source_path has doubled extension (e.g. '.pdf.pdf'): {caminho}")

    for forma, variantes in sorted(tags_por_forma.items()):
        if len(variantes) > 1:
            avisos.append(f"tag spelling variants {sorted(variantes)} — normalize to one form")

    return erros, avisos


def varrer_docs() -> tuple[list[str], list[str], set[str]]:
    """Cross-check Sxx references in docs against the manifest."""
    erros, avisos = [], []
    try:
        dados = json.loads(MANIFEST.read_text(encoding="utf-8"))
        ids = {x.get("id") for x in dados if isinstance(x, dict)}
    except Exception as exc:  # noqa: BLE001
        return [f"cannot read manifest for cross-check: {exc}"], avisos, set()

    usados: set[str] = set()
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for ref in REF_PADRAO.findall(md.read_text(encoding="utf-8", errors="ignore")):
            usados.add(ref)
            if ref not in ids:
                erros.append(f"{md.relative_to(ROOT)}: references {ref}, absent from manifest")
    for sid in sorted(ids - usados):
        avisos.append(f"{sid} is never referenced in any .md (orphan source)")
    return erros, avisos, usados


def checar_arquivos(base: Path) -> tuple[list[str], list[str]]:
    erros, avisos = [], []
    try:
        dados = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"cannot read manifest: {exc}"], avisos
    for item in dados:
        if not isinstance(item, dict):
            continue
        alvo = base / str(item.get("source_path", ""))
        if not alvo.exists():
            avisos.append(f"{item.get('id')}: file not found under {base} "
                          f"(ok if the archive is not distributed)")
    return erros, avisos


def main() -> int:
    p = argparse.ArgumentParser(description="Validate sources/manifest.json.")
    p.add_argument("--json", action="store_true", help="machine-readable report")
    p.add_argument("--scan-docs", action="store_true", help="cross-check Sxx references in *.md")
    p.add_argument("--check-files", metavar="DIR", help="check that source files exist under DIR")
    a = p.parse_args()

    try:
        dados = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: cannot read {MANIFEST}: {exc}", file=sys.stderr)
        return 2

    erros, avisos = checar(dados)
    referencias = None
    if a.scan_docs:
        e2, a2, usados = varrer_docs()
        erros += e2
        avisos += a2
        referencias = sorted(usados)
    if a.check_files:
        e3, a3 = checar_arquivos(Path(a.check_files))
        erros += e3
        avisos += a3

    if a.json:
        print(json.dumps({
            "manifest": str(MANIFEST.relative_to(ROOT)),
            "sources": len(dados) if isinstance(dados, list) else None,
            "valid": not erros,
            "errors": erros,
            "warnings": avisos,
            "references_found": referencias,
        }, ensure_ascii=False, indent=2))
    else:
        total = len(dados) if isinstance(dados, list) else 0
        for msg in erros:
            print(f"ERROR: {msg}")
        for msg in avisos:
            print(f"warning: {msg}")
        print(f"\n{'INVALID' if erros else 'OK'}: {total} sources, "
              f"{len(erros)} error(s), {len(avisos)} warning(s).")
    return 1 if erros else 0


if __name__ == "__main__":
    raise SystemExit(main())
