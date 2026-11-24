"""Issue-specific data for Koken & genieten KG2212 (december 2022).

Christmas issue, 90 pages, the older 2022 layout.  Same shape as extract.py's
built-in KG2510 tables, so the engine processes this issue unchanged:

    python convert_pdf.py --pdf KG2212.pdf --md KG2212.md
    python add_images.py  --issue 2212
    python extract.py     --issue 2212 --write --out recipes-2212.json
"""
ISSUE = "12-2022"
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "2022-12"
ISSUE_AS_LABEL = True

PDF = "KG2212.pdf"
MD = "KG2212.md"
OUT = "recipes-2212.json"
IMAGE_FOLDER = "images-2212"

DONNA = "Donna Hay"                # the "Kerstmis" book (p. 14-19)
RUDOLPH = "Rudolph van Veen"       # the "Rudolph's Kitchen" book (p. 22-27)
JACQUELINE = "Jacqueline Sluijter"  # the Coop christmas menu (p. 36-39)
SUSAN = "Susan Aretz"              # the "Altijd Borreltijd" book (p. 66-71)
MONCHOU = "MonChou"                # the MonChou pages (p. 20-21 and 52-55)
KG = "Koken & genieten"

# column labels, section titles and advert lines that are not ingredients
EXTRA_NOISE = {
    "Brenda Kookt", "Kerstborrel", "Lekker feestelijk zonder vlees",
    "Groots uitpakken", "Lekker feestelijk", "De hele week genieten",
    "Simpel en snel genieten", "De zoete afsluiter", "De ster van de tafel",
    "Lekker prikken", "Kerstkoekjes", "Een cadeautje om op te eten",
    "Auteur: Donna Hay", "Receptuur: Donna Hay Fotografie: Chris Court, Ben Dearnley, William Meppem, Con Poulos, Anson Smart",
    "Titel: Rudolph’s Kitchen –", "Auteur: Rudolph van Veen",
    "Receptuur, styling en foodstyling: Jacqueline Sluĳter Foto’s: Sander Damen",
    "Receptuur: Susan Aretz", "Auteur: Susan Aretz",
    # the MonChou advert that the magazine prints inside the TiraMonChou recipe
    "MONCHOU® ALS BLIJVERTJE IN DE KOELKAST",
    "Je kent MonChou natuurlijk van de MonChoutaart, een oer-Hollandse",
    "traditie. Want hoe Frans de naam MonChou ook klinkt, MonChou is",
    "een Nederlands merk. Gebruik hem niet alleen voor deze taart, maar",
    "houd hem standaard in je koelkast, want je kunt er alle kanten mee",
    "op. Van toetjes tot borrelhapjes en van cheesecake tot pastasaus.",
    "monchou.nl", "}KOKEN & GENIETEN",
    # the size of an icing nozzle that wrapped onto its own line
    "(ca. 5 mm Ø)",
}

