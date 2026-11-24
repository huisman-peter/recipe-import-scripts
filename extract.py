"""Turn the KG2510.md Markdown into RecipeSage-ready Schema.org JSON-LD.

The magazine's recipes are delimited by the ``## `` headings in KG2510.md; the
list below says where each recipe starts and what metadata the magazine gives
for it.  The ingredient list and the steps are read straight from the Markdown
so the texts stay verbatim.

The issue the recipes come from is in ``ISSUE`` at the top of this file: it ends
up in ``publisher.name`` ("Koken & genieten 10-2025") and, as ``datePublished``,
in every recipe - so recipes from different issues stay distinguishable.  For
the next magazine only ``ISSUE`` has to change.

Every recipe also gets an ``image``: the contents-page photo that
``add_images.py`` saved under the recipe's own name.  Run the pipeline in this
order, because those photos are embedded from ``images/``:

    python convert_pdf.py      # PDF -> KG2510.md
    python add_images.py       # PDF -> images/*.jpg (+ links in KG2510.md)
    python extract.py --write  # MD  -> recipes.json
"""
import base64
import importlib
import json
import pathlib
import re
import sys

MD = pathlib.Path("KG2510.md")
OUT = pathlib.Path("recipes.json")

# Which magazine issue this file covers.  For the next issue only these two
# lines need changing - the publisher name, the publication date and the
# validator all follow from them.
ISSUE = "10-2025"                                     # as printed on the cover
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "-".join(reversed(ISSUE.split("-"))) if ISSUE else ""   # 2025-10

# how the recipe photo is put into the JSON
IMAGE_FOLDER = "images"
IMAGE_MODE = "data"     # "data" = base64 data URI | "url" = public URL | "path"
BASE_URL = ""           # only used when IMAGE_MODE == "url"

# RecipeSage ignores "publisher" but turns "recipeCategory" into labels, so the
# issue goes in there as well - that is the only way recipes from different
# issues stay filterable inside RecipeSage.
ISSUE_AS_LABEL = True

# some tables name a recipe differently from its "## " heading in the Markdown
# (a longer title, or a typo in the magazine); map those here
HEADING_AS = {}

PAULINE = "Uit Paulines Keuken"
WELMOED = "Welmoed Bezoen"
KG = "Koken & genieten"


def image_filename(name):
    """The photo's file name: lowercase, whitespace -> '-' (as asked).

    Brackets are dropped as well: a name like "Sugo (tomatensaus)" would
    otherwise produce a Markdown link whose target the readers of the file
    (and the tests) cannot parse unambiguously.
    """
    slug = re.sub(r"\s+", "-", name.lower())
    return re.sub(r"[()\[\]]+", "", slug) + ".jpg"


def load_issue(name):
    """Switch the issue-specific data to another magazine issue.

    Everything below is KG2510's.  ``issue_2511.py`` (and the next one) holds
    the same names for another issue, so the engine itself never changes:

        python extract.py --issue 2511 --write
    """
    module = importlib.import_module(f"issue_{name}")
    for field in ("ISSUE", "PUBLISHER", "ISSUE_DATE", "MD", "OUT", "PDF",
                  "IMAGE_FOLDER", "IMAGE_MODE", "BASE_URL", "RECIPE_TABLE",
                  "OVERRIDES", "ISSUE_AS_LABEL", "HEADING_AS", "CAPTION_SPLIT"):
        if hasattr(module, field):
            value = getattr(module, field)
            if field in ("MD", "OUT", "PDF") and isinstance(value, str):
                value = pathlib.Path(value)
            globals()[field] = value
    if hasattr(module, "EXTRA_NOISE"):
        globals()["NOISE"] = globals()["NOISE"] | set(module.EXTRA_NOISE)
    return module


