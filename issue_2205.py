"""Issue-specific data for Koken & genieten KG2205 (mei 2022).

Theme "Uit mama's keuken", 68 pages, the older 2022 layout.  Same shape as
extract.py's built-in KG2510 tables, so the engine processes this issue
unchanged:

    python convert_pdf.py --pdf KG2205.pdf --md KG2205.md
    python add_images.py  --issue 2205
    python extract.py     --issue 2205 --write --out recipes-2205.json
"""
ISSUE = "05-2022"
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "2022-05"
ISSUE_AS_LABEL = True

PDF = "KG2205.pdf"
MD = "KG2205.md"
OUT = "recipes-2205.json"
IMAGE_FOLDER = "images-2205"

KARIN = "Karin Luiten"      # the "Vega zónder pakjes en zakjes" book (p. 44-49)
KG = "Koken & genieten"

# column labels, section titles and advert lines that are not ingredients
EXTRA_NOISE = {
    "VOOR ELKE DAG", "doordeweekse", "inspiratie", "BOEK",
    "ZONDER PAKJES EN", "ZAKJES VEGA", "ABONNEMENT",
    "Alleskunner", "Bitterzoet", "Lekker grillen", "Mooi in bloei",
    "TIP", "HORIZONTAAL", "VERTICAAL", "VEGA ZÓNDER PAKJES EN ZAKJES",
    "T.W.V. 25,99 EURO", "KOKEN & GENIETEN", "42% MINDER VET",
    "Variatietip", "VAN DE KOK", "Klantenservice",
    "www.kokengenieten.nl/contact", "€5,- korting", "IN HET", "NUMMER",
    "ZOMERKONINKJES IN DE", "SPOTLIGHTS", "VERS VAN DE MARKT:",
    "NIEUWE AARDAPPELS", "ON THE ROAD", "momentogusto.nl",
    "BUFFET", "receptenindex", "juni", "STAP VOOR STAP", "4tips",
}

# (line of the "## " heading, full name, author, category, total time override)
RECIPE_TABLE = [
    # Moeders gehaktballen (p. 6-10)
    (338, "Gehaktballen met gerookte paprika, venkelzaad en tomatenjus", KG, "Hoofdgerecht", None),
    (390, "Pasta met bifteki-balletjes in Griekse saus", KG, "Hoofdgerecht", None),
    (452, "Burgers met appel en romige zuurkool", KG, "Hoofdgerecht", None),
    (514, "Torta di polpette - gehaktballetjestaart", KG, "Hoofdgerecht", None),
    (570, "Broodje gehaktballetjes met pruimensaus", KG, "Hoofdgerecht", None),
    (606, "Ricottaburgers met gesmoorde boerenkool", KG, "Hoofdgerecht", None),
    # Vega schnitzels (p. 12-14)
    (661, "Tofu-schnitzel met pindakorst en noedelsalade", KG, "Hoofdgerecht", None),
    (712, "Courgette-schnitzels met kwarkdip", KG, "Hoofdgerecht", None),
    (753, "Paddenstoelenschnitzel met mierikswortel-aardappelpuree", KG, "Hoofdgerecht", None),
    (799, "Gevulde knolselderijschnitzels", KG, "Hoofdgerecht", None),
    # De hele week genieten (p. 16-22)
    (856, "Orecchiette carbonara met erwtjes", KG, "Hoofdgerecht", None),
    (890, "Wortel-mangosoep met feta", KG, "Soep", None),
    (926, "Knapperige visfilet met koolrabi-aardappelsalade", KG, "Hoofdgerecht", None),
    (966, "Spinazie-quiche", KG, "Hoofdgerecht", None),
    (1001, "Ovenschotel met casselerrib, brood en spitskool", KG, "Hoofdgerecht", None),
    (1040, "Aardbeien-amuses", KG, "Bijgerecht", None),
    (1050, "Kalkoenrolletjes met romige sperziebonen", KG, "Hoofdgerecht", None),
    (1105, "Limoensoesjes", KG, "Zoet & desserts", None),
    (1146, "Rijstdessert met bosvruchten", KG, "Zoet & desserts", None),
    (1171, "Frisse perziksorbet", KG, "Zoet & desserts", None),
    # Geurige kruidnagel (p. 24-27)
    (1312, "Aspic met kruidige groentefond", KG, "Bijgerecht", None),
    (1375, "Rollade met kruidnagel en jeneverbes", KG, "Hoofdgerecht", None),
    # Simpel en snel genieten (p. 28-32)
    (1452, "Pasta met paprika en spiegelei", KG, "Hoofdgerecht", None),
    (1488, "Gehaktballetjes met champignonroomsaus", KG, "Hoofdgerecht", None),
    (1526, "Lentegroentesoep", KG, "Soep", None),
    (1556, "Teriyaki-kip met bimi", KG, "Hoofdgerecht", None),
    (1590, "Dubbelgebakken tosti ham-kaas", KG, "Hoofdgerecht", None),
    (1622, "Gehakt-stroganoff", KG, "Hoofdgerecht", None),
    # Naar buiten! (p. 34-39)
    (1747, "Groentemuffins met feta", KG, "Bijgerecht", None),
    (1781, "Vlierbloesem-limoensiroop", KG, "Drank", None),
    (1797, "Gemarineerde karbonades", KG, "Hoofdgerecht", None),
    (1816, "Frisse aardappelsalade met radijsjes", KG, "Salade", None),
    (1862, "Rabarberkruimeltaart", KG, "Zoet & desserts", None),
    (1897, "Pizzastrudel met spinazie en zongedroogde tomaten", KG, "Bijgerecht", None),
    (1935, "Romige witte-bonenpuree", KG, "Bijgerecht", None),
    (1950, "Sesam-yoghurtdip", KG, "Bijgerecht", None),
    # Zonder pakjes en zakjes (Karin Luiten, p. 44-49)
    (2018, "Koude radijssoep", KARIN, "Soep", None),
    (2053, "Rodelinzenbolognese", KARIN, "Hoofdgerecht", None),
    (2095, "Kokoscurry met ananas", KARIN, "Hoofdgerecht", None),
    (2148, "Sierlijke filotaart met snijbiet", KARIN, "Hoofdgerecht", None),
    # Een pan vol voorjaarsgroenten (p. 50-51)
    (2230, "Romige stoof met voorjaarsgroenten", KG, "Hoofdgerecht", None),
    # Terug naar de kindertijd (p. 54-57)
    (2413, "Gehaktballen uit de oven met hutspot", KG, "Hoofdgerecht", None),
    (2464, "Entrecote met gebakken uitjes", KG, "Hoofdgerecht", None),
    (2508, "Erwtensoep met worst", KG, "Soep", None),
    (2548, "Fusilli met worst en ei uit de oven", KG, "Hoofdgerecht", None),
    # Mama's appelgebak (p. 58-62)
    (2601, "Appel-walnotenplaatkoek", KG, "Zoet & desserts", None),
    (2641, "Geglaceerde appeltaart", KG, "Zoet & desserts", None),
    (2683, "Appelstrudel met lemoncurd en hazelnoten", KG, "Zoet & desserts", None),
    (2734, "Appel-browniecarrés", KG, "Zoet & desserts", None),
    (2799, "Appeltaart met amandelkorst", KG, "Zoet & desserts", None),
    # Moederdagtaart (p. 64-65)
    (2841, "Kleurrijke Moederdagkrans", KG, "Zoet & desserts", None),
]

