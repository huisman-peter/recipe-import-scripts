"""Add the recipe photos from the contents pages (2 and 3) to KG2510.md.

Every thumbnail on those pages carries the recipe name as its caption, so each
image can be saved under the recipe's own name (lowercase, spaces -> '-') and
linked from that recipe in the Markdown.
"""
import argparse
import pathlib
import re
import statistics
import sys
import unicodedata

import fitz

import extract

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SRC = pathlib.Path("KG2510.pdf")      # --issue overwrites these from its config
MD = pathlib.Path("KG2510.md")
FOLDER = extract.IMAGE_FOLDER
DPI = 300


def key(text):
    """Compare names while ignoring spaces, punctuation and case."""
    text = unicodedata.normalize("NFKD", text.lower())
    return re.sub(r"[^0-9a-z]+", "", text)


def caption_for(words, bb):
    """The caption printed directly underneath an image."""
    picked = [w for w in words
              if bb.x0 - 4 <= (w[0] + w[2]) / 2 <= bb.x1 + 4
              and bb.y1 - 3 <= w[1] <= bb.y1 + 46]
    picked.sort(key=lambda w: (round(w[1] / 6), w[0]))
    text = ""
    for word in picked:
        if text and not text.endswith("-"):
            text += " "
        text += word[4]
    return text.strip()


def single_bands(page):
    """The x ranges of a page's one-column thumbnails.

    Those are the columns the contents pages use for both the photos and their
    captions, so they also tell us how to cut a photo that spans several
    columns into the pieces the recipes actually are.
    """
    return _bands(page, 0)


def row_bands(page):
    """The y ranges of a page's one-column thumbnails (the photo rows)."""
    return _bands(page, 1)


def _bands(page, axis):
    """The bands of one page: the x ranges (or y ranges) of its thumbnails.

    One-column thumbnails give the columns directly.  Some issues print their
    contents photos two or three columns wide, though, which would leave a
    column out, so the wider photos are cut into columns of the same size;
    those are only estimates, so the measured bands win.
    """
    found, wide = [], []
    for xref, *_ in page.get_images(full=True):
        for rect in page.get_image_rects(xref):
            if rect.height < 60:
                continue
            if 90 <= rect.width <= 150:
                found.append((rect.y0, rect.y1) if axis else (rect.x0, rect.x1))
            elif rect.width > 150 and rect.height <= 120:
                wide.append(rect)

    def far_from(bands, span):
        return not any(abs(span[0] - other[0]) <= 4 and abs(span[1] - other[1]) <= 8
                       for other in bands)

    bands = []
    for span in sorted(found):
        if far_from(bands, span):
            bands.append(span)
    if bands and wide:
        step = statistics.median(end - start for start, end in bands)
        for rect in wide:
            start = rect.y0 if axis else rect.x0
            end = rect.y1 if axis else rect.x1
            parts = max(1, round((end - start) / step))
            for index in range(parts):
                span = (start + (end - start) * index / parts,
                        start + (end - start) * (index + 1) / parts)
                if far_from(bands, span):
                    bands.append(span)
    return sorted(bands)


def caption_columns(words, region, bands):
    """-> [(caption text, x0, x1)] one caption per column under a wide photo.

    A photo that spans several columns simply has its caption written over
    those columns, with the page number at its right-hand edge; a group of
    words without a number of its own therefore continues in the next column.
    """
    inside = [w for w in words
              if region.x0 - 4 <= (w[0] + w[2]) / 2 <= region.x1 + 4
              and region.y1 - 3 <= w[1] <= region.y1 + 46]
    groups = []
    for x0, x1 in bands:
        if x1 <= region.x0 + 4 or x0 >= region.x1 - 4:
            continue                      # that column is not under this photo
        picked = [w for w in inside
                  if x0 - 4 <= (w[0] + w[2]) / 2 <= x1 + 4]
        if not picked:
            continue
        picked.sort(key=lambda w: (round(w[1] / 6), w[0]))
        text = ""
        for word in picked:
            if text and not text.endswith("-"):
                text += " "
            text += word[4]
        if groups and not re.search(r"(?:^|\s)\d+(?:$|\s)", groups[-1][0]):
            previous = groups.pop()
            groups.append((previous[0] + " " + text, previous[1], x1))
            continue
        groups.append((text, x0, x1))
    return groups


