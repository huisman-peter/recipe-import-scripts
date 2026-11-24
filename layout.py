"""Recover the visual reading order of a magazine page from word boxes.

Neither extractor gets this right on its own:

* ``pdftotext -raw`` follows the PDF content stream.  Usually that is the
  reading order, but not always - e.g. page 10 of this issue stores the middle
  column of a three-column page *after* the right-hand column, and on page 46
  the section title that tops the page comes last.
* PyMuPDF's own line/block assembly sorts across the whole page, which mixes
  side-by-side recipes, and it glues columns together into one block.

So the lines are reconstructed from the word boxes and then ordered with a
recursive XY-cut: at every level prefer a vertical cut through a gutter that no
line crosses, and fall back to a horizontal cut (a band of white space between
two groups of lines).  Featuring a vertical cut first is what keeps a page of
side-by-side recipes in column order instead of interleaving them; allowing a
horizontal cut is what lifts a full-width heading above the columns.

The word text is only used to look the line up in the ``pdftotext`` output,
which spells the words correctly.
"""
import re

import fitz

SPLIT_GAP = 10.0     # words further apart than this never belong to one line
MIN_GUTTER = 6.0     # minimum width of a vertical cut
MIN_BLANK = 6.0      # minimum height of a horizontal cut
MAX_DEPTH = 40

# amounts / units as used in the ingredient lists
AMOUNT = r"(?:\d+(?:[,.]\d+)?\s*[-–]\s*\d+(?:[,.]\d+)?|\d*[½¼¾⅓⅔]|\d+(?:[,.]\d+)?)"
UNIT = (r"(?:el|tl|g|kg|ml|cl|dl|l|liter|stuks?|takjes?|takje|blaadjes?|tenen?|teen|"
        r"bosjes?|handjevol|snufjes?|mespuntjes?|mespunt|zakjes?|plakjes?|plakje|"
        r"sneetjes?|snee|blik(?:ken)?|potjes?|pot|punten|eetlepels?|theelepels?)")
BARE_QUANTITY = re.compile(rf"^(?:ca\.\s*)?(?:{AMOUNT})(?:\s+{UNIT})?\.?$")


def _segments(page):
    """Split the page's words into visual line segments (rows cut at big gaps)."""
    words = [{"bb": fitz.Rect(w[:4]), "t": w[4]} for w in page.get_text("words")]

    rows = []
    for word in sorted(words, key=lambda w: (w["bb"].y0 + w["bb"].y1) / 2):
        cy = (word["bb"].y0 + word["bb"].y1) / 2
        height = word["bb"].height or 1.0
        for row in rows[-20:]:
            if abs(cy - row["cy"]) <= max(2.0, 0.35 * max(height, row["h"])):
                row["words"].append(word)
                row["h"] = max(row["h"], height)
                break
        else:
            rows.append({"cy": cy, "h": height, "words": [word]})
    rows.sort(key=lambda r: r["cy"])

    segments = []
    for row in rows:
        group = []
        for word in sorted(row["words"], key=lambda w: w["bb"].x0):
            if group:
                gap = word["bb"].x0 - group[-1]["bb"].x1
                # a quantity always keeps company with the ingredient it counts,
                # even when the ingredient starts a "column" further to the right
                quantity = BARE_QUANTITY.match(" ".join(w["t"] for w in group))
                if gap > SPLIT_GAP and not (quantity and gap < 60):
                    segments.append(group)
                    group = []
            group.append(word)
        if group:
            segments.append(group)

    out = []
    for group in segments:
        bb = fitz.Rect(group[0]["bb"])
        for word in group[1:]:
            bb |= word["bb"]
        out.append({"bb": bb, "text": " ".join(w["t"] for w in group)})
    return out


def _vertical_cut(segs):
    """Return the x of the widest gutter no segment crosses, or None."""
    left = min(s["bb"].x0 for s in segs)
    right = max(s["bb"].x1 for s in segs)
    width = int(right) + 2
    covered = bytearray(width + 1)
    for seg in segs:
        for x in range(int(left), int(right) + 1):
            if seg["bb"].x0 < x < seg["bb"].x1:
                covered[x] = 1
    best = None
    start = None
    for x in range(int(left), int(right) + 2):
        if not covered[x]:
            if start is None:
                start = x
        elif start is not None:
            if (x - start >= MIN_GUTTER
                    and any(s["bb"].x1 <= start for s in segs)
                    and any(s["bb"].x0 >= x - 1 for s in segs)):
                if best is None or x - start > best[0]:
                    best = (x - start, (start + x - 1) / 2)
            start = None
    return None if best is None else best[1]


def _horizontal_cut(segs):
    """Return the y of the tallest band of white space between two groups."""
    ordered = sorted(segs, key=lambda s: s["bb"].y0)
    best, bottom = None, None
    for seg in ordered:
        if bottom is not None and seg["bb"].y0 - bottom >= MIN_BLANK:
            if best is None or seg["bb"].y0 - bottom > best[0]:
                best = (seg["bb"].y0 - bottom, (bottom + seg["bb"].y0) / 2)
        bottom = seg["bb"].y1 if bottom is None else max(bottom, seg["bb"].y1)
    return None if best is None else best[1]


def _order(segs, out, depth=0):
    if not segs:
        return
    if depth > MAX_DEPTH or len(segs) == 1:
        out.extend(sorted(segs, key=lambda s: (s["bb"].y0, s["bb"].x0)))
        return

    cut = _vertical_cut(segs)
    if cut is not None:
        left = [s for s in segs if (s["bb"].x0 + s["bb"].x1) / 2 < cut]
        right = [s for s in segs if (s["bb"].x0 + s["bb"].x1) / 2 >= cut]
        if left and right:
            _order(left, out, depth + 1)
            _order(right, out, depth + 1)
            return

    cut = _horizontal_cut(segs)
    if cut is not None:
        top = [s for s in segs if s["bb"].y0 < cut]
        bottom = [s for s in segs if s["bb"].y0 >= cut]
        if top and bottom:
            _order(top, out, depth + 1)
            _order(bottom, out, depth + 1)
            return

    out.extend(sorted(segs, key=lambda s: (s["bb"].y0, s["bb"].x0)))


def page_lines(page):
    """-> list of {text, bb} in visual reading order."""
    out = []
    _order(_segments(page), out)
    return out
