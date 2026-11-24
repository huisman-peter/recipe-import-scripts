"""Issue-specific data for Koken & genieten KG2508 (augustus 2025, jaargang 20).

Summer/Italian issue, 68 pages.  Same shape as extract.py's built-in KG2510
tables, so the engine processes this issue unchanged:

    python convert_pdf.py --pdf KG2508.pdf --md KG2508.md
    python add_images.py  --issue 2508
    python extract.py     --issue 2508 --write --out recipes-2508.json
"""
ISSUE = "8-2025"
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "2025-08"
ISSUE_AS_LABEL = True

PDF = "KG2508.pdf"
MD = "KG2508.md"
OUT = "recipes-2508.json"
IMAGE_FOLDER = "images-2508"

PAULINE = "Uit Paulines Keuken"
LETITIA = "Letitia Clark"          # the "For the Love of Lemons" book preview
KG = "Koken & genieten"

# column labels, section titles and advert lines that are not ingredients
EXTRA_NOISE = {
    "Uit Paulines Keuken", "Receptuur: Uit Paulines Keuken Fotografie: Marianne Snel",
    "Prima pomodori", "Hasta la pasta!", "Op en top zomer", "Kookboek",
    "Zomerkruiden", "Groeten uit de moestuin", "Salute!", "4x risotto",
    "Goeie toetjes", "De laatste kruimel", "Frisse skyr", "Coverrecept",
    "Receptuur: Letitia Clark Fotografie: Charlotte Bland",
    "Titel: For the Love of Lemons", "Prijs: 29,99 euro",
    "Uitgeverij: Becht – Harper Collins NL",
}

