"""Issue-specific data for Koken & genieten KG2511 (november 2025, jaargang 20).

Same shape as the tables built into extract.py for KG2510, so the engine can
process this issue unchanged:

    python convert_pdf.py --pdf KG2511.pdf --md KG2511.md
    python add_images.py  --issue 2511
    python extract.py     --issue 2511 --write
"""
ISSUE = "11-2025"
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "2025-11"
ISSUE_AS_LABEL = True

PDF = "KG2511.pdf"
MD = "KG2511.md"
OUT = "recipes-2511.json"
IMAGE_FOLDER = "images-2511"

PAULINE = "Uit Paulines Keuken"
KG = "Koken & genieten"

# column labels and section titles that are not ingredients
EXTRA_NOISE = {
    "Seizoen", "De snelle keuken", "Kookboek", "Knus in de keuken",
    "Dat kwaakt naar meer!", "Simpel en snel genieten", "Hartverwarmende hapjes",
    "Het beste van broccoli", "Oma’s ovengerechten", "Herfstige toetjes",
    "Goudkoorts in de keuken", "Zwart & wit", "Uit Paulines Keuken",
    "Uit Paulines keuken", "Coverrecept", "gourmetgids", "cadeau!",
}

# (line of the "## " heading, full name, author, category, total time override)
RECIPE_TABLE = [
    (295, "Ajam pangang", PAULINE, "Hoofdgerecht", None),
    (341, "Marokkaanse couscous", PAULINE, "Bijgerecht", None),
    (380, "Appelkruimelplaatcake", PAULINE, "Zoet & desserts", None),
    (427, "Lasagne puttanesca", PAULINE, "Hoofdgerecht", None),
    (482, "Indiase kikkererwtensoep", PAULINE, "Soep", None),
    (529, "Wildstoof met spaghetti en romige savooiekool", KG, "Hoofdgerecht", None),
    (598, "Uienquiche met cranberryjam", KG, "Hoofdgerecht", None),
    (643, "Gestoofde runderwangen", KG, "Hoofdgerecht", None),
    (705, "Parelgort-groentemaaltijdsoep met broodharten", KG, "Soep", None),
    (753, "Ribeye met koolraapfriet", KG, "Hoofdgerecht", None),
    (888, "Pekingeend met pannenkoekjes", KG, "Hoofdgerecht", None),
    (937, "Eendenbouillon met knödels", KG, "Soep", None),
    (985, "Eendenspiesen met rodekoolsla", KG, "Hoofdgerecht", None),
    (1112, "Romige pasta met savooiekool", KG, "Hoofdgerecht", None),
    (1151, "Gehaktballetjes in tomaten-paprikasaus", KG, "Hoofdgerecht", None),
    (1187, "Kruidige zoete-aardappelcurry", KG, "Hoofdgerecht", None),
    (1224, "Winterburger met aardappelpartjes", KG, "Hoofdgerecht", None),
    (1261, "Gyrossteaks op warme witte kool", KG, "Hoofdgerecht", None),
    (1294, "Snelle salade met worst", KG, "Salade", None),
    (1326, "Gebakken vis met snelle aardappelsalade", KG, "Hoofdgerecht", None),
    (1358, "Pittige tomatensoep met krokante topping", KG, "Soep", None),
    (1421, "Kleurrijke saladekrans", KG, "Salade", None),
    (1465, "Bonensoep met procureur", KG, "Soep", None),
    (1489, "Bladerdeeg-fetapasteitjes", KG, "Bijgerecht", None),
    (1530, "Rodewijn-rozemarijnzout", KG, "Bijgerecht", None),
    (1541, "Citroen-limoenolie", KG, "Bijgerecht", None),
    (1552, "Zoete sneeuwballetjes met koffiemousse", KG, "Zoet & desserts", None),
    (1603, "Chocoappels", KG, "Zoet & desserts", None),
    (1631, "Witte vanillesinaasappelglühwein", KG, "Drank", None),
    (1645, "Chocoladeglühwein", KG, "Drank", None),
    (1674, "Aziatische omelet met aspergebroccoli", KG, "Hoofdgerecht", None),
    (1713, "Groene soep met knoflookcroutons", KG, "Soep", None),
    (1741, "Broccolikikkererwtensalade", KG, "Salade", None),
    (1779, "Mini-ovenschotels met broccoli en hazelnoten", KG, "Hoofdgerecht", None),
    (1826, "Vis Wellington", "Oma Bep Boon", "Hoofdgerecht", None),
    (1881, "Witlof met kip en boursin", "Oma Anny", "Hoofdgerecht", None),
    (1910, "Zalmstrudel met pistachenoten", "Oma Bep Boon", "Hoofdgerecht", None),
    (1954, "Franse kip uit de oven", "Oma Donna", "Hoofdgerecht", None),
    (2028, "Peperkoek-sinaasappeltrifle", KG, "Zoet & desserts", None),
    (2055, "Pannacotta met kaneelpruimen", KG, "Zoet & desserts", None),
    (2087, "Pannenkoekenovenschotel", KG, "Zoet & desserts", None),
    (2121, "Chocolade-kastanjetoetje", KG, "Zoet & desserts", None),
    (2155, "Amsterdamse koggetjes", KG, "Zoet & desserts", None),
    (2201, "Choco-karamellaagjestaart", KG, "Zoet & desserts", None),
    (2252, "Appel-kwarktaart met karamelsaus", KG, "Zoet & desserts", None),
    (2292, "Snelle karamelkrokant", KG, "Zoet & desserts", None),
    (2305, "Chocolade-karamelrepen", KG, "Zoet & desserts", None),
    (2344, "Banoffeetaart met meringuetoefjes", KG, "Zoet & desserts", None),
    (2458, "Botercrème-maanzaadtaart", KG, "Zoet & desserts", None),
]

