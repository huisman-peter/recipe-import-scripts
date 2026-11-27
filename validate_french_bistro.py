"""Structural validation of recipes-french-bistro.json.

    python validate_french_bistro.py [recipes-french-bistro.json]

It checks the delivery of the "French Bistro Cooking" EPUB against the same
RecipeSage conventions the magazine pipeline uses, plus the two things that are
specific to this book: everything must be Dutch and every measure metric.

Exit code is 0 when every check passes, 1 otherwise.
"""
import base64
import io
import json
import pathlib
import re
import sys
import urllib.parse

from PIL import Image

import epub_extract as E

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_files = [a for a in sys.argv[1:] if not a.startswith("--")]
json_path = pathlib.Path(_files[0] if _files else E.OUT)
recipes = json.loads(json_path.read_text(encoding="utf-8"))

TIME = re.compile(r"^PT(?:\d+H)?(?:\d+M)?$")
# every remaining imperial / English measure the book uses
IMPERIAL = re.compile(r"\b(cups?|tablespoons?|teaspoons?|tbsp|tsp|pounds?|lbs?|"
                      r"ounces?|oz|quarts?|pints?|fl oz|inches?|inch|°F)\b", re.I)
# an English word inside a Dutch delivery means a line was not translated;
# Dutch words that double as English ones (pan, water, oven) are left out
ENGLISH = re.compile(r"\b(the|and|with|from|fresh|salt|pepper|minutes?|hours?|"
                     r"cups?|butter|flour|cheese|cream|olive|olives|eggs?|"
                     r"sugar|watercress|onion|garlic|celery|carrot)\b", re.I)
MARKUP = re.compile(r"<[a-z/]|&#|&[a-z]+;")
EXPECTED = len(E.french_bistro_nl.RECIPES)
CATEGORIES = set(E.SECTION_NL.values())

print("recipes:", len(recipes), "| expected:", EXPECTED)
print("size:", round(json_path.stat().st_size / 1024 / 1024, 2), "MB")

# the image mode is read from the file, so the validator always checks what is
# actually in it (a data URI, a public URL, or a path on disk)
sample = next((r["image"][0] for r in recipes if r.get("image")), "")
if sample.startswith("data:image/"):
    MODE = "data"
elif sample.startswith(("http://", "https://")):
    MODE = "url"
else:
    MODE = "path"
print("image mode:", MODE)