# (line of the "## " heading, full name, author, category, total time override)
RECIPE_TABLE = [
    (336, "Maritozzi met pistacheroom", PAULINE, "Zoet & desserts", None),
    (382, "Bruschetta met burrata", PAULINE, "Bijgerecht", None),
    (410, "Plaatpizza met venkel en pancetta", PAULINE, "Hoofdgerecht", None),
    (454, "Pasta met ricotta en tomaat", PAULINE, "Hoofdgerecht", None),
    (501, "Tomatensalade met basilicumdressing", PAULINE, "Salade", None),
    (541, "Tomatentaart met geitenkaasroom", KG, "Bijgerecht", None),
    (605, "Spaghetti all’amatriciana", KG, "Hoofdgerecht", None),
    (627, "Sugo (tomatensaus)", KG, "Bijgerecht", None),
    (649, "Varkenshaasmedaillons met tomaten", KG, "Hoofdgerecht", None),
    (703, "Provençaalse tomaten met kabeljauw", KG, "Hoofdgerecht", None),
    (752, "Tomatensalade met kipspiesjes", KG, "Salade", None),
    (790, "Ketchup van geroosterde tomaten", KG, "Bijgerecht", None),
    (816, "Tomatenchips", KG, "Bijgerecht", None),
    (832, "Zoetzure ingelegde tomaat", KG, "Bijgerecht", None),
    (998, "Zomerse ravioli uit de oven", KG, "Hoofdgerecht", None),
    (1054, "Udonnoedels met koningsoesterzwam", KG, "Hoofdgerecht", None),
    (1105, "Spaghettipizza met salami", KG, "Hoofdgerecht", None),
    (1135, "Griekse orzoschotel met gyros", KG, "Hoofdgerecht", None),
    (1197, "Frisse pastasalade met venkel en Griekse yoghurt", KG, "Salade", None),
    (1334, "Burrata met citroenige lentegroenten", LETITIA, "Bijgerecht", None),
    (1389, "Courgette-carbonara met citroen", LETITIA, "Hoofdgerecht", None),
    (1436, "Instant mascarponemousse van citroen & witte chocolade", LETITIA, "Zoet & desserts", None),
    (1473, "Citroenrepen met polentadeeg en olijfolie", LETITIA, "Zoet & desserts", None),
    (1527, "Koolvis met romige komkommersalade", KG, "Hoofdgerecht", None),
    (1567, "Koude erwten-muntsoep", KG, "Soep", "PT3H20M"),
    (1607, "Frisse salade met gegrilde kip", KG, "Salade", None),
    (1655, "Courgetti met kruidenpesto", KG, "Hoofdgerecht", None),
    (1696, "Biefstuk met courgette-fetasalade", KG, "Hoofdgerecht", None),
    (1732, "Gevulde courgette met ham en bulgur", KG, "Hoofdgerecht", None),
    (1783, "Zomerse gehaktschotel met basilicumcrunch", KG, "Hoofdgerecht", None),
    (1832, "Frisse courgette-muntdip", KG, "Bijgerecht", None),
    (1852, "Pasta met twee sauzen", KG, "Hoofdgerecht", None),
    (1912, "Bonencrème", KG, "Bijgerecht", "PT13H15M"),
    (1935, "Antipasti met basilicumolie", KG, "Bijgerecht", None),
    (1963, "Antipasti di verdure", KG, "Bijgerecht", None),
    (1996, "Torta al limone", KG, "Zoet & desserts", None),
    (2045, "Campari Amalfi", KG, "Drank", None),
    (2057, "Scaloppine al tartufo", KG, "Hoofdgerecht", None),
    (2123, "Risotto met linzen en worst", KG, "Hoofdgerecht", None),
    (2156, "Milanese risotto met saffraan en garnalen", KG, "Hoofdgerecht", None),
    (2188, "Noord-Italiaanse risotto met pompoen en geitenkaas", KG, "Hoofdgerecht", None),
    (2219, "Siciliaanse risotto met gorgonzola en vijgen", KG, "Hoofdgerecht", None),
    (2257, "Warm rabarbertoetje met amandel", KG, "Zoet & desserts", None),
    (2292, "Lavacakejes met pindakaas", KG, "Zoet & desserts", None),
    (2315, "Aardbeien-ijsbeker", KG, "Zoet & desserts", None),
    (2339, "Île flottante", KG, "Zoet & desserts", None),
    (2372, "Basisrecept kruimeldeeg", KG, "Zoet & desserts", None),
    (2394, "Appel-bramentaart", KG, "Zoet & desserts", None),
    (2448, "Knapperige gebakjes met kersenroom", KG, "Zoet & desserts", None),
    (2505, "Bosvruchtenkruimelgebak", KG, "Zoet & desserts", None),
    (2553, "Kwetsentaart met koffiekruimels", KG, "Zoet & desserts", "PT2H"),
    (2576, "Zelfgemaakte koffiesiroop", KG, "Zoet & desserts", None),
    (2682, "Blauwebessen-skyrrepen", KG, "Zoet & desserts", None),
]