HEADING_AS = {}
CAPTION_SPLIT = {}
NO_TIME_OK = set()
# these print no ingredient list: the quantities sit in the running text
OVERRIDES = {
    "Aardbeien-amuses": {
        "ingredients": [
            "200 g verse roomkaas", "½ bio-citroen (schil en sap)",
            "zout en peper", "3 radijsjes", "6 aardbeien",
            "2-3 takjes oregano",
        ],
    },
    "Vlierbloesem-limoensiroop": {
        "ingredients": [
            "2 bio-limoenen", "20 vlierbloesemtakjes", "1 kg suiker", "1 l water",
        ],
    },
    "Romige witte-bonenpuree": {
        "ingredients": [
            "400 g witte bonen (blik)", "2 takjes munt", "1 teentje knoflook",
            "2 el Griekse yoghurt", "3 el olijfolie", "1 tl komijnpoeder",
            "2 el citroensap", "zout en peper",
        ],
    },
    "Sesam-yoghurtdip": {
        "ingredients": [
            "2 tl sesamzaad", "300 g Griekse yoghurt", "100 g tahin (sesampasta)",
            "2 el citroensap", "zout", "paar druppeltjes tabasco",
        ],
    },
    # the karbonades are printed next to the potato salad: the magazine put
    # their steps in the salad's column, so both recipes get their own text back
    "Gemarineerde karbonades": {
        "ingredients": [
            "2 el paprikapoeder", "1 el suiker", "zout en peper",
            "6 schouderkarbonades (ca. 1,2 kg)", "6 uien", "500 ml appelsap",
            "100 ml barbecuesaus (fles)", "1 tl worcestersaus", "3 el olie",
            "2 el tomatenpuree", "250 ml groentebouillon",
        ],
        "instructions": [
            "EEN DAG VAN TEVOREN Meng het paprikapoeder, de suiker, 1½ tl zout en 1½ tl peper. Wrijf de karbonades ermee in. Pel de uien en snijd ze in ringen. Doe de uien met de karbonades in een kom. Roer het appelsap, de barbecuesaus en de worcestersaus door elkaar en schenk het mengsel over de karbonades. Dek af met folie en zet een nacht in de koelkast.",
            "DE VOLGENDE DAG Verwarm de oven voor (elektrisch: 200°C / hetelucht: 180°C). Neem de karbonades uit de marinade. Houd de marinade apart. Dep de karbonades droog. Verhit de olie in een ovenvaste pan met deksel. Bak er de karbonades ca. 2 minuten per zijde op hoog vuur in. Neem uit de pan. Bak de tomatenpuree in het hete bakvet. Voeg de karbonades weer toe. Voeg de marinade, de ui en de bouillon toe en breng aan de kook. Zet afgedekt ca. 1 uur en 30 minuten in de oven.",
            "Neem de karbonades uit de pan en houd warm. Zeef het braadvocht in een pannetje, breng aan de kook en breng op smaak met zout en peper. Serveer de karbonades met de jus. Lekker met de aardappelsalade (zie recept hieronder) en met de peterselie-gremolata (zie kader).",
        ],
    },
    "Frisse aardappelsalade met radijsjes": {
        "instructions": [
            "Was de aardappels en kook ze in water met een snufje zout in ca. 20 minuten gaar. Kook de erwten de laatste 3 minuten mee. Pel en snipper de uien. Breng de balsamico, de bouillon en de ui in een pan aan de kook. Neem van het vuur en laat staan. Giet de aardappels en de erwten af en spoel kort. Pel de aardappels en snijd ze in plakken. Hak de kappertjes. Meng de aardappels, de kappertjes, de erwten en het uienmengsel. Laat ca. 30 minuten marineren.",
            "Maak de radijsjes schoon en schaaf of snijd ze in dunne plakken. Was de sla en snijd hem in stukken. Spatel de zure room, de radijsjes en de sla door de salade. Breng op smaak met zout en peper.",
        ],
    },
}