def image_value(name):
    """RecipeSage reads a list of photo URLs; its own export uses data URIs."""
    target = pathlib.Path(IMAGE_FOLDER) / image_filename(name)
    if IMAGE_MODE == "data":
        if not target.exists():
            return None
        encoded = base64.b64encode(target.read_bytes()).decode("ascii")
        return f"data:image/jpeg;base64,{encoded}"
    if IMAGE_MODE == "url" and BASE_URL:
        return f"{BASE_URL.rstrip('/')}/{IMAGE_FOLDER}/{image_filename(name)}"
    return f"{IMAGE_FOLDER}/{image_filename(name)}"


# line number of the "## " heading that opens the recipe, its full name, the
# author, the category and (when it needs one) the ISO-8601 total time
RECIPE_TABLE = [
    (307, "Zoete-aardappelgratin met chorizo", PAULINE, "Hoofdgerecht", None),
    (343, "Groentetaart met wortel", PAULINE, "Hoofdgerecht", None),
    (388, "Gochujangnoedels", PAULINE, "Hoofdgerecht", None),
    (432, "Sinaasappeltaart", PAULINE, "Zoet & desserts", "PT1H30M"),
    (472, "Pompoencurry met kip", PAULINE, "Hoofdgerecht", None),
    (522, "Hamburgse aalsoep", KG, "Soep", "PT10H30M"),
    (588, "Russische soljanka", KG, "Soep", None),
    (625, "Erwtensoep met pannenkoeken", KG, "Soep", "PT10H30M"),
    (684, "Goedgevulde pompoensoep", KG, "Soep", None),
    (740, "Aardappelsoep met appelcake", KG, "Soep", None),
    (868, "Lamstajine met couscous", KG, "Hoofdgerecht", None),
    (912, "Geurige muntthee", KG, "Drank", None),
    (925, "Ingelegde citroenen", KG, "Bijgerecht", "PT20M"),
    (947, "Kip-dadelbastilla", KG, "Hoofdgerecht", None),
    (997, "Köfte in pittige tomatensaus", KG, "Hoofdgerecht", None),
    (1054, "Pistachebaklava", KG, "Zoet & desserts", None),
    (1174, "Tiroler pastaschotel", KG, "Hoofdgerecht", None),
    (1208, "Snel zalm-venkelpannetje", KG, "Hoofdgerecht", None),
    (1237, "Krokante kipnuggets met worteltjes", KG, "Hoofdgerecht", None),
    (1267, "Spekmedaillons met bulgursalade", KG, "Hoofdgerecht", None),
    (1301, "Schnitzelspiesjes met Aziatische rijst", KG, "Hoofdgerecht", None),
    (1340, "Groente-broodgratin met feta", KG, "Hoofdgerecht", None),
    (1375, "Fruitige herfstsalade met procureur", KG, "Salade", None),
    (1430, "Griezelige linzensalade", KG, "Salade", "PT1H30M"),
    (1466, "Ovenkalkoen met herfstgroenten", KG, "Hoofdgerecht", None),
    (1511, "Roomkaaspompoen", KG, "Bijgerecht", None),
    (1536, "Groentesticks", KG, "Bijgerecht", None),
    (1548, "Griezelige crackers", KG, "Bijgerecht", None),
    (1574, "Heksenbrouwsel", KG, "Drank", None),
    (1586, "Spookachtige brownietaart", KG, "Zoet & desserts", None),
    (1645, "Savooiekool met kip en appel-yoghurtsaus", KG, "Hoofdgerecht", None),
    (1682, "Kleurrijke herfstsalade met linzen en grapefruit", KG, "Salade", None),
    (1725, "Plaatpannenkoek met appel en noten", KG, "Zoet & desserts", None),
    (1769, "Zelfgemaakte appelchips", KG, "Zoet & desserts", None),
    (1795, "Tagliatelle met pompoen en salieboter", KG, "Hoofdgerecht", None),
    (1821, "Pompoenpuree met spek-uientopping", KG, "Bijgerecht", None),
    (1845, "Romige pompoensoep met gember", KG, "Soep", None),
    (1882, "Geroosterde pompoen en prei met frisse dip", KG, "Bijgerecht", None),
    (1937, "Oesterzwammenshoarma", WELMOED, "Hoofdgerecht", None),
    (1984, "Ingelegde jalapeño’s", WELMOED, "Bijgerecht", None),
    (2002, "Gekaramelliseerde venkel met linzen en appel", WELMOED, "Bijgerecht", None),
    (2051, "Gekonfijte pompoen met tahin en yoghurt", WELMOED, "Bijgerecht", None),
    (2089, "Bietentzatziki", WELMOED, "Bijgerecht", None),
    (2117, "Knolselderijgnocchi met paddenstoelen en hazelnoten", WELMOED, "Hoofdgerecht", None),
    (2212, "Pruimen-port-ijs", KG, "Zoet & desserts", None),
    (2247, "Rijstpudding uit de oven met appelcompote", KG, "Zoet & desserts", None),
    (2289, "Hazelnootschuimgebakjes met chocoladesaus", KG, "Zoet & desserts", None),
    (2337, "Plaatkoek met kweepeer en walnoot", KG, "Zoet & desserts", None),
    (2390, "Shortbreadcheesecake met pecannotenkaramel", KG, "Zoet & desserts", None),
    (2433, "Plukcake met pistache", KG, "Zoet & desserts", None),
    (2483, "Notenvlecht met glazuur", KG, "Zoet & desserts", None),
    (2540, "Hazelnootlaagjestaart met eekhoornkoekjes", KG, "Zoet & desserts", None),
    (2619, "Volkoren appel-notencake", KG, "Zoet & desserts", None),
    (2743, "Bananen-chocoladetulband", KG, "Zoet & desserts", None),
]