def caption_cells(words, region, col_bands, rows):
    """-> [(caption text, crop)] for captions printed *inside* a photo.

    Some contents pages print one big collage instead of loose thumbnails; its
    captions then sit inside the collage area, each under the row of photos it
    belongs to.
    """
    cells = []
    for y0, y1 in rows:
        if y0 < region.y0 - 4 or y1 > region.y1 + 4:
            continue                      # that row is not inside this photo
        row = fitz.Rect(region.x0, y0, region.x1, y1)
        for text, x0, x1 in caption_columns(words, row, col_bands):
            cells.append((text, fitz.Rect(max(x0, region.x0), y0,
                                          min(x1, region.x1), y1)))
    return cells


def clean_caption(text):
    """Drop the page number and the running foot from a caption."""
    text = text.replace("koken & genieten", " ")
    text = re.sub(r"-\d+", "-", text)                 # "Bananen-65" -> "Bananen-"
    return " ".join(p for p in text.split() if not p.isdigit()).strip()


def cluster(rects, gap=8.0):
    """Merge image pieces that touch or nearly touch into one region."""
    clusters = [fitz.Rect(r) for r in rects]
    changed = True
    while changed:
        changed = False
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                a, b = clusters[i], clusters[j]
                grown = fitz.Rect(a.x0 - gap, a.y0 - gap, a.x1 + gap, a.y1 + gap)
                if grown.intersects(b):
                    clusters[i] = a | b
                    del clusters[j]
                    changed = True
                    break
            if changed:
                break
    return clusters


def thumbnails(doc):
    """-> list of (page index, caption, region) for the contents thumbnails."""
    found = []
    for pno in (1, 2):
        page = doc[pno]
        words = page.get_text("words")
        placements = []
        for xref, *_ in page.get_images(full=True):
            placements += list(page.get_image_rects(xref))
        main = [r for r in placements if r.width >= 90 and r.height >= 60]

        for rect in main:
            region = fitz.Rect(rect)
            for other in placements:       # a few thumbnails are image slices
                if other in main or other.width * other.height < 250:
                    continue
                centre = (other.x0 + other.x1) / 2
                if (rect.x0 - 15 <= centre <= rect.x1 + 15
                        and rect.y1 - 95 <= other.y1 <= rect.y1 + 5):
                    region |= other
            found.append((pno, clean_caption(caption_for(words, rect)), region))

        # thumbnails that consist of loose image pieces only
        pieces = [r for r in placements
                  if r not in main and r.width * r.height >= 250]
        for region in cluster(pieces):
            if region.width < 90 or region.height < 60:
                continue
            found.append((pno, clean_caption(caption_for(words, region)), region))
    return found


