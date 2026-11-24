"""Issue-specific data for Koken & genieten KG2507 (juli 2025, jaargang 20).

Summer issue ("en zonnig buffet"), 66 pages.  Same shape as extract.py's
built-in KG2510 tables, so the engine processes this issue unchanged:

    python convert_pdf.py --pdf KG2507.pdf --md KG2507.md
    python add_images.py  --issue 2507
    python extract.py     --issue 2507 --write --out recipes-2507.json
"""
ISSUE = "7-2025"
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "2025-07"
ISSUE_AS_LABEL = True

PDF = "KG2507.pdf"
MD = "KG2507.md"
OUT = "recipes-2507.json"
IMAGE_FOLDER = "images-2507"

PAULINE = "Uit Paulines Keuken"
CHING = "Ching-He Huang"           # the "Wok express" book preview
JACQUELINE = "Jacqueline Sluijter"  # the "4x lekker" avocado pages
KG = "Koken & genieten"

# column labels, section titles and advert lines that are not ingredients
EXTRA_NOISE = {
    "Uit Paulines Keuken", "Receptuur: Uit Paulines Keuken Fotografie: Marianne Snel",
    "In de buitenlucht", "Of je worst lust", "Boek", "Lekker uit de wok",
    "Diner en blanc", "Proteïnepower", "4x lekker", "Gek op kaas",
    "Korrels met karakter", "Zoet zomerfruit", "Fruit van de boom",
    "Sprookjestaart", "Coverrecept", "Eiwithype",
    "Receptuur: Jacqueline Sluijter Fotografie: Sander Damen",
    "Titel: Wok express", "Auteur: Ching-He Huang", "Fotografie: Tamin Jones",
    "Prijs: 24,00 euro", "Uitgeverij: Becht", "Tekst: Yvonne Doorten",
}

# (line of the "## " heading, full name, author, category, total time override)
RECIPE_TABLE = [
    # Uit Paulines keuken (p. 6-11)
    (310, "Aardbeientiramisu", PAULINE, "Zoet & desserts", None),
    (351, "Gazpacho", PAULINE, "Soep", None),
    (393, "Carpacciopastasalade", PAULINE, "Salade", None),
    (446, "Griekse wraps", PAULINE, "Hoofdgerecht", None),
    (492, "Tomatencouscous met feta", PAULINE, "Bijgerecht", None),
    # In de buitenlucht (p. 12-19)
    (549, "Citroenrisotto met gesmoorde komkommer en garnalen", KG, "Hoofdgerecht", None),
    (588, "BBQ-enchilada’s caprese met entrecote", KG, "Hoofdgerecht", None),
    (623, "Romige pestokip met feta", KG, "Hoofdgerecht", None),
    (662, "Varkenshaas in knoflookboter", KG, "Hoofdgerecht", None),
    (704, "Zomerse groentekokossoep met hartige wentelteefjes", KG, "Soep", None),
    # Of je worst lust (p. 20-25)
    (802, "Bruschetta-worstrolletjes", KG, "Bijgerecht", None),
    (848, "Zomers chorizobonenpannetje", KG, "Hoofdgerecht", None),
    (891, "Gevulde paprika met venkelworst", KG, "Hoofdgerecht", None),
    (938, "Lichte ragout met worstballetjes", KG, "Hoofdgerecht", None),
    # Boek: Wok express (p. 26-31)
    (1034, "Hete zoetzure kip", CHING, "Hoofdgerecht", None),
    (1079, "Sperzieboontjes op silken tofu", CHING, "Bijgerecht", None),
    (1129, "Biefstuk met spicy ponzu-saus", CHING, "Hoofdgerecht", None),
    (1178, "Roerbak van satékip met pittige kokos-pindasaus", CHING, "Hoofdgerecht", None),
    # Diner en blanc (p. 32-39)
    (1252, "Honing-chilikalkoen met komkommerrelish", KG, "Hoofdgerecht", None),
    (1299, "Aardappelcarpaccio met hamroom", KG, "Bijgerecht", None),
    (1342, "Orzosalade met garnalen", KG, "Salade", None),
    (1386, "Kokos-kersentiramisu", KG, "Zoet & desserts", None),
    (1430, "Camembertdip met abrikoos", KG, "Bijgerecht", None),
    (1440, "Krokante baguettes", KG, "Bijgerecht", None),
    # Proteïnepower (p. 40-43)
    (1524, "Shakshuka met pompoen", KG, "Hoofdgerecht", None),
    (1561, "Granola met gojibessen", KG, "Bijgerecht", None),
    (1573, "Ontbijtwrap met fruit", KG, "Bijgerecht", None),
    (1584, "Zaden-notenbrood", KG, "Bijgerecht", None),
    # 4x lekker (p. 44-45)
    (1620, "Gehaktballetjes met avocadovulling", JACQUELINE, "Bijgerecht", None),
    (1648, "Avocado-garnalensalade", JACQUELINE, "Salade", None),
    (1671, "Quesadilla’s met avocado en feta", JACQUELINE, "Bijgerecht", None),
    (1705, "Avocadofrietjes", JACQUELINE, "Bijgerecht", None),
    # Gek op kaas (p. 46-49)
    (1735, "Tiramisurol", KG, "Zoet & desserts", None),
    (1778, "Gnocchi met gorgonzolasaus", KG, "Hoofdgerecht", None),
    # Korrels met karakter (p. 50-53)
    (2001, "Runderburgers met peper en cognacsaus", KG, "Hoofdgerecht", None),
    (2053, "Linzenpannetje met groene peper", KG, "Hoofdgerecht", None),
    (2090, "Duits runderstoofpotje met peper", KG, "Hoofdgerecht", None),
    (2124, "Roerei met kampotpeper", KG, "Bijgerecht", None),
    # Zoet zomerfruit (p. 54-55)
    (2152, "Blauwebessengelei met luchtige sabayon", KG, "Zoet & desserts", None),
    (2182, "Perzikcrumble met vanille", KG, "Zoet & desserts", None),
    (2205, "Supersnel cassistoetje", KG, "Zoet & desserts", None),
    (2228, "Verkoelend citroen- en mangoijs", KG, "Zoet & desserts", None),
    # Fruit van de boom (p. 56-63)
    (2264, "Chique kersenmuffins", KG, "Zoet & desserts", None),
    (2307, "Peren met Oostenrijkse buchteln en vanillesaus", KG, "Zoet & desserts", "PT2H05M"),
    (2369, "Abrikozenplaatcake met amandel", KG, "Zoet & desserts", None),
    (2400, "Appeltaart met custard en hazelnoot", KG, "Zoet & desserts", None),
    (2457, "Kruimelcheesecake met kwetsencompote", KG, "Zoet & desserts", None),
    # Sprookjestaart (p. 64-65)
    (2584, "Aardbeien-rozentaart", KG, "Zoet & desserts", None),
    (2624, "Gesuikerde rozen", KG, "Zoet & desserts", "PT2H30M"),
]

