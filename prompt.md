# Prompt: zet een Koken & genieten-nummer om naar `recipes-<editie>.json`

Gebruik deze prompt als je een nieuw nummer van *Koken & genieten* (of een vergelijkbaar
Nederlands kooktijdschrift) wilt omzetten naar een JSON-LD receptenbestand voor RecipeSage,
met dezelfde aanpak als de nummers 2510, 2511 en 2512 in dit project.

---

## 1. Opdracht

> Converteer de PDF van één tijdschriftnummer naar een valide Schema.org JSON-LD-bestand met
> **alle** recepten uit dat nummer, plus een Markdown-versie en de receptfoto's. Werk met de
> bestaande scripts in deze map; pas ze alleen aan als een nieuw nummer iets blootlegt dat nog
> niet wordt afgehandeld. Rapporteer aan het eind de aantallen en de uitkomsten van de controles.

## 2. Wat er al staat

| bestand | rol |
|---|---|
| `convert_pdf.py` | PDF → Markdown (kolomherkenning via XY-cut, koppen, hygiëne) |
| `layout.py` | bouwt de leesorde van een pagina op uit woord-boxen |
| `add_images.py` | haalt de receptfoto's van de inhoudspagina's, schrijft `images-<editie>/` + links in de Markdown |
| `extract.py` | Markdown → JSON-LD (bevat de nummergegevens van 2510; laadt `issue_<editie>.py` voor andere nummers) |
| `issue_2312.py`, `issue_2410.py`, `issue_2506.py`, `issue_2507.py`, `issue_2508.py`, `issue_2511.py`, `issue_2512.py` | alle nummergegevens van die edities |
| `validate_recipes.py` | veldniveau-controle per recept (`python validate_recipes.py [--issue=2512] bestand.json`) |
| `acceptance_test.py` | eindtest over de hele keten (`python acceptance_test.py [--issue=2512] bestand.json`) |

Uitvoer per nummer: `<EDITIE>.md`, `recipes-<editie>.json`, `images-<editie>/`.
Gebruik voor 2510 de bestaande `KG2510.md` + `images/` (die zitten ingebakken in `extract.py`).

## 3. Harde eisen aan het JSON-bestand

* Eén **JSON-array** (begint met `[`, eindigt met `]`), geldig UTF-8, geen commentaar.
* Per recept exact deze velden — laat een veld **weg** als het blad het niet geeft (niets verzinnen):

```json
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "Naam van het recept",
  "author": { "@type": "Person", "name": "Auteur of 'Koken & genieten'" },
  "publisher": { "@type": "Organization", "name": "Koken & genieten <editie>" },
  "datePublished": "JJJJ-MM",
  "recipeYield": "4 personen",
  "image": [ "<data-URI of URL>" ],
  "totalTime": "PT1H15M",
  "recipeCategory": [ "Hoofdgerecht", "Koken & genieten <editie>" ],
  "recipeIngredient": [ "500 ml slagroom" ],
  "recipeInstructions": [ { "@type": "HowToStep", "text": "Volledige tekst van stap 1" } ],
  "nutrition": { "@type": "NutritionInformation", "calories": "450 kcal",
                 "proteinContent": "20 g", "fatContent": "15 g",
                 "carbohydrateContent": "40 g" }
}
```

Opschoonregels:

* Zet ingrediënten als losse strings; **laat keukengerei weg** (bakpapier, aluminiumfolie,
  vershoudfolie, springvorm, steker, spiesen, spuitzak, spuitmondje) — eetbare dingen als
  "boter, om in te vetten" en "olie, om in te bakken" blijven staan.
* Verwijder afbreekstreepjes die door een regeleinde zijn ontstaan (`kom-` + `kommer` →
  `komkommer`; `hete-` + `lucht` → `hetelucht`).
* Neem de tekst verder **letterlijk** over; typefouten van het blad blijven staan.
* `totalTime` is ISO-8601 en bevat ook wachttijden die in uren worden gegeven
  ("ca. 2 uur en 30 min. + ca. 8 uur wachttijd" → `PT10H30M`). Wachttijden van dagen/weken
  (marineren) tellen niet mee.
