"""Issue-specific data for Koken & genieten KG2512 (december 2025, jaargang 20).

Christmas special, 84 pages.  Same shape as extract.py's built-in KG2510 tables:

    python convert_pdf.py --pdf KG2512.pdf --md KG2512.md
    python add_images.py  --issue 2512
    python extract.py     --issue 2512 --write --out recipes-2512.json
"""
ISSUE = "12-2025"
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "2025-12"
ISSUE_AS_LABEL = True

PDF = "KG2512.pdf"
MD = "KG2512.md"
OUT = "recipes-2512.json"
IMAGE_FOLDER = "images-2512"

PAULINE = "Uit Paulines Keuken"
KG = "Koken & genieten"

# column labels and section titles that are not ingredients
EXTRA_NOISE = {
    "Seizoen", "De snelle keuken", "Kookboek", "De zoete oven", "Buffet",
    "Uit Paulines Keuken", "Coverrecept", "EXTRA DIK", "KERSTNUMMER",
    "feestelijke", "inspiratie", "Bestel nu voor", "Voor- en bijgerechten",
    "Hoofdgerechten", "Zoet en desserts", "In het", "nummer",
}

# the table calls a recipe differently from its "## " heading in the Markdown
HEADING_AS = {
    "Krokante roodbaars met romige zuurkool": "Krokante roodbaars het romige zuurkool",
    "Italiaanse gegratineerde aardappel met gorgonzola": "Italiaans met gorgonzola",
    "Mediterrane gegratineerde aardappel met courgette en tomaat": "Mediterraan met courgette en tomaat",
    "Scandinavische gegratineerde aardappel met zalm en spinazie": "Scandinavisch met zalm en spinazie",
    "Franse gegratineerde aardappel met lente-ui en ham": "Frans met lente-ui en ham",
}

