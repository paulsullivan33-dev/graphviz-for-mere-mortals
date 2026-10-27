# Shapes, Colours and Labels

This chapter makes a diagram say more
without adding a single node: the shape
of a node, its colour, and the words on
it and on its edges.

The lab's specimen is
`graphviz-lab/shapes.dot` — one small
graph that uses each idea once, so you
can find them all in a single picture.

## Shapes carry meaning

A node's `shape` is its silhouette, and
readers learn the common ones fast:

| Shape | Usual meaning |
|---|---|
| `box` | A thing, a step, a place (the default for most work) |
| `ellipse` | A person, a group, a start or end state |
| `diamond` | A decision — something with more than one way out |
| `cylinder` | A store of data: a file, a database, a shelf |
| `note` | A note, a document, a comment made visible |
| `circle` | A point in a process rather than a thing |
| `plaintext` | No outline at all: just the words |

```dot
choice [shape=diamond, label="Worth doing?"]
store  [shape=cylinder, label="Store"]
```

The discipline is consistency: if a
diamond means *decision* in one diagram,
it must never mean *cupboard* in the
next. Shapes are a tiny language you
teach your reader once.

## Colour, used sparingly

Three attributes do most colour work:
`color` (the outline), `fillcolor` (the
inside, which only shows with
`style=filled`), and `fontcolor` (the
words). Colours can be names (`red`,
`lightblue`) or hex values in quotes
(`"#dbeafe"`), and hex is what this guide
uses, because a named *lightblue* is
whatever your version thinks it is.

```dot
idea [shape=box, style="filled,rounded",
      fillcolor="#fef3c7", label="Idea"]
```

`style` takes a list: `filled`, `rounded`,
`dashed`, `bold`, `dotted` — for nodes
and edges alike. A dashed edge is this
guide's convention for *sometimes*, or
*not yet*; the lab file's grey dashed
arrow back from the decision to the idea
says exactly that, with
`style=dashed, color="#6b7280"`.

Colour is emphasis, not decoration. A
diagram where everything is filled is a
diagram where nothing is. Fill the one
node the reader should find first; leave
the rest plain.

## Labels: the words that do the work

A node's printed words are its `label`,
independent of its name:

```dot
SignIn [label="Sign-in sheet"]
```

Names stay short and safe (`SignIn`);
labels carry the spaces, capitals and
punctuation the reader needs. Inside a
label, `\n` makes a new line, and a label
can be split deliberately — `label="Idea\n(first line)"`
in the lab file centres two lines in one
box.

Edge labels sit beside their arrow:

```dot
choice -> task [label="yes"]
```

Keep them to a word or three. An edge
label is a caption, not a paragraph; a
diagram that needs sentences on its
arrows usually needs another node instead.

Two more label tools, used rarely and
gladly: `labelloc` and a graph's own
`label` make the diagram's title
(chapter 4), and `xlabel` puts a node's
label *outside* its shape, for crowded
pictures where inside will not fit.

Check: render `shapes.dot` with
`dot -Tsvg` and read it back — the lab's
SVG holds 11 `<title>` elements and every
shape in the table above appears in one
small picture (transcripts in
`graphviz-lab/transcripts/`).
