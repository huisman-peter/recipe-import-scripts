"""Issue-specific data for Koken & genieten KG2312 (december 2023).

Extra-thick Christmas issue ("Kerst is... samen rond de eettafel", 80 recipes),
90 pages.  Same shape as extract.py's built-in KG2510 tables, so the engine
processes this issue unchanged:

    python convert_pdf.py --pdf KG2312.pdf --md KG2312.md
    python add_images.py  --issue 2312
    python extract.py     --issue 2312 --write --out recipes-2312.json
"""
ISSUE = "12-2023"
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "2023-12"
ISSUE_AS_LABEL = True

PDF = "KG2312.pdf"
MD = "KG2312.md"
OUT = "recipes-2312.json"
IMAGE_FOLDER = "images-2312"

BRENDA = "Brenda Kookt"          # the monthly blog contribution (p. 6-11)
GENTL = "Andrea Gentl"           # the "Koken met paddenstoelen" book (p. 24-29)
ANOUK = "Anouk"                  # "Het beste van 10 jaar Heel Holland Bakt" (p. 66-73)
ELIZABETH = "Elizabeth"
HANS = "Hans"
KG = "Koken & genieten"

# column labels, section titles and advert lines that are not ingredients
EXTRA_NOISE = {
    "Brenda Kookt", "BRENDA KOOKT", "Zelf (w)eten", "Brenda’s kerstmenu",
    "Jouw kerstdiner", "Herfst & kerst", "Groentefeestje", "Neusje van de zalm",
    "Peertje uit de aarde", "Raclettefeestje", "3 x kerstkoekjes",
    "Happyhourtaarten", "Simpel en snel genieten", "Happy New Year!",
    "Heel Holland Bakt met kerst", "Feestelijke taarten", "SEIZOEN",
    "Cover recept", "Bijgerecht", "Hoofdgerecht", "Zoet & desserts",
    "KOOKBOEK: KOKEN MET PADDENSTOELEN",
    "KOOKBOEK: HET BESTE VAN 10 JAAR HEEL HOLLAND BAKT",
    "Fotografie en receptuur: Brenda Kookt",
    "Receptuur & fotografie: Andrea Gentl", "Auteur: Andrea Gentl",
    "Auteur: koken & genieten", "Tekst: Lotus van Overveldt",
    # a tip box and two titles the layout promoted to headings, printed between
    # a recipe's own lines
    "Tip: Je kunt de", "## varkenshaaspakketjes", "ook van tevoren maken en",
    "invriezen. Zo hoef je ze op de", "dag van het kerstdiner alleen in de",
    "oven af te bakken. Bak de pakketjes in dat geval in totaal",
    "30-35 minuten.",
    "## kubus, vraag dan een handige Harry in je omgeving om zo’n leuke kubusstandaard te maken.”",
    "## HORIZONTAAL", "## VERTICAAL",
    # labels that share their line with the text (the parser keeps the text)
    "**VOOR DE** VULLING Schil de appels, snijd ze",
    "VOOR HET JOCONDEBISCUIT Doe de boter, de helft",
    # the wrapping of a piece of equipment is not an ingredient either
    "uitsteker in hertvorm", "(à ca. 5 cm)",
    "uitsteker in poppetjesvorm", "(ca. 3,5 cm)",
}