# lines that only mark a section or a column and must not become ingredients
NOISE = {
    "Seizoen", "De snelle keuken", "Uit Paulines Keuken", "Kookboek", "Gebak",
    "Buffet", "De gezonde keuken", "Het zoete leven", "4x lekker", "Pronkstuk",
    "Fotografie: Willem van Santen", "Coverrecept", "wachttijd",
    "Receptuur en fotografie: Uit Paulines Keuken",
}

# kitchen kit that is not an ingredient
EQUIPMENT = (
    "aluminiumfolie", "vershoudfolie", "bakpapier", "springvorm", "steker",
    "spiesen", "spuitzak", "spuitmondje", "uitsteker", "stervormig",
)

AMOUNT = r"(?:\d+(?:[,.]\d+)?\s*[-–]\s*\d+(?:[,.]\d+)?|\d*[½¼¾⅓⅔]|\d+(?:[,.]\d+)?)"
UNIT = (r"(?:el|tl|g|kg|ml|cl|dl|l|liter|stuks?|takjes?|takje|blaadjes?|tenen?|teen|"
        r"bosjes?|handjevol|snufjes?|mespuntjes?|mespunt|zakjes?|plakjes?|plakje|"
        r"sneetjes?|snee|blik(?:ken)?|potjes?|pot|punten|eetlepels?|theelepels?)")
BARE_QUANTITY = re.compile(rf"^(?:ca\.\s*)?(?:{AMOUNT})(?:\s+{UNIT})?\.?$")
STEP_WITH_UNIT = re.compile(rf"^(?:{AMOUNT})\s+{UNIT}\s")   # "5 el crème ..."
STEP_START = re.compile(r"^(\d+)\s+(\S+)(.*)$")
NUTRITION = re.compile(r"^(\d+)\s*g\s*eiwit\s*\|\s*(\d+)\s*g\s*vet\s*\|\s*(\d+)\s*g\s*koolhydraten")
CALORIES = re.compile(r"ca\.\s*(\d+)\s*kcal")
YIELD = re.compile(r"^Ingrediënten\s*(?:voor)?\s*:?\s*(?:voor\s*)?(.+)$")
TIME_RE = re.compile(r"(\d+)\s*uur|(\d+)\s*min")


