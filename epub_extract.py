"""Turn the EPUB "French Bistro Cooking" (Sarah Spencer) into RecipeSage JSON-LD.

This is a second, self-contained pipeline next to the Koken & genieten magazine
one (convert_pdf.py -> add_images.py -> extract.py).  It shares nothing with it
on purpose: an EPUB already *is* structured text, so no PDF/Markdown step is
needed and the magazine's Dutch ingredient heuristics do not apply.

The source book is English and uses US measures; the delivery is Dutch with
metric units.  The structure (order, section, cook/prep time, servings, photo)
is read from the EPUB, while the recipe text comes from ``french_bistro_nl.py``,
the hand-made Dutch translation of all 45 recipes::

    python epub_extract.py                 # dry run: nothing is written
    python epub_extract.py --dump-en       # write _en_dump.json (source text)
    python epub_extract.py --write         # images + recipes-french-bistro.json

Import in RecipeSage: *Settings -> Import -> JSON-LD*.  RecipeSage ignores
``publisher`` and turns every ``recipeCategory`` entry into a label, so the book
goes into ``recipeCategory`` as well - that is the only way these recipes stay
distinguishable inside RecipeSage.
"""
import argparse
import base64
import json
import pathlib
import re
import sys
import urllib.parse
import zipfile
import xml.etree.ElementTree as ET

import french_bistro_nl

SRC = pathlib.Path("French Bistro Cooking_ Easy Classic French Cuisine Recipes "
                   "to Make at Home by Spencer Sarah.epub")
OUT = pathlib.Path("recipes-french-bistro.json")
IMAGE_FOLDER = pathlib.Path("images-french-bistro")
IMAGE_MODE = "data"           # "data" = base64 data URI | "url" | "path"
BASE_URL = ""

# book metadata (OPF: dc:creator "Spencer, Sarah", dc:date 2016-02-16)
BOOK = "French Bistro Cooking"
AUTHOR = "Sarah Spencer"
DATE_PUBLISHED = "2016-02"

NS = "{http://www.w3.org/1999/xhtml}"
OPF = "{http://www.idpf.org/2007/opf}"

# the eight section titles printed in the book -> Dutch categories
SECTION_NL = {
    "Bistro Appetizers": "Bistrohapjes",
    "Soups and Stews": "Soepen en stoofschotels",
    "Classic Chicken and Poultry": "Klassieke kip en gevogelte",
    "Delectable Pork and Veal Dishes": "Varkens- en kalfsvleesgerechten",
    "French Beef Masterpieces": "Rundvleesklassiekers",
    "Coastal Seafood Creations": "Vis en zeevruchten",
    "Vegetables and Side Dishes": "Groenten en bijgerechten",
    "Sweet French Endings": "Zoete desserts",
}


def text(element):
    """All visible text of an element, whitespace collapsed."""
    return re.sub(r"\s+", " ", "".join(element.itertext())).strip()


def image_filename(name):
    """The photo's file name: lowercase, whitespace -> '-', brackets dropped.

    Same rule as extract.image_filename so both pipelines name their photos
    alike; brackets are dropped so the name stays a clean Markdown/JSON target.
    """
    slug = re.sub(r"\s+", "-", name.lower())
    return re.sub(r"[()\[\]]+", "", slug) + ".jpg"


def spine(z):
    """The content documents of the EPUB, in reading order."""
    found = re.search(rb'full-path="([^"]+)"', z.read("META-INF/container.xml"))
    opf_path = found.group(1).decode("utf-8")
    folder = pathlib.PurePosixPath(opf_path).parent
    opf = ET.fromstring(z.read(opf_path))
    files = {item.get("id"): item.get("href") for item in opf.iter(OPF + "item")}
    hrefs = []
    for ref in opf.iter(OPF + "itemref"):
        href = files.get(ref.get("idref"))
        if href:
            hrefs.append(str(folder / href))
    return hrefs


