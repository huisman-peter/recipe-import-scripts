"""Issue-specific data for Koken & genieten KG2211 (november 2022).

Herfstnummer, 68 pages, the older 2022 layout.  Same shape as extract.py's
built-in KG2510 tables, so the engine processes this issue unchanged:

    python convert_pdf.py --pdf KG2211.pdf --md KG2211.md
    python add_images.py  --issue 2211
    python extract.py     --issue 2211 --write --out recipes-2211.json
"""
ISSUE = "11-2022"
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "2022-11"
ISSUE_AS_LABEL = True

PDF = "KG2211.pdf"
MD = "KG2211.md"
OUT = "recipes-2211.json"
IMAGE_FOLDER = "images-2211"

MONCHOU = "MonChou"              # the "Lekker romig" MonChou pages (p. 46-49)
SOU = "Soumia Aattaoui"          # the "Keuken van Sou" book (p. 50-55)
KG = "Koken & genieten"

# column labels, section titles and advert lines that are not ingredients
EXTRA_NOISE = {
    "SEIZOEN", "FAVORIET VAN DE MAAND", "VOOR IEDERE DAG",
    "DE SNELLE KEUKEN", "DE GEZONDE KEUKEN", "CULINAIRE INSPIRATIE",
    "STAP VOOR STAP", "VAN DE KOK", "LEKKER ZUUR",
    "LEKKER AROMATISCH & FRIS", "LAUWWARM HET", "LEKKERST",
    "MENU", "WEEKENDMENU", "Hoofdgerecht", "Voorgerecht", "Nagerecht",
    "BOEK", "COVERRECEPT", "GEBAK", "MONCHOU®", "}KOKEN & GENIETEN",
    # the sub-headings of the two-column ingredient lists (Soumia's book pages)
    "Voor de kip", "Voor de saus", "Voor de caesardressing",
    "Voor de gepofte aardappelen", "Voor de kip-chiliroomsaus",
    "Voor de dressing",
    # the tip box the magazine prints above the "Chocolade mug cake" ingredients
    "Serveer de cakejes", "lauwwarm met de",
    "slagroom en eventueel", "een bolletje vanille-ijs.",
    # the marinade tip box the magazine prints inside the "Braadstuk" recipe
    "In een klassieke marinade is een zuurtje",
    "een ‘must’. Door het zuur wordt het vlees",
    "lekker zacht en daardoor extra lekker. Kies",
    "voor een azijn van hoge kwaliteit.",
}

