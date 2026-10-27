# Glossary

**Attribute** — a name-and-value setting
in square brackets (`[shape=box]`) on a
graph, a node or an edge; nearly
everything about appearance is one
(chapters 2 and 6).

**Backend** — the half of a render chosen
by `-T` that decides the form of the
output: SVG, PNG, PDF, plain text and
more (chapter 10).

**Cluster** — a subgraph whose name
begins `cluster_`, drawn as a labelled
box around its members (chapter 7).

**Directed graph** — a graph whose edges
are arrows with a direction that means
something; written `digraph`, edges `->`.

**DOT** — the text language Graphviz
reads: graphs written as nodes, edges and
attributes in a plain file.

**Edge** — a connection between two
nodes: an arrow in a directed graph, a
line in an undirected one.

**Engine** — the program that turns DOT
into positions: `dot`, `neato`, `fdp`,
`circo`, `twopi`, `sfdp` and kin
(chapter 8).

**Graph** — the whole subject of a DOT
file: a set of nodes and the edges
between them. Also, in DOT, the keyword
for the undirected kind.

**Label** — the words printed on a node,
an edge or a whole graph, set with the
`label` attribute; independent of the
node's name.

**Layout** — the positions the engine
chooses for nodes and edges; the work
you describe and Graphviz does.

**Node** — one thing in a diagram,
brought into being by naming it in the
file.

**Rank** — a layer in a `dot` layout:
nodes the same distance along the flow
share one. `rankdir` chooses which way
the ranks run.

**Root** — the centre node of a `twopi`
layout, chosen by you with `root=X` or
by the engine if you leave it.

**Strict graph** — a graph opened with
`strict`, in which writing the same edge
twice draws it once (chapter 5).

**Subgraph** — a named set of statements
inside a graph; the file's unit of
grouping, and a cluster when so named.

**SVG** — Scalable Vector Graphics: a
picture described as text, which scales
without blurring and can be read back
and checked (chapter 10).

**viewBox** — the coordinate frame named
at the top of an SVG file; its width and
height are the picture's size in points,
and this guide's way of confirming a
render's dimensions without opening it.