HEADING_AS = {}
CAPTION_SPLIT = {}
OVERRIDES = {
    # these recipes carry their quantities inside the running text, so the
    # parser finds no ingredient box; the lists below are read out of the text
    "Camembertdip met abrikoos": {
        "ingredients": [
            "300 g camembert", "200 g crème fraîche", "1 el dijonmosterd",
            "50 g gedroogde abrikozen", "1 bosje bieslook", "zout en peper",
        ],
        "instructions": [
            "Pureer 300 g camembert, 200 g crème fraîche en 1 el dijonmosterd fijn. Hak 50 g gedroogde abrikozen fijn. Was 1 bosje bieslook en hak fijn. Roer samen met de abrikoos door de camembertdip. Breng op smaak met zout en peper. Bestrooi de dip eventueel met bieslookbloemetjes en serveer.",
        ],
    },
    "Granola met gojibessen": {
        "ingredients": [
            "150 g havervlokken", "150 g speltvlokken (bij de supermarkt)",
            "50 g sesamzaad", "150 g pompoenpitten", "100 ml ahornsiroop",
            "100 g gedroogde gojibessen (bij de grotere (ecologische) supermarkt of reformwinkel)",
        ],
        "instructions": [
            "Verwarm de oven voor (elektrisch: 160°C / hetelucht: 140°C). Meng in een kom 150 g havervlokken, 150 g speltvlokken (bij de supermarkt), 50 g sesamzaad en 150 g pompoenpitten met elkaar. Schenk 100 ml ahornsiroop erbij en roer door elkaar. Verdeel het mengsel over een met bakpapier beklede bakplaat en bak ca. 20 minuten in de oven. Schep daarbij regelmatig om. Neem uit de oven en laat afkoelen. Roer 100 g gedroogde gojibessen (bij de grotere (ecologische) supermarkt of reformwinkel) erdoorheen.",
        ],
    },
    "Ontbijtwrap met fruit": {
        "ingredients": [
            "2 kiwi’s", "1 mango", "100 g aardbeien", "125 g blauwe bessen",
            "1 vanillestokje", "250 g skyr (IJslandse yoghurt)", "2 el honing",
            "6 tarwetortilla’s", "40 g gedroogde cranberry’s",
            "50 g havervlokken", "1 el honing",
        ],
        "instructions": [
            "Schil 2 kiwi’s en snijd ze in partjes. Schil 1 mango, snijd het vruchtvlees van de pit en snijd het in plakjes. Was 100 g aardbeien en snijd in plakjes. Was 125 g blauwe bessen. Splijt 1 vanillestokje in de lengte en schraap het merg eruit. Roer het vanillemerg, 250 g skyr (IJslandse yoghurt) en 2 el honing door elkaar. Bestrijk 6 tarwetortilla’s met de skyr en verdeel het fruit erover. Bestrooi met 40 g gedroogde cranberry’s en 50 g havervlokken. Rol de wraps op en besprenkel met 1 el honing.",
        ],
    },
    # the kader with the roses sits before the taart in the Markdown, so its own
    # heading (the second one) carries no text of its own; the "Per stuk" line
    # under it belongs to the taart
    "Gesuikerde rozen": {
        "yield": "decoratie van 1 taart",
        "ingredients": [
            "7-8 onbespoten rozen", "2 eiwitten", "200 g suiker",
        ],
        "instructions": [
            "Verwarm de oven voor (hetelucht: 50°C)*. Was de knopjes en blaadjes van 7-8 onbespoten rozen en dep droog. Klop 2 eiwitten stijf. Doop de rozen erin, bestrooi met 200 g suiker en verdeel over een met bakpapier beklede bakplaat. Bak 90-120 minuten in de oven met de deur op een kier. Draai de rozen tijdens het bakken af en toe om en controleer of ze niet aanbranden. Neem uit de oven en laat de rozen op een droge plek verder drogen.",
            "Een elektrische oven is voor dit recept niet geschikt.",
        ],
        "nutrition": None,
    },
    # the taart's last step runs into the kader heading, and its nutrition line
    # ended up under that heading, so both are put back here
    "Aardbeien-rozentaart": {
        "instructions": [
            "EEN DAG VAN TEVOREN Maak de gesuikerde rozen (zie kader). DE VOLGENDE DAG Klop de eieren, 200 g poedersuiker, de vanillesuiker en een snufje zout in ca. 5 minuten heel romig. Voeg al kloppend langzaam de olie toe. Meng de bloem met de maizena en het bakpoeder en roer afwisselend met de melk in delen kort door het beslag. Doe de helft van het beslag in een ingevette, met bloem bestoven springvorm (26 cm Ø) en strijk glad. Bak in ca. 25 minuten gaar in de oven en laat afkoelen. Neem de cake uit de vorm en was de vorm af. Bak van de rest van het beslag op dezelfde manier nog een cake en laat afkoelen.",
            "VOOR DE CRÈME Week de gelatine in water. Was de aardbeien, verwijder de kroontjes en halveer de aardbeien. Pureer met het citroensap en de vanille. Knijp de gelatine uit, los hem op volgens de aanwijzingen op de verpakking en meng met 2 el aardbeienpuree. Meng het gelatinemengsel met de rest van de puree. Roer de roomkaas, de mascarpone, de crème fraîche, de aardbeienpuree en 100 g poedersuiker door elkaar. Zet de crème ca. 1 uur in de koelkast.",
            "Halveer de cakes horizontaal. Sluit om één cakeplak een taartring en bestrijk met ¹∕₅ van de crème. Leg een tweede cakeplak erop. Herhaal tot alle cake en ⁴∕₅ van de crème opgebruikt zijn. Zet de taart en de overige crème minimaal 5 uur in de koelkast. Neem de taart uit de taartring. Roer de overige crème door en bestrijk de rand van de taart ermee. Versier met de gesuikerde rozen.",
        ],
        "nutrition": {
            "@type": "NutritionInformation", "calories": "560 kcal",
            "proteinContent": "10 g", "fatContent": "37 g",
            "carbohydrateContent": "43 g",
        },
    },
    # the magazine prints "41 g koolhdyraten" (sic), which the nutrition line
    # cannot be parsed from, so the values are given here
    "Kruimelcheesecake met kwetsencompote": {
        "nutrition": {
            "@type": "NutritionInformation", "calories": "440 kcal",
            "proteinContent": "10 g", "fatContent": "25 g",
            "carbohydrateContent": "41 g",
        },
    },
}