def key(text):
    """Normalised comparison key (case, spaces and punctuation ignored)."""
    return re.sub(r"[^0-9a-z]+", "", text.lower())


def iso_time(text):
    """'ca. 1 uur en 10 min.' -> 'PT1H10M'."""
    hours = minutes = 0
    found = TIME_RE.search(text)
    while found:
        if found.group(1):
            hours += int(found.group(1))
        elif found.group(2):
            minutes += int(found.group(2))
        found = TIME_RE.search(text, found.end())
    parts = "PT"
    if hours:
        parts += f"{hours}H"
    if minutes:
        parts += f"{minutes}M"
    return parts if parts != "PT" else ""


def is_step(line, previous=None):
    """Does this line open a new instruction step?"""
    match = STEP_START.match(line)
    if not match:
        return False
    number, first, rest = match.group(1), match.group(2), match.group(3)
    if not number.isdigit():
        return False
    if previous is None and number != "1":
        return False
    if len(line) > 55 or first.isupper() and len(first) >= 3:
        return True
    return line.endswith(".") and len(rest.split()) > 3


# hand corrections: recipes the generic parser cannot split correctly
OVERRIDES = {
    "Goedgevulde pompoensoep": {
        "fix": {"1 mespunt gemalen": ["1 mespunt gemalen komijn"],
                "6 el crème fraîche (ca. 6 cm Ø)": ["6 el crème fraîche"]},
    },
    "Aardappelsoep met appelcake": {
        "fix": {"2 tl poedersuiker, om te": ["2 tl poedersuiker, om te bestuiven"],
                "bestuiven (24 cm)": []},
    },
    "Köfte in pittige tomatensaus": {
        "fix": {"100 g gedroogde zachte": ["100 g gedroogde zachte abrikozen"],
                "abrikozen": []},
    },
    "Oesterzwammenshoarma": {
        "fix": {"1 snufje versgeraspte": ["1 snufje versgeraspte nootmuskaat"],
                "nootmuskaat": []},
    },
    "Geurige muntthee": {
        "ingredients": ["5-6 takjes munt", "1 l water",
                        "1 el losse groene thee (of 2 theezakjes)", "100 g suiker"],
    },
    "Ingelegde citroenen": {
        "ingredients": ["4-5 bio-citroenen", "1 tl zwarte peperkorrels",
                        "80 g grof zeezout", "5-6 laurierblaadjes",
                        "3 extra citroenen", "60 ml olijfolie"],
    },
    "Groentesticks": {
        "ingredients": ["2 paprika’s (bijvoorbeeld geel en rood)",
                        "2 grote wortels", "2 snackkomkommers"],
    },
    "Heksenbrouwsel": {
        "ingredients": ["8 glazen, elk 3-4 ijsblokjes",
                        "300 ml crème de cassis (zwartebessenlikeur, bij de slijter)",
                        "175 ml wodka (40% alcohol)", "1 l gingerbeer",
                        "8 takjes rozemarijn", "16 bramen"],
    },
    "Bietentzatziki": {
        "instructions": [
            "Roer de yoghurt, mierikswortel, knoflook en het citroenrasp glad. Breng op smaak met het citroensap en wat zout en peper.",
            "Roer de bieten en bijna alle dille er kort maar losjes door, zodat er een gemarmerd effect ontstaat. Giet de olijfolie erover en bestrooi met de overige dille en nog een snufje zout en peper. Serveer met trekbrood of pita.",
        ],
    },
    "Hamburgse aalsoep": {
        "instructions": [
            "EEN DAG VAN TEVOREN Week het gedroogde fruit een nacht in koud water.",
            "DE VOLGENDE DAG Schenk het fruit af. Schil de knolselderij en de wortels. Maak de prei schoon en was de overige groenten. Was ook de schillen en de afsnijdsels. Snijd de knolselderij, de wortels en de prei in stukjes van ca. 1 cm. Dek af met een vochtige doek en houd apart.",
            "Snijd de spareribs in grove stukken en doe ze in een grote pan. Schenk de bouillon erbij. Voeg de kruidnagels, de laurierblaadjes, de peterselie, de groenteschillen en de afsnijdsels toe. Breng alles aan de kook en laat ca. 1 uur en 30 minuten zachtjes koken.",
            "Was de sperziebonen en halveer ze. Schenk de bouillon door een fijne zeef in een tweede pan. Voeg de rest van de soepgroenten, de sperziebonen en het gedroogde fruit toe aan de soep. Breng aan de kook en laat ca. 30 minuten zachtjes koken. Voeg de erwten ca. 5 minuten voor het einde van de gaartijd toe en laat meegaren. Neem het vlees van de ribbetjes, pluk het in kleine stukjes en voeg weer toe aan de soep. Breng de soep op smaak met de azijn, de suiker, de nootmuskaat, zout en peper.",
            "Was de dille en neem de blaadjes van de takjes. Verhit de olie in een pan en bak spiegeleieren van de eieren. Serveer de soep en leg op iedere portie een spiegelei. Garneer met de dille.",
        ],
    },
    "Zelfgemaakte appelchips": {
        "ingredients": ["3 el citroensap", "1,5 l water", "2 appels",
                        "1 tl kaneel", "1 tl chilivlokken"],
        "instructions": [
            "Verwarm de oven voor (hetelucht: 80°C). Meng 3 el citroensap met 1,5 l water. Was 2 appels en verwijder het klokhuis met een appelboor. Schaaf de appels in dunne plakjes en leg ze direct in het citroenwater. Laat de plakjes uitlekken en verdeel ze over twee met bakpapier beklede bakplaten. Droog de appelplakjes 4½-5 uur in de oven.",
            "Klem tijdens het drogen een houten lepel tussen de ovendeur, zodat hij op een kier blijft staan en het vocht kan ontsnappen. Neem de chips uit de oven en bestrooi naar wens met 1 tl kaneel en 1 tl chilivlokken. De chips is in een afgesloten trommel ca. 1 week houdbaar.",
        ],
    },
    "Ingelegde jalapeño’s": {
        "yield": "1 pot van 400 ml",
        "ingredients": ["150 ml appelazijn", "35 g suiker",
                        "½ tl chipotle-chilivlokken", "2 gekneusde tenen knoflook",
                        "100 ml water", "250 g jalapeño’s"],
    },
}


