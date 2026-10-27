# Limits

What Graphviz cannot do — the chapter the
rest of the guide has been promising,
kept in the same plain style.

## You do not control the layout

The founding bargain, seen from its other
side: positions belong to the engine. You
can *influence* them — ranks, weights,
invisible edges used as gentle hints,
clusters — but you cannot place a node at
*x, y* and have the tool respect it as a
drawing program would. Readers arrive
wanting one node *just there* and leave
either converted (the layout knew better)
or frustrated. If the exact geometry is
the message — a floor plan, a map, a
poster — chapter 13's hand-drawing tools
are the right ones and this is the wrong
book for that picture.

## Automatic is not the same as clear

An engine optimises what it can measure:
crossings, bends, symmetry, spring
energy. It cannot measure *meaning*. It
will place the most important node in a
corner with the same serenity as in the
centre, route the one arrow that matters
behind four that do not, and produce a
tidy, finished, *misleading* picture of a
graph it laid out perfectly. Tidy is not
true (chapter 1's rule, from the layout's
side): the human still has to read the
render and ask whether the geometry is
arguing something the facts do not.

## Scale has a ceiling

Chapter 9's remedies postpone a real
limit. Somewhere in the low thousands of
nodes, every engine's output stops being
a diagram and becomes a texture. `sfdp`
will finish, bravely, on graphs far past
that, and the result is a screensaver:
true, complete, and unreadable. Past that
ceiling the honest tools are aggregation
and questions — diagrams *of subsets* —
not bigger renders.

## It draws connections, not data

Graphviz knows nothing of the quantities
your nodes may carry. It will not total,
average, or check; a node labelled with a
wrong number is drawn as beautifully as a
right one. (Chapter 11's generator is
where such checks belong, in your code,
before the DOT is printed.) Nor does it
do the chart family's work — bars, lines,
scatters — at all: that is a different
toolbox, and forcing a graph engine into
it produces pictures that are neither.

## The text cuts both ways

A DOT file is only as checkable as it is
short. Generated files of ten thousand
lines are write-only artefacts: nobody
reviews them, and errors ride into
pictures on the authority of the tool's
tidiness. And the coupling is loose by
design — rename a thing in your data and
nothing anywhere complains; the diagram
simply starts describing last month's
world, beautifully.

## What is not in the box

No interactivity of its own, no animation,
no live update as data changes (a pipeline
can re-render, which is a script's
virtue, not the tool's). Fonts are the
host machine's, so the same file can
render wider on another computer and
occasionally break a carefully tuned
label. And the layout of a very large or
very tangled graph can be *slow* —
minutes, on the spring engines — because
the problem being solved is genuinely
hard, not because the tool is lazy.