# (line of the "## " heading, full name, author, category, total time override)
RECIPE_TABLE = [
    # Lekker feestelijk zonder vlees (p. 6-9)
    (367, "Gevulde flespompoen met knapperige driehoekjes", KG, "Hoofdgerecht", None),
    (415, "Bietenrisotto met bietenchips en notencrunch", KG, "Hoofdgerecht", None),
    (462, "Gegratineerde zoete aardappel met geitenkaas en rodekool", KG, "Hoofdgerecht", None),
    # Zoete & sappige mandarijnen (p. 10-13)
    (509, "Winterse salade met mandarijn, vijgen en geitenkaas", KG, "Salade", None),
    (540, "Mandarijnencocktail", KG, "Drank", None),
    (553, "Gebakken zalmzijde in sherrymandarijnenmarinade", KG, "Hoofdgerecht", None),
    (592, "Omgekeerde mandarijnencake", KG, "Zoet & desserts", None),
    # Boek Kerstmis (Donna Hay, p. 14-19)
    (641, "Met biet en zout ingelegde forel", DONNA, "Bijgerecht", None),
    (695, "In citroentijm gepekelde kalkoen", DONNA, "Hoofdgerecht", None),
    (738, "Aardappel-kruidenbroodkrans", DONNA, "Bijgerecht", None),
    # TiraMonChou (p. 20-21)
    (798, "TiraMonChou", MONCHOU, "Zoet & desserts", None),
    # Boek Rudolph's Kitchen (p. 22-27)
    (968, "Borrelhapjeskrans", RUDOLPH, "Bijgerecht", None),
    (1000, "Heisse Liebe", RUDOLPH, "Zoet & desserts", None),
    (1054, "Italiaanse hartige oliebollen", RUDOLPH, "Bijgerecht", None),
    (1105, "Champagnetaart", RUDOLPH, "Zoet & desserts", None),
    # De hele week genieten (p. 28-35)
    (1205, "Warme aardappelsalade met rosbiefrolletjes", KG, "Salade", None),
    (1252, "Aziatisch kalkoenpannetje", KG, "Hoofdgerecht", None),
    (1298, "Roggebroodpannenkoekjes met ham", KG, "Hoofdgerecht", None),
    (1333, "Bloemkoolballetjes met rodekoolsalade", KG, "Bijgerecht", None),
    (1377, "Choco-granola", KG, "Bijgerecht", None),
    (1390, "Snoekbaarsfilet met romige appelzuurkool", KG, "Hoofdgerecht", None),
    (1439, "Limoenmousse met passievrucht", KG, "Zoet & desserts", None),
    (1463, "Tiramisu met bosvruchten", KG, "Zoet & desserts", None),
    (1499, "Crêpes Suzette met sinaasappel", KG, "Zoet & desserts", None),
    # Kerst met COOP (Jacqueline Sluijter, p. 36-39)
    (1539, "Salade met gebakken peer en geitenkaas", JACQUELINE, "Salade", "PT25M"),
    (1583, "Biefstuk met sjalotten-portsaus en knapperige sterren", JACQUELINE, "Hoofdgerecht", None),
    (1677, "Butterscotch-ijstaart met nougatine en meringueschuimpjes", JACQUELINE, "Zoet & desserts", None),
    # Simpel en snel genieten (p. 40-43)
    (1794, "Bulgursalade met kip", KG, "Salade", None),
    (1829, "Gekruide karbonade met amandelbroccoli", KG, "Hoofdgerecht", None),
    (1869, "Aardappelsoep met gember en pistachegremolata", KG, "Soep", None),
    (1916, "Broodje smac-burger met gekarameliseerde uien", KG, "Hoofdgerecht", None),
    # Winterse cocktails (p. 44-45)
    (1964, "Cranberry mule", KG, "Drank", None),
    # this drink has no "## " heading of its own (the magazine prints its name
    # over two lines), so the block starts at the line below; the number is the
    # ingredient box's line in the *generated* Markdown
    (2068, "Brandy spritz", KG, "Drank", None),
    (1989, "Winterfizz sangria", KG, "Drank", None),
    (1999, "Roze Winterse", KG, "Drank", None),
    # De zoete afsluiter (p. 46-51)
    (2018, "Kersen-speculaastiramisu", KG, "Zoet & desserts", None),
    (2056, "Kerstmutsen", KG, "Zoet & desserts", None),
    (2066, "Pruimensorbet met yoghurt-amarettoroom", KG, "Zoet & desserts", None),
    (2107, "Gebakken appeltjes met vanillesaus", KG, "Zoet & desserts", None),
    (2149, "Glühwein-dessert met sinaasappel-vanillesaus", KG, "Zoet & desserts", None),
    (2173, "Cranberry-cheesecake in een glaasje", KG, "Zoet & desserts", None),
    (2212, "Mini-ijstaartjes met notencrunch", KG, "Zoet & desserts", None),
    # Feestelijk borrelen met MonChou (p. 52-55)
    (2344, "Wonton-bakjes met MonChou en spekjes", MONCHOU, "Bijgerecht", "PT1H30M"),
    (2384, "Bladerdeegsterren met MonChou, zalm en parmaham", MONCHOU, "Bijgerecht", "PT1H40M"),
    (2424, "MonChou-truffels in vier smaken", MONCHOU, "Zoet & desserts", "PT20M"),
    (2453, "Gevulde eitjes met MonChou", MONCHOU, "Bijgerecht", "PT20M"),
    (2483, "Gevulde jalapeño’s met MonChou en spek", MONCHOU, "Bijgerecht", "PT45M"),
    (2527, "Flammkuchen met MonChou, courgette en parmaham", MONCHOU, "Hoofdgerecht", "PT45M"),
    # De ster van de tafel (p. 56-59)
    (2593, "Chocolade-dripcake met koffiecrème, pecannoten en karamel", KG, "Zoet & desserts", None),
    # Fonduefeestje! (p. 60-65)
    (2758, "Groentebouillon", KG, "Bijgerecht", None),
    (2799, "Ei-augurkendip", KG, "Bijgerecht", None),
    (2823, "Auberginemousse", KG, "Bijgerecht", None),
    (2852, "Sinaasappel-tapenade", KG, "Bijgerecht", None),
    (2872, "Lekker prikken", KG, "Hoofdgerecht", None),
    (2890, "Mozzarella-mascarponeterrine", KG, "Bijgerecht", None),
    (2929, "Rodebieten-taboulé", KG, "Bijgerecht", None),
    (2957, "Frisse salade met aardappel-mosterddressing", KG, "Salade", None),
    (2988, "Parmaham-pestostengels", KG, "Bijgerecht", None),
    (3007, "Spek-fruitrolletjes", KG, "Bijgerecht", None),
    (3019, "Bloody Mary-soep", KG, "Soep", None),
    # Boek Altijd Borreltijd (Susan Aretz, p. 66-71)
    (3108, "Bladerdeeghapjes met brie en cranberry", SUSAN, "Bijgerecht", None),
    (3140, "Burrata met bloedsinaasappelmarmelade en roggebroodkruim", SUSAN, "Bijgerecht", None),
    (3196, "Komkommerrolletjes met gerookte zalm en kruidenmascarpone", SUSAN, "Bijgerecht", None),
    (3222, "Gebakken polenta met tapenade", SUSAN, "Bijgerecht", None),
    (3264, "Trio van tex-mex salsa", SUSAN, "Bijgerecht", None),
    # Koekjes van eigen deeg (p. 72-79)
    (3320, "Chocolade-hazelnootblokjes", KG, "Zoet & desserts", None),
    (3361, "Gemberkoekjes met lemoncurd", KG, "Zoet & desserts", None),
    (3398, "Sinaasappel-tijmkransjes", KG, "Zoet & desserts", None),
    (3428, "Dennenboom-koekjes met citroenglazuur", KG, "Zoet & desserts", None),
    (3471, "Vanillekoekjes met amandelen", KG, "Zoet & desserts", None),
    (3498, "Chocolade-notenkoekjes", KG, "Zoet & desserts", None),
    (3531, "Amandelpralines met sinaasappellikeur", KG, "Zoet & desserts", None),
    (3573, "Matcha-berenklauwtjes", KG, "Zoet & desserts", None),
    (3602, "Mini-kaneelkoekjes", KG, "Zoet & desserts", None),
    # Een cadeautje om op te eten (p. 80-81)
    (3719, "Choco-whisky-kersencake in een potje", KG, "Zoet & desserts", None),
]

