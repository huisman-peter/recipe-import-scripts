"""Turn the EPUB "The Ultimate Belgian Cookbook" (Bodic Slavka) into
RecipeSage JSON-LD.

This is the fourth, self-contained pipeline next to the Koken & genieten magazine
one (convert_pdf.py -> add_images.py -> extract.py) and the EPUB ones for
"French Bistro Cooking" (epub_extract.py) and "The Ultimate Indonesian Cookbook"
(indonesian_extract.py).  It shares the layout logic of the Indonesian pipeline -
same publisher, same EPUB template - and starts from an EPUB, so no
PDF/Markdown step is needed.

The source book is English and uses US measures; the delivery is Dutch with
metric units.  The structure (order, section, yield, times, nutrition, photo) is
read from the EPUB, while the recipe text comes from ``belgian_nl.py``, the
hand-made Dutch translation of all 111 recipes::

    python belgian_extract.py                 # dry run: nothing is written
    python belgian_extract.py --dump-en       # write _be_en_dump.json
    python belgian_extract.py --write         # images + recipes-belgian.json

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

import belgian_nl

SRC = pathlib.Path("The Ultimate Belgian Cookbook_ 111 Dishes From Belgium "
                   "To Cook Right Now by Bodic Slavka.epub")
OUT = pathlib.Path("recipes-belgian.json")
IMAGE_FOLDER = pathlib.Path("images-belgian")
IMAGE_MODE = "data"           # "data" = base64 data URI | "url" | "path"
BASE_URL = ""

# book metadata (OPF: dc:creator "Bodic, Slavka", dc:date 2023-04-07)
BOOK = "The Ultimate Belgian Cookbook"
AUTHOR = "Slavka Bodic"
DATE_PUBLISHED = "2023-04"

NS = "{http://www.w3.org/1999/xhtml}"
OPF = "{http://www.idpf.org/2007/opf}"

# the seven section titles printed in the book -> Dutch categories
SECTION_NL = {
    "Breakfast": "Ontbijt",
    "Appetizers and Snacks": "Voorgerechten en snacks",
    "Salads and Side Dishes": "Salades en bijgerechten",
    "Soups and Stews": "Soepen en stoofschotels",
    "Main Dishes": "Hoofdgerechten",
    "Desserts": "Zoet & desserts",
    "Drinks": "Dranken",
}


def text(element):
    """All visible text of an element, whitespace collapsed."""
    return re.sub(r"\s+", " ", "".join(element.itertext())).strip()


def image_filename(name):
    """The photo's file name: lowercase, whitespace -> '-', brackets dropped.

    Same rule as extract.image_filename / epub_extract.image_filename so all
    pipelines name their photos alike.
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


# a recipe page always prints these three labels; nothing else in the book does
PREP_LABEL = "Preparation time:"
COOK_LABEL = "Cook time:"
SERVES = re.compile(r"Ingredients?\s*\(\s*(\d+(?:\s*[-–]\s*\d+)?)\s*servings?\s*\)", re.I)
CALORIES = re.compile(r"(\d+(?:[.,]\d+)?)\s*Cal\b", re.I)
FAT = re.compile(r"(\d+(?:[.,]\d+)?)\s*g?\s*fat", re.I)
PROTEIN = re.compile(r"(\d+(?:[.,]\d+)?)\s*g?\s*protein", re.I)
FIBER = re.compile(r"(\d+(?:[.,]\d+)?)\s*g?\s*fiber", re.I)


def nutrition_value(lines):
    """'381 Cal (6g fat, 3g protein, 1g fiber)' -> a NutritionInformation dict.

    The book is sloppy about this line: sometimes a macro has no number at all
    ("23.8g fat, protein, fiber") or drops the unit ("33 protein"), so each macro
    is matched on its own and only the ones with a value are kept.
    """
    if not CALORIES.search(lines):
        return None
    value = {
        "@type": "NutritionInformation",
        "calories": f"{CALORIES.search(lines).group(1).replace(',', '.')} kcal",
    }
    for key, pattern in (("fatContent", FAT), ("proteinContent", PROTEIN),
                         ("fiberContent", FIBER)):
        found = pattern.search(lines)
        if found:
            value[key] = f"{found.group(1).replace(',', '.')} g"
    return value


