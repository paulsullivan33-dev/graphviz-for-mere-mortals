# Graphviz for Mere Mortals

Most diagrams are drawn by dragging
boxes around a page, and redrawn the
same way every time something changes.
**Graphviz** takes the opposite bargain:
you write a short text file in the
**DOT** language saying what connects to
what, and a **layout engine** works out
where everything goes — positions,
spacing, the routing of every arrow. Edit
the words, render again, and the picture
rebalances itself.

This guide explains how that works: the
moving parts (nodes, edges, attributes,
and the family of engines — **dot**,
**neato**, **fdp**, **circo**, **twopi**),
the DOT language itself, shapes, colours
and labels, subgraphs and clusters, what
to do when a graph grows too big to read,
the output formats (SVG, PNG and PDF),
and how to generate diagrams from data
with small scripts, so a table of steps
becomes a picture nobody had to draw.

The rule that governs everything here is
stated in chapter 1: **a diagram is a
claim — draw what you know, and label
the rest as a guess.** Graphviz will lay
out a guess as tidily as a fact. Every
example in this guide is invented for the
purpose: a fictional club's committee,
a made-up workshop, a handful of letters
standing for a network.

The lab behind this guide ran the real
thing: **Graphviz 2.43.0** on a small
Linux machine. Against it the lab
rendered a first diagram and read the
SVG back as text — counting its elements
and its viewBox to prove the picture —
drew one small network five ways with
five different engines, rendered the same
graph to SVG, PNG and PDF, drew a
forty-node graph with both `dot` and
`sfdp`, generated a diagram from a CSV
table with a twenty-line Python program,
and fed the engines a deliberately broken
DOT file to record the exact words of
its refusal.

What the lab could not do, it did not
fake. It had one machine with one set of
fonts, so the same file rendering wider
on another computer is taught as a limit,
not demonstrated. The `patchwork` and
`osage` engines are characterised from
the project's documentation rather than
run. Interactive and graphical editors
built on Graphviz by other projects are
named in passing, not taught.
`criteria.md` keeps the full ledger of
what was run and what was only read.

## What this guide covers

- [**What Graphviz is**](what-graphviz-is.md) —
  the mental model: describe connections
  in text, let an engine do the geometry,
  and the honesty rule that comes with it
- [**The moving parts**](the-moving-parts.md) —
  nodes, edges, attributes and the layout
  engines, and which part holds what
- [**Installing Graphviz**](installing-graphviz.md) —
  the package install, the row of engine
  commands it gives you, and the version check
- [**Your first diagram**](your-first-diagram.md) —
  a fictional club's committee, written,
  rendered, checked, and then changed
- [**The DOT language**](the-dot-language.md) —
  the whole small grammar: graphs, chains,
  defaults, strict graphs and comments
- [**Shapes, colours and labels**](shapes-colours-and-labels.md) —
  making a diagram say more without adding
  a single node
- [**Subgraphs and clusters**](subgraphs-and-clusters.md) —
  grouping nodes that belong together,
  and the `cluster_` prefix that makes a
  group visible
- [**Layout engines**](layout-engines.md) —
  one graph, five engines, five different
  correct pictures — and how to choose
- [**Big graphs**](big-graphs.md) —
  how large diagrams fail, and the
  remedies in the order to try them
- [**Output formats**](output-formats.md) —
  SVG for the web, PNG for slides, PDF
  for print, and the formats machines
  read back
- [**Graphviz in scripts and pipelines**](graphviz-in-scripts.md) —
  generating diagrams from data: a CSV
  table in, a picture out
- [**Recipes**](recipes.md) — an
  organisation chart, a process with a
  decision, a state machine, a clickable
  diagram, and diffing two versions of
  a system
- [**The neighbours**](the-neighbours.md) —
  Mermaid, PlantUML, and drawing by hand:
  what each does that Graphviz doesn't,
  and vice versa
- [**Limits**](limits.md) — no placing
  nodes by hand, tidy is not the same as
  true, the scale ceiling, and what is
  not in the box
- [**Troubleshooting**](troubleshooting.md) —
  the syntax error that names its line,
  the doubled node, the missing cluster
  box, the blurry PNG, and the traps this
  guide's lab met so you don't have to
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Charts of numbers — bars, lines and
scatter plots are a different toolbox,
and chapter 14 says why forcing a graph
engine into them helps nobody. Exact,
hand-placed geometry — floor plans, maps
and posters belong to drawing tools.
UML taught as a discipline: chapter 13
points at PlantUML and moves on. And
the graphical editors other projects
build on top of Graphviz are named,
not taught; this guide stays with the
text file and the engines, where the
tool does its honest work.

## How to use this guide

Read chapter 1 for the model and the
rule, and chapter 2 before rendering
anything — knowing which part holds what
turns later confusion into a named
problem. Chapter 4 takes your first
diagram in the same sitting as the
install. Chapters 5 to 7 are the
language, learned once and used in every
file afterwards. Chapter 8 is the one
that repays experimentation: render the
lab's little network with every engine
and look at all five pictures. Chapter
11 is the chapter that changes what the
tool is *for* — write the generator
while the example is small enough to
check by eye. The lab's DOT sources and
rendered pictures live in `graphviz-lab/`;
its transcripts are
`graphviz-lab/transcripts/`; its notes
are `examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Markdown for Mere Mortals](https://paulsullivan33-dev.github.io/markdown-for-mere-mortals/)
- [MkDocs for Mere Mortals](https://paulsullivan33-dev.github.io/mkdocs-for-mere-mortals/)
- [Pandoc for Mere Mortals](https://paulsullivan33-dev.github.io/pandoc-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/graphviz-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/graphviz-for-mere-mortals/blob/main/LICENSE-CODE).