# (line of the "## " heading, full name, author, category, total time override)
RECIPE_TABLE = [
    # Brenda Kookt (p. 6-11)
    (342, "Carpacciotorentjes", BRENDA, "Bijgerecht", None),
    (384, "Geroerbakte spruitjes met cranberry en spekjes", BRENDA, "Bijgerecht", None),
    (411, "Tonijntartaar met avocado en balsamico", BRENDA, "Bijgerecht", None),
    (456, "Varkenshaaspakketjes met parmaham", BRENDA, "Hoofdgerecht", None),
    (525, "Tiramisu-ijstaart", BRENDA, "Zoet & desserts", "PT7H30M"),
    # Jouw kerstdiner (p. 12-23)
    (606, "Selderij-vanillesoep met groentechips", KG, "Soep", None),
    (642, "Salade met gerookte eendenborst en sherrygelei", KG, "Salade", None),
    (658, "Garnalen met frisse groenten", KG, "Bijgerecht", None),
    (672, "Romige savooiekool met spek", KG, "Bijgerecht", None),
    (696, "Tagliatelle met geroosterde noten", KG, "Hoofdgerecht", None),
    (713, "Kruidige gebakken uitjes", KG, "Bijgerecht", "PT15M"),
    (776, "Eend met honing en speculaaskruiden", KG, "Hoofdgerecht", None),
    (825, "Saltimbocca van tarbot met saffraanrisotto", KG, "Hoofdgerecht", "PT50M"),
    (831, "Iberico-varkenshaas wellington", KG, "Hoofdgerecht", None),
    (906, "Reerolletjes met crème-de-cassis-saus", KG, "Hoofdgerecht", None),
    (951, "Felroze citroensorbet", KG, "Zoet & desserts", None),
    (975, "Kerstige chocolade-panna-cotta", KG, "Zoet & desserts", None),
    (987, "Tiramisu met mandarijn", KG, "Zoet & desserts", None),
    # Herfst & kerst, boek Koken met paddenstoelen (p. 24-29)
    (1024, "Kruidige paddenstoeldumplings", GENTL, "Bijgerecht", None),
    (1114, "Crostata van bladerdeeg met paddenstoelen en ansjovis", GENTL, "Bijgerecht", None),
    (1175, "Brick-paddenstoelen", GENTL, "Bijgerecht", None),
    (1212, "Infused gin met shiitake en eikhaas", GENTL, "Drank", None),
    (1237, "Paddenstoelenijs met ahornsiroop", GENTL, "Zoet & desserts", None),
    # Groentefeestje (p. 30-33)
    (1413, "Zoete aardappel wellington", KG, "Hoofdgerecht", None),
    # the index and the contents caption call this one "met geitenkaas", the page
    # heading says "met pompoen"; the box has both, so the caption wins
    (1464, "Linzensalade met geitenkaas en walnoten", KG, "Salade", None),
    (1505, "Balsamicopaddenstoelen met parmezaanpuree", KG, "Bijgerecht", None),
    # Neusje van de zalm (p. 34-35)
    (1554, "Ingelegde zalmforel met gin", KG, "Bijgerecht", None),
    (1572, "Mosterd-honing-dillesaus", KG, "Bijgerecht", None),
    # Peertje uit de aarde (p. 36-39)
    (1613, "Aardpeerroomsoep met kruidige groentesalsa", KG, "Soep", None),
    (1662, "Salade met geroosterde aardpeer, peer en bacon", KG, "Salade", None),
    (1705, "Aardpeer-courgettekoekjes met ei", KG, "Bijgerecht", None),
    # Raclettefeestje (p. 40-41)
    (1757, "Raclette met zalm en granaatappel", KG, "Hoofdgerecht", None),
    (1783, "Raclette met varkenshaas en mozzarella", KG, "Hoofdgerecht", None),
    (1805, "Raclette met eendenborst en rode peper", KG, "Hoofdgerecht", None),
    (1834, "Raclette met vijgen en geitenkaas", KG, "Hoofdgerecht", None),
    # 3 x kerstkoekjes (p. 42-43)
    (1876, "Kaneelkoekjes", KG, "Zoet & desserts", "PT30M"),
    (1901, "Raviolikoekjes met marsepein", KG, "Zoet & desserts", "PT1H"),
    (1918, "Zachte vanillekoekjes", KG, "Zoet & desserts", None),
    (1953, "Koekjesdeeg", KG, "Zoet & desserts", "PT45M"),
    # Happyhourtaarten (p. 44-51)
    (1988, "Strawberry-daiquiri-taart", KG, "Zoet & desserts", None),
    (2038, "Pina-coladataart", KG, "Zoet & desserts", None),
    (2085, "Pisco-sourtaart", KG, "Zoet & desserts", None),
    (2152, "Gember-basilicumcake", KG, "Zoet & desserts", None),
    (2190, "Basilicumsuiker", KG, "Zoet & desserts", None),
    (2204, "White-Russiantaartjes", KG, "Zoet & desserts", None),
    # Simpel en snel genieten (p. 52-57)
    (2308, "Winterse flammkuchen met boerenkool", KG, "Hoofdgerecht", None),
    (2350, "Aardappels met mosterd-champignonsaus", KG, "Hoofdgerecht", None),
    (2381, "Worstjes in bier met savooiekool", KG, "Hoofdgerecht", None),
    (2410, "Entrecote met kruidige couscous", KG, "Hoofdgerecht", None),
    (2435, "Spaghetti in kip-dragonroomsaus", KG, "Hoofdgerecht", None),
    (2462, "Rodebieten-sinaasappelsalade met rundergehaktballetjes", KG, "Hoofdgerecht", None),
    (2496, "Roerei met avocado, chorizo en spek", KG, "Bijgerecht", None),
    (2526, "Snelle gebakken rijst met garnalen", KG, "Hoofdgerecht", None),
    # Happy New Year! (p. 58-65)
    (2560, "Ossenhaas uit Australië", KG, "Hoofdgerecht", None),
    (2596, "Fruitige groentespiesen", KG, "Bijgerecht", None),
    (2609, "Thaise noedels met mango en garnalen", KG, "Hoofdgerecht", None),
    (2671, "Duitse middernachtssoep", KG, "Soep", None),
    (2708, "Kruidenbrood", KG, "Bijgerecht", None),
    (2726, "Russische salade", KG, "Salade", None),
    (2771, "Gevulde eieren met zalm en kaviaar", KG, "Bijgerecht", None),
    (2788, "Tomatensalsa", KG, "Bijgerecht", None),
    (2802, "Braziliaanse linzenempanada’s", KG, "Bijgerecht", None),
    (2839, "Amerikaanse cheesecake met blauwebessensaus", KG, "Zoet & desserts", None),
    # Heel Holland Bakt met kerst (p. 66-73)
    (2937, "Kubus van jocondebiscuit", ANOUK, "Zoet & desserts", None),
    (3087, "Chateautaart", ELIZABETH, "Zoet & desserts", None),
    (3188, "Klassieke opera", HANS, "Zoet & desserts", None),
    # Feestelijke taarten (p. 74-81)
    (3405, "Hemelse frambozen-laagjestaart", KG, "Zoet & desserts", None),
    (3505, "Kerstbûche met paddenstoelen", KG, "Zoet & desserts", None),
    (3604, "Appelstrudelkrans met kaneel", KG, "Zoet & desserts", None),
    (3669, "Speculaas-cheesecake met granaatappelgelei", KG, "Zoet & desserts", "PT5H"),
    (3757, "Krans van vruchtenmuffins", KG, "Zoet & desserts", None),
]

