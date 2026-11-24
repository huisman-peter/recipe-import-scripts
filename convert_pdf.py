"""Build a readable Markdown version of the Koken & genieten issue KG2510.pdf.

Why this two-tool approach
--------------------------
The magazine uses a nested multi-column layout: two or three recipes sit side
by side on a page and ingredient lists are sometimes split over two
sub-columns.  That makes both extractors imperfect on their own:

* ``pdftotext -raw`` returns the text in PDF content-stream order, which for
  this issue is exactly the logical reading order (left column first, then the
  right one, sub-columns likewise).  It also joins word fragments and ligatures
  correctly.  It does not expose layout/style information, though.
* PyMuPDF knows the fonts and sizes (so it can tell a recipe title from body
  copy) but its extractor sorts text across the whole page, which mixes up
  side-by-side recipes, and it inserts spurious spaces inside words.

So we take the text from ``pdftotext -raw`` and the heading information from
PyMuPDF, and then

* turn recipe/feature titles into Markdown headings,
* emphasise the labels and the ingredient amounts,
* remove the hyphens that were only introduced by a line break,
* drop the running heads, footers and page numbers.
"""
import pathlib
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict, deque

import fitz

import layout

SRC = pathlib.Path("KG2510.pdf")
OUT = pathlib.Path("KG2510.md")

BOLD_FONTS = ("Bold", "Black", "ExtraBold", "SemiBold", "Heavy")

# amount / unit patterns used to emphasise ingredient quantities
UNIT = (r"(?:el|tl|g|kg|ml|cl|dl|l|liter|stuks?|takjes?|takje|blaadjes?|tenen?|teen|"
        r"bosjes?|handjevol|snufjes?|mespuntjes?|mespunt|zakjes?|plakjes?|plakje|"
        r"sneetjes?|snee|blik(?:ken)?|potjes?|pot|punten|eetlepels?|theelepels?)")
AMOUNT = r"(?:\d+(?:[,.]\d+)?\s*[-–]\s*\d+(?:[,.]\d+)?|\d*[½¼¾⅓⅔]|\d+(?:[,.]\d+)?)"
LABELS = ("Ingrediënten voor:", "Bereidingstijd:", "Per portie:", "Per stuk:",
          "VOOR DE", "EEN DAG VAN TEVOREN", "DE VOLGENDE DAG")

# unit/amount regex: "**3-4 el** witte balsamicoazijn", "**500 g** slagroom"
INGREDIENT_RE = re.compile(rf"^({AMOUNT})(?:\s+({UNIT}))?\s+(\S.*)$")
FOOTER_RE = re.compile(r"^koken\s*&\s*genieten\s+\d+$", re.I)

# pdftotext -enc UTF-8 keeps the typographic ligatures; expand them
LIGATURES = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl",
             "ﬅ": "ft", "ﬆ": "st"}

# KG2508 prints the "snel klaar" / "zonder vlees of vis" marks in the ingredient
# lists and the bullets of the index with a font whose ToUnicode map is broken,
# so they arrive as C0 control codes (\x07 inside the ingredients, \x08 in the
# index).  They carry no text and must not reach the Markdown or the JSON.
CONTROL = {code: None for code in range(0x20) if chr(code) not in "\t\n"}
CONTROL[0x7f] = None


def is_bold(font):
    return any(k in font for k in BOLD_FONTS)


def key(text):
    """Normalised text, used to match pdftotext lines against PyMuPDF spans."""
    return re.sub(r"[^0-9a-z]+", "", text.lower())


def normalise(text):
    for bad, good in LIGATURES.items():
        text = text.replace(bad, good)
    return unicodedata.normalize("NFC", text.translate(CONTROL))


def heading_keys(doc):
    """Per page: (set of h1 keys, set of h2 keys) derived from the font sizes."""
    pages = []
    for page in doc:
        h1, h2 = set(), set()
        for block in page.get_text("dict")["blocks"]:
            if block.get("type") != 0:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"]
                    if not text.strip():
                        continue
                    size = round(span["size"], 1)
                    if size >= 24:
                        h1.add(key(text))
                    elif size >= 12.5 and is_bold(span["font"]):
                        h2.add(key(text))
        pages.append((h1, h2))
    return pages


def raw_pages():
    """pdftotext -raw, one string per PDF page."""
    proc = subprocess.run(["pdftotext", "-raw", "-enc", "UTF-8", str(SRC), "-"],
                          capture_output=True, check=True)
    # normalise() drops the C0 control codes, so the form feed that separates
    # the pages has to be consumed first
    pages = [normalise(page) for page in
             proc.stdout.decode("utf-8").split("\f")]
    if pages and not pages[-1].strip():
        pages.pop()          # the form feed that closes the last page
    return pages


