# The Moving Parts

This chapter names the pieces — nodes,
edges, attributes and the layout
engines — so that every later surprise
has a name and a place to live.

## Nodes

A **node** is one thing in the diagram:
a person-shaped idea like `Chair`, a
step like `Inspect`, a place like
`Store`. Writing a name in a DOT file
brings the node into being; there is no
separate step that declares it. A node
has a **shape** (box, ellipse, diamond,
circle and more — chapter 6), a **label**
(the words printed in it, which need not
be its name), and a position that the
engine, not you, will choose.

## Edges

An **edge** joins two nodes. In a
**directed graph** — written `digraph` —
edges are arrows, written `A -> B`, and
direction means something: flow, order,
command. In an **undirected graph** —
written `graph` — edges are plain lines,
written `A -- B`, and mean only
*connected*. Choosing between them is the
first real decision in any diagram:
arrows claim a direction, so do not draw
one you do not mean (chapter 1's rule).

## Attributes

Almost everything about how a piece
looks is an **attribute**: a name and a
value in square brackets after the thing
it describes.

```dot
Chair [shape=box, style=filled, fillcolor="#dbeafe"]
Secretary -> Members [label="minutes"]
```

Attributes exist at three levels. **Graph
attributes** set the whole picture (its
title, its direction). **Node** and
**edge attributes** set one piece — or,
written as a defaults line (`node [shape=box]`),
every piece that follows. Chapter 5
covers the grammar; chapter 6 is the
catalogue of the ones you will actually
use.

## The layout engines

The **layout engine** is the program that
turns text into positions. Graphviz
ships several, and each is a separate
command reading the same DOT files:

| Engine | Rule of thumb | Shape of result |
|---|---|---|
| **dot** | Directed graphs with a downhill flow | Neat layers, top to bottom (or left to right) |
| **neato** | Undirected networks | A spring model: connected nodes pull close |
| **fdp** | Larger undirected networks | Like neato, faster and looser |
| **circo** | Rings and cycles | Nodes arranged around circles |
| **twopi** | One centre, everything radiating | Concentric rings around a root node |
| **sfdp** | Very large graphs | A scaled-up spring model (chapter 9) |
| **patchwork** | Nested parts of a whole | Rectangles packed by size |
| **osage** | Grouped, clustered graphs | Clusters laid out as the skeleton |

The engine is chosen by the command you
run, not by anything in the file: the
same `engines.dot` in this guide's lab
was rendered by five engines and came out
five different, all correct, ways
(transcript `t02-all-engines.txt`).

## Output backends

Layout decides *where*; a **backend**
decides *in what form*: the `-T` option.
`-Tsvg` makes a scalable picture for the
web, `-Tpng` a bitmap, `-Tpdf` a document
page, `-Tplain` a plain text list of the
coordinates the engine chose — the
machine-readable proof of the layout,
and chapter 10's quiet star. One layout,
many renderings.

## Who holds what, when it breaks

- The **DOT file** holds the facts: nodes,
  edges, labels. If a connection is wrong
  in the picture, it was wrong in the text.
- The **engine** holds the geometry. If
  the picture is ugly but the facts are
  right, the fix is another engine or
  different attributes — never dragging.
- The **backend** holds the format. A
  blurry PNG is not a layout problem;
  chapter 10 covers sizes and resolution.
- A **syntax error** (chapter 15) names
  its line: the file is read strictly, and
  the first broken line stops the render.
