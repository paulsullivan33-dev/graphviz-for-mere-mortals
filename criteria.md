# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's diagrams are all invented: a fictional club, a
   made-up workshop, six letters for a network.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 14 names what the tool
   cannot do: place a node exactly where you want it, know
   whether an automatic layout is arguing something the facts
   do not, stay readable past a few thousand nodes, check the
   numbers in your labels, or draw the chart family's pictures
   at all.
8. **The honesty rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *a diagram is a claim: draw
   what you know, and label the rest as a guess* — before any
   procedure depends on it, and later chapters point back to it
   where an automatic layout would make an invented connection
   look tidy and true.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a small Ubuntu 24.04 sandbox. Graphviz
**2.43.0** was installed from the distribution's packages and
exercised entirely on files the lab wrote for the purpose. All
DOT sources are in `graphviz-lab/`, all rendered output in
`graphviz-lab/rendered/`, and all transcripts in
`graphviz-lab/transcripts/`.

Run for real, with transcripts as evidence:

- Install and version, answered identically by five engines:
  `dot`, `neato`, `fdp`, `circo` and `twopi` all report
  Graphviz 2.43.0 (t00).
- The first diagram (a fictional club's committee): rendered
  to SVG and read back as text — a viewBox of 296 by 227
  points and 9 `<title>` elements (t01).
- One small network rendered by all five engines above, each
  a complete SVG naming the same 15 `<title>` elements —
  identical facts, five geometries (t02).
- One graph rendered to SVG, PNG and PDF, with the PNG's
  pixel size (1403 by 181) and the PDF's version read back
  with `file` (t03).
- A deliberately broken DOT file: exit 1, and the exact
  message `Error: broken.dot: syntax error in line 3 near ';'`
  recorded verbatim (t04).
- A forty-node graph rendered with both `dot` and `sfdp`;
  both SVGs complete, each with 83 `<title>` elements (t05).
- The pipeline: a twenty-line Python program turned a CSV
  table of steps into DOT, and `dot` rendered it — an SVG
  with 11 `<title>` elements (t06). The clusters and shapes
  specimens were rendered the same way and read back (11
  `<title>` elements each).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- The `patchwork` and `osage` engines: characterised in
  chapters 2 and 8, not rendered in the lab. The six engines
  that were run cover every claim the guide makes about
  choosing one.
- Rendering differences on other operating systems and font
  sets: the lab had one machine and one set of fonts, so the
  same file rendering wider elsewhere is stated as a limit
  (chapter 14), not shown.
- Graphical editors and viewers built on Graphviz by other
  projects: named in passing in chapters 3 and 13, not used.
- The comparison tools in chapter 13 are characterised, not
  benchmarked.

Fixtures are this guide's own and deliberately generic: a
fictional hobby club's committee, a made-up workshop workflow,
two clusters named for rooms any club might have, forty
numbered stations on invented loops, and a five-row table of
steps. No example is modelled on any real person, network,
service or organisation.
