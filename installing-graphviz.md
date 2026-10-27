# Installing Graphviz

This chapter ends with the layout engines
on your machine and a version line you
can check — the same check this guide's
lab recorded before drawing anything.

Graphviz is an old, settled tool, and it
is installed the ordinary ways: from your
operating system's packages, or from the
downloads on the project's site,
graphviz.org. There is nothing to sign up
for and no service to run; the engines
are plain commands that read a file and
write a file.

## On Debian and Ubuntu

```bash
sudo apt install graphviz
dot -V
```

On Fedora the package has the same name
(`sudo dnf install graphviz`); on macOS
with Homebrew it is `brew install graphviz`;
on Windows the project ships an installer,
after which the commands live in the
folder it names, and the installer can
add them to your path.

Check: the version line names the release
and answers on every engine, not just
`dot`:

```text
$ dot -V
dot - graphviz version 2.43.0 (0)
$ neato -V
neato - graphviz version 2.43.0 (0)
```

(from transcript
`graphviz-lab/transcripts/t00-version.txt`,
which records the same answer from `dot`,
`neato`, `fdp`, `circo` and `twopi`).

This guide's lab is a small Ubuntu 24.04
machine, and the version matters the
usual way: attribute names and engines
are stable across many years of Graphviz,
but a tip written for a much older or
newer release may name something yours
spells differently. The transcripts in
`graphviz-lab/transcripts/` are all from
**2.43.0**.

## What you actually got

The package installs a row of commands,
one per engine — `dot`, `neato`, `fdp`,
`sfdp`, `circo`, `twopi`, `patchwork`,
`osage` — plus a few helpers this guide
mentions only in passing: `nop` (which
reads a graph and prints it tidied),
`gvedit` (a simple graphical editor some
packages include), and the `xdot` format
for viewers. Chapter 2's table is the map
from engine to job; you need no more of
the row today than `dot` itself.

## A thirty-second smoke test

Before the next chapter, prove the whole
chain — file in, picture out — in four
lines:

```bash
printf 'digraph G { Hello -> World }\n' > /tmp/smoke.dot
dot -Tsvg /tmp/smoke.dot -o /tmp/smoke.svg
ls -l /tmp/smoke.svg
```

A small SVG file (a few thousand bytes of
text) appears. Open it in any browser and
two boxes, *Hello* above *World*, joined
by an arrow, are looking at you. If `dot`
is not found, the install did not finish
or the command is not on your path —
chapter 15 starts there.