def parse_part(data):
    """-> the source fields of one recipe page, or None if it is not a recipe.

    Every recipe prints ``Directions:`` and ``Serves:``; nothing else in the
    book does, so those two labels identify a recipe page.
    """
    body = ET.fromstring(data).find(NS + "body")
    if body is None:
        return None
    kids = list(body)
    texts = [text(kid) for kid in kids]
    if not any(t.startswith("Directions:") for t in texts):
        return None
    if not any(t.startswith("Serves:") for t in texts):
        return None

    head = body.find(NS + "h1")
    section = text(head) if head is not None else None

    name = None
    for div in body.findall(NS + "div"):
        if (div.get("class") or "").startswith("heading_"):
            paragraph = div.find(NS + "p")
            if paragraph is not None and text(paragraph):
                name = text(paragraph)

    # the "Ingredients:" label is printed as a lone ":" in part0022 (Canard à la
    # Moutarde); that page is the only one affected
    start = next((i for i, t in enumerate(texts) if t == "Ingredients:"), None)
    if start is None:
        start = next((i for i, t in enumerate(texts) if t == ":"), None)
    if start is None:
        return None
    end = next(i for i, t in enumerate(texts) if t.startswith("Directions:"))
    ingredients = [texts[i] for i in range(start + 1, end)
                   if kids[i].tag == NS + "p" and texts[i]]

    def labelled(prefix):
        return next((t for t in texts if t.startswith(prefix)), "")

    photo = body.find(".//" + NS + "img")
    ordered = body.find(NS + "ol")
    steps = [text(li) for li in ordered.findall(NS + "li")] if ordered is not None else []

    return {
        "name": name,
        "section": section,
        "cook": labelled("Cook Time:")[len("Cook Time:"):].strip(),
        "prep": labelled("Prep Time:")[len("Prep Time:"):].strip(),
        "serves": labelled("Serves:")[len("Serves:"):].strip(),
        "photo": photo.get("src") if photo is not None else None,
        "ingredients": ingredients,
        "steps": steps,
    }


FRACTIONS = {"½": 0.5, "¼": 0.25, "¾": 0.75, "⅓": 1 / 3, "⅔": 2 / 3}
RANGE = re.compile(r"(\d+(?:[.,]\d+)?)\s*[-–]\s*(\d+(?:[.,]\d+)?)\s*(hours?|minutes?|min\.?)", re.I)
GLYPH = re.compile(r"(\d+)\s*([½¼¾⅓⅔])")
DURATION = re.compile(r"(\d+(?:[.,]\d+)?)\s*(hours?|minutes?|min\.?)", re.I)


def minutes(value):
    """Total minutes in a time line.

    A range counts as its lower bound ("4-6 hours" -> 4 hours) and a wait the
    book calls "approximately" (a full day) is left out, matching the magazine
    rule that day/week waits do not belong in ``totalTime``.
    """
    if not value or value.strip().lower() == "none":
        return 0
    value = GLYPH.sub(lambda m: f"{int(m.group(1)) + FRACTIONS[m.group(2)]:g}",
                      value)
    value = RANGE.sub(lambda m: f"{m.group(1)} {m.group(3)}", value)
    total = 0.0
    for match in DURATION.finditer(value):
        before = value[max(0, match.start() - 20):match.start()].lower()
        if "approximat" in before:
            continue
        number = float(match.group(1).replace(",", "."))
        total += number * (60 if match.group(2).lower().startswith("hour") else 1)
    return round(total)


def iso_time(cook, prep):
    """'4-6 hours' + '20 minutes' -> 'PT4H20M'."""
    total = minutes(cook) + minutes(prep)
    if not total:
        return ""
    hours, rest = divmod(total, 60)
    parts = "PT"
    if hours:
        parts += f"{hours}H"
    if rest:
        parts += f"{rest}M"
    return parts


def dutch_yield(serves):
    """'8-10' -> '8-10 personen'; '6 as an appetizer' -> '6 personen (als voorgerecht)'."""
    if not serves:
        return ""
    if re.fullmatch(r"[\d,–\- ]+", serves):
        return f"{serves} personen"
    match = re.match(r"^([\d\-–]+)\s+as an appetizer$", serves, re.I)
    if match:
        return f"{match.group(1)} personen (als voorgerecht)"
    return serves


def image_value(dutch_name):
    """RecipeSage reads a list of photo URLs; its own export uses data URIs."""
    target = pathlib.Path(IMAGE_FOLDER) / image_filename(dutch_name)
    if IMAGE_MODE == "data":
        if not target.exists():
            return None
        encoded = base64.b64encode(target.read_bytes()).decode("ascii")
        return f"data:image/jpeg;base64,{encoded}"
    if IMAGE_MODE == "url":
        if not target.exists() or not BASE_URL:
            return None
        folder = urllib.parse.quote(str(IMAGE_FOLDER))
        file = urllib.parse.quote(image_filename(dutch_name))
        return f"{BASE_URL.rstrip('/')}/{folder}/{file}"
    return f"{IMAGE_FOLDER}/{image_filename(dutch_name)}"