# (line of the "## " heading, full name, author, category, total time override)
RECIPE_TABLE = [
    # De smaak van wild (p. 6-9)
    (439, "Reerug met spinazie", KG, "Hoofdgerecht", None),
    (495, "Konijnrollade met whiskey-roomsaus", KG, "Hoofdgerecht", None),
    (542, "Broodje pulled hert met appel en coleslaw", KG, "Hoofdgerecht", None),
    # Herfsttijd, paddenstoelentijd (p. 10-13)
    (600, "Pasta carbonara met bospaddenstoelen", KG, "Hoofdgerecht", None),
    (633, "Cantharellen-pompoenlasagne", KG, "Hoofdgerecht", None),
    (678, "Spinazieknoedels met paddenstoelenragout", KG, "Hoofdgerecht", None),
    (727, "Mini-flammkuchen met rode ui, paddenstoelen en gremolata", KG, "Bijgerecht", None),
    # De hele week genieten (p. 14-21)
    (786, "Broccoli-pompoenroerbak met biefstukreepjes", KG, "Hoofdgerecht", None),
    (833, "Groenten-linzencurry", KG, "Hoofdgerecht", None),
    (867, "Zuurkool met worst", KG, "Hoofdgerecht", None),
    (910, "Pasta met spruitjes en kip", KG, "Hoofdgerecht", None),
    (948, "Alcoholvrije hot toddy", KG, "Drank", None),
    (959, "Zelfgemaakte lekkerbek met groenten", KG, "Hoofdgerecht", None),
    (999, "Rijstdessert met perzik uit de oven", KG, "Zoet & desserts", None),
    (1027, "Gebakken kweepeer met marsepein-walnotenvulling", KG, "Zoet & desserts", None),
    (1057, "Schwarzwälder-tiramisu-trifle", KG, "Zoet & desserts", None),
    (1084, "Chocolade mug cake", KG, "Zoet & desserts", None),
    # Het is weekend! (p. 22-25)
    (1250, "Appel-selderijsoep met spek", KG, "Soep", None),
    (1288, "Braadstuk met spätzle en veldsla", KG, "Hoofdgerecht", None),
    (1377, "Sinaasappelcustardtaartjes", KG, "Zoet & desserts", None),
    # Simpel en snel genieten (p. 26-31)
    (1445, "Snelle courgettepizza met granaatappelpitjes", KG, "Hoofdgerecht", None),
    (1473, "Kip in spek met friet en broccoli", KG, "Hoofdgerecht", None),
    (1507, "Kikkererwten-pompoensoep", KG, "Soep", None),
    (1543, "Pasta met romige spek-kaassaus", KG, "Hoofdgerecht", None),
    (1578, "Aziatisch gehaktpannetje met spiegelei", KG, "Hoofdgerecht", None),
    (1603, "Zoete-aardappelsalade voor onderweg", KG, "Salade", None),
    # Uit het bos, op je bord (p. 32-35)
    (1683, "Wildzwijnmedaillons met koolraapstamppot, gebakken uien en spek", KG, "Hoofdgerecht", None),
    # Gezond met noten (p. 36-41)
    (1863, "Overnight oats met gekaramelliseerde banaan", KG, "Bijgerecht", None),
    (1901, "Hazelnoten-broccoliovenschaaltjes", KG, "Bijgerecht", None),
    (1931, "Kabeljauw met pistachekorst", KG, "Hoofdgerecht", None),
    (1973, "Aardappelsalade met knapperig gebakken ham", KG, "Salade", None),
    # De keuken van Zuid-Tirol (p. 42-45)
    (2059, "Kaasknoedels met spitskool", KG, "Hoofdgerecht", None),
    (2102, "Aardappels in spek", KG, "Bijgerecht", None),
    # Lekker romig (MonChou, p. 46-49)
    (2199, "Zalmfilet met romige mosterd-dilletopping", MONCHOU, "Hoofdgerecht", None),
    (2227, "Gepofte zoete aardappel met MonChouvulling en spek-boontjesdressing", MONCHOU, "Hoofdgerecht", None),
    # Boek Keuken van Sou (Soumia Aattaoui, p. 50-55)
    (2369, "Lotusparfait", SOU, "Zoet & desserts", None),
    (2402, "Filipijnse Adobo", SOU, "Hoofdgerecht", None),
    (2449, "Gepofte aardappel met kip-chiliroomsaus", SOU, "Hoofdgerecht", None),
    (2513, "Kip caesar quesadilla", SOU, "Hoofdgerecht", None),
    # Coverrecept (p. 56-57)
    (2569, "Varkenshaasje met parmaham, appel en salie", KG, "Hoofdgerecht", None),
    # In de chocoladehemel (p. 58-65)
    (2620, "Chocolade-perentaart", KG, "Zoet & desserts", None),
    (2671, "Chocolade-cupcakes met cappuccinotopping", KG, "Zoet & desserts", None),
    (2713, "Chocolade-cakerol met roomvulling", KG, "Zoet & desserts", None),
    (2760, "Tiramisu-taart", KG, "Zoet & desserts", None),
]

HEADING_AS = {}
CAPTION_SPLIT = {}
NO_TIME_OK = set()