HEADING_AS = {}
CAPTION_SPLIT = {}
OVERRIDES = {
    # these recipes carry their quantities inside the running text, so the
    # parser finds no ingredient box; the lists below are read out of the text
    "Sugo (tomatensaus)": {
        "ingredients": [
            "2,5 kg rijpe tomaten", "500 g uien", "5 teentjes knoflook",
            "100 ml olijfolie", "150 g Kalamataolijven", "10 takjes tijm",
            "10 takjes oregano", "100 ml witte balsamicoazijn",
            "2 el lichte basterdsuiker", "zout en peper",
        ],
        "instructions": [
            "Was 2,5 kg rijpe tomaten en snijd in blokjes. Pel 500 g uien en 5 teentjes knoflook en snipper fijn. Verhit 100 ml olijfolie in een grote pan en bak de ui en de knoflook glazig erin. Voeg de tomaat toe, breng aan de kook en laat met het deksel op de pan ca. 45 minuten smoren. Hak 150 g Kalamataolijven fijn. Was 10 takjes tijm en 10 takjes oregano en hak fijn. Doe de olijven en de kruiden bij de saus, breng aan de kook en laat ca. 5 minuten zachtjes koken. Breng op smaak met 100 ml witte balsamicoazijn, zout, peper en 2 el lichte basterdsuiker. Breng de sugo nogmaals aan de kook. Doe de sugo in gesteriliseerde potten en sluit ze af. Schenk heet water in een grote pan en zet de potten sugo erin, zodat ze voor ⅔ onder staan. Breng het water aan de kook en laat ca. 40 minuten koken. Laat afkoelen.",
        ],
    },
    "Ketchup van geroosterde tomaten": {
        "ingredients": [
            "6 teentjes knoflook", "1,2 kg rijpe tomaten (bijv. vleestomaten)",
            "2 rode uien", "2 cm gember", "1 vanillestokje",
            "4 laurierblaadjes", "2-3 el olie", "100 g lichte basterdsuiker",
            "100 ml appelazijn", "zout en peper",
        ],
        "instructions": [
            "Verwarm de oven voor (elektrisch: 230°C / hetelucht: 210°C). Pel 6 teentjes knoflook en hak ze fijn. Was 1,2 kg rijpe tomaten (bijv. vleestomaten), halveer ze en leg op een bakplaat. Bestrooi met zout en peper en verdeel de knoflook erover. Leg 4 laurierblaadjes erbij en bak ca. 45 minuten in de oven. Pel 2 rode uien en hak grof. Schil 2 cm gember en rasp fijn. Halveer 1 vanillestokje in de lengte en schraap het merg eruit. Verhit 2-3 el olie in een grote pan en bak de ui erin. Voeg het vanillemerg, het -stokje en de gember toe en bak mee. Bestrooi met 100 g lichte basterdsuiker en laat karamelliseren. Schenk 100 ml appelazijn erbij en breng aan de kook. Neem de tomaten van de bakplaat en doe ze in de pan. Breng opnieuw aan de kook en breng op smaak met zout en peper. Laat zonder deksel 15-20 minuten zachtjes koken en roer daarbij meermaals door. Schenk in porties door een zeef. Bewaar in een gesteriliseerde fles of pot.",
        ],
    },
    "Tomatenchips": {
        "ingredients": [
            "700 g rijpe tomaten (bijv. pruimtomaten)", "2 teentjes knoflook",
            "2 takjes rozemarijn", "4 el olijfolie", "½ tl zout",
        ],
        "instructions": [
            "Verwarm de oven voor (elektrisch: 90°C / hetelucht: 70°C). Was 700 g rijpe tomaten (bijv. pruimtomaten) en dep droog. Snijd in de lengte in plakjes van ca. 3 mm dik en verdeel gelijkmatig over twee met bakpapier beklede bakplaten. Pel 2 teentjes knoflook en hak fijn. Was 2 takjes rozemarijn en hak fijn. Roer de rozemarijn, de knoflook, 4 el olijfolie en ½ tl zout door elkaar. Bestrijk de tomaat met het mengsel. Laat ca. 5 uur drogen in de oven.",
        ],
    },
    "Frisse courgette-muntdip": {
        "ingredients": [
            "1 ui", "600 g courgette", "4 el olie", "1 tl zout",
            "5 teentjes knoflook", "6 takjes munt", "½ tl gemalen komijn",
            "1 tl citroensap", "1 el olie",
        ],
        "instructions": [
            "Pel en snipper 1 ui fijn. Was 600 g courgette en rasp grof. Verhit 4 el olie in een pan en fruit de ui erin. Voeg de courgette en 1 tl zout toe. Laat het geheel 12-15 minuten al roerend rustig koken, tot het vocht is verdampt en de courgette lichtbruin kleurt. Pel en snipper 5 teentjes knoflook. Was 6 takjes munt, neem de blaadjes van de takjes en hak fijn. Voeg de knoflook en de munt toe aan de courgette en roer door. Breng op smaak met zout en ½ tl gemalen komijn. Laat ca. 3 minuten koken. Neem de pan van het vuur en roer 1 tl citroensap erdoorheen. Laat de dip iets afkoelen. Besprenkel voor het serveren met 1 el olie. Lekker met gegrild stokbrood of platbrood.",
        ],
    },
    "Campari Amalfi": {
        "ingredients": [
            "2 bio-grapefruits",
            "400 ml campari (Italiaanse kruidenlikeur, bij de slijter)",
            "100 ml grapefruitsap", "800 ml gekoelde bitter lemon", "ijsblokjes",
        ],
        "instructions": [
            "Was 2 bio-grapefruits en snijd in partjes. Meng 400 ml campari (Italiaanse kruidenlikeur, bij de slijter) met 100 ml grapefruitsap. Doe in elk glas wat ijsblokjes. Schenk het camparimengsel eroverheen en vul aan met 800 ml gekoelde bitter lemon. Garneer de campari Amalfi met de grapefruitpartjes en serveer.",
        ],
    },
    "Bonencrème": {
        "ingredients": [
            "500 g gedroogde kleine, witte bonen", "2,5 l water",
            "2 tenen knoflook", "2 laurierblaadjes", "4 takjes peterselie",
            "1 ingelegde groene peper (pot)", "1 bio-citroen", "4 el olijfolie",
            "1 el olijfolie", "zout en peper",
        ],
        "instructions": [
            "EEN DAG VAN TEVOREN Laat 500 g gedroogde kleine, witte bonen een nacht in koud water weken. DE VOLGENDE DAG Pel 2 tenen knoflook. Giet de bonen af en doe ze samen met 2,5 l water in een pan. Voeg de knoflook en 2 laurierblaadjes toe. Breng aan de kook en laat met deksel op de pan ca. 1 uur zachtjes koken. Was 4 takjes peterselie en hak fijn. Snijd 1 ingelegde groene peper (pot) in de lengte in, verwijder de zaadlijsten, was de peper en hak hem fijn. Was 1 bio-citroen en rasp de schil er fijn af. Pers de citroen uit. Giet de bonen af en vang daarbij 5 el kookwater en de knoflook op. Houd 2 el bonen apart. Pureer de rest van de bonen met de knoflook en het kookwater fijn. Roer de groene peper, de peterselie, 4 el olijfolie, de citroenschil en het -sap door de bonenpuree. Breng op smaak met zout en peper. Bestrooi met de apart gehouden bonen en besprenkel met 1 el olijfolie.",
        ],
    },
    "Zelfgemaakte koffiesiroop": {
        "ingredients": [
            "400 ml hete koffie", "150 g lichte basterdsuiker", "1 snufje kaneel",
        ],
        "instructions": [
            "Breng 400 ml hete koffie en 150 g lichte basterdsuiker aan de kook. Laat in 10-15 minuten inkoken tot ca. 225 ml en roer daarbij meermaals door. Breng op smaak met 1 snufje kaneel. Doe de siroop in een schoon flesje, sluit goed af en laat afkoelen. Lekker als aroma in baksels (bijvoorbeeld de kwetsentaart hierboven) of als topping op desserts, in gebak, in koffies of cocktails.",
        ],
    },
    "Basisrecept kruimeldeeg": {
        "ingredients": [
            "200 g boter", "375 g bloem", "150 g suiker", "1 snufje zout", "1 ei",
        ],
        "instructions": [
            "Smelt 200 g boter en laat even afkoelen. Meng 375 g bloem met 150 g suiker en een snufje zout. Kneed de gesmolten boter en 1 ei met de deeghaken van een handmixer erdoorheen. Kneed naar wens extra ingrediënten erdoorheen. Zie het lijstje hieronder voor inspiratie!",
            "Kruimeldeeg is lekker met: 150 g gehakte toffees, 100 g verbrokkelde Oreo’s, 100 g cranberrymuesli, 100 g minimarshmallows, 150 g pinda’s, 25 g gehakte + 50 g gemalen pistachenoten, geraspte schil van 1 biosinaasappel, 100 g geraspte marsepein, 4 el discodip, 60 g gemalen gevriesdroogde frambozen, 4 el maanzaad, 80 g verbrokkelde pretzelzoutjes, 100 g gehakte pure chocolade + 2 el cacaopoeder.",
        ],
    },
    # the taart's ingredient box and its method sit on facing pages, so the
    # engine put the method in the koffiesiroop's block and the siroop in this one
    "Kwetsentaart met koffiekruimels": {
        "ingredients": [
            "350 g bloem (+ bestuiven)", "325 g koude boter (+ invetten)",
            "50 g suiker", "8 g vanillesuiker", "4 el koffiesiroop (zie onder)",
            "1 snufje zout", "35 g custardpoeder", "75 g poedersuiker", "1 ei",
            "1 tl bakpoeder", "900 g kwetsen (of andere pruimen)",
            "125 ml slagroom", "12 chocolade-mokkaboontjes",
        ],
        "instructions": [
            "VOOR HET KRUIMELDEEG Kneed 150 g bloem, 100 g koude boter in stukjes, de suiker, de vanillesuiker, de koffiesiroop en het zout tot een grof kruimeldeeg. Zet het koffiekruimeldeeg in de koelkast.",
            "VOOR HET DEEG Doe het custardpoeder, 225 g koude boter in stukjes, de poedersuiker, het ei, 200 g bloem, het bakpoeder en 2 el ijswater in een kom en kneed snel door elkaar. Rol het deeg op een met bloem bestoven werkblad rond (ca. 32 cm Ø) uit. Doe het deeg in een ingevette en met bloem bestoven taartvorm met uitneembare bodem (28 cm Ø) en druk tegen de rand aan. Steek het deeg meermaals in met een vork. Zet ca. 30 minuten in de koelkast.",
            "Verwarm de oven voor (elektrisch: 180°C / hetelucht: 160°C). Was de kwetsen, halveer ze en verwijder de pit. Houd 4 halve kwetsen apart en verdeel de rest over de deegbodem. Bestrooi gelijkmatig met het koffiekruimeldeeg. Bak in ca. 35 minuten gaar in de oven. Neem uit de oven en laat op een rooster in de vorm helemaal afkoelen.",
            "VOOR DE VERSIERING Klop de slagroom stijf en doe hem in een spuitzak met stervormig spuitmondje. Snijd de apart gehouden halve kwetsen in heel dunne partjes. Neem de taart uit de vorm en versier met toefjes slagroom, de kwetsenpartjes en de mokkaboontjes.",
        ],
    },
    # the magazine misprints the step numbers of this recipe (1, 3, 4), so the
    # engine glued the three steps into one; only the steps need overriding
    "Antipasti di verdure": {
        "instructions": [
            "Kook de sjalotten ca. 5 minuten zachtjes in een pan water. Giet af en spoel met koud water. Snijd de uiteindes van de sjalotten af en duw ze uit de schil. Was de aubergine en de courgette en snijd in plakken van ca. ½ cm dik. Bestrooi de aubergine en de courgette met zout en laat ca. 20 minuten intrekken. Schrap de wortels, was ze en snijd schuin in dunne plakken. Was de kruiden en scheur in grove stukken.",
            "Verwarm de oven voor (elektrisch: 220°C / hetelucht: 200°C). Dep de aubergine en de courgette droog. Verdeel de groenten en de sjalotten in aparte, brede strepen op twee met bakpapier beklede bakplaat. Bestrooi met zout en peper en verdeel de kruiden erover. Besprenkel beide bakplaten elk met 8 el olie. Zet de bakplaten boven elkaar in de oven en bak de groenten ca. 20 minuten. Wissel de bakplaten om en bak nog eens ca. 20 minuten.",
            "Bestrooi de groenten met zout en peper en laat afkoelen. Verdeel de groenten over een grote schaal en besprenkel met balsamicocrème. Garneer eventueel met extra tijm en basilicum.",
        ],
    },
    # running text again; the block also holds the crossword puzzle that
    # follows it on the page, whose number rows used to end up in the steps
    "Zoetzure ingelegde tomaat": {
        "ingredients": [
            "150 g cherrytomaten (gele en rode)", "1 teentje knoflook",
            "1 takje rozemarijn", "250 ml witte balsamicoazijn", "120 g suiker",
            "1 tl mosterdzaad", "1 laurierblaadje",
        ],
        "instructions": [
            "Was 150 g cherrytomaten (gele en rode) en prik ze met een satéprikker twee à drie keer in. Pel 1 teentje knoflook. Was 1 takje rozemarijn. Doe alles in een weckpot. Breng 250 ml witte balsamicoazijn, 120 g suiker, 1 tl mosterdzaad en 1 laurierblaadje aan de kook en laat ca. 5 minuten zachtjes koken. Schenk de hete azijn over de tomaten, zodat alles bedekt is. Sluit de pot af en laat ca. 1 dag op smaak komen.",
        ],
    },
}

