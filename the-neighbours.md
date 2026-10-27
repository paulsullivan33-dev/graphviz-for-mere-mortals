# The Neighbours

Graphviz is not the only way to turn an
idea into a diagram, and two of its
neighbours live in the same
diagrams-from-text country. An honest map:

## Mermaid

**Mermaid** is a JavaScript tool that
turns short text descriptions — in a
syntax of its own, lighter than DOT —
into diagrams *inside a web page or a
Markdown document*. Its home turf is
documentation that is read where it is
written: many Markdown renderers,
including the one that builds this
guide's site, can draw a Mermaid block
in place, with nothing installed.

The trade is reach against depth.
Mermaid's common diagrams — flowcharts,
sequence diagrams, class diagrams — are
quicker to write and prettier by default,
and it has diagram *kinds* Graphviz does
not attempt, sequence diagrams above all.
Graphviz counters with fifty attribute
knobs where Mermaid offers five, engines
for graphs of thousands of nodes, and
output as a file you own. If the diagram
lives inside a document and is small,
Mermaid is usually the right reach. If
the diagram *is* the document, or the
graph is large, or a script is generating
it, DOT is the deeper well. This series
has a Markdown guide; Mermaid is best met
there, in its native soil.

## PlantUML

**PlantUML** is the other elder: a text
language grown around UML — the software
designer's diagram family of class,
sequence, activity and state diagrams —
rendered by a Java program. Where a
diagram is *about software's design* and
must speak UML precisely (classes with
typed members, lifelines and messages),
PlantUML is speaking its mother tongue
and Graphviz is translating. PlantUML in
fact *uses* Graphviz inside itself for
several of its layouts — the neighbour
has this guide's tool in its own engine
room. For committees, processes and
networks with no UML in them, DOT remains
the smaller language to learn whole.

## Drawing by hand

The drawing programs — a whiteboard, a
shapes-and-arrows editor, paper — win
whenever the picture is the point: a
poster, a page whose exact composition
carries the message, a diagram drawn
*with* people in a room, changing as the
conversation changes. They also win for
the one-off sketch of three boxes that
would take longer to type than to drag.

What they cannot do is the rest of this
guide: redraw themselves after an edit,
be generated from data, be diffed in
version control, or lay out five hundred
nodes before lunch. The honest rule of
thumb is chapter 1 turned sideways: if
you will change the diagram twice, or a
machine could write it once, write text.
If it will be drawn once, in company, for
effect — pick up the pen, and let
Graphviz sit that one out.