def apply_overrides(data):
    changes = OVERRIDES.get(data["name"])
    if not changes:
        return data
    if "drop" in changes:
        data["recipeIngredient"] = [i for i in data["recipeIngredient"]
                                    if i not in changes["drop"]]
    for old, replacement in changes.get("fix", {}).items():
        try:
            position = data["recipeIngredient"].index(old)
        except ValueError:
            print("OVERRIDE MISMATCH", data["name"], repr(old),
                  data["recipeIngredient"], file=sys.stderr)
            raise
        data["recipeIngredient"][position:position + 1] = replacement
    if "ingredients" in changes:
        data["recipeIngredient"] = changes["ingredients"]
    if "yield" in changes:
        data["recipeYield"] = changes["yield"]
    if "instructions" in changes:
        data["recipeInstructions"] = [{"@type": "HowToStep", "text": text}
                                      for text in changes["instructions"]]
    return data


def build():
    lines = MD.read_text(encoding="utf-8").split("\n")

    # locate the recipes by their "## " heading (the Markdown may have gained
    # image lines since the table was written, so line numbers are unreliable)
    heads = [(i, line[3:].strip()) for i, line in enumerate(lines)
             if line.startswith("## ")]
    starts, cursor = [], 0
    for row in RECIPE_TABLE:
        wanted = key(HEADING_AS.get(row[1], row[1]))
        found = None
        for position in range(cursor, len(heads)):
            index, text = heads[position]
            if key(text) and wanted.startswith(key(text)):
                found = (position, index)
                break
        if found is None:
            found = (cursor, row[0] - 1)          # fall back to the table
        cursor, index = found[0] + 1, found[1]
        starts.append(index)

    recipes, report = [], []

    for position, (_, name, author, category, total_time) in enumerate(RECIPE_TABLE):
        start = starts[position]
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        block = lines[start:end]
        yield_, time_text, ingredients, steps, nutrition = parse_block(block)

        data = {
            "@context": "https://schema.org",
            "@type": "Recipe",
            "name": name,
            "author": {"@type": "Person", "name": author},
            "publisher": {"@type": "Organization", "name": PUBLISHER},
        }
        if ISSUE_DATE:
            data["datePublished"] = ISSUE_DATE
        if yield_:
            data["recipeYield"] = yield_
        photo = image_value(name)
        if photo:
            data["image"] = [photo]
        time_value = total_time or iso_time(time_text or "")
        if time_value:
            data["totalTime"] = time_value
        data["recipeCategory"] = [category] + ([PUBLISHER] if ISSUE_AS_LABEL else [])
        data["recipeIngredient"] = ingredients
        data["recipeInstructions"] = [
            {"@type": "HowToStep", "text": text} for text in steps]
        if nutrition and nutrition[0] is not None or (nutrition and nutrition[1]):
            kcal, macros = nutrition
            entry = {"@type": "NutritionInformation"}
            values = (("calories", kcal, " kcal"),)
            if macros:
                values += (("proteinContent", macros[0], " g"),
                           ("fatContent", macros[1], " g"),
                           ("carbohydrateContent", macros[2], " g"))
            for field, value, unit in values:
                if value is not None:
                    entry[field] = f"{value}{unit}"
            data["nutrition"] = entry
        recipes.append(apply_overrides(data))

        report.append(
            f"{name[:44]:46s} yield={str(yield_):16s} t={data.get('totalTime', '-'):9s} "
            f"ing={len(ingredients):3d} steps={len(steps):d} nut={bool(nutrition)}")
    return recipes, report