def recipes():
    """-> (all source recipes in book order, the picture bytes per file name)."""
    with zipfile.ZipFile(SRC) as z:
        pages, photos = [], {}
        for href in spine(z):
            if not href.endswith((".xhtml", ".html")):
                continue
            found = parse_part(z.read(href))
            if found is not None:
                pages.append(found)
                if found["photo"]:
                    folder = pathlib.PurePosixPath(href).parent
                    photos[found["photo"]] = z.read(str(folder / found["photo"]))
    return pages, photos


def build():
    """-> (the RecipeSage objects, a per-recipe report line)."""
    pages, photos = recipes()
    out, report, section = [], [], ""
    for page in pages:
        section = page["section"] or section
        english = re.sub(r"\s+", " ", page["name"] or "")
        translate = french_bistro_nl.RECIPES.get(english)
        if translate is None:
            print(f"WARNING: no Dutch translation for {english!r} - "
                  f"using the English text verbatim", file=sys.stderr)
            translate = {"name": english,
                         "ingredients": page["ingredients"],
                         "instructions": page["steps"]}
        name = translate["name"]

        data = {
            "@context": "https://schema.org",
            "@type": "Recipe",
            "name": name,
            "author": {"@type": "Person", "name": AUTHOR},
            "publisher": {"@type": "Organization", "name": BOOK},
            "datePublished": DATE_PUBLISHED,
        }
        yield_value = dutch_yield(page["serves"])
        if yield_value:
            data["recipeYield"] = yield_value
        if page["photo"]:
            pathlib.Path(IMAGE_FOLDER).mkdir(exist_ok=True)
            target = pathlib.Path(IMAGE_FOLDER) / image_filename(name)
            target.write_bytes(photos[page["photo"]])
            value = image_value(name)
            if value:
                data["image"] = [value]
        time_value = iso_time(page["cook"], page["prep"])
        if time_value:
            data["totalTime"] = time_value
        data["recipeCategory"] = [SECTION_NL.get(section, section), BOOK]
        data["recipeIngredient"] = list(translate["ingredients"])
        data["recipeInstructions"] = [{"@type": "HowToStep", "text": step}
                                      for step in translate["instructions"]]
        out.append(data)
        report.append(
            f"{name[:46]:48s} yield={data.get('recipeYield', '-'):28s} "
            f"t={data.get('totalTime', '-'):9s} "
            f"ing={len(data['recipeIngredient']):3d} "
            f"steps={len(data['recipeInstructions']):2d} "
            f"img={'yes' if data.get('image') else 'no'}")
    return out, report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the JSON file")
    parser.add_argument("--dump-en", action="store_true",
                        help="write _en_dump.json with the untranslated source text")
    parser.add_argument("--images", choices=("data", "url", "path"), default=None,
                        help="how the recipe photo is referenced in the JSON")
    parser.add_argument("--base-url", default=None,
                        help="public URL of the images folder (with --images=url)")
    parser.add_argument("--out", type=pathlib.Path, default=None,
                        help="output file, e.g. recipes-french-bistro.json")
    args = parser.parse_args()

    OUT = args.out or OUT
    IMAGE_MODE = args.images or IMAGE_MODE
    BASE_URL = args.base_url if args.base_url is not None else BASE_URL
    if IMAGE_MODE == "url" and not BASE_URL:
        parser.error("--images=url needs --base-url=https://host/folder")

    if args.dump_en:
        source, _ = recipes()
        pathlib.Path("_en_dump.json").write_text(
            json.dumps(source, ensure_ascii=False, indent=2), encoding="utf-8")
        print("wrote _en_dump.json with", len(source), "recipes")
        raise SystemExit

    data, report = build()
    print("\n".join(report))
    print(f"image mode: {IMAGE_MODE}" + (f" ({BASE_URL})" if BASE_URL else ""))
    if args.write:
        OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                       encoding="utf-8")
        print("wrote", OUT, "with", len(data), "recipes")
