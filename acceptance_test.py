"""End-to-end acceptance test for the KG2510 delivery.

    python acceptance_test.py

It checks the whole chain in one go:

  A. KG2510.md   - markup hygiene and the 54 photo links
  B. text intact - the Markdown holds exactly the words pdftotext finds
  C. images/     - 54 valid JPEGs, each named after its own recipe
  D. recipes.json - structure, issue metadata, decodable photos and texts
                    that really come from the Markdown

Exit code is 0 when every check passes, 1 otherwise.
"""
import base64
import collections
import io
import json
import pathlib
import re
import ssl
import sys
import urllib.error
import urllib.request

import fitz
from PIL import Image

import convert_pdf as C
import extract as E

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# --issue=2511 checks that issue instead of the built-in 2510
_issue = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--issue=")), "2510")
if _issue != "2510":
    _config = E.load_issue(_issue)
    C.SRC = pathlib.Path(_config.PDF)
_files = [a for a in sys.argv[1:] if not a.startswith("--")]

WORD = re.compile(r"[0-9A-Za-zÀ-ÿ][0-9A-Za-zÀ-ÿ'’]*")
LINK = re.compile(r"^!\[([^\]]+)\]\(([^)]+)\)$", re.M)
fails = []


def check(label, ok, detail=""):
    print(f"  {'OK  ' if ok else 'FAIL'}  {label}{'  ' + str(detail) if detail else ''}")
    if not ok:
        fails.append(label)


def fetch_image(url):
    """(status, content-type) of an image URL.

    Falls back to an unverified TLS context when the machine has no CA store
    configured, so the test measures the URL and not the local setup.
    """
    def get(context):
        with urllib.request.urlopen(url, timeout=15, context=context) as response:
            return response.status, response.headers.get("Content-Type", "")

    try:
        return get(ssl.create_default_context())
    except urllib.error.URLError as error:
        if isinstance(error.reason, ssl.SSLCertVerificationError):
            return get(ssl._create_unverified_context())
        raise


md = E.MD.read_text(encoding="utf-8")
json_file = pathlib.Path(_files[0] if _files else E.OUT)
recipes = json.loads(json_file.read_text(encoding="utf-8"))
EXPECTED = len(E.RECIPE_TABLE)

# the image mode is read from the file itself
sample = next((r["image"][0] for r in recipes if r.get("image")), "")
if sample.startswith("data:image/"):
    MODE = "data"
elif sample.startswith(("http://", "https://")):
    MODE = "url"
else:
    MODE = "path"
print(f"checking {json_file}  (image mode: {MODE})")

print("A. Markdown")
links = LINK.findall(md)
photos_on_disk = sorted(pathlib.Path(E.IMAGE_FOLDER).glob("*.jpg"))
check("one photo link per photo on disk",
      len(links) == len(photos_on_disk),
      f"{len(links)} links, {len(photos_on_disk)} photos")
check("every linked photo exists",
      all(pathlib.Path(target).exists() for _, target in links))
check("no soft hyphens", "\u00ad" not in md)
check("no double spaces", "  " not in md)
# a word broken by the ligature handling reads "<fragment>ffi <rest>"
# ("koffi e"); the joined form has to occur in the PDF text as well, otherwise
# it is ordinary prose such as "… campari Amalfi met de grapefruitpartjes"
pages = C.raw_pages()
pdf_words = {E.key(word) for word in WORD.findall("\n".join(pages))}
artefacts = [match.group(0)
             for match in re.finditer(r"\S*(?:ffi|ffl|fi|fl|ff) [a-z]\S*", md)
             if E.key(match.group(0).replace(" ", "")) in pdf_words]
check("no ligature artefacts", not artefacts, artefacts[:3])

print("B. text intact")
doc = fitz.open(C.SRC)
body = "\n".join(line for line in md.split("\n")
                 if not line.startswith("!["))
reference = "\n".join(line for number, text in enumerate(pages)
                      for line in text.split("\n")
                      if line.strip() and not C.is_noise(line.strip(), number + 1))


def letters(text):
    return collections.Counter(E.key(text))


# order-insensitive: one lost or duplicated letter changes the counts, while
# the deliberate column reordering of the cover and contents pages does not
extra = letters(body) - letters(reference)
missing = letters(reference) - letters(body)
check("no letter lost or duplicated between PDF and Markdown",
      not extra and not missing,
      {"only in Markdown": dict(list(extra.items())[:6]),
       "only in PDF": dict(list(missing.items())[:6])})


def counted(texts):
    """Letters, not words: the extractor re-spaces a few lines where pdftotext
    lost them, which would show up as a word difference but not as a letter one."""
    return collections.Counter(ch for text in texts for ch in E.key(text))