OVERRIDES = {
    # this drink prints no ingredient list: its quantities sit in the running text
    "Alcoholvrije hot toddy": {
        "ingredients": [
            "2 el honing", "2 tl citroensap", "2 kleine kaneelstokjes",
            "2 snufjes gemalen kruidnagel", "2 snufjes gemalen nootmuskaat",
            "400 ml hete, zwarte thee", "partje citroen",
        ],
        "instructions": [
            "Doe in elk glas 1 el honing, 1 tl citroensap, 1 klein kaneelstokje, "
            "1 snufje gemalen kruidnagel en 1 snufje gemalen nootmuskaat. Schenk "
            "in elk glas 200 ml hete, zwarte thee en roer door. Serveer naar "
            "smaak met een partje citroen.",
        ],
    },
    # the "100 g" of the ham above ran on into this recipe's ingredient list
    "Kabeljauw met pistachekorst": {
        "fix": {"100 g 2 sjalotjes": ["2 sjalotjes"]},
    },
    "Aardappelsalade met knapperig gebakken ham": {
        "fix": {"ham (in plakken)": ["100 g ham (in plakken)"]},
    },
    # a step number that opens a wrapped line ("4 spiegeleieren") split the step
    "Aziatisch gehaktpannetje met spiegelei": {
        "instructions": [
            "Kook de rijst volgens de aanwijzingen op de verpakking in water met "
            "wat zout. Maak de lente-uitjes schoon. Snijd het groene en het witte "
            "deel apart in ringen.",
            "Verhit 1 el olie in een pan. Bak er het gehakt rul in. Breng op smaak "
            "met zout en cayennepeper. Voeg de witte lente-uiringen toe en bak ca. "
            "3 minuten verder. Voeg de chilisaus, 3 el water en de sojasaus toe en "
            "verhit ca. 3 minuten verder op laag vuur.",
            "Verhit 1 el olie in een koekenpan met antiaanbaklaag. Bak er van de "
            "eieren 4 spiegeleieren. Bestrooi met zout en peper.",
            "Giet de rijst af. Serveer alles samen en bestrooi met de overige "
            "lente-ui.",
        ],
    },
    # the two-column ingredient lists of the book pages got read column by column
    "Gepofte aardappel met kip-chiliroomsaus": {
        "ingredients": [
            "4 grote aardappelen", "60 g roomboter (kamertemperatuur)",
            "4 tl geraspte mozzarella", "1 el zonnebloemolie", "snufje zout",
            "500 g kipfilet", "400 ml frituur-/zonnebloemolie",
            "200 ml kookroom", "60 ml water",
            "50 g geraspte Parmezaanse kaas", "2 eiwitten", "1 ui", "1 wortel",
            "1 groene paprika", "1 handvol rucola", "3 teentjes knoflook",
            "2 el maizena", "2 el zoete chilisaus", "1 el sojasaus",
            "1 el oestersaus", "1 tl chilivlokken", "½ tl zwarte peper",
            "1 tl zout", "1 tl paprikapoeder",
        ],
    },
    "Kip caesar quesadilla": {
        "ingredients": [
            "6 kleine tortillawraps", "200 g geraspte mozzarella",
            "100 g ijsberg-/kropsla", "50 g geraspte Parmezaanse kaas",
            "1 sneetje brood", "450 g kipfilet", "2 teentjes knoflook",
            "2 el dijonmosterd", "1 el zonnebloemolie",
            "1 el gedroogde rozemarijn", "sap van ½ citroen", "zout", "peper",
            "50 g geraspte Parmezaanse kaas", "2 ansjovisfilets",
            "4 el mayonaise", "2 el olijfolie", "sap van ½ citroen",
            "1 tl dijonmosterd", "1 tl sojasaus", "1 tl tomatenketchup",
            "1 el natuurazijn",
        ],
    },
    # wrapped ingredient tails the generic parser cannot see are one ingredient
    "Reerug met spinazie": {
        "fix": {"geraspte schil en sap": ["geraspte schil en sap van 1 bio-limoen"],
                "van 1 bio-limoen": []},
    },
    "Broodje pulled hert met appel en coleslaw": {
        "fix": {"1 ui \t(bijv. rode)": ["1 ui (bijv. rode)"]},
    },
    "Rijstdessert met perzik uit de oven": {
        "fix": {"poedersuiker om te": ["poedersuiker om te bestuiven"],
                "bestuiven": []},
    },
    "Overnight oats met gekaramelliseerde banaan": {
        "fix": {"evt. citroenmelisse om te": ["evt. citroenmelisse om te versieren"],
                "versieren": []},
    },
    "Gepofte zoete aardappel met MonChouvulling en spek-boontjesdressing": {
        "fix": {"3 bosuitjes, 2 fijngehakt en 1 in":
                ["3 bosuitjes, 2 fijngehakt en 1 in ringetjes"],
                "ringetjes": [],
                "50 g witte bonen uit blik, afgespoeld":
                ["50 g witte bonen uit blik, afgespoeld en uitgelekt"],
                "en uitgelekt": []},
    },
    "Lotusparfait": {
        "fix": {"7 el Lotus Biscoff": ["7 el Lotus Biscoff speculaaspasta"],
                "speculaaspasta": []},
    },
    "Zalmfilet met romige mosterd-dilletopping": {
        "fix": {"1 citroen, ½ uitgeperst en ½ in":
                ["1 citroen, ½ uitgeperst en ½ in partjes"],
                "partjes": []},
    },
    # the freezer bag the marinade is put in is kitchen kit, not an ingredient
    "Braadstuk met spätzle en veldsla": {
        "fix": {"1 grote diepvrieszak": []},
    },
    "Mini-flammkuchen met rode ui, paddenstoelen en gremolata": {
        "fix": {"zoutenpeper.": ["zout en peper"]},
    },
}