HEADING_AS = {}
CAPTION_SPLIT = {}
# the fondue platter is the one recipe the magazine prints without a time
NO_TIME_OK = {"Lekker prikken"}
OVERRIDES = {
    # these print no ingredient list: the quantities sit in the running text
    "Mandarijnencocktail": {
        "ingredients": [
            "2 el suiker", "2 takjes rozemarijn", "8 mandarijnen",
            "1 bio-mandarijn", "120 ml droge sherry",
            "750 ml gekoelde prosecco", "ijsblokjes",
        ],
    },
    "Choco-granola": {
        "ingredients": [
            "100 g hazelnoten", "150 g havervlokken", "150 g speltvlokken",
            "100 g gepofte granen (bijv. rijst of boekweit)", "5 el chiazaad",
            "50 g cacaonibs", "130 ml kokosvet", "6 el ahornsiroop",
            "180 ml sojamelk", "3-4 el cacaopoeder",
        ],
    },
    "Cranberry mule": {
        "ingredients": [
            "250 ml wodka", "250 ml cranberrysap", "2 bio-limoenen",
            "3 takjes basilicum", "1 l ginger beer", "1 granaatappel",
            "crushed ice",
        ],
    },
    "Brandy spritz": {
        "ingredients": [
            "250 ml water", "1 kaneelstokje", "8 kruidnagels", "2 steranijs",
            "de dunne schil van 1 bio-sinaasappel", "60 g suiker",
            "1 rode appel (bijv. elstar)", "75 ml brandy",
            "3 takjes citroenmelisse", "750 ml bruisend mineraalwater",
            "750 ml gekoelde prosecco",
        ],
    },
    "Winterfizz sangria": {
        "ingredients": [
            "1 l grapefruitsap", "4 el citroensap", "50 ml suikersiroop",
            "500 ml gin", "1 bio-grapefruit", "1,5 l bruisend mineraalwater",
            "ijsblokjes",
        ],
    },
    "Roze Winterse": {
        "ingredients": [
            "250 g frambozen (diepvries)", "3 el citroensap", "4 el suiker",
            "5 el grand marnier (sinaasappellikeur)", "250 g frambozen (diepvries)",
            "750 ml gekoelde roséwijn", "750 ml bruisend mineraalwater",
            "takjes munt, om te garneren",
        ],
    },
    "Parmaham-pestostengels": {
        "ingredients": [
            "2 rollen vers pizzadeeg (koelvak)", "6-8 el pesto (pot)",
            "30 plakjes parmaham",
        ],
    },
    "Spek-fruitrolletjes": {
        "ingredients": [
            "200 g gedroogde pruimen", "200 g gedroogde abrikozen",
            "200 g gedroogde dadels", "150 g amandelen zonder vlies",
            "400 g plakken ontbijtspek",
        ],
    },
    "Lekker prikken": {
        "ingredients": [
            "750 g kipfilet", "750 g ossenhaas", "600 g zalmfilet",
            "350 g rauwe garnalen (zonder kop en schaal)", "750 g broccoli",
            "500 g braadworst", "800 g artisjokharten (blik)",
            "1 kg krieltjes",
        ],
    },
    # the calories of this one are printed apart from its macros
    "Choco-whisky-kersencake in een potje": {
        "nutrition": {
            "@type": "NutritionInformation", "calories": "869 kcal",
            "proteinContent": "10 g", "fatContent": "30 g",
            "carbohydrateContent": "90 g",
        },
    },
    # these two sit on the MonChou section page, which repeats their titles, so
    # the engine starts their block on that page instead of at the recipe
    "Wonton-bakjes met MonChou en spekjes": {
        "yield": "12 stuks",
        "ingredients": [
            "12 wonton-deegvellen (diepvries, van de toko)",
            "olie (om te bestrijken)",
            "200 g MonChou Original, op kamertemperatuur", "2 el zure room",
            "½ limoen, de schil geraspt, uitgeperst", "1 tl knoflookpoeder",
            "1 tl uienpoeder", "zout en peper", "30 g uitgebakken spekjes",
            "2 verse jalapeñopepers, zaadlijsten verwijderd, fijngehakt",
            "2 lente-uitjes, in ringetjes",
        ],
        "instructions": [
            "Verwarm de oven voor (elektrisch: 205°C / hetelucht: 185°C). Laat de wontonvellen ontdooien op een schoon werkblad. Bestrijk de wontonvellen aan beide zijden licht met olie en duw ze in de holtes van het bakblik. Bak in ca. 10 minuten knapperig in de oven. Haal uit de oven en laat de bakjes afkoelen op een rooster.",
            "Roer de MonChou in een kom los. Roer de zure room, de limoenschil en het sap, het knoflookpoeder en het uienpoeder erdoorheen en breng op smaak met zout en peper. Vul de spuitzak met het MonChoumengsel en spuit toefjes in de afgekoelde wontonbakjes. Garneer met de spekjes, de jalapeño en de lente-ui.",
        ],
    },
    "Bladerdeegsterren met MonChou, zalm en parmaham": {
        "yield": "ca. 18 stuks",
        "ingredients": [
            "200 g MonChou Zacht & luchtig (in een kuipje)",
            "1 teentje knoflook, geperst", "½ tl chilivlokken (optioneel)",
            "½ citroen, de schil geraspt, uitgeperst", "zout en peper",
            "1 rol bladerdeeg (koelvak)", "1 ei, geklutst",
            "50 g gerookte zalmsnippers", "50 g parmaham, in stukjes",
        ],
        "instructions": [
            "Verwarm de oven voor (elektrisch: 220°C / hetelucht: 200°C). Meng de MonChou met de knoflook, de chilivlokken, de citroenschil en het citroensap. Breng op smaak met zout en peper.",
            "Rol het bladerdeeg uit. Steek met de vorm sterren uit het bladerdeeg en leg ze op een met bakpapier beklede bakplaat. Prik met een vork gaatjes in de sterren en bestrijk ze met geklutst ei. Bak de sterren in 15-20 minuten goudbruin en knapperig in de oven. Haal ze uit de oven laat ze afkoelen op een rooster.",
            "Vul de spuitzak met de MonChouvulling en maak mooie toefjes op de sterren. Garneer met de zalmsnippers en de stukjes ham.",
        ],
    },
}
