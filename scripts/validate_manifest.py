#!/usr/bin/env python3
import json, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((root/"sources/manifest.json").read_text(encoding="utf-8"))
ids=[x["id"] for x in data]
assert len(data)==49, len(data)
assert len(ids)==len(set(ids))
required={"id","title","source_path","language","pages","tags"}
assert all(required <= x.keys() for x in data)
print(f"OK: {len(data)} sources, unique IDs, required fields present.")