HEADING_AS = {}
CAPTION_SPLIT = {}
OVERRIDES = {
    # these recipes print no ingredient list at all: every quantity sits in the
    # running text, so the list is read out of that text
    "Salade met gerookte eendenborst en sherrygelei": {
        "ingredients": [
            "2 blaadjes gelatine", "150 ml sherry", "5 el appelgelei (pot)",
            "200 g gemengde sla", "4 el walnoten", "4 takjes peterselie",
            "4 el sherryazijn", "2 tl mosterd", "4 el olijfolie",
            "zout en peper", "200 g gerookte eendenborst (in plakken)",
        ],
    },
    "Garnalen met frisse groenten": {
        "ingredients": [
            "½ bosje bieslook", "150 ml volle yoghurt",
            "1 el mierikswortel (pot)", "1 el mosterd", "een snufje suiker",
            "2 tl citroensap", "1 snackkomkommer", "1 gele paprika",
            "150 g cherrytomaten", "4 takjes peterselie", "2 tl citroensap",
            "8 panklare garnalen (à ca. 40 g, zonder kop en schaal)",
            "2 el olijfolie", "zout en peper",
        ],
    },
    "Kerstige chocolade-panna-cotta": {
        "ingredients": [
            "4 blaadjes gelatine", "50 g pure chocolade", "400 ml slagroom",
            "100 ml melk", "8 g vanillesuiker", "2 kardemompeulen",
            "100 g suiker", "1 el cacaopoeder",
            "50 g pure chocolade (voor de schilfers)",
            "gouden suikerparels, om te versieren",
        ],
    },
    "Tiramisu met mandarijn": {
        "ingredients": [
            "2 blikjes (à ca. 300 g) mandarijntjes",
            "1 tl koek- en speculaaskruiden", "1 tl maizena", "2 el water",
            "100 ml koffie", "6 el amandellikeur", "500 g mascarpone",
            "500 g volle kwark", "250 ml slagroom", "150 g suiker",
            "16 g vanillesuiker", "400 g lange vingers", "2 el cacaopoeder",
        ],
    },
    "Basilicumsuiker": {
        "ingredients": ["8-10 grote basilicumblaadjes", "2 el suiker"],
    },
    "Koekjesdeeg": {
        "ingredients": [
            "450 g bloem", "300 g koude boter", "een snufje zout",
            "150 g poedersuiker", "1 ei",
        ],
    },
    # these four carry the magazine's "Voor:" label instead of an ingredient box
    "Fruitige groentespiesen": {
        "yield": "ca. 20 stuks",
        "ingredients": [
            "½ ananas", "3 paprika’s (rode en gele)", "4 lente-uitjes",
            "200 g cherrytomaten", "1 tl kerriepoeder", "een snufje zout",
            "geraspte schil van ½ bio-citroen", "4-5 el citroensap",
            "4 el olijfolie",
        ],
    },
    "Kruidenbrood": {
        "yield": "ca. 18 sneetjes",
        "ingredients": [
            "mix voor boerenbrood (ca. 500 g, voor zuurdesem en gistbrood)",
            "1 bosje peterselie", "1 bosje dille", "½ bosje bieslook",
            "125 g zachte boter", "geraspte schil van 1 bio-citroen",
            "zout en peper",
        ],
    },
    "Gevulde eieren met zalm en kaviaar": {
        "yield": "10 personen",
        "ingredients": [
            "250 g plakken gerookte zalm", "10 hardgekookte eieren",
            "100 g yoghurtmayonaise", "1 tl mosterd", "zout en peper",
            "50 g forelkaviaar", "dille",
        ],
    },
    "Tomatensalsa": {
        "yield": "8 personen",
        "ingredients": [
            "2 uien", "3 teentjes knoflook", "1 rode peper", "3 el olie",
            "3 tl tomatenpuree", "400 g tomatenblokjes", "zout", "peper",
            "paprikapoeder", "een snufje suiker",
            "1-2 el witte balsamicoazijn", "tuinkers, om te garneren",
        ],
    },
    # the tarbot recipe's box and steps follow this one, so its block has to be
    # cut off by hand
    "Kruidige gebakken uitjes": {
        "ingredients": ["6 uien", "1 tl paprikapoeder", "2 el olie"],
        "instructions": [
            "Pel 6 uien, snijd ze in ringen en bestuif ze met 1 tl paprikapoeder. Verhit 2 el olie in een pan. Bak er de ui knapperig in. Neem de ui uit de pan en laat uitlekken.",
        ],
    },
    # the crossword page follows this one in the Markdown, so its clue lines were
    # glued onto the last step; the seven steps below are the recipe's own
    "Paddenstoelenijs met ahornsiroop": {
        "instructions": [
            "VOOR HET PADDENSTOELENPOEDER Doe de paddenstoelen in een specerijenmolen, minikeukenmachine of vijzel en maal of stamp ze tot een fijn poeder. Zeef het door een fijne zeef om grotere stukjes te verwijderen en doe die terug in de molen. Herhaal het fijnmalen en zeven tot alles een fijn poeder is. Doe het in een afgesloten pot en bewaar in de koelkast of diepvries. Het is eindeloos houdbaar.",
            "Meng 10 g paddenstoelenpoeder, de gedroogde paddenstoelen en slagroom in een steelpan met zware bodem en breng het op halfhoog vuur tegen de kook aan. Het mag echt niet aan de kook komen. Neem de pan van het vuur, leg er een deksel op en laat het 30 minuten trekken. Zeef de room door een fijne zeef boven een kom (en gooi de stukjes paddenstoel weg).",
            "Meng de melk, 125 ml van de ahornsiroop en het Keltische zout in een andere pan en breng het op halfhoog vuur zachtjes tegen de kook aan. Neem de pan van het vuur en zet opzij.",
            "Klop de eidooiers met de resterende 125 ml ahornsiroop 10-12 minuten in een kom tot ze als een lint van de garde lopen.",
            "Spatel het warme melkmengsel geleidelijk door het eidooiermengsel om de eidooiers te temperen. Schenk het melk-eidooiermengsel terug in de pan en verwarm het circa 5 minuten al roerend zachtjes op halfhoog tot laag vuur tot het mengsel de achterkant van een houten lepel gelijkmatig bedekt. Laat de custard niet aan de kook komen!",
            "Roer de getrokken room voorzichtig door de custard tot het een glad mengsel is. Zet minstens 2 uur in de koelkast tot het volledig is afgekoeld.",
            "Draai het mengsel in een ijsmachine tot ijs. Schep het als je het niet meteen serveert in een luchtdichte bak. In de diepvries is het ijs een week houdbaar.",
        ],
    },
    # the tarbot's box and steps sit in the onion recipe's block above; the
    # cookie titles are repeated on the section page, and the salmon's steps sit
    # under the sauce
    "Saltimbocca van tarbot met saffraanrisotto": {
        "yield": "4 personen",
        "ingredients": [
            "800 g tarbotfilet zonder huid (bij de viswinkel)", "zout en peper",
            "rasp en sap van ½ bio-citroen", "4 takjes salie",
            "8 plakken parmaham", "800 ml groentebouillon", "2 sjalotjes",
            "3 el boter", "250 g risottorijst", "een snufje saffraan",
            "100 ml witte wijn", "500 g sperziebonen", "300 g cherrytomaten",
            "2 el truffelboter", "2 el olie", "50 g geraspte parmezaan",
        ],
        "instructions": [
            "VOOR DE SALTIMBOCCA Snijd de tarbotfilet in 8 stukken en bestrooi met zout, peper, citroenrasp en citroensap. Was de salie en neem de blaadjes van de takjes. Leg op elk stuk tarbotfilet 2 blaadjes salie en wikkel elk stuk in een plak parmaham. Houd de overige salie apart.",
            "VOOR DE RISOTTO Verhit de bouillon. Pel en snipper de sjalotjes. Verhit 2 el boter in een ruime pan. Fruit er de sjalotjes in. Voeg de rijst toe en bak kort. Breng op smaak met peper. Roer de saffraan erdoorheen. Schenk al roerend beetje bij beetje de wijn en de bouillon erbij tot al het vocht opgenomen is. Gaar in totaal 30-35 minuten.",
            "VOOR DE GROENTEN Maak de sperziebonen schoon en kook ze in water met een snufje zout in ca. 8 minuten gaar. Was de cherrytomaten. Giet de bonen af. Verhit de truffelboter in een pan. Fruit er de bonen en de tomaten ca. 8 minuten in. Breng op smaak met zout en peper.",
            "Verhit de olie in een tweede pan. Bak er de overige salie in ca. 1 minuut knapperig in. Laat de salie op keukenpapier uitlekken. Bak de saltimbocca in de hete salieolie ca. 3 minuten per zijde. Verhit 1 el boter al roerend in het bakvet. Wentel de saltimbocca erin.",
            "Roer de parmezaan door de risotto. Breng op smaak met zout en peper. Verdeel de risotto over borden. Verdeel de groenten met het bakvet eroverheen. Leg de saltimbocca erop. Garneer met de knapperige salie.",
        ],
    },
    "Kaneelkoekjes": {
        "yield": "ca. 20 koekjes",
        "ingredients": [
            "80 g rietsuiker", "2 tl kaneel", "1⁄3 recept koekjesdeeg", "bloem",
        ],
        "instructions": [
            "Meng de rietsuiker en de kaneel in een kleine kom. Rol het deeg op een met bloem bestoven werkblad rechthoekig (ca. 20x40 cm) uit. Bestrijk het deeg met koud water en bestrooi gelijkmatig met de kaneelsuiker. Rol het deeg langs de lange zijde op.",
            "Verwarm de oven voor (elektrisch: 180°C / hetelucht: 160°C). Snijd de deegrol in plakjes van ca. 1 cm dik en leg de plakjes met een beetje afstand van elkaar op een met bakpapier beklede bakplaat. Bak in 10-12 minuten goudbruin. Laat afkoelen.",
        ],
    },
    "Ingelegde zalmforel met gin": {
        "ingredients": [
            "4 zalmforelfilets met huid (à ca. 150 g, bij de viswinkel)",
            "½ tl zwarte peperkorrels", "½ tl korianderzaad", "50 g zout",
            "40 g suiker", "1 bosje dille",
            "geraspte schil van 1 biosinaasappel", "5-8 el gin",
            "verse dille en sinaasappelschil, om te garneren",
        ],
        "instructions": [
            "EEN DAG VAN TEVOREN Dep de zalmfilets droog en leg ze met de huidzijde naar beneden naast elkaar in een ovenschaal. Maal de peperkorrels en het korianderzaad in een vijzel fijn. Meng het zout en de suiker erdoorheen. Was de dille, schud hem droog en hak hem fijn. Meng de dille, de sinaasappelschil en de gin in een schaaltje en verdeel het mengsel gelijkmatig over de zalm. Bestrooi met het zoutmengsel. Dek de zalmfilets af met vershoudfolie. Leg een snijplank erop en verzwaar de snijplank met een boek, een tweede kleinere ovenschaal of iets anders zwaars. Zet ca. 12 uur in de koelkast.",
            "DE VOLGENDE DAG Spoel het zoutmengsel met koud water van de zalmfilets en dep ze droog. Snijd de zalmfilets met een lang, scherp mes schuin in dunne plakken van de huid (zie afbeelding linksonder). Snijd elke plakje op gelijke wijze van de huid. Garneer de zalm met de dille en de sinaasappelschil. De zalm is in folie gewikkeld 3 dagen houdbaar in de koelkast.",
        ],
    },
}