# page by page, so text that ended up on the wrong page shows up too
wrong = []
for number in range(doc.page_count):
    produced = [text for text in C.page_entries(doc, number, pages[number],
                                                number + 1)
                if not C.is_noise(text, number + 1)]
    original = [line.strip() for line in pages[number].split("\n")
                if line.strip() and not C.is_noise(line.strip(), number + 1)]
    if counted(produced) != counted(original):
        wrong.append(number + 1)
check("every page holds exactly its own PDF text", not wrong, wrong[:6])

print("C. images/")
photos = sorted(pathlib.Path(E.IMAGE_FOLDER).glob("*.jpg"))
print(f"       {len(photos)} photos for {EXPECTED} recipes")
broken = []
for photo in photos:
    try:
        with Image.open(photo) as image:
            image.verify()
    except Exception as error:
        broken.append(f"{photo.name}: {error}")
check("every photo on disk is a valid JPEG", not broken, broken[:2])
known = {E.image_filename(row[1]) for row in E.RECIPE_TABLE}
strange = [photo.name for photo in photos if photo.name not in known]
check("every photo is named after a recipe", not strange, strange[:3])

print("D. recipes.json")
check("is a JSON array", isinstance(recipes, list))
check(f"{EXPECTED} recipes", len(recipes) == EXPECTED, f"({len(recipes)})")
required = ("@context", "@type", "name", "author", "publisher", "recipeYield",
            "recipeCategory", "recipeIngredient", "recipeInstructions",
            "datePublished")
check("all recipe fields present",
      all(all(r.get(field) for field in required) for r in recipes))
# not every recipe has a photo on the contents pages; those simply have no image
without = [r["name"] for r in recipes
           if not r.get("image")
           and (pathlib.Path(E.IMAGE_FOLDER) / E.image_filename(r["name"])).exists()]
check("every recipe with a photo file has it embedded", not without, without[:3])
no_photo = [r["name"] for r in recipes if not r.get("image")]
if no_photo:
    print(f"       (no photo on the contents pages for {len(no_photo)} recipes)")
no_time = [r["name"] for r in recipes if "totalTime" not in r]
check("totalTime present unless the magazine gives no time",
      no_time == ["Ingelegde jalapeño’s"] or not no_time, no_time)
check(f"publisher carries the issue ({E.PUBLISHER})",
      all(r["publisher"]["name"] == E.PUBLISHER for r in recipes))
check(f"datePublished carries the issue ({E.ISSUE_DATE})",
      all(r["datePublished"] == E.ISSUE_DATE for r in recipes))
check("recipeCategory is a list", all(isinstance(r["recipeCategory"], list)
                                      and r["recipeCategory"] for r in recipes))
if E.ISSUE_AS_LABEL:
    no_label = [r["name"] for r in recipes
                if E.PUBLISHER not in r["recipeCategory"]]
    check(f"issue label present ({E.PUBLISHER})", not no_label, no_label[:3])

broken = []
for recipe in recipes:
    if not recipe.get("image"):
        continue          # no photo on the contents pages for this one
    value = recipe["image"][0]
    try:
        if MODE == "data":
            raw = base64.b64decode(value.split(",", 1)[1], validate=True)
            with Image.open(io.BytesIO(raw)) as image:
                image.verify()
        elif MODE == "url":
            status, kind = fetch_image(value)
            if status != 200:
                raise OSError(f"HTTP {status}")
            if not kind.startswith("image/"):
                raise OSError(f"Content-Type {kind!r}")
        else:
            with Image.open(value) as image:
                image.verify()
    except Exception as error:
        broken.append(f"{recipe['name']}: {error}")
what = {"data": "decodable JPEG data URI",
        "url": "reachable image URL over http(s)",
        "path": "readable JPEG file"}[MODE]
check(f"every photo is a {what}", not broken, broken[:2])

# column labels that the extractor drops ("Uit Paulines Keuken", "Seizoen", …)
# interrupt a step in the Markdown, so they are removed here as well
source_lines = [line for line in md.split("\n")
                if not line.startswith("![")
                and line.strip() not in E.NOISE]
source = E.key(" ".join(source_lines))
overridden = set(E.OVERRIDES)
skipped, invented = 0, []
for recipe in recipes:
    texts = list(recipe["recipeIngredient"])
    texts += [step["text"] for step in recipe["recipeInstructions"]]
    if recipe["name"] in overridden:
        skipped += len(texts)
        continue
    for text in texts:
        if E.key(text) not in source:
            invented.append(f"{recipe['name']}: {text[:40]}")
check("ingredients/steps are verbatim from the Markdown",
      not invented, invented[:3])
print(f"       ({skipped} texts in {len(overridden)} hand-corrected recipes "
      f"were not checked verbatim)")

print()
print(f"FAILED CHECKS: {len(fails)} " + (", ".join(fails) if fails else "-"))
sys.exit(1 if fails else 0)