# (line of the "## " heading, full name, author, category, total time override)
RECIPE_TABLE = [
    (334, "Carpacciobonbon", PAULINE, "Bijgerecht", None),
    (376, "Truffelrisotto met paddenstoelen", PAULINE, "Hoofdgerecht", None),
    (425, "Gevulde kip met gehakt", PAULINE, "Hoofdgerecht", None),
    (468, "Chocoladepudding met room", PAULINE, "Zoet & desserts", None),
    (508, "Tulbandcake met stroopwafel", PAULINE, "Zoet & desserts", None),
    (570, "Varkenshaas met spek en whiskysaus", KG, "Hoofdgerecht", None),
    (611, "Aardappelkroketjes", KG, "Bijgerecht", None),
    (626, "Ahornspruitjes", KG, "Bijgerecht", None),
    (638, "Romige pompoenzuurkool", KG, "Bijgerecht", None),
    (651, "Boereneend met knödels en sinaasappelrodekool", KG, "Hoofdgerecht", None),
    (696, "Aardappelbolletjes", KG, "Bijgerecht", None),
    (726, "Kaas-cranberryflapjes", KG, "Bijgerecht", None),
    (756, "Kabeljauw met mascarponepuree en chorizotomaatjes", KG, "Hoofdgerecht", None),
    (807, "Filodeeg-groentetaart met kastanje", KG, "Hoofdgerecht", None),
    (862, "Sinaasappelrodekool", KG, "Bijgerecht", None),
    (895, "Walnotensoep met truffelolie", KG, "Soep", None),
    (923, "Laagjessalade met garnalen", KG, "Salade", None),
    (958, "Rundercarpaccio met parmezaancrème", KG, "Bijgerecht", None),
    (987, "Tiramisu met marsepein en sinaasappel", KG, "Zoet & desserts", None),
    (1018, "Tobleronemousse", KG, "Zoet & desserts", None),
    (1043, "Gepofte appel met marshmallows en vanillesaus", KG, "Zoet & desserts", None),
    (1077, "Kersen-kokosdessert", KG, "Zoet & desserts", None),
    (1183, "Klassiek zuurgebraad met rodewijnsaus", KG, "Hoofdgerecht", None),
    (1248, "Pittige champignon-pepersaus", KG, "Bijgerecht", None),
    (1271, "Sinaasappel-sjalotsaus", KG, "Bijgerecht", None),
    (1300, "Kruidenmayonaise", KG, "Bijgerecht", None),
    (1325, "Zwitserse kaassaus", KG, "Bijgerecht", None),
    (1373, "Gnocchi-ovenschotel caprese", KG, "Hoofdgerecht", None),
    (1409, "Snelle broccoli-kaaspasta", KG, "Hoofdgerecht", None),
    (1443, "Linzensalade met savooiekool en granaatappel", KG, "Salade", None),
    (1480, "Cranberryschmarrn met sinaasappel", KG, "Zoet & desserts", None),
    (1506, "Krokante roodbaars met romige zuurkool", KG, "Hoofdgerecht", None),
    (1534, "Malse filetlapjes met spinazie en roomsaus", KG, "Hoofdgerecht", None),
    (1562, "Paté Hawaï op boerenbrood", KG, "Bijgerecht", None),
    (1605, "Speculaasmarmertulband", KG, "Zoet & desserts", None),
    (1646, "Zalmtaart met verse kruiden", KG, "Hoofdgerecht", None),
    (1688, "Kokos-tequilacocktail met Cointreau", KG, "Drank", None),
    (1699, "Krokante sterren en manen", KG, "Zoet & desserts", None),
    (1717, "Gouden bloemkoolsoep met granaatappel", KG, "Soep", None),
    (1758, "Kip uit de oven met saliegnocchi en bietensalade", KG, "Hoofdgerecht", None),
    (1836, "Chaiparfait met rumvruchten", KG, "Zoet & desserts", None),
    (1965, "Italiaanse gegratineerde aardappel met gorgonzola", KG, "Bijgerecht", None),
    (1989, "Mediterrane gegratineerde aardappel met courgette en tomaat", KG, "Bijgerecht", None),
    (2014, "Scandinavische gegratineerde aardappel met zalm en spinazie", KG, "Bijgerecht", None),
    (2046, "Franse gegratineerde aardappel met lente-ui en ham", KG, "Bijgerecht", None),
    (2080, "Citroentulband met basilicum", KG, "Zoet & desserts", None),
    (2144, "Croissantpudding met frambozen", KG, "Zoet & desserts", None),
    (2181, "Pistachepavlovaatjes", KG, "Zoet & desserts", None),
    (2217, "Speculaasbrokken", KG, "Zoet & desserts", None),
    (2296, "Amandel-meringuetaart met rumkersen", KG, "Zoet & desserts", None),
    (2347, "Kaneeltaart met sinaasappel", KG, "Zoet & desserts", None),
    (2399, "Koek-kerstboompjes", KG, "Zoet & desserts", None),
    (2445, "Chocoladespritsen met wittechocoladevulling", KG, "Zoet & desserts", None),
    (2471, "Florentinekoekjes", KG, "Zoet & desserts", None),
    (2510, "Kerststolkoekjes met walnootvulling", KG, "Zoet & desserts", None),
    (2562, "Kerstcake met wittechocoladeroom en cranberrycompote", KG, "Zoet & desserts", None),
    (2736, "Crème brûlée van geitenkaas", KG, "Zoet & desserts", None),
    (2782, "Kabeljauwfilet met amandelkorst", KG, "Hoofdgerecht", None),
    (2815, "Ravioli met paddenstoelenvulling", KG, "Hoofdgerecht", None),
    (2863, "Glutenvrij kerstbrood", KG, "Bijgerecht", None),
    (2920, "Zwartebessenscones met jam en clotted cream", KG, "Zoet & desserts", None),
    (2963, "Sandwiches met appel-kerriesalade", KG, "Bijgerecht", None),
    (3015, "Feestelijke kaneelstertaart", KG, "Zoet & desserts", None),
    (3102, "Sinaasappel-chocoladespekkoek", KG, "Zoet & desserts", None),
    (3158, "Speculoosvlechtbrood", KG, "Bijgerecht", None),
    (3210, "Luxe red velvettaart", KG, "Zoet & desserts", None),
    (3275, "Marsepeinen kerstballetjes", KG, "Zoet & desserts", None),
    (3283, "Appel-marsepeintaart", KG, "Zoet & desserts", None),
]

CAPTION_SPLIT = {}