def decorate(text):
    """Emphasise labels and ingredient amounts (markup only, text unchanged)."""
    for label in LABELS:
        if text.startswith(label):
            return "**" + label + "**" + text[len(label):]
    if text.endswith((".", ",")):
        return text
    match = INGREDIENT_RE.match(text)
    if match and (match.group(2) or len(text) <= 30):
        amount = match.group(1) + (f" {match.group(2)}" if match.group(2) else "")
        return f"**{amount}** {match.group(3)}"
    return text


def is_noise(text, page_no):
    if not text:
        return True
    if FOOTER_RE.match(text):
        return True
    if re.fullmatch(r"\d{1,3}", text) and int(text) == page_no:
        return True       # the printed page number
    return bool(re.fullmatch(r"[\s•|*\-–—]+", text))


def spaced_better(pool_text, cell_text):
    """pdftotext normally spaces a line better than PyMuPDF, but on a few lines
    it loses every space (leaving one 25+ character 'word'); there the PyMuPDF
    text is the readable one."""
    pool_words = pool_text.split()
    cell_words = cell_text.split()
    if not pool_words or not cell_words:
        return pool_text
    if (max(len(word) for word in pool_words) >= 25
            and max(len(word) for word in cell_words) < 25):
        return cell_text
    return pool_text


def page_entries(doc, index, page_text, page_no):
    """Order the pdftotext lines of one page by the position of the matching
    layout cell, so no text is lost and nothing is duplicated."""
    cells = layout.page_lines(doc[index])
    available = defaultdict(list)
    for position, cell in enumerate(cells):
        available[key(cell["text"])].append(position)

    pool = [line.strip() for line in page_text.split("\n") if line.strip()]
    placed = []
    last = -1.0
    for order, text in enumerate(pool):
        k = key(text)
        cell = cells[available[k][0]] if available[k] else None
        position = available[k].pop(0) if available[k] else None
        if position is not None:
            text = spaced_better(text, cell["text"])
        if position is None:
            for other in sorted(available, key=len, reverse=True):
                if not other or not available[other]:
                    continue
                if (other in k or k in other) and min(len(other), len(k)) >= 0.5 * max(len(other), len(k)):
                    position = available[other].pop(0) + 0.5
                    break
        if position is None:
            position = last + 0.5      # keep it next to its neighbours
        last = position
        placed.append((position, order, text))

    placed.sort()
    return [text for _, _, text in placed]


def glue_hyphens(entries):
    """Re-join words that were split over two lines by a (soft) hyphen."""
    out = []
    for text, level in entries:
        if out:
            prev, prev_level = out[-1]
            if (prev.endswith("-") or prev.endswith("\u00ad")) and text[:1].islower():
                out[-1] = (prev.rstrip("-\u00ad") + text, max(prev_level, level))
                continue
            if not level and not prev_level and text.startswith("-"):
                out[-1] = (prev + " " + text[1:], 0)
                continue
        out.append((text, level))
    return out


def build_markdown(report=False):
    doc = fitz.open(SRC)
    headings = heading_keys(doc)
    pages = raw_pages()

    entries = []
    for index in range(doc.page_count):
        h1, h2 = headings[index]
        page_text = pages[index] if index < len(pages) else ""
        for text in page_entries(doc, index, page_text, index + 1):
            if is_noise(text, index + 1):
                continue
            k = key(text)
            level = 1 if k in h1 else (2 if k in h2 else 0)
            entries.append((text, level))

    # a line whose successor opens the ingredient list closes a recipe title
    for pos, (text, level) in enumerate(entries):
        if level:
            continue
        following = next((t for t, lv in entries[pos + 1:] if t), "")
        if following.startswith("Ingrediënten voor:"):
            entries[pos] = (text, 2)

    entries = glue_hyphens(entries)
    if report:
        print("entries:", len(entries))

    lines = []
    for text, level in entries:
        if level:
            lines += ["", "#" * level + " " + text, ""]
        else:
            lines.append(decorate(text))
    md = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"
    md = md.replace("\u00ad", "")
    # dropping the icon/bullet glyphs above can leave a gap behind ("verdure  46")
    md = re.sub(r"  +", " ", md)
    # a soft hyphen inside a real compound keeps its hyphen
    md = md.replace("vanilleextract", "vanille-extract")
    return md


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=pathlib.Path, default=SRC,
                        help="the magazine to convert (default KG2510.pdf)")
    parser.add_argument("--md", type=pathlib.Path, default=OUT,
                        help="where to write the Markdown")
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    SRC = args.pdf                  # raw_pages() and build_markdown() read these
    result = build_markdown(report=args.report)
    args.md.write_text(result, encoding="utf-8")
    print("WROTE", args.md, len(result), "chars")


