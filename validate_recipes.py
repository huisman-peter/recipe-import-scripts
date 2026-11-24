"""Structural validation of recipes.json."""
import base64
import io
import json
import pathlib
import re
import sys
import urllib.parse

from PIL import Image

import extract as E

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# --issue=2511 checks that issue instead of the built-in 2510
_issue = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--issue=")), "2510")
if _issue != "2510":
    E.load_issue(_issue)
_files = [a for a in sys.argv[1:] if not a.startswith("--")]

EQUIPMENT = ("bakpapier", "aluminiumfolie", "vershoudfolie", "springvorm", "steker",
             "spiesen", "spuitzak", "uitsteker", "stervormig", "(24 cm)", "(26 cm",
             "stervormig spuitmondje")
TIME = re.compile(r"^PT(?:\d+H)?(?:\d+M)?$")

json_path = pathlib.Path(_files[0] if _files else "recipes.json")
recipes = json.load(open(json_path, encoding="utf-8"))

# the image mode is read from the file, so the validator always checks what is
# actually in it
sample = next((r["image"][0] for r in recipes if r.get("image")), "")
if sample.startswith("data:image/"):
    MODE = "data"
elif sample.startswith(("http://", "https://")):
    MODE = "url"
else:
    MODE = "path"

size_mb = json_path.stat().st_size / 1024 / 1024
print("recipes:", len(recipes), "| image mode:", MODE)
print("size:", round(size_mb, 2), "MB")
if size_mb > 6:
    print(f"  WARNING: {json_path} is larger than 6 MB ({size_mb:.1f} MB)")

problems = 0
for r in recipes:
    name = r["name"]
    issues = []
    for field in ("@context", "@type", "name", "author", "publisher",
                  "recipeYield", "recipeCategory",
                  "recipeIngredient", "recipeInstructions"):
        if field not in r or not r[field]:
            issues.append(f"missing {field}")
    if r.get("@type") != "Recipe":
        issues.append("bad @type")
    if r.get("author", {}).get("@type") != "Person":
        issues.append("bad author type")
    if r.get("publisher", {}).get("@type") != "Organization":
        issues.append("bad publisher type")
    if r.get("publisher", {}).get("name") != E.PUBLISHER:
        issues.append(f"publisher is not the current issue: "
                      f"{r.get('publisher', {}).get('name')!r} != {E.PUBLISHER!r}")
    if E.ISSUE_DATE and r.get("datePublished") != E.ISSUE_DATE:
        issues.append(f"datePublished is not {E.ISSUE_DATE}: "
                      f"{r.get('datePublished')!r}")
    if r.get("totalTime") and not TIME.match(r["totalTime"]):
        issues.append(f"bad totalTime {r['totalTime']}")

    # a single category, wrapped in a list (that is what RecipeSage expects)
    if not isinstance(r.get("recipeCategory"), list) or not all(
            isinstance(c, str) and c.strip() for c in r.get("recipeCategory", [])):
        issues.append(f"recipeCategory is not a list of strings: {r.get('recipeCategory')!r}")

    # the photo: a list with one base64 JPEG data URI.  A recipe whose photo is
    # not on the contents pages simply has no image, and that is not an error.
    photo_file = pathlib.Path(E.IMAGE_FOLDER) / E.image_filename(name)
    image = r.get("image")
    if not isinstance(image, list) or not image:
        if photo_file.exists():
            issues.append(f"image is missing while {photo_file} exists")
    else:
        if not all(isinstance(v, str) and v.strip() for v in image):
            issues.append("image contains non-strings")
        for value in image:
            if MODE == "data":
                if not value.startswith("data:image/jpeg;base64,"):
                    issues.append(f"image is not a jpeg data URI: {value[:40]!r}")
                    continue
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
                elif not pathlib.Path(value).exists():
                    issues.append(f"image file missing: {value!r}")

    for ingredient in r["recipeIngredient"]:
        if any(word in ingredient.lower() for word in EQUIPMENT):
            issues.append(f"equipment as ingredient: {ingredient}")
        if "](" in ingredient or ingredient.startswith("!["):
            issues.append(f"markdown link as ingredient: {ingredient}")
        if len(ingredient) > 120:
            issues.append(f"suspicious ingredient: {ingredient}")
        if ingredient != ingredient.strip() or "  " in ingredient:
            issues.append(f"whitespace: {ingredient!r}")
    for step in r["recipeInstructions"]:
        if step.get("@type") != "HowToStep" or not step.get("text"):
            issues.append("bad step")
        elif re.match(r"^\d+\s", step["text"]):
            issues.append(f"step keeps its number: {step['text'][:40]}")
    if "nutrition" in r:
        n = r["nutrition"]
        if n.get("@type") != "NutritionInformation":
            issues.append("bad nutrition type")
        for key in ("calories", "proteinContent", "fatContent", "carbohydrateContent"):
            if key not in n:
                issues.append(f"missing {key}")
            elif not re.fullmatch(r"\d+( kcal| g)", n[key]):
                issues.append(f"bad {key}: {n[key]}")
    if issues:
        problems += 1
        print(f"  {name}")
        for issue in issues:
            print(f"      - {issue}")

print("recipes with problems:", problems)

# --- compatibility smoke test -------------------------------------------
# these are the keys an importer dereferences directly (name, recipeYield,
# recipeIngredient, recipeInstructions[].text, image[0] and the
# recipeCategory list), so they must always be present
shape = []
for r in recipes:
    fields = ["name", "recipeYield", "recipeIngredient",
              "recipeInstructions", "recipeCategory"]
    if r.get("image") or (pathlib.Path(E.IMAGE_FOLDER)
                          / E.image_filename(r["name"])).exists():
        fields.append("image")
    for field in fields:
        if not r.get(field):
            shape.append((r.get("name"), f"no {field}"))
    for step in r.get("recipeInstructions", []):
        if "text" not in step:
            shape.append((r.get("name"), "step without text"))
print("import-shape problems:", len(shape), shape[:4])
