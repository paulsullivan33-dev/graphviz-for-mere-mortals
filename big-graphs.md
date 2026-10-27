# Big Graphs

This chapter keeps a diagram readable as
it grows — because every technique before
this chapter works beautifully at ten
nodes and starts to fail, in named ways,
at fifty.

The lab's specimen is
`graphviz-lab/big.dot`: forty nodes on
three loops, written by a pattern rather
than by hand (transcript
`t05-big-graph.txt`). At forty nodes the
disease is already visible, which is what
makes it a good teaching size.

## How big graphs fail

- **The hairball.** A spring layout of a
  dense graph settles into a round knot
  where every node touches every region
  and no path can be followed by eye.
- **The wallpaper.** A `dot` layout of a
  wide graph becomes a page metres across
  and centimetres tall: technically laid
  out, practically a banner.
- **The directory.** Forty labels at full
  size is a phone book, not a picture.
  The information is all there and none
  of it can be found.

Notice that none of these is Graphviz
failing to compute. The layout finished.
The *reading* failed — and reading is the
job.

## The remedies, in the order to try them

**1. Draw less.** The strongest tool is a
smaller graph. Split the subject: one
diagram per loop, per department, per
stage, with a one-page overview that
names the parts and shows only how they
touch. Ten honest diagrams beat one
heroic one, and each stays checkable.
This is a writing decision, not a
Graphviz feature, and it solves more big
graphs than everything below combined.

**2. Change the engine.** For the lab's
forty nodes, `dot` produces a tall,
orderly banner; `sfdp` produces a compact
knot you can at least see whole. Both
SVGs are in `graphviz-lab/rendered/`
with the same 83 `<title>` elements —
same facts, different compromises. For
large undirected graphs `sfdp` is the
engine built for the size; expect to give
up fine detail in exchange for finishing
at all.

**3. Spend attributes on scale.** Smaller
`fontsize`, tighter `nodesep` and `ranksep`
(the gaps between nodes and ranks),
`concentrate=true` to merge parallel edge
segments into shared trunks, and dropping
labels to initials with a key beside the
picture. Each is a small lie of omission
told openly, in the key, where the reader
can find it.

**4. Cluster with intent.** Chapter 7's
clusters become load-bearing here:
grouped nodes give the eye a harbour.
A clustered big graph reads as six
medium facts instead of forty small ones.

**5. Filter before you render.** If the
DOT file came from a script (chapter 11),
the time to shrink the graph is in the
script: only the nodes within two steps
of the one you care about, only the edges
of one kind. A diagram *of a question*
stays small because the question is small.

## What not to do

Do not shrink the finished PNG until the
labels blur and call it solved: the SVG
was the readable form, and scaling a
picture of a phone book gives you a
smaller phone book. Do not hand-place the
forty nodes either — the moment positions
are yours again, you have bought back the
problem Graphviz exists to remove.

Check: the lab rendered the same big.dot
through `dot` and `sfdp`, and both files
are complete, valid SVGs with identical
element counts — the difference between
them is purely how a reader survives them.