def insert_points(lines, table):
    """line index (0-based) after which each recipe's image belongs."""
    points = {}
    for row in table:
        start = row[0] - 1
        last = start
        index = start
        while index < len(lines):
            line = lines[index]
            if line.startswith("## "):
                last = index
            elif line.strip():
                break
            index += 1
        points[row[1]] = last
    return points


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issue", default="2510",
                        help="magazine issue: 2510 (built in) or 2511, 2512 …")
    parser.add_argument("--pdf", type=pathlib.Path, default=None)
    parser.add_argument("--md", type=pathlib.Path, default=None)
    args = parser.parse_args()

    config = extract.load_issue(args.issue) if args.issue != "2510" else extract
    pdf = args.pdf or pathlib.Path(getattr(config, "PDF", SRC))
    markdown = pathlib.Path(args.md or config.MD)
    folder = config.IMAGE_FOLDER
    table = config.RECIPE_TABLE

    doc = fitz.open(pdf)
    names = {key(row[1]): row[1] for row in table}
    pathlib.Path(folder).mkdir(exist_ok=True)

    saved, unmatched = {}, []
    split_map = getattr(config, "CAPTION_SPLIT", {})

    def lookup(caption, loose=False):
        """Captions are sometimes only the first line of a longer title."""
        # the text layer doubles a word now and then ("met spruitjes spruitjes en")
        caption = re.sub(r"\b(\S+)(?: \1\b)+", r"\1", caption)
        name = names.get(key(caption)) or names.get(key(caption.split(" ")[0]))
        if name:
            return name
        wanted = key(caption)
        hits = [other for other_key, other in names.items()
                if other_key.startswith(wanted)]
        if len(hits) == 1:
            return hits[0]
        # the caption sometimes runs on into the next column's label
        # ("Courgetti met kruidenpesto Zoet &"), so the recipe name may be the
        # shorter half of the caption instead of the longer one
        hits = [other for other_key, other in names.items()
                if wanted.startswith(other_key)]
        if len(hits) == 1:
            return hits[0]
        if not loose:
            return None
        # a caption can also lose a letter to the PDF's font ("wentelteef es"
        # for "wentelteefjes"), so drop one or two words from its end
        words = caption.split()
        for cut in range(len(words) - 1, max(len(words) - 3, 0), -1):
            if cut < 2:
                continue              # a single word is too guessy to match on
            partial = key(" ".join(words[:cut]))
            if not partial:
                continue
            hits = [other for other_key, other in names.items()
                    if other_key.startswith(partial)]
            if len(hits) == 1:
                return hits[0]
        # a word can also lose one letter to the PDF's font ("gepof e" for
        # "gepofte"), so accept a recipe name that is exactly one letter longer
        if len(wanted) >= 12:
            hits = [other for other_key, other in names.items()
                    if len(other_key) == len(wanted) + 1
                    and any(other_key[:index] + other_key[index + 1:] == wanted
                            for index in range(len(other_key)))]
            if len(hits) == 1:
                return hits[0]
        return None

    columns, rows = {}, {}

    def caption_bands(page_no):
        if page_no not in columns:
            columns[page_no] = single_bands(doc[page_no])
        return columns[page_no]

    def photo_rows(page_no):
        if page_no not in rows:
            rows[page_no] = row_bands(doc[page_no])
        return rows[page_no]

    def write(target, piece):
        filename = extract.image_filename(target)
        pix = doc[pno].get_pixmap(clip=piece, dpi=DPI)
        pix.save(str(pathlib.Path(folder) / filename), jpg_quality=92)
        saved[target] = filename

    for pno, caption, region in thumbnails(doc):
        name = lookup(caption)
        # an explicit split for this issue wins over the caption heuristics
        split = list(split_map.get(caption, []))
        targets = split or ([name] if name else [])
        # a caption that had to be guessed may be a jumble of several recipes,
        # so cut that photo into the columns its captions are written in
        exact = bool(name) and key(caption) == key(name)
        if region.width > 150 and not split and not exact:
            # such a photo holds the photos of several recipes, so cut it along
            # the columns the captions are written in; a collage can even hide
            # the captions inside its own area
            pieces = []
            for text, x0, x1 in caption_columns(doc[pno].get_text("words"),
                                                region, caption_bands(pno)):
                target = lookup(clean_caption(text), loose=True)
                if target:
                    pieces.append((target,
                                   fitz.Rect(max(x0, region.x0), region.y0,
                                             min(x1, region.x1), region.y1)))
                else:
                    unmatched.append(text)
            if not pieces:
                for text, cell in caption_cells(doc[pno].get_text("words"),
                                                region, caption_bands(pno),
                                                photo_rows(pno)):
                    target = lookup(clean_caption(text), loose=True)
                    if target:
                        pieces.append((target, cell))
                    else:
                        unmatched.append(text)
            for target, piece in pieces:
                write(target, piece)
            if pieces:
                continue

        if not targets:
            # a caption that lost a letter to the PDF's font only becomes
            # recognisable once its tail is dropped
            name = lookup(caption, loose=True)
            targets = [name] if name else []
        if not targets:
            unmatched.append(caption)
            continue
        # one wide photo can hold the photos of two recipes side by side
        for index, target in enumerate(targets):
            piece = fitz.Rect(region)
            if len(targets) > 1:
                step = region.width / len(targets)
                piece = fitz.Rect(region.x0 + index * step, region.y0,
                                  region.x0 + (index + 1) * step, region.y1)
            filename = extract.image_filename(target)
            pix = doc[pno].get_pixmap(clip=piece, dpi=DPI)
            pix.save(str(pathlib.Path(folder) / filename), jpg_quality=92)
            saved[target] = filename

    missing = [row[1] for row in table if row[1] not in saved]
    print(f"images written: {len(saved)}")
    print(f"unmatched captions: {unmatched}")
    print(f"recipes without a photo: {missing}")

    # always start from a freshly generated Markdown, so the link positions
    # (which come from the recipe table) stay correct
    import convert_pdf
    convert_pdf.SRC = pdf
    base = convert_pdf.build_markdown()
    markdown.write_text(base, encoding="utf-8")

    lines = base.split("\n")
    for name, index in sorted(insert_points(lines, table).items(),
                              key=lambda kv: -kv[1]):
        if name in saved:
            lines.insert(index + 1, f"\n![{name}]({folder}/{saved[name]})\n")
    markdown.write_text("\n".join(lines), encoding="utf-8")
    print(markdown, "updated")

if __name__ == "__main__":
    main()