* `recipeCategory` is een **lijst**: de categorie plus de issuelabel. Gebruik de bestaande
  categorieën: `Hoofdgerecht`, `Zoet & desserts`, `Soep`, `Salade`, `Bijgerecht`, `Drank`.
* `publisher` wordt door RecipeSage genegeerd; de issuelabel in `recipeCategory` is de enige
  route waarmee je nummers in RecipeSage kunt filteren.

## 4. Werkwijze

### Stap 1 — PDF naar Markdown
```bash
python convert_pdf.py --pdf KG2513.pdf --md KG2513.md
```
68–84 pagina's duren enkele seconden. Controleer daarna:
```bash
grep -n 'jaargang' KG2513.md | head -2      # editie/jaargang, bv. "Januari 2026 jaargang 21"
grep -c 'Ingrediënten' KG2513.md            # indicatie van het aantal recepten
grep -n '^## ' KG2513.md                    # alle koppen (recepten én advertenties/secties)
```
Een editie als `KG2513` hoort bij `januari 2026` → `ISSUE = "1-2026"`, `ISSUE_DATE = "2026-01"`.

### Stap 2 — de receptenlijst uit het blad halen
Lees het begin van de Markdown: daar staat *"De snelle weg door het blad"* en
*"Alle recepten op een rij"* met per recept de naam, de paginanummer en de rubriek
(voorgerechten & bijgerechten / hoofdgerechten / zoet en desserts). Lees ook de
inhoudsopgave-pagina met de rubrieken en hun paginanummers; die vertelt welke recepten bij
welke sectie horen (en dus vaak wie de auteur is).

Bepaal daarna per recept:
* **naam** — gebruik de titel zoals het blad die noemt; bij een meerregelige kop de delen
  aaneen ("Geroosterde pompoen en prei" + "met frisse dip").
* **auteur** — standaard `Koken & genieten`. Neem de credit over waar het blad die geeft:
  de maandelijkse sectie *Uit Paulines Keuken* → `Uit Paulines Keuken`; een boekpreview met
  een naam of een "Van Oma …"-credit → die naam.
* **categorie** — uit de rubriek-indeling in de inhoudsopgave; kies anders zelf uit de
  zes categorieën hierboven.
* **regelnummer** — het regelnummer van de `## `-kop (alleen als terugvaloptie; de extractor
  zoekt recepten op hun kop).

### Stap 3 — `issue_<editie>.py` maken
Kopieer `issue_2512.py` als sjabloon en vul in: `ISSUE`, `PUBLISHER`, `ISSUE_DATE`, `PDF`,
`MD`, `OUT`, `IMAGE_FOLDER`, `EXTRA_NOISE`, `RECIPE_TABLE` (en zo nodig `HEADING_AS`,
`CAPTION_SPLIT`, `OVERRIDES`). De tabelregel is:

```python
(regelnummer, "Naam", AUTEUR, "Categorie", None)   # laatste veld = totalTime-override
```

### Stap 4 — droogloop en anomalieën oplossen
```bash
python extract.py --issue 2513          # schrijft niets, toont per recept yield/tijd/ing/steps
```
Loop de uitvoer na en repareer wat opvalt:

| symptoom | oorzaak | oplossing |
|---|---|---|
| `ing=0` of `ing=1` bij een recept | het blad zet de hoeveelheden in de lopende tekst (geen ingrediëntenbox) | `OVERRIDES` met `ingredients` + `instructions` (letterlijk uit de tekst) |
| stappen van recept A staan bij recept B | twee recepten naast elkaar op één pagina, waarbij de ene kolom tussen de andere valt | `OVERRIDES` voor beide recepten (ingrediënten én stappen) |
| vreemd eerste ingrediënt ("+ 2 uur wachttijd") | tijdregel met wachttijd | hoort automatisch goed te gaan; blijft het staan, meld het als engine-bug |
| recept ontbreekt of pakt de verkeerde tekst | kop in het blad wijkt af (lange titel of typefout in het blad) | `HEADING_AS = {"Naam in tabel": "letterlijke kop in de markdown"}` |
| een sectiekop of advertentietekst wordt ingrediënt | kolomlabel nog niet bekend | zet het label in `EXTRA_NOISE` |
| `totalTime` te hoog/laag | wachttijd wel/niet meegeteld | `totalTime`-override in de tabel (bv. `"PT4H20M"`) |
| voedingsregel niet te lezen | typefout in het blad ("41 g koolhdyraten") of de regel staat in het blok van het volgende recept | `OVERRIDES` met `"nutrition"`: een dict met de waarden, of `None` om de voedingswaarden weg te laten |

