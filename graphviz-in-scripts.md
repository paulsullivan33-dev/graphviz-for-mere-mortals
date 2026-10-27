# Graphviz in Scripts and Pipelines

This chapter generates a diagram from
data — a small table of steps becomes a
picture with no hand-written DOT at all —
which is where Graphviz stops being a
drawing aid and becomes a stage in a
pipeline.

## The one idea

DOT is text, and text is the one thing
every program can already produce. So the
pattern is always the same three stages:

1. Something holds facts as data — a
   table, a list, a log, the output of
   another command.
2. A small program prints those facts as
   DOT.
3. An engine renders the DOT.

Stage 2 is usually the shortest program
in the building, because DOT asks so
little: a header, one line per node, one
line per edge, a closing brace.

## The lab's pipeline, whole

The lab keeps a made-up workshop's steps
in `graphviz-lab/pipeline/steps.csv` —
five rows of *from, to, label*:

```text
from,to,label
Intake,Sort,
Sort,Test,checked
Test,Pack,pass
Test,Sort,fail
Pack,Dispatch,
```

and a twenty-line Python program,
`graphviz-lab/pipeline/make_dot.py`, that
reads the table and prints DOT:

```python
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
```

```bash
python3 pipeline/make_dot.py pipeline/steps.csv > pipeline/generated.dot
dot -Tsvg pipeline/generated.dot -o rendered/pipeline.svg
```

Transcript `t06-pipeline.txt` shows the
generated DOT and the render: an SVG with
11 `<title>` elements — every step in the
table, drawn, including the *fail* arrow
looping back from Test to Sort that nobody
drew by hand because nobody had to.

## The shell-only version

Not every pipeline needs a program. A
loop in the shell renders a whole folder
of diagrams in one breath:

```bash
for f in *.dot; do
    dot -Tsvg "$f" -o "${f%.dot}.svg"
done
```

and a `Makefile` (this series has a Make
guide) turns *render when the source
changes* into a habit instead of a chore.
The build of this very guide's website
is a pipeline of the same shape: text in,
site out, nothing done by hand in between.

## Rules for generated diagrams

- **Generate the DOT, keep the DOT.** Save
  the generated file beside the picture.
  When a reader asks *why does this arrow
  exist*, the answer lives in the DOT and
  the data behind it — not in the PNG.
- **Quote defensively.** Data contains
  spaces, quotes and worse. Names from
  data should be reduced to safe DOT
  identifiers by the generator, with the
  full text kept in `label`, where quotes
  can be escaped once, in one place.
- **Use `strict` and expect duplicates.**
  Real data repeats itself; chapter 5's
  `strict digraph` keeps the picture sane
  while you fix the data at leisure.
- **Let the data be wrong loudly.** A row
  naming a node that should not exist is
  a finding about the data. A generator
  that silently tidies such rows away has
  hidden the one diagram worth looking at
  (chapter 1's rule, in work clothes).

## Where this leads

Anything with connections can feed the
pipeline: the structure of a database,
the steps of a build, the messages
between parts of a system, the results
of the other tools in this series — a
package list, a network scan of your own
machines, a folder of notes and the links
between them. The programs stay small
because the hard part — the layout — was
never yours to write.
