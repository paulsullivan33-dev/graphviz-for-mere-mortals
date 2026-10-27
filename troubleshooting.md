# Troubleshooting

Symptom first, cause second. Most of
these were met by this guide's own lab,
whose transcripts are the evidence.

## A syntax error names a line

```text
Error: broken.dot: syntax error in line 3 near ';'
```

Graphviz stops at the first line it
cannot parse and says where (transcript
`t04-broken.txt`, from the lab's
deliberately broken file: `B -> ;` — an
arrow with nothing after it). Work
through the usual causes in order:

1. **A missing closing brace or quote.**
   The named line is where the parser
   gave up, which is often the line
   *after* the real omission.
2. **The wrong arrow for the graph kind.**
   `--` in a `digraph`, or `->` in a
   `graph`, is a syntax error every time.
3. **An unquoted name with spaces or
   punctuation in it.** Quote it
   (chapter 5), or shorten the name and
   put the long form in the `label`.
4. **A stray character from another
   world**: curly quotes pasted from a
   document, a non-breaking space, an
   arrow typed as a Unicode arrow instead
   of `->`. Retype the line by hand in a
   plain editor and compare.

A fast check that separates *syntax*
from *sense*: run the file through
`-Tcanon`. A file that canonicalises is
grammatically fine, and your problem is
elsewhere on this page.

## The render works and the picture is wrong

- **A node appears twice** under two
  spellings: DOT is case-sensitive
  (chapter 5). `Chair` and `chair` are
  two people as far as the file knows.
- **An arrow points the wrong way.**
  `A -> B` means *from A to B*; the
  engine never guesses politeness or
  seniority. If half the chart feels
  inverted, you have been writing edges
  destination-first — pick one habit
  (this guide writes source first) and
  keep it.
- **Every edge is drawn twice.** The
  statement was written twice, or
  generated twice. `strict digraph`
  (chapter 5) makes the file refuse the
  second copy.
- **A cluster has no box.** The subgraph
  is not named `cluster_...` (chapter 7).
  The prefix is the whole trick.

## The picture is the wrong shape entirely

- **Tall when it should be wide** (or
  reverse): set `rankdir=LR` for
  left-to-right, `rankdir=TB` for the
  default top-to-bottom. This one graph
  attribute fixes more first diagrams
  than everything else on this page.
- **A network forced into layers** is
  `dot` being asked the wrong question:
  try `neato` or `circo` (chapter 8)
  before fighting the ranks.
- **Nodes will not line up in a row.**
  Nodes share a rank only by structure
  (same distance from a root, or explicit
  `{rank=same; A; B;}`). If the eye wants
  a row the graph does not imply, the
  graph is the authority; add the missing
  edge or the rank statement openly, and
  know you have made a claim (chapter 1).

## The output file disappoints

- **The PNG is blurry.** It was rendered
  at screen size and printed at page
  size. Raise `-Gdpi` or render SVG/PDF
  for print (chapter 10).
- **The SVG is enormous or empty.** An
  empty file usually means the command
  failed and the shell created the file
  anyway on an earlier run: delete it,
  re-run, and read the command's own
  words before its output file.
- **`dot` is not found** after installing:
  the package did not install, or its
  commands are not on the path (on
  Windows, the installer's path option).
  `dot -V` is the whole test — chapter 3.

## It worked yesterday

Fonts changed, a Graphviz upgrade
changed, or the data feeding a generator
changed shape (chapter 11). Render the
*old* file, from version control, with
the *current* tool: if the old picture
returns, the data moved; if it does not,
the tool or its fonts did. Either way
you have halved the problem with one
command, which is what this page is for.