def parse_part(data, section):
    """-> the source fields of one recipe page, or None if it is not a recipe.

    Every recipe prints ``Preparation time:`` and an ``Ingredients (N
    servings)`` label; nothing else in the book does, so those two identify a
    recipe page and skip the table of contents and the section pages.
    """
    body = ET.fromstring(data).find(NS + "body")
    if body is None:
        return None
    head = body.find(NS + "h1")
    if head is not None and text(head):
        section = text(head)
    h2 = body.find(NS + "h2")
    if h2 is None:
        return None
    kids = list(body)
    texts = [text(kid) for kid in kids]

    def labelled(prefix):
        return next((t for t in texts if t.startswith(prefix)), "")

    if not labelled(PREP_LABEL):
        return None
    start = next((i for i, t in enumerate(texts) if SERVES.match(t)), None)
    # the section pages repeat the recipe title, so also require the method
    stop = next((i for i, t in enumerate(texts)
                 if t in ("Preparation", "Preparations")), None)
    if start is None or stop is None or stop <= start:
        return None

    # the one-line blurb sits right above the "Ingredients" label
    description = ""
    for i in range(start - 1, -1, -1):
        if not texts[i]:
            continue
        if texts[i].startswith((PREP_LABEL, COOK_LABEL, "Nutrition facts")):
            break
        description = texts[i]
        break

    photo = body.find(".//" + NS + "img")
    ingredients = [texts[i] for i in range(start + 1, stop)
                   if kids[i].tag == NS + "p" and texts[i]]
    steps = [texts[i] for i in range(stop + 1, len(kids))
             if kids[i].tag == NS + "p" and texts[i]]
    serves = SERVES.search(texts[start]).group(1)
    return {
        "name": text(h2),
        "section": section,
        "prep": labelled(PREP_LABEL)[len(PREP_LABEL):].strip(),
        "cook": labelled(COOK_LABEL)[len(COOK_LABEL):].strip(),
        "serves": serves,
        "nutrition": nutrition_value(" ".join(texts)),
        "description": description,
        "photo": photo.get("src") if photo is not None else None,
        "ingredients": ingredients,
        "steps": steps,
    }


FRACTIONS = {"½": 0.5, "¼": 0.25, "¾": 0.75, "⅓": 1 / 3, "⅔": 2 / 3}
RANGE = re.compile(r"(\d+(?:[.,]\d+)?)\s*[-–]\s*(\d+(?:[.,]\d+)?)\s*"
                   r"(hours?|minutes?|min\.?)", re.I)
GLYPH = re.compile(r"(\d+)\s*([½¼¾⅓⅔])")
DURATION = re.compile(r"(\d+(?:[.,]\d+)?)\s*(hours?|minutes?|min\.?)", re.I)