def looks_like_ingredient(line):
    match = re.match(rf"^(?:{AMOUNT})(?:\s+{UNIT})?\s+(.*)$", line)
    if not match:
        return False
    return len(line) <= 60 and len(match.group(1).split()) <= 6


def is_continuation(previous, line):
    """Is this line the wrapped tail of the previous ingredient?"""
    if not previous:
        return False
    if previous.count("(") > previous.count(")"):
        return True
    if line[0] in "()":
        return True
    return previous.endswith((",", " à", " of", " bijv.", " met", " en", " van",
                              " voor", " tot", "/"))


def parse_block(lines):
    """Split a recipe's Markdown lines into yield, time, ingredients, steps."""
    yield_, time_text, kcal, macros = None, None, None, None
    content = []
    consumed = set()
    for index, raw in enumerate(lines):
        if index in consumed:
            continue
        line = raw.strip()
        if not line or line in NOISE or line.startswith(("##", "![")):
            continue
        if line.startswith("# "):
            break                       # a new section starts
        plain = line.replace("**", "")
        if plain.startswith("Ingrediënten"):
            match = YIELD.match(plain)
            if match:
                yield_ = match.group(1).strip()
            content.append(("<label>", plain))
            continue
        if plain.startswith("Bereidingstijd"):
            time_text = plain.split(":", 1)[-1].strip().strip("·")
            following = next(((number, ln.strip())
                              for number, ln in enumerate(lines[index + 1:], index + 1)
                              if ln.strip()), (None, ""))
            if following[1] and (re.fullmatch(r"[a-zà-ÿ]+", following[1])
                                 or ("wachttijd" in following[1]
                                     and len(following[1]) < 40)):
                time_text += " " + following[1]
                consumed.add(following[0])   # it belonged to the time, not to the ingredients
            continue
        match = CALORIES.search(plain)
        if match:
            kcal = int(match.group(1))
            continue
        if plain.startswith(("Per portie", "Per stuk")):
            continue
        match = NUTRITION.match(plain)
        if match:
            macros = tuple(int(g) for g in match.groups())
            break                       # nutrition is the last line of a recipe
        if plain.startswith(("VOOR DE", "VOOR HET")) or "kokengenieten" in plain:
            continue
        content.append(("line", plain))

    # the instructions start at the "1 ..." line whose 1,2,3... chain covers
    # the most text (a wrapped line such as "1 minuut erin" also starts with a
    # number, so a plain "last 1-line" rule would pick the wrong one)
    best, start = None, None
    for position, (kind, text) in enumerate(content):
        if kind != "line" or STEP_WITH_UNIT.match(text):
            continue
        if not re.match(r"^1\s", text) or not STEP_START.match(text):
            continue
        expected = 1
        for following in range(position, len(content)):
            kind2, text2 = content[following]
            if kind2 != "line":
                continue
            match = STEP_START.match(text2)
            if match and match.group(1) == str(expected):
                expected += 1
        # a real step is long prose; an ingredient line is short and quantity-led
        score = (0 if looks_like_ingredient(text) else 1, expected - 1, position)
        if best is None or score > best:
            best, start = score, position
    labelled = any(kind == "<label>" for kind, _ in content)

    if start is None:
        # no numbered steps: the text is one block of prose (a few recipes
        # carry their quantities inside the running text)
        prose = " ".join(text for kind, text in content if kind == "line")
        steps = [prose] if prose.strip() else []
        return yield_, time_text, [], steps, (kcal, macros)

    ingredients, steps, expected = [], [], 1
    body = content[start:]

    for kind, text in content[:start]:
        if kind == "<label>":
            continue
        # an ingredient whose name wrapped onto the next line leaves its amount
        # alone ("15 g" | "basilicum (+ extra, om te" | "garneren)"); put the
        # amount back together with the name
        if (ingredients and BARE_QUANTITY.match(ingredients[-1])
                and not BARE_QUANTITY.match(text)):
            ingredients[-1] += " " + text
            continue
        if is_continuation(ingredients[-1] if ingredients else "", text):
            if ingredients:
                ingredients[-1] += " " + text
            continue
        if not any(word in text.lower() for word in EQUIPMENT):
            ingredients.append(text)

    if not labelled:
        ingredients = []
    for kind, text in body:
        if kind == "<label>":
            continue
        match = STEP_START.match(text)
        if match and match.group(1) == str(expected) and not STEP_WITH_UNIT.match(text):
            steps.append(text)
            expected += 1
        elif steps:
            steps[-1] += " " + text

    steps = [re.sub(r"^\d+\s+", "", s.strip()) for s in steps if s.strip()]
    return yield_, time_text, ingredients, steps, (kcal, macros)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issue", default="2510",
                        help="magazine issue: 2510 (built in) or 2511, 2512 …")
    parser.add_argument("--write", action="store_true", help="write the JSON file")
    parser.add_argument("--images", choices=("data", "url", "path"), default=None,
                        help="how the recipe photo is referenced in the JSON")
    parser.add_argument("--base-url", default=None,
                        help="public URL of the images folder (with --images=url)")
    parser.add_argument("--out", type=pathlib.Path, default=None,
                        help="output file, e.g. recipes-11-2025.json")
    args = parser.parse_args()

    if args.issue != "2510":
        load_issue(args.issue)
    OUT = args.out or OUT
    IMAGE_MODE = args.images or IMAGE_MODE    # image_value() reads this at call time
    BASE_URL = args.base_url if args.base_url is not None else BASE_URL
    if IMAGE_MODE == "url" and not BASE_URL:
        parser.error("--images=url needs --base-url=https://host/folder")

    recipes, report = build()
    print("\n".join(report))
    print(f"image mode: {IMAGE_MODE}" + (f" ({BASE_URL})" if BASE_URL else ""))
    if args.write:
        args.out.write_text(json.dumps(recipes, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        print("wrote", args.out, "with", len(recipes), "recipes")

