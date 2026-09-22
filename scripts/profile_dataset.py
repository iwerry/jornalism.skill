#!/usr/bin/env python3
"""profile_dataset.py — dataset profile for journalism work (read-only).

Turns a raw dataset into a method-ready report: schema, missing/suppressed
values, duplicates, outliers, PII exposure and a reproducibility block.

Usage:
    python3 scripts/profile_dataset.py data.csv
    python3 scripts/profile_dataset.py data.csv --key cnpj --format json -o profile.json
    python3 scripts/profile_dataset.py plan.xlsx --sheet "2024"

Never modifies the input file. Writes only to stdout or --output.
Requires: pandas (plus openpyxl for .xlsx).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ENCODINGS = ("utf-8", "utf-8-sig", "latin-1", "cp1252")
MISSING_SENTINELS = {
    "", "na", "n/a", "nan", "null", "none", "-", "--", "...", "ignorado",
    "ignorado/nao informado", "nao informado", "não informado", "sem dado",
    "suprimido", "suppressed", "confidencial", "sigilo",
}
PII_PATTERNS = [
    ("email", r"e-?mail|correo"),
    ("phone", r"fone|telefone|celular|whatsapp|phone|mobile"),
    ("tax id (cpf/cnpj)", r"\bcpf\b|\bcnpj\b|tax_?id|tin\b"),
    ("address", r"endereco|endereço|address|logradouro|\bcep\b|\bzip\b"),
    ("name", r"\bnome\b|\bname\b|responsavel|titular"),
    ("sensitive", r"raca|raça|religiao|religião|saude|saúde|biometr|voto|vitima|vítima"),
]
DATE_HINT = re.compile(r"(data|date|dt_|_at$|timestamp|dia$)", re.I)


def load(path: Path, encoding: str | None, sep: str | None, sheet: str | None):
    import pandas as pd

    suf = path.suffix.lower()
    if suf in (".xlsx", ".xls"):
        return pd.read_excel(path, sheet_name=sheet) if sheet else pd.read_excel(path)
    if suf == ".json":
        return pd.read_json(path)

    erros = []
    for enc in ((encoding,) if encoding else ENCODINGS):
        if sep:
            try:
                return pd.read_csv(path, sep=sep, encoding=enc, dtype=str)
            except Exception as exc:  # noqa: BLE001
                erros.append(f"{enc}/{sep!r}: {exc}")
                continue
        try:  # auto-detect separator (handles BR ";" + decimal comma)
            return pd.read_csv(path, sep=None, engine="python", encoding=enc, dtype=str)
        except Exception as exc:  # noqa: BLE001
            erros.append(f"{enc}/auto: {exc}")
    raise SystemExit("Could not read the file. Tried:\n  " + "\n  ".join(erros))


def coerce(df):
    """Infer numeric/date columns from string columns (handles BR decimal comma)."""
    import pandas as pd

    convertidos = {}
    for c in df.columns:
        s = df[c]
        nulo_antes = s.isna() | s.astype(str).str.strip().str.lower().isin(MISSING_SENTINELS)
        preenchido = int((~nulo_antes).sum())
        if preenchido == 0:
            continue
        limpo = s.where(~nulo_antes).astype(str).str.strip()
        num = pd.to_numeric(limpo, errors="coerce")
        if num.notna().sum() < preenchido * 0.9:
            # tenta decimal a la br (1.234,56 -> 1234.56)
            alt = limpo.str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
            num_alt = pd.to_numeric(alt, errors="coerce")
            if num_alt.notna().sum() > num.notna().sum():
                num = num_alt
        if num.notna().sum() >= max(3, preenchido * 0.9):
            convertidos[c] = num
            continue
        if DATE_HINT.search(str(c)):
            dt = pd.to_datetime(limpo, errors="coerce", dayfirst=True)
            if dt.notna().sum() >= max(3, preenchido * 0.9):
                convertidos[c] = dt
    return convertidos


def sha256_de(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for bloco in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def analisar(df, nome: str, key: str | None, comando: str) -> dict:
    convertidos = coerce(df)
    colunas, sentinels, pii = [], [], []

    for c in df.columns:
        s = df[c].astype(str)
        mascara_sent = s.str.strip().str.lower().isin(MISSING_SENTINELS)
        faltantes_reais = int(df[c].isna().sum())
        marcados = int(mascara_sent.sum())
        if marcados > 0:
            sentinels.append({"column": str(c), "marked_cells": marcados})
        for rotulo, padrao in PII_PATTERNS:
            if re.search(padrao, str(c), re.I):
                pii.append({"column": str(c), "looks_like": rotulo})
                break
        col = {
            "column": str(c),
            "dtype": str(df[c].dtype),
            "missing": faltantes_reais,
            "missing_pct": round(faltantes_reais / max(len(df), 1), 4),
            "missing_markers": marcados,
            "unique": int(df[c].nunique(dropna=True)),
        }
        if c in convertidos:
            v = convertidos[c].dropna()
            if str(convertidos[c].dtype).startswith("datetime"):
                col["range"] = f"{v.min()} .. {v.max()}"
            elif len(v):
                q1, q3 = v.quantile(0.25), v.quantile(0.75)
                inf, sup = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
                col["numeric"] = {
                    "min": float(v.min()), "median": float(v.median()),
                    "mean": round(float(v.mean()), 3),
                    "max": float(v.max()),
                    "std": round(float(v.std()), 3) if len(v) > 1 else None,
                    "iqr_outliers": int(((v < inf) | (v > sup)).sum()),
                }
        colunas.append(col)

    duplicadas_chave = None
    if key:
        if key not in df.columns:
            raise SystemExit(f"--key {key!r} not found. Columns: {list(df.columns)}")
        duplicadas_chave = int(df[key].duplicated().sum())

    return {
        "dataset": nome,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "command": comando,
        "rows": len(df),
        "columns_detail": colunas,
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_key": {"key": key, "duplicates": duplicadas_chave} if key else None,
        "missing_markers_found": sentinels,
        "pii_like_columns": pii,
        "methodology_note_draft": {
            "research_question": "",
            "source": "",
            "retrieved_at": "",
            "coverage": f"{len(df)} rows; universe: sample or census?",
            "transformations": [],
            "outliers_treated": [],
            "limitations": ["what this dataset cannot answer"],
            "reproducibility": comando,
            "variable_dictionary": "fill: name, type, unit, description, origin of each column",
        },
    }


def markdown(res: dict) -> str:
    L = [f"# Dataset profile — `{res['dataset']}`", "",
         f"- Rows: **{res['rows']}** · Columns: **{len(res['columns_detail'])}**",
         f"- Generated: {res['generated_at']} · Command: `{res['command']}`", "",
         "## Columns", "",
         "| column | type | missing | markers | unique | notes |",
         "|---|---|---:|---:|---:|---|"]
    for c in res["columns_detail"]:
        nota = []
        if "numeric" in c:
            n = c["numeric"]
            nota.append(f"median {n['median']} / mean {n['mean']} / min {n['min']} / max {n['max']}")
            if n["iqr_outliers"]:
                nota.append(f"**{n['iqr_outliers']} IQR outlier(s)** — investigate before deleting")
        if "range" in c:
            nota.append(c["range"])
        L.append(f"| {c['column']} | {c['dtype']} | {c['missing']} ({c['missing_pct']:.1%}) | "
                 f"{c['missing_markers']} | {c['unique']} | {'; '.join(nota)} |")

    L += ["", f"- Duplicate rows: **{res['duplicate_rows']}**"]
    if res["duplicate_key"]:
        L.append(f"- Duplicates on key `{res['duplicate_key']['key']}`: "
                 f"**{res['duplicate_key']['duplicates']}**")
    if res["missing_markers_found"]:
        L += ["", "## Missing / suppressed markers found", "",
              "> DATA.md: distinguish zero, missing and suppressed. Fix these before analysis.", ""]
        for s in res["missing_markers_found"]:
            L.append(f"- `{s['column']}`: {s['marked_cells']} cell(s)")
    if res["pii_like_columns"]:
        L += ["", "## ⚠️ Columns that look like personal data", "",
              "> ETHICS_AND_SAFETY.md: data minimization. Aggregate or drop before publishing microdata.", ""]
        for p in res["pii_like_columns"]:
            L.append(f"- `{p['column']}` (looks like {p['looks_like']})")

    L += ["", "## Methodology note draft (fill in)", ""]
    for k, v in res["methodology_note_draft"].items():
        L.append(f"- {k}: {v}")
    return "\n".join(L) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description="Profile a journalism dataset (read-only).")
    p.add_argument("file")
    p.add_argument("-o", "--output", help="write report to this file (default: stdout)")
    p.add_argument("--format", choices=["md", "json"], default="md")
    p.add_argument("--key", help="column to check for duplicate records (e.g. cnpj, processo)")
    p.add_argument("--sep", help="force separator (default: auto-detect)")
    p.add_argument("--encoding", help=f"force encoding (default: try {', '.join(ENCODINGS)})")
    p.add_argument("--sheet", help="Excel sheet name")
    a = p.parse_args()

    try:
        import pandas  # noqa: F401
    except ImportError:
        raise SystemExit("pandas is required: pip install pandas openpyxl")

    caminho = Path(a.file)
    if not caminho.exists():
        raise SystemExit(f"File not found: {caminho}")

    df = load(caminho, a.encoding, a.sep, a.sheet)
    comando = "python3 " + " ".join(sys.argv)
    res = analisar(df, caminho.name, a.key, comando)
    res["integrity"] = {"sha256": sha256_de(caminho), "bytes": caminho.stat().st_size}

    saida = json.dumps(res, ensure_ascii=False, indent=2, default=str) if a.format == "json" else markdown(res)
    if a.output:
        Path(a.output).write_text(saida, encoding="utf-8")
        print(f"report written to {a.output}")
    else:
        print(saida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