problems = []
for r in recipes:
    name = r.get("name", "?")
    issues = []

    for field in ("@context", "@type", "name", "author", "publisher",
                  "datePublished", "recipeYield", "recipeCategory",
                  "recipeIngredient", "recipeInstructions"):
        if not r.get(field):
            issues.append(f"missing {field}")
    if r.get("@type") != "Recipe":
        issues.append("bad @type")
    if r.get("author", {}).get("@type") != "Person":
        issues.append("bad author type")
    if r.get("author", {}).get("name") != E.AUTHOR:
        issues.append(f"author is not {E.AUTHOR!r}")
    if r.get("publisher", {}) != {"@type": "Organization", "name": E.BOOK}:
        issues.append(f"publisher is not {E.BOOK!r}")
    if r.get("datePublished") != E.DATE_PUBLISHED:
        issues.append(f"datePublished is not {E.DATE_PUBLISHED!r}")
    if r.get("totalTime") and not TIME.match(r["totalTime"]):
        issues.append(f"bad totalTime {r['totalTime']}")

    categories = r.get("recipeCategory")
    if (not isinstance(categories, list) or len(categories) != 2
            or not all(isinstance(c, str) and c.strip() for c in categories)):
        issues.append(f"recipeCategory is not a 2-item list: {categories!r}")
    else:
        if categories[0] not in CATEGORIES:
            issues.append(f"unknown category {categories[0]!r}")
        if categories[1] != E.BOOK:
            issues.append(f"book label missing: {categories[1]!r}")

    # the photo: a data URI / a public URL / a path, according to the file
    photo_file = pathlib.Path(E.IMAGE_FOLDER) / E.image_filename(name)
    image = r.get("image")
    if image:
        if not isinstance(image, list) or len(image) != 1:
            issues.append("image is not a one-item list")
        else:
            value = image[0]
            if MODE == "data":
                if not value.startswith("data:image/jpeg;base64,"):
                    issues.append(f"image is not a jpeg data URI: {value[:40]!r}")
                else:
                    try:
                        raw = base64.b64decode(value.split(",", 1)[1], validate=True)
                        with Image.open(io.BytesIO(raw)) as im:
                            im.verify()
                    except Exception as error:
                        issues.append(f"image does not decode: {error}")
            elif MODE == "url":
                if not value.startswith(("http://", "https://")):
                    issues.append(f"image is not a URL: {value!r}")
                elif not urllib.parse.unquote(value).endswith(E.image_filename(name)):
                    issues.append(f"image URL points at another file: {value!r}")
            else:
                if value != f"{E.IMAGE_FOLDER}/{E.image_filename(name)}":
                    issues.append(f"image path mismatch: {value!r}")
        if MODE != "url" and not photo_file.exists():
            issues.append(f"no file {photo_file} for the embedded photo")
    elif MODE != "url" and photo_file.exists():
        issues.append(f"{photo_file} exists but the recipe has no image")

    for ingredient in r.get("recipeIngredient", []):
        for label, pattern in (("imperial unit", IMPERIAL), ("English word", ENGLISH),
                               ("markup", MARKUP)):
            if pattern.search(ingredient):
                issues.append(f"{label} in ingredient: {ingredient}")
        if not ingredient.strip() or ingredient != ingredient.strip() or "  " in ingredient:
            issues.append(f"whitespace: {ingredient!r}")
        if len(ingredient) > 120:
            issues.append(f"suspicious ingredient: {ingredient}")
    for step in r.get("recipeInstructions", []):
        if step.get("@type") != "HowToStep" or not step.get("text"):
            issues.append("bad step")
            continue
        text = step["text"]
        for label, pattern in (("imperial unit", IMPERIAL), ("English word", ENGLISH),
                               ("markup", MARKUP)):
            if pattern.search(text):
                issues.append(f"{label} in step: {text[:60]}")
        if re.match(r"^\d+\s", text):
            issues.append(f"step keeps its number: {text[:40]}")
        if text != text.strip() or "  " in text:
            issues.append(f"whitespace in step: {text[:40]!r}")

    if issues:
        problems.append((name, issues))


# the ingredients and steps must be exactly the curated Dutch text
translated = set()
for entry in E.french_bistro_nl.RECIPES.values():
    translated.update(entry["ingredients"])
    translated.update(entry["instructions"])
invented = [(r["name"], t) for r in recipes
            for t in (list(r.get("recipeIngredient", []))
                      + [s["text"] for s in r.get("recipeInstructions", [])])
            if t not in translated]

print()
per_section, per_author, with_photo, without = {}, {}, 0, []
for r in recipes:
    per_section[r["recipeCategory"][0]] = per_section.get(r["recipeCategory"][0], 0) + 1
    per_author[r["author"]["name"]] = per_author.get(r["author"]["name"], 0) + 1
    if r.get("image"):
        with_photo += 1
    else:
        without.append(r["name"])

for section, count in sorted(per_section.items(), key=lambda kv: -kv[1]):
    print(f"  {count:2d}  {section}")
print("per author:", per_author)
print(f"photos: {with_photo} of {len(recipes)}")
for name in without:
    print(f"  no photo: {name}")

count_problems = sum(len(issues) for _, issues in problems)
for name, issues in problems:
    for issue in issues:
        print(f"  PROBLEM  {name}: {issue}")
print()
print(f"recipes: {len(recipes)} | problem entries: {len(problems)} | "
      f"problems: {count_problems} | invented texts: {len(invented)}")
if len(recipes) != EXPECTED:
    print(f"  PROBLEM: expected {EXPECTED} recipes, found {len(recipes)}")
for name, text in invented[:5]:
    print(f"  PROBLEM  {name}: not from the Dutch source: {text[:60]}")
sys.exit(1 if problems or invented or len(recipes) != EXPECTED else 0)