### Stap 5 — foto's van de inhoudspagina's
```bash
python add_images.py --issue 2513
```
Dit schrijft `images-<editie>/*.jpg`, zet de links in de Markdown en meldt drie dingen:
aantal geschreven foto's, ongeldige onderschriften en recepten zónder foto. De
inhoudspagina's (meestal p. 2-4) tonen bij bijna elk recept een thumbnail met de receptnaam
eronder; die naam bepaalt de bestandsnaam (kleine letters, spaties → `-`).

* Ongeldige onderschriften: meestal is het onderschrift alleen de **eerste regel** van een
  lange titel (dat wordt nu automatisch op prefix gematcht) of betreft het een niet-recept
  (puzzel, advertentie).
* Eén brede foto waar twee recepten op staan: zet de caption-tekst in
  `CAPTION_SPLIT = {"<caption>": ["Naam 1", "Naam 2"]}`; de foto wordt dan in tweeën gedeeld.
* Recepten zonder foto: dat is geen fout (het blad toont ze niet op de inhoudspagina's); de
  JSON laat `image` daar weg en de controles accepteren dat. Wil je ze tóch, haal ze dan van
  de eigen receptpagina (de grote foto) en meld dat als handmatige aanvulling.

### Stap 6 — JSON genereren
```bash
python extract.py --issue 2513 --write --out recipes-2513.json
```
Doe dit **na** stap 5: de foto's worden uit `images-<editie>/` in de JSON gezet.

### Stap 7 — valideren (verplicht, beide moeten 0 zijn)
```bash
python validate_recipes.py --issue=2513 recipes-2513.json
python acceptance_test.py  --issue=2513 recipes-2513.json
```
`validate_recipes.py` controleert per recept alle velden, de categorie-lijst, de issuelabel,
de geldigheid van elke foto (JPEG-decodering), keukengerei in de ingrediënten,
voedingswaarden en de velden die een importeur direct aanroept.
`acceptance_test.py` controleert de hele keten: fotolinks, geen soft hyphens/dubbele
spaties/ligaturen, **geen enkele letter verloren of gedupliceerd t.o.v. de PDF**, per pagina
exact de eigen PDF-tekst, de foto's op schijf, de structuur van de JSON en of alle
ingrediënten/stappen letterlijk uit de Markdown komen.

## 5. Wat de engine al automatisch doet (niet handmatig doen)

* Leesorde per pagina via kolomherkenning (XY-cut), inclusief geneste subkolommen en
  paginabrede koppen.
* Koppen (`## `) uit de lettergroottes, vetgedrukte labels en hoeveelheden,
  `**Ingrediënten voor:**`/`**Bereidingstijd:**` eruit halen, keukengerei weglaten.
* Afbreekstreepjes aan het regeleinde en soft hyphens lijmen; ligaturen normaliseren.
* Tekens met een kapotte letterafbeelding (KG2508: de symbolen "snel klaar" en
  "zonder vlees of vis" in de ingrediëntenlijsten, en de bullets van de index)
  verdwijnen uit de tekst; ze hebben geen leesbare letter.
* Een ingrediënt waarvan de naam doorloopt op de volgende regel — het bedrag staat dan
  alleen op zijn regel ("15 g" / "basilicum (+ extra, om te" / "garneren)") — wordt
  weer aan elkaar gezet.
* De bestandsnaam van een foto laat haakjes weg, zodat een recept als
  "Sugo (tomatensaus)" een leesbare Markdown-link houdt.
* Een inhoudsfoto die over meerdere kolommen loopt, wordt langs dezelfde kolommen
  gesneden als waarin de onderschriften staan; een onderschrift dat door de letter van
  het blad een teken kwijtraakte ("wentelteef es") wordt nog herkend. `CAPTION_SPLIT`
  is daardoor alleen nog nodig als de opmaak echt afwijkt.
* Tijdregels inclusief een wachttijd die op de volgende regel staat.
* Als pdftotext de spaties in een regel kwijtraakt (één "woord" van 25+ tekens), wordt de
  PyMuPDF-tekst gebruikt.
* Een blanco laatste pagina breekt de conversie niet meer af.
* Draaihoofden, voetteksten en paginanummers weglaten.
* Recepten lokaliseren op hun **kop** in de Markdown (regelnummers zijn alleen terugval).

## 6. Rapportage

Rapporteer aan het eind:
1. de bestandsnamen en groottes (`recipes-<editie>.json`, `<EDITIE>.md`, `images-<editie>/`);
2. het aantal recepten, en per categorie en per auteur;
3. hoeveel recepten een foto hebben en welke niet (met reden);
4. de uitkomsten van `validate_recipes.py` en `acceptance_test.py` (aantallen problemen);
5. welke recepten handmatig zijn aangevuld en waarom;
6. welke engine-aanpassingen een nieuw nummer nodig maakte, en of de oudere nummers daarna
   opnieuw gegenereerd en getest zijn.

## 7. Checklist

- [ ] Markdown gegenereerd en gecontroleerd (datum/jaargang, koppen, geen regels zonder spaties)
- [ ] Receptenlijst uit de inhoudsopgave, met auteur en categorie per recept
- [ ] `issue_<editie>.py` gevuld
- [ ] Droogloop nagelopen; `OVERRIDES`/`HEADING_AS`/`EXTRA_NOISE` waar nodig
- [ ] Foto's geschreven; afwijkende onderschriften verklaard
- [ ] `recipes-<editie>.json` geschreven (geldige array, `image` als data-URI's)
- [ ] `validate_recipes.py` → 0 problemen én 0 import-shape problemen
- [ ] `acceptance_test.py` → 0 gefaalde checks
- [ ] oudere nummers opnieuw gegenereerd en nog steeds 0 (bij engine-wijzigingen)

## 8. Import in RecipeSage (let op)

RecipeSage's JSON-LD-import leest `image` wel, maar **haalt de afbeelding daarna als URL op**:
een base64 data-URI komt er dus niet door. Voor een import met foto's:

1. upload de inhoud van `images-<editie>/` naar een publieke map, bijvoorbeeld naar
   `https://jouw-domein.nl/kg2513/images/`;
2. genereer de URL-variant en test elke foto-URL:
   ```bash
   python extract.py --issue 2513 --write --images=url \
          --base-url=https://jouw-domein.nl/kg2513 --out recipes-2513.json
   python acceptance_test.py --issue=2513 recipes-2513.json   # eist HTTP 200 + image/*
   ```
3. importeer `recipes-2513.json` via *Settings → Import → JSON-LD*.

`--base-url` is de map **boven** `images/`; `recipeCategory` wordt in RecipeSage een label,
`publisher` wordt genegeerd.

Een publieke map die zonder extra diensten werkt is een GitHub-repository:

```bash
python extract.py --issue 2513 --write --images=url \
       --base-url=https://raw.githubusercontent.com/<gebruiker>/recipe-import-scripts/main \
       --out recipes-2513-url.json
```

* Gebruik de `raw.githubusercontent.com`-vorm (of `fastly.jsdelivr.net/gh/...`), **niet** de
  `github.com/.../blob/...`-link van de adresbalk: die levert HTML en dan laat RecipeSage de
  foto stil vallen. De repository moet publiek zijn.
* Bestandsnamen met accenten of `&` worden percent-gecodeerd (`bonencr%C3%A8me.jpg`,
  `instant-mascarponemousse-van-citroen-%26-witte-chocolade.jpg`); RecipeSage decodeert dat
  weer. Zonder codering weigert een aantal HTTP-clients de URL.
* RecipeSage haalt elke foto tijdens de import op en zet hem in zijn eigen opslag: de URL hoeft
  daarna niet meer online te staan. Reken op een thumbnail van 200×200 (1024 px met de
  betaalde `HighResImages`-capability) en op één foto per recept, tenzij het account
  `MultipleImages` heeft. Mislukte foto's zijn geen fout: het recept wordt zonder foto
  geïmporteerd.


