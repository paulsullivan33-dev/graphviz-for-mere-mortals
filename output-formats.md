# Output Formats

This chapter chooses the right picture
for the place it will live — a web page,
a printed document, a slide — and proves
the choice with the same diagram rendered
three ways.

One layout can be rendered into many
formats. The `-T` option names the
format; everything before it stays the
same. The lab rendered its workshop graph
all three ways (transcript
`t03-formats.txt`):

```bash
dot -Tsvg workshop.dot -o workshop.svg
dot -Tpng workshop.dot -o workshop.png
dot -Tpdf workshop.dot -o workshop.pdf
```

Same nodes, same layout: an SVG of about
5 KB, a PNG of about 39 KB at 1403 by 181
pixels, and a one-page PDF. Which one you
want depends entirely on where the picture
is going.

## SVG: for screens and the web

**SVG** is a description of the picture
in text: shapes, positions and words.
It scales to any size without blurring,
it is small, and a browser shows it
natively — which is why every picture in
this guide was checked as SVG. Two more
powers matter. Text inside an SVG stays
text, so a reader can search the page for
a label and find the node. And a node can
carry a `URL` attribute, turning it into
a link in the rendered SVG: a diagram of
a system's parts, where clicking a part
opens its page. That one feature turns a
picture into an index.

## PNG: for anywhere a picture must be a picture

**PNG** is a bitmap: a grid of pixels, at
a size fixed when you render it. Slides,
chat messages, documents that cannot
embed SVG — PNG goes everywhere, and
looks exactly as rendered. Its trap is
resolution: a PNG made small stays small.
Two levers fix that. `-Gdpi=200` renders
more pixels into the same inches for
print, and simply rendering larger and
letting the destination scale down beats
rendering at display size and hoping.
If a PNG of yours is blurry, the layout
was never the problem; the pixel count was.

## PDF: for pages that will be printed

**PDF** is the page-shaped format: vector
like SVG, so it prints sharply at any
size, and it is what a document, a report
or a book chapter wants embedded. A
multi-page diagram is the one surprise:
a graph too big for one page is scaled to
fit it by default, and chapter 9's advice
(split the graph) beats fighting the
scaler.

## The formats that are not pictures

Two backends deserve a paragraph because
they are how machines read layouts back:

- **`-Tplain`** prints one line per node
  and edge with the coordinates the engine
  chose, in a format any script can parse.
  It is the bridge between *Graphviz laid
  it out* and *my program needs to know
  where things landed*.
- **`-Tcanon`** prints the graph back as
  tidy DOT — parsed, ordered, comments
  gone. It is the quickest syntax check
  there is (`nop` does a similar job), and
  the way to normalise a file a script
  wrote before diffing it against another.

Beyond those, the engines can emit
PostScript, image maps for web pages
(`-Timap`, the clickable-diagram partner
of SVG), JSON descriptions of the layout
(`-Tjson`), and more. The full list is one
command away: ask for an unknown format
and the error message prints every format
your build supports.

Check: your three renders of the same
file should agree on content and differ
only in kind — and `file workshop.png`
should report the pixel size you asked
for, as the lab's transcript shows.
