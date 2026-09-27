#!/usr/bin/env python3
"""Profile a journalism dataset without modifying the original."""
from __future__ import annotations
import argparse
from pathlib import Path

def load(path: Path, encoding="utf-8"):
    import pandas as pd
    if path.suffix.lower() in {".xlsx",".xls"}:
        return pd.read_excel(path)
    if path.suffix.lower()==".json":
        return pd.read_json(path)
    for sep in ("; ", ";", ",", "\t"):
        try:
            df=pd.read_csv(path, sep=sep, encoding=encoding)
            if df.shape[1]>1: return df
        except Exception: pass
    return pd.read_csv(path, encoding=encoding)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("file")
    p.add_argument("--output")
    a=p.parse_args()
    import pandas as pd
    f=Path(a.file)
    if not f.exists(): raise SystemExit(f"File not found: {f}")
    df=load(f)
    lines=[f"# Dataset profile — `{f.name}`", "", f"- Rows: **{len(df)}**", f"- Columns: **{len(df.columns)}**", ""]
    lines += ["## Columns","", "| column | type | missing | unique |","|---|---|---:|---:|"]
    for c in df.columns:
        lines.append(f"| {c} | {df[c].dtype} | {df[c].isna().sum()} | {df[c].nunique(dropna=True)} |")
    lines += ["",f"Duplicate rows: **{df.duplicated().sum()}**","",
              "> Investigate outliers and duplicates before deleting them. Record every transformation in the methodology note."]
    text="\n".join(lines)+"\n"
    if a.output: Path(a.output).write_text(text,encoding="utf-8")
    else: print(text)
if __name__=="__main__": main()
