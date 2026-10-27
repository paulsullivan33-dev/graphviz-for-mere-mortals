# Subgraphs and Clusters

This chapter groups nodes that belong
together — so a diagram can show *where*
things live, not only what connects.

## A subgraph is a set with a name

A **subgraph** is a group of statements
inside the graph, written with braces and
the word `subgraph`:

```dot
subgraph helpers {
    Ann; Bea; Cy;
}
```

On its own that only organises the
*file*: the picture does not change. A
subgraph earns its keep two ways — edges
can be drawn to and from the whole set at
once (`helpers -> Chair` means each of
them), and its defaults apply inside it
(a subgraph can set its own `node` style
for its members only).

## A cluster is a subgraph you can see

Name a subgraph `cluster_` followed by
anything — `cluster_kitchen`,
`cluster_back` — and the layout changes:
the members are drawn together inside a
box of their own, which can carry a label
and a fill colour.

```dot
subgraph cluster_back {
    label="Back room";
    style=filled; fillcolor="#fef3c7";
    Sort -> Shelve;
}
```

The lab's specimen is
`graphviz-lab/clusters.dot`: a fictional
club split into a *Public desk* cluster
and a *Back room* cluster, pale blue and
pale yellow, with two edges crossing
between them — the sign-in sheet's forms
going in, finished displays coming back.
Crossing edges are the point: clusters
answer *where*, edges answer *what flows*,
and most real diagrams need both.

## The rules that bite

- **The `cluster_` prefix is the whole
  trick.** A subgraph named anything else
  is invisible. Readers lose an hour to
  this; you will not.
- **Clusters suit `dot` best.** The other
  engines honour clusters unevenly —
  `osage` is built around them, `neato`
  largely ignores the boxes. Chapter 8's
  table says which.
- **Edges between clusters are ordinary
  edges.** Write them between two nodes,
  outside both braces. Drawing an arrow
  from a cluster itself needs an extra
  mechanism (`compound=true` and `lhead` /
  `ltail`) that this guide names here and
  otherwise leaves alone: in practice an
  arrow to a named member reads better.
- **Do not nest without a reason.** A
  cluster inside a cluster is legal and
  occasionally true — a room inside a
  building — but two levels is where
  readers stop following. If everything
  is grouped, nothing is.

## When to cluster

Cluster when the grouping is itself a
fact the reader needs: departments, rooms,
machines, stages owned by different
hands. Do not cluster to make a diagram
prettier; a cluster is a claim (chapter
1's rule) that these things belong
together and those do not, and it should
be exactly as true as an arrow is.

Check: `dot -Tsvg clusters.dot` renders
two filled rectangles with their labels,
and the lab's SVG holds 11 `<title>`
elements — the graph, both clusters, and
every node and edge inside them.