# these five carry their quantities inside the running text
OVERRIDES = {
    "Aardappelkroketjes": {
        "ingredients": ["1 kg aardappels", "2 eieren", "110 g bloem",
                        "35 g maizena", "zout en nootmuskaat",
                        "150 g paneermeel", "1 l frituurolie"],
        "instructions": [
            "Was 1 kg aardappels en kook ze in water in ca. 20 minuten gaar. Giet af, laat iets afkoelen en schil ze. Pers de warme aardappels door een aardappelpers in een kom. Splits 2 eieren. Houd het eiwit apart. Voeg de eidooiers, 110 g bloem, 35 g maizena, zout en nootmuskaat toe aan de aardappels en kneed alles snel door elkaar. Kneed niet te lang, anders wordt het deeg taai. Verdeel het aardappeldeeg in vieren en rol elk deel op een beetje bloem uit tot een rol (ca. 1,5 cm Ø). Snijd de rollen in stukken van 3-4 cm en vorm er kroketjes van. Kluts de eiwitten. Haal de kroketten eerst door het eiwit en daarna door 150 g paneermeel. Verhit 1 l frituurolie in een diepe pan of brede pot tot 160°C. Frituur de aardappelkroketjes in porties in 5-6 minuten goudbruin en gaar. Laat uitlekken. Lekker bij varkenshaas (p. 15).",
        ],
    },
    "Ahornspruitjes": {
        "ingredients": ["750 g spruitjes", "1 ui", "50 g walnoten", "2 el boter",
                        "1 el olie", "4 el ahornsiroop", "zout en peper"],
        "instructions": [
            "Maak 750 g spruitjes schoon, was ze en kook ze in kokend water met zout in ca. 10 minuten beetgaar. Pel en snipper intussen 1 ui. Rooster 50 g walnoten in een droge koekenpan. Neem ze uit de pan en hak ze grof. Giet de spruitjes af. Verhit 2 el boter en 1 el olie in een pan. Fruit de ui glazig erin. Voeg de spruitjes toe en bak ca. 5 minuten. Schenk 4 el ahornsiroop erover bestrooi met de walnoten en meng alles met elkaar. Breng op smaak met zout en peper. Lekker bij varkenshaas (p. 15).",
        ],
    },
    "Romige pompoenzuurkool": {
        "ingredients": ["1 ui", "2 el boter", "850 g zuurkool (zak of pot)",
                        "2 tl suiker", "4 jeneverbessen", "2 laurierblaadjes",
                        "400 ml groentebouillon", "750 g hokkaidopompoen",
                        "100 g crème fraîche", "½ bosje bieslook", "1 tl suiker",
                        "zout en peper"],
        "instructions": [
            "Pel en snipper 1 ui. Verhit 2 el boter in een pan en fruit de ui glazig. Voeg 850 g zuurkool (zak of pot), 2 tl suiker, 4 jeneverbessen en 2 laurierblaadjes toe en bak kort mee. Blus af met 400 ml groentebouillon, breng aan de kook en laat afgedekt ca. 15 minuten zachtjes koken. Snijd intussen 750 g hokkaidopompoen in vieren, verwijder de pitten, was de stukken en snijd ze in dunne plakjes. Snijd de plakjes vervolgens in repen van ca. 1 cm breed. Schep de pompoen door de zuurkool en laat nog ca. 10 minuten zachtjes koken. Was en hak ½ bosje bieslook fijn. Roer 100 g crème fraîche door de zuurkool, breng aan de kook en breng op smaak met zout, peper en 1 tl suiker. Serveer warm. Lekker bij varkenshaas (p. 15).",
        ],
    },
    "Krokante sterren en manen": {
        "ingredients": ["1 mespuntje kaneel", "2 el suiker",
                        "270 g bladerdeeg (rol, koeling)", "1 eidooier",
                        "1 el melk", "2 el sesamzaad"],
        "instructions": [
            "Meng 1 mespuntje kaneel met 2 el suiker. Rol 270 g bladerdeeg (rol, koeling) met het bijbehorende bakpapier uit. Steek met uitsteekvormpjes halvemanen (ca. 6 cm) en sterren (ca. 5 cm) dicht op elkaar uit het deeg. Kluts 1 eidooier met 1 el melk. Bestrijk de deegvormpjes hiermee. Snijd voor de cocktailglazen (zie recept links) 6 deegvormpjes ca. 2 mm breed in en bestrooi ze met wat van de kaneelsuiker. Bestrooi de overige deegvormpjes met 2 el sesamzaad. Verwarm de oven voor (elektrisch: 200°C / hetelucht: 180°C). Leg de deegvormpjes op een met bakpapier beklede bakplaat. Bak ca. 8 minuten in de oven. Neem uit de oven en laat afkoelen.",
        ],
    },
    "Marsepeinen kerstballetjes": {
        "ingredients": ["100 g marsepein", "2 druppels vanille-extract",
                        "eetbare kleur- of glitterpoeders (bij de bakwinkel)"],
        "instructions": [
            "Kneed 100 g marsepein en 2 druppels vanille-extract glad. Vorm er 8-10 kleine balletjes van. Doe verschillende eetbare kleur- of glitterpoeders (bij de bakwinkel) apart in kleine kommetjes en rol de balletjes naar wens erdoorheen, tot ze volledig bedekt zijn met kleur.",
        ],
    },
    "Kokos-tequilacocktail met Cointreau": {
        "ingredients": [
            "kaneelsuiker (restant van de sterren en manen)",
            "120 ml limoensap", "180 ml tequila (bij de slijter)",
            "120 ml Cointreau (bij de slijter)", "250 ml kokosmelk (blik)",
            "2 el suiker- of agavesiroop", "ijsblokjes",
            "krokante sterren en manen, om te garneren",
        ],
        "instructions": [
            "Strooi de overgebleven kaneelsuiker (restant van de sterren en manen, zie rechts) op een plat bord. Bestrijk de randen van 6 glazen met wat limoensap en doop ze in de kaneelsuiker. Meng 120 ml limoensap, 180 ml tequila (bij de slijter), 120 ml Cointreau (bij de slijter), 250 ml kokosmelk (blik) en 2 el suiker- of agavesiroop met elkaar. Verdeel ijsblokjes over de glazen. Schud het tequilamengsel in twee porties krachtig in een cocktailshaker. Schenk in de glazen. Garneer de glazen met de koekjes (zie sterren en manen, rechts).",
        ],
    },
}