def minutes(value):
    """Total minutes in a time line.

    A range counts as its lower bound ("4-6 hours" -> 4 hours) and a wait the
    book calls "approximately" is left out, matching the magazine rule that
    day/week waits do not belong in ``totalTime``.
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
    """'20 minutes' + '15 minutes' -> 'PT35M'."""
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
    """'8' -> '8 personen'; '1' -> '1 persoon'."""
    if not serves:
        return ""
    return f"{serves} persoon" if serves.strip() == "1" else f"{serves} personen"


# the book's own images that are not recipe photos: the cover and the three
# intro/promotional photographs.  The cover doubles as the fallback photo for the
# recipes the book leaves unillustrated (only 4 of the 111 have a photo of their own).
FLAT_IMAGES = {
    "image_rsrc3A7.jpg": "omslag.jpg",
    "image_rsrc3A8.jpg": "inleiding.jpg",
    "image_rsrc3A9.jpg": "waarom-belgische-keuken.jpg",
    "image_rsrc3AA.jpg": "belgie.jpg",
}
COVER_FILE = "omslag.jpg"


def image_value(file):
    """RecipeSage reads a list of photo URLs; its own export uses data URIs."""
    target = pathlib.Path(IMAGE_FOLDER) / file
    if IMAGE_MODE == "data":
        if not target.exists():
            return None
        encoded = base64.b64encode(target.read_bytes()).decode("ascii")
        return f"data:image/jpeg;base64,{encoded}"
    if IMAGE_MODE == "url":
        if not target.exists() or not BASE_URL:
            return None
        folder = urllib.parse.quote(str(IMAGE_FOLDER))
        return f"{BASE_URL.rstrip('/')}/{folder}/{urllib.parse.quote(file)}"
    return f"{IMAGE_FOLDER}/{file}"


def recipes():
    """-> (all source recipes in book order, the recipe-picture bytes per source
    file name, the book's flat images {output file name: bytes})."""
    with zipfile.ZipFile(SRC) as z:
        pages, photos, section = [], {}, ""
        for href in spine(z):
            if not href.endswith((".xhtml", ".html")):
                continue
            found = parse_part(z.read(href), section)
            if found is None:
                continue
            section = found["section"] or section
            pages.append(found)
            if found["photo"]:
                folder = pathlib.PurePosixPath(href).parent
                photos[found["photo"]] = z.read(str(folder / found["photo"]))
        flat = {FLAT_IMAGES[pathlib.PurePosixPath(name).name]: z.read(name)
                for name in z.namelist()
                if pathlib.PurePosixPath(name).name in FLAT_IMAGES}
    return pages, photos, flat


def build():
    """-> (the RecipeSage objects, a per-recipe report line)."""
    pages, photos, flat = recipes()
    pathlib.Path(IMAGE_FOLDER).mkdir(exist_ok=True)
    for file, blob in flat.items():
        (pathlib.Path(IMAGE_FOLDER) / file).write_bytes(blob)
    out, report, section = [], [], ""
    for page in pages:
        section = page["section"] or section
        english = re.sub(r"\s+", " ", page["name"] or "")
        translate = belgian_nl.RECIPES.get(english)
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
        # the book only illustrates a handful of recipes; the rest fall back to
        # the cover, so every recipe still gets one image
        if page["photo"]:
            file = image_filename(name)
            (pathlib.Path(IMAGE_FOLDER) / file).write_bytes(photos[page["photo"]])
        else:
            file = COVER_FILE
        value = image_value(file)
        if value:
            data["image"] = [value]
        time_value = iso_time(page["cook"], page["prep"])
        if time_value:
            data["totalTime"] = time_value
        if page["nutrition"]:
            data["nutrition"] = page["nutrition"]
        data["recipeCategory"] = [SECTION_NL.get(section, section), BOOK]
        data["recipeIngredient"] = list(translate["ingredients"])
        data["recipeInstructions"] = [{"@type": "HowToStep", "text": step}
                                      for step in translate["instructions"]]
        out.append(data)
        report.append(
            f"{name[:46]:48s} yield={data.get('recipeYield', '-'):12s} "
            f"t={data.get('totalTime', '-'):9s} "
            f"ing={len(data['recipeIngredient']):3d} "
            f"steps={len(data['recipeInstructions']):2d} "
            f"img={'yes' if data.get('image') else 'no'}")
    return out, report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the JSON file")
    parser.add_argument("--dump-en", action="store_true",
                        help="write _id_en_dump.json with the untranslated source")
    parser.add_argument("--images", choices=("data", "url", "path"), default=None,
                        help="how the recipe photo is referenced in the JSON")
    parser.add_argument("--base-url", default=None,
                        help="public URL of the images folder (with --images=url)")
    parser.add_argument("--out", type=pathlib.Path, default=None,
                        help="output file, e.g. recipes-belgian.json")
    args = parser.parse_args()

    OUT = args.out or OUT
    IMAGE_MODE = args.images or IMAGE_MODE
    BASE_URL = args.base_url if args.base_url is not None else BASE_URL
    if IMAGE_MODE == "url" and not BASE_URL:
        parser.error("--images=url needs --base-url=https://host/folder")

    if args.dump_en:
        source, _, _ = recipes()
        pathlib.Path("_be_en_dump.json").write_text(
            json.dumps(source, ensure_ascii=False, indent=2), encoding="utf-8")
        print("wrote _be_en_dump.json with", len(source), "recipes")
        raise SystemExit

    data, report = build()
    print("\n".join(report))
    print(f"image mode: {IMAGE_MODE}" + (f" ({BASE_URL})" if BASE_URL else ""))
    if args.write:
        OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                       encoding="utf-8")
        print("wrote", OUT, "with", len(data), "recipes")
