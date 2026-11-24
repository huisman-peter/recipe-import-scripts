"""Issue-specific data for Koken & genieten KG2410 (oktober 2024).

Autumn issue ("Het is herfst!"), 68 pages, the older 2024 layout.  Same shape as
extract.py's built-in KG2510 tables, so the engine processes this issue unchanged:

    python convert_pdf.py --pdf KG2410.pdf --md KG2410.md
    python add_images.py  --issue 2410
    python extract.py     --issue 2410 --write --out recipes-2410.json
"""
ISSUE = "10-2024"
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "2024-10"
ISSUE_AS_LABEL = True

PDF = "KG2410.pdf"
MD = "KG2410.md"
OUT = "recipes-2410.json"
IMAGE_FOLDER = "images-2410"

BRENDA = "Brenda Kookt"          # the monthly blog contribution (p. 6-11)
EMMA = "Emma de Thouars"         # the "Solo" book preview (p. 42-47)
KG = "Koken & genieten"

# column labels, section titles and advert lines that are not ingredients
EXTRA_NOISE = {
    "Brenda Kookt", "BRENDA KOOKT", "Heerlijke herfst", "Smoorverliefd",
    "Gezondheid!", "Simpel en snel genieten", "Oogstfeest", "Het rijk alleen",
    "Immuunboost", "Gietijzer", "Süße Grüße", "Toffe peren", "Coverrecept",
    "In het seizoen...", "Kookboek", "Kookboek: Solo",
    "Fotografie en receptuur: Brenda Kookt",
    "Receptuur: Emma de Thouars Fotografie: Sophia van den Hoek",
    "Titel: Solo", "Auteur: Emma de Thouars",
    "Fotografie: Sophia van den Hoek",
}

# (line of the "## " heading, full name, author, category, total time override)
RECIPE_TABLE = [
    # Brenda Kookt (p. 6-11)
    (281, "Traybake van pompoen met spruitjes en worstjes", BRENDA, "Hoofdgerecht", None),
    (310, "Tomatensoep", BRENDA, "Soep", None),
    (339, "Andijvieschotel met gehakt en spek", BRENDA, "Hoofdgerecht", None),
    (380, "Kip stroganoff met macaroni", BRENDA, "Hoofdgerecht", None),
    (427, "Appeltaartcinnamonrolls", BRENDA, "Zoet & desserts", None),
    # Smoorverliefd (p. 12-19)
    (472, "Kipstoof met gepofte parelgort", KG, "Hoofdgerecht", None),
    (524, "Schnitzelschotel met ham en pompoen", KG, "Hoofdgerecht", None),
    (571, "Perzische koolrolletjes", KG, "Hoofdgerecht", None),
    (623, "Paddenstoelen-bonennoedels met misoroom", KG, "Hoofdgerecht", None),
    (658, "Wildzwijnovenschotel", KG, "Hoofdgerecht", None),
    # Gezondheid! (p. 20-25)
    (819, "Koolraap-bietensoep met pastinaak", KG, "Soep", None),
    (864, "Savooiekoolsoep met gehaktballetjes", KG, "Soep", None),
    (900, "Thaise kokos-kippensoep", KG, "Soep", None),
    (944, "Linzensoep met appel", KG, "Soep", None),
    # Simpel en snel genieten (p. 26-31)
    (1034, "Zalm uit de oven met bieten en sinaasappel", KG, "Hoofdgerecht", None),
    (1067, "Snelle eenpansspaghetti met champignons", KG, "Hoofdgerecht", None),
    (1103, "Aardappelsoep met krokante topping", KG, "Soep", None),
    (1136, "Kogelbiefstuk met tomatenrijst", KG, "Hoofdgerecht", None),
    (1184, "Sandwich met prei en rookvlees", KG, "Hoofdgerecht", None),
    (1206, "Kalkoen stroganoff met wilde rijst", KG, "Hoofdgerecht", None),
    # Oogstfeest (p. 32-41)
    (1267, "Herfstige borrelplank", KG, "Bijgerecht", None),
    (1295, "Kaasbezempjes", KG, "Bijgerecht", None),
    (1307, "Knapperig platbrood met druiven en crème fraîche", KG, "Bijgerecht", None),
    (1325, "Uiensoep met pannenkoek", KG, "Soep", None),
    (1376, "Warme groentesalade met krokante pitten", KG, "Salade", None),
    (1416, "Varkensgebraad met mosterd", KG, "Hoofdgerecht", None),
    (1448, "Hazelnootkoekjes met perencompote", KG, "Zoet & desserts", None),
    # Kookboek: Solo (p. 42-47)
    (1573, "Harissa-aubergine caprese", EMMA, "Bijgerecht", None),
    (1614, "Boterkoek", EMMA, "Zoet & desserts", None),
    (1650, "Pasta met tomaatjes, ansjovis en knoflookamandelcrispies", EMMA, "Hoofdgerecht", None),
    # Immuunboost (p. 48-51)
    (1701, "Tropische havermout", KG, "Bijgerecht", None),
    (1727, "Wortel-geitenkaasplaattaart", KG, "Hoofdgerecht", None),
    (1755, "Erwten-gortrisotto met chorizo", KG, "Hoofdgerecht", None),
    (1781, "Gebakken uien met tex-mexvulling", KG, "Bijgerecht", None),
    (1813, "Herfstige groentesoep", KG, "Soep", None),
    # Gietijzer (p. 52-55)
    (1857, "Sappige lamssteaks met bietencarpaccio", KG, "Hoofdgerecht", None),
    (1901, "Varkensfiletpannetje met aardappel", KG, "Hoofdgerecht", None),
    (1931, "Geroosterde artisjokharten met knoflookrijst", KG, "Hoofdgerecht", None),
    (1957, "Pruimen-appeltaart", KG, "Zoet & desserts", None),
    # Süße Grüße (p. 56-63)
    (1994, "Saffraancake met amandel en frambozen", KG, "Zoet & desserts", None),
    (2033, "Duitse wafels met ijs", KG, "Zoet & desserts", None),
    (2058, "Sinaasappelkwarktaart", KG, "Zoet & desserts", None),
    (2104, "Kruimelkoek met appel en pruim", KG, "Zoet & desserts", None),
    (2144, "Slagroomsoezen met lemoncurd", KG, "Zoet & desserts", None),
    # Toffe peren (p. 64-65)
    (2263, "Perentaart met marsepeinsaus", KG, "Zoet & desserts", None),
]

