#!/usr/bin/env python3
"""Read a tiny CSV of steps and print a DOT graph on stdout."""
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1], newline="", encoding="utf-8")))
print("digraph Pipeline {")
print('    label="Made by a script"; rankdir=LR;')
seen = set()
for r in rows:
    for n in (r["from"], r["to"]):
        if n not in seen:
            seen.add(n); print(f"    {n};")
    label = f' [label="{r["label"]}"]' if r["label"] else ""
    print(f'    {r["from"]} -> {r["to"]}{label};')
print("}")
