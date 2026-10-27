# The DOT Language

This chapter gives you the whole grammar
of DOT — which is small enough to give —
so no file you meet later holds a
surprise you cannot parse.

## The skeleton

Every DOT file is one graph:

```dot
digraph Name {
    // statements, one per line is the custom
}
```

`digraph` makes a directed graph (arrows,
`->`); `graph` makes an undirected one
(lines, `--`), and mixing the two arrow
styles in one file is an error. The name
is yours to choose. Statements end with a
semicolon or a newline; this guide uses
semicolons, because a file you can scan
is a file you can debug.

Three kinds of statement do all the work:

```dot
A                       // a node, brought into being by naming it
A -> B                  // an edge between two nodes
A [label="Start here"]  // a node with attributes
```

## Names and words

A node name is a word (`Chair`), a number
(`42`), or a quoted string (`"Sign-in sheet"`).
Quote any name containing spaces or
punctuation — and quote labels always, as
a habit. DOT is **case-sensitive**:
`Chair` and `chair` are two different
people, which has embarrassed more than
one committee chart. A few words are
reserved (`node`, `edge`, `graph`,
`digraph`, `subgraph`, `strict`) and
cannot be node names unquoted.

## Chains and lists

Real diagrams repeat themselves, and DOT
has two compressions worth learning now:

```dot
A -> B -> C -> D          // a chain: three edges in one line
{Secretary Treasurer} -> Members   // both officers point at Members
```

The chain is sugar: it means exactly the
three separate edges. The brace list on
one side of an arrow makes one edge per
member — the neatest way to say *everyone
reports to the Chair* without writing it
four times.

## Defaults

A statement beginning `node`, `edge` or
`graph` sets defaults for everything that
follows:

```dot
digraph G {
    graph [rankdir=LR]
    node [shape=box, fontname="Helvetica"]
    edge [color="#444444"]
    // every node from here is a box
}
```

`rankdir=LR` deserves its own sentence:
it turns a `dot` layout sideways, flowing
left to right instead of top to bottom —
the single most-used graph attribute in
this guide, because processes read more
naturally across a wide page than down a
long one.

## The strict word

Writing the same edge twice draws it
twice. A graph opened as `strict digraph`
forbids duplicates: `A -> B` written
twice is one arrow. For diagrams generated
by scripts (chapter 11), which may not
know they have repeated themselves,
`strict` is cheap insurance.

## Comments

Three styles, all ignored by the engine:

```dot
// to the end of the line
/* across several
   lines */
#  also to the end of the line (a pre-processor line)
```

Comment the *why*, not the *what*: the
reader can see that the Treasurer sends
dues; what they cannot see is why the
Librarian does not. That is what the
comment is for.

Check: every file in `graphviz-lab/`
parses under this grammar, and the one
that does not — `broken.dot`, chapter 15's
specimen — fails on a line this chapter
lets you diagnose: a statement that ends
in an arrow and nothing after it.