# one wide photo on the contents page holds two recipes side by side
CAPTION_SPLIT = {
    "Appel-kwarktaart Snelle karamelkrokant met karamelsaus": [
        "Appel-kwarktaart met karamelsaus", "Snelle karamelkrokant"],
}

OVERRIDES = {
    # page 36 puts the two recipes next to each other, so the steps of the soup
    # ended up between the ingredients of the pasteitjes
    "Bonensoep met procureur": {
        "ingredients": [
            "4-5 wortels", "1 knolselderij (ca. 750 g)", "2 uien",
            "2 teentjes knoflook",
            "1,2 kg gerookte procureur, zonder been (bij de slager)",
            "2 laurierblaadjes", "5 jeneverbessen", "zout en peper",
            "2 el tomatenpuree", "2 tl paprikapoeder",
            "½ tl pittig paprikapoeder",
            "250 g witte bonen (blik, uitlekgewicht)",
            "250 g kidneybonen (blik, uitlekgewicht)",
            "400 g witte bonen in tomatensaus (blik)", "6 takjes peterselie",
        ],
        "instructions": [
            "Schil de wortels en de knolselderij, was ze en snijd de helft grof. Pel de uien en de knoflook en snipper ze grof. Dep de procureur droog. Doe de procureur in een grote pan en bedek met ca. 2 liter water. Voeg de laurierblaadjes en de jeneverbessen toe. Breng aan de kook en laat ca. 10 minuten zachtjes koken. Schep het ontstane schuim eraf. Bestrooi met zout en peper. Voeg de grof gesneden groenten, de ui, de knoflook, de tomatenpuree en beide soorten paprikapoeder toe en laat de procureur in nog ca. 30 minuten gaar koken.",
            "Snijd de overige groenten in blokjes van ca. 1 cm. Neem de procureur uit de bouillon en snijd het vlees in kleine stukjes. Schenk de bouillon door een zeef in een tweede pan en wrijf de groenten door de zeef. Giet de witte bonen en de kidneybonen af en voeg ze toe aan de bouillon. Voeg ook de witte bonen in tomatensaus toe. Voeg de kleine groenteblokjes toe. Breng alles aan de kook en laat 10-12 minuten zachtjes koken. Voeg de stukjes vlees toe en verwarm kort. Breng de soep op smaak met zout en peper. Was de peterselie en hak hem fijn. Serveer de soep en bestrooi met de peterselie. Lekker met een lepel crème fraîche.",
        ],
    },
    "Bladerdeeg-fetapasteitjes": {
        "instructions": [
            "Laat de feta goed uitlekken en snijd elke plak in drieën. Neem de vellen filodeeg uit de verpakking. Smelt de boter. Leg 3 vellen deeg op het werkblad. Bestrijk één vel met de gesmolten boter, leg het tweede vel erop en bestrijk opnieuw. Leg het derde vel erop en bestrijk ook dit met de boter. Snijd de stapel deeg in 4 gelijke stukken.",
            "Was de citroen en rasp de schil er fijn af. Was de tijm, neem de blaadjes van de takjes en hak ze fijn. Leg op elk stuk filodeeg een stuk feta. Bestrooi met wat citroenschil en tijm. Vouw of rol het deeg om de feta heen tot kleine pakketjes. Bestrijk de deegpakketjes dun met de overige boter. Herhaal dit proces met nog 6 vellen deeg en de rest van de feta.",
            "Verwarm de oven voor (elektrisch: 180°C / hetelucht: 160°C). Leg de fetapakketjes op een met bakpapier beklede bakplaat. Bak ze in 25-30 minuten goudbruin in de oven. Steek uit het resterende vel deeg sterren van verschillende groottes en leg deze op een met bakpapier beklede bakplaat. Bestrijk ze met boter. Bak de sterren in 8-10 minuten goudbruin in de hete oven. Besprenkel de fetapasteitjes met de honing. Garneer met de deegsterren en eventueel wat tijm.",
        ],
    },
    # these four carry their quantities inside the running text
    "Rodewijn-rozemarijnzout": {
        "ingredients": ["600 g grof zeezout", "150 ml rode wijn",
                        "3 takjes rozemarijn"],
        "instructions": [
            "Verwarm de oven voor (elektrisch: 80°C / hetelucht: 60°C). Doe 600 g grof zeezout in een kom. Schenk 150 ml rode wijn er geleidelijk bij en meng alles goed. Verdeel het zout over een met bakpapier beklede bakplaat. Laat het ca. 3 uur in de oven drogen met de ovendeur op een kier. Roer het zout regelmatig om. Droog het zout tot de wijn volledig verdampt is. Was 3 takjes rozemarijn, dep goed droog en hak fijn. Neem de bakplaat uit de oven en roer de rozemarijn door het zout. Laat volledig afkoelen. Verdeel het zout over 8 potjes.",
        ],
    },
    "Citroen-limoenolie": {
        "ingredients": ["2 bio-limoenen", "1 grote bio-citroen",
                        "4 takjes tijm", "600 ml olijfolie"],
        "instructions": [
            "Was 2 bio-limoenen en 1 grote bio-citroen met heet water en wrijf ze goed droog. Schil de schil er met een dunschiller in lange, dunne spiralen af. Verdeel de schillen over 2 schone flessen. Was 4 takjes tijm, dep hem goed droog en doe 2 takjes in elke fles. Schenk 600 ml olijfolie erbij en zorg ervoor dat de schillen en de kruiden volledig bedekt zijn. Sluit de flessen goed af. Laat de olie 2-3 weken op een donkere en koele plek trekken. Schud de flessen regelmatig.",
        ],
    },
    "Witte vanillesinaasappelglühwein": {
        "ingredients": [
            "ca. 5 cm gember", "500 ml sinaasappelsap",
            "750 ml droge witte wijn", "1½ tl kaneel", "8 g vanillesuiker",
            "1 sanufje gemalen anijszaad", "3 kruidnagels", "3 el suiker",
            "schijfjes bio-sinaasappel, om te garneren",
        ],
        "instructions": [
            "Schil ca. 5 cm gember en snijd grof. Meng in een pan 500 ml sinaasappelsap, 750 ml droge witte wijn, de gember, 1½ tl kaneel, 8 g vanillesuiker, 1 sanufje gemalen anijszaad, 3 kruidnagels en 3 el suiker met elkaar. Verhit het mengsel (laat het niet koken!) en laat 10-15 minuten trekken. Serveer heet. Garneer naar wens met schijfjes bio-sinaasappel in het glas.",
        ],
    },
    "Chocoladeglühwein": {
        "ingredients": [
            "500 ml rode wijn", "300 ml rode port", "2 kaneelstokjes",
            "2 steranijs", "2 kruidnagels", "4 el lichte basterdsuiker",
            "1 l melk", "300 g pure chocolade",
            "toef stijfgeklopte slagroom, om te garneren",
        ],
        "instructions": [
            "Verwarm in een pan 500 ml rode wijn, 300 ml rode port, 2 kaneelstokjes, 2 steranijs, 2 kruidnagels en 4 el lichte basterdsuiker en laat op laag vuur ca. 15 minuten trekken. Verwarm intussen de melk in een andere pan. Hak 300 g pure chocolade grof en laat hem al roerend op laag vuur smelten in 1 l melk. Schenk het rode-wijnmengsel door een zeef langzaam bij de hete chocolademelk. Serveer de hete chocoladeglühwein direct. Garneer naar wens met een toef stijfgeklopte slagroom.",
        ],
    },
    "Snelle karamelkrokant": {
        "ingredients": ["200 g suiker"],
        "instructions": [
            "Bekleed een bakplaat met het bakpapier. Karamelliseer 200 g suiker in een pan tot hij goudbruin is. Schenk direct op het bakpapier. Strijk eventueel glad met een paletmes. Laat hard worden. Breek in stukken en bewaar luchtdicht. Gebruik als decoratie of (fijngehakt) als strooisel voor taarten of klein gebak.",
        ],
    },
}
