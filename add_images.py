"""Add the recipe photos from the contents pages (2 and 3) to KG2510.md.

Every thumbnail on those pages carries the recipe name as its caption, so each
image can be saved under the recipe's own name (lowercase, spaces -> '-') and
linked from that recipe in the Markdown.
"""
import argparse
import pathlib
import re
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

    def lookup(caption):
        """Captions are sometimes only the first line of a longer title."""
        name = names.get(key(caption)) or names.get(key(caption.split(" ")[0]))
        if name:
            return name
        wanted = key(caption)
        hits = [other for other_key, other in names.items()
                if other_key.startswith(wanted)]
        return hits[0] if len(hits) == 1 else None

    for pno, caption, region in thumbnails(doc):
        name = lookup(caption)
        targets = [name] if name else list(split_map.get(caption, []))
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

