# Layout Engines

This chapter runs one small graph through
five engines and reads the five pictures,
so the choice of engine stops being a
guess and becomes a habit.

The specimen is `graphviz-lab/engines.dot`:
six nodes, A to F, joined as two triangles
with bridges — small enough that every
layout fits on a page, connected enough
that the engines genuinely differ.

```bash
for e in dot neato fdp circo twopi; do
    $e -Tsvg engines.dot -o engines-$e.svg
done
```

(All five succeed; transcript
`t02-all-engines.txt`. Each SVG names the
same 15 `<title>` elements — the facts are
identical; only the geometry moves.)

## dot: the layered answer

`dot` assumes direction matters. It ranks
nodes into layers and draws arrows
flowing from rank to rank, minimising
crossings. For anything that is a process,
a hierarchy or a sequence — the workshop
of this guide's recipes, the committee of
chapter 4 — it is the default and usually
the finish. Its weakness is the flip side
of its strength: a graph with no natural
downhill gets forced into layers anyway,
and circular relationships come out
looking like they have a boss.

## neato and fdp: the spring answer

`neato` treats edges as springs: connected
nodes pull together, all nodes push apart,
and the picture settles where the forces
balance. Nothing is up or down; closeness
*is* the message, which makes it the right
answer for networks — who is connected to
whom, and where the dense knots are.
`fdp` uses a faster, coarser version of
the same idea: for a few dozen nodes the
results are cousins, and for a few hundred
`fdp` finishes where `neato` is still
thinking. Both accept undirected graphs
most naturally, and both can look like a
hairball if the graph is one — chapter 9
is about that failure and its remedies.

## circo: the ring answer

`circo` finds cycles and draws them as
circles, with the rest attached around
them. A process that loops — check, fix,
check again — or a set of peers with no
centre and no start reads instantly in
`circo` and awkwardly everywhere else.
For engines.dot it finds the two triangles
and shows you the graph's actual shape in
a way `dot` never hinted at.

## twopi: the centred answer

`twopi` puts one node — the **root**,
chosen by you with `root=X` or by the
engine if you do not — at the centre, and
arranges the rest in rings by distance
from it. It answers *what hangs off this
one thing, and how far away is the rest*:
one server and its dependents, one idea
and its consequences. Choose the root
deliberately; the picture is an argument
about what matters most, and chapter 1's
rule applies to it.

## The rest of the row

`sfdp` is the spring model scaled to
thousands of nodes (chapter 9 uses it).
`patchwork` draws nested rectangles sized
by a `weight` — parts of a whole, like a
disk-usage map. `osage` lays clusters out
as the skeleton of the picture and hangs
their contents inside. Each reads the
same DOT; each is one word on the command
line; the lab verified the five above and
`sfdp`, and describes `patchwork` and
`osage` from the project documentation.

## Choosing, in one breath

Flow or hierarchy: **dot**. Network:
**neato**, large network: **fdp** or
**sfdp**. Ring or loop: **circo**. One
centre of the world: **twopi**. If in
doubt, render two and compare — it costs
one command, and the better picture is
usually obvious in seconds.