HEADING_AS = {}
CAPTION_SPLIT = {}
OVERRIDES = {
    # these recipes carry their quantities inside the running text, so the
    # parser finds no ingredient box; the lists below are read out of the text
    "Kaasbezempjes": {
        "ingredients": ["6 plakken kaas", "zoute sticks", "bieslook"],
        "instructions": [
            "Snijd 6 plakken kaas elk in 2 rechthoeken (ca. 6 x 10 cm). Snijd de kaasplakjes in de lengte elke paar millimeter tot de helft in. Leg een zoute stick op het ongesneden deel van een plakje kaas en rol hem in de kaas. Bind vast met bieslook. Herhaal met de rest van de kaas.",
        ],
    },
    # the platbrood's steps are printed inside the soup's block (below), and the
    # soup lost its own steps to them, so both recipes get their text back
    "Knapperig platbrood met druiven en crème fraîche": {
        "ingredients": [
            "30 g verse gist (of 12 g droge gist)", "400 g bloem (+ bestuiven)",
            "1 tl suiker", "zout en peper", "10 el olijfolie", "10 takjes tijm",
            "400 g kleine, pitloze rode druiven", "400 g crème fraîche",
            "3-4 rode uien", "2 lente-uitjes",
        ],
        "instructions": [
            "VOOR HET DEEG Roer de gist en 200 ml lauwwarm water door elkaar. Doe de bloem, de suiker en een snufje zout in een kom en maak een kuiltje in het midden. Voeg 8 el olie en het gistwater toe en kneed alles tot een glad deeg. Laat het deeg afgedekt op een warme plek ca. 45 minuten rijzen.",
            "VOOR DE TOPPING Was de tijm en de druiven. Neem de druiven van de takjes en halveer ze. Hak de tijm fijn. Breng de crème fraîche op smaak met flink wat zout en peper. Pel de uien, halveer ze en snijd ze in dunne halve ringen. Was de lente-uitjes, snijd ze in ringetjes en meng ze met de druiven.",
            "Verdeel het deeg op een met bloem bestoven werkblad in acht stukken. Vorm van elk stuk een bolletje en rol het uit tot een ovaal platbrood (ca. 12 cm). Leg de platbroden op twee met bakpapier beklede bakplaten en laat nog ca. 15 minuten rijzen.",
            "Verwarm de oven voor (elektrisch: 220°C / hetelucht: 200°C). Bestrijk de platbroden met de crème fraîche en laat daarbij een randje vrij. Verdeel de rode ui, de druiven met lente-ui en de tijm gelijkmatig over de broden en besprenkel met 2 el olie. Bak de broden in ca. 15 minuten gaar in de oven.",
        ],
    },
    "Uiensoep met pannenkoek": {
        "ingredients": [
            "4 grote uien", "2 grote tomaten", "2 el olie",
            "2 grote runderschenkels met been (ca. 1 kg)", "500 g soepgroente (zak)",
            "2 laurierblaadjes", "1 el zwarte peperkorrels", "5 pimentkorrels",
            "zout en peper", "100 g bloem", "200 ml melk", "2 eieren",
            "50 ml water met koolzuur", "5 el boter", "½ bosje bieslook",
        ],
        "instructions": [
            "VOOR DE BOUILLON Halveer 1 ui en bak hem op hoog vuur in een grote, droge pan. Snijd een kruisje in de tomaten. Neem de ui uit de pan. Verhit 1 el olie in de pan en bak de schenkels er kort in aan. Blus af met 3,5 l water, breng aan de kook en schep het schuim eraf. Voeg de ui, de tomaten, de soepgroente, de laurier, de peperkorrels, de pimentkorrels en 1 el zout toe. Laat op laag vuur ca. 2 uur en 30 minuten zachtjes koken.",
            "VOOR DE PANNENKOEK Roer de bloem, de melk, de eieren en een snufje zout door elkaar. Laat het beslag ca. 30 minuten rusten. Roer het prikwater erdoorheen. Verhit 3 el boter in porties in een kleine koekenpan (ca. 18 cm Ø). Bak ca. 6 pannenkoeken van het beslag, rol ze op en laat afkoelen. Snijd de rolletjes schuin in plakjes. Pel 3 uien en snijd ze in dunne ringen. Verhit 2 el boter en 1 el olie in een koekenpan en bak de ui er ca. 15 minuten in. Breng op smaak met zout.",
            "Schenk de bouillon door een met kaasdoek beklede zeef. Breng op smaak met zout en peper. Was de bieslook en hak hem fijn. Serveer de soep met de pannenkoek, de ui en de bieslook.",
        ],
    },
}
