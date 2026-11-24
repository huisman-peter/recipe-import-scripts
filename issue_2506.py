"""Issue-specific data for Koken & genieten KG2506 (juni 2025, jaargang 20).

Summer/BBQ issue ("De smaak van de zomer"), 66 pages.  Same shape as extract.py's
built-in KG2510 tables, so the engine processes this issue unchanged:

    python convert_pdf.py --pdf KG2506.pdf --md KG2506.md
    python add_images.py  --issue 2506
    python extract.py     --issue 2506 --write --out recipes-2506.json
"""
ISSUE = "6-2025"
PUBLISHER = f"Koken & genieten {ISSUE}"
ISSUE_DATE = "2025-06"
ISSUE_AS_LABEL = True

PDF = "KG2506.pdf"
MD = "KG2506.md"
OUT = "recipes-2506.json"
IMAGE_FOLDER = "images-2506"

PAULINE = "Uit Paulines Keuken"
KG = "Koken & genieten"

# column labels, section titles and advert lines that are not ingredients
EXTRA_NOISE = {
    "Uit Paulines Keuken", "Receptuur: Uit Paulines Keuken Fotografie: Marianne Snel",
    "Viva Brasil!", "Vederlicht", "Zwoele zomeravonden", "Op hete kolen",
    "Koken met cola", "Antihooikoorts", "Mexico in je mandje", "Rabarbertijd",
    "Zoete inval", "Makkie van ’n bakkie", "Lekker voor erbij", "Coverrecept",
    "Frisse cheesecake", "Titel: Uit Paulines Keuken",
    "Auteur: Uit Paulines Keuken",
}

# (line of the "## " heading, full name, author, category, total time override)
RECIPE_TABLE = [
    # Uit Paulines keuken (p. 6-11)
    (336, "Vleesspiesjes met chorizo", PAULINE, "Hoofdgerecht", None),
    (376, "Gemarineerde aardbeien met hangop", PAULINE, "Zoet & desserts", None),
    (398, "Zoete aardappel van de barbecue", PAULINE, "Bijgerecht", None),
    (439, "Griekse orzosalade met citroendressing", PAULINE, "Salade", None),
    (474, "Vispakketjes van de barbecue", PAULINE, "Hoofdgerecht", None),
    # Viva Brasil! (p. 12-16)
    (527, "Rozemarijnkip met ui en zoete-aardappelpuree", KG, "Hoofdgerecht", None),
    (565, "IJskoude caipirinha", KG, "Drank", None),
    (581, "Feijoadinha (Braziliaanse bonenschotel)", KG, "Hoofdgerecht", None),
    (627, "Romige karamelflan met tropisch fruit", KG, "Zoet & desserts", None),
    # Vederlicht (p. 17-20)
    (673, "Kipminestrone met erwtenpesto", KG, "Soep", None),
    (712, "Broodje kalkoendöner", KG, "Hoofdgerecht", None),
    (750, "Thaise kipsalade", KG, "Salade", None),
    (789, "In melk gesmoorde kalkoenfilet", KG, "Hoofdgerecht", None),
    # Zwoele zomeravonden (p. 21-24)
    (847, "Frisse regenboogsalade", KG, "Salade", None),
    (891, "Heerlijk barbecuevlees", KG, "Hoofdgerecht", None),
    (921, "Zomerse rode wijn ‘Tinto de verano’", KG, "Drank", None),
    (932, "Tomatendip met amandelen", KG, "Bijgerecht", None),
    (944, "Zomerse barbecuegroenten", KG, "Bijgerecht", None),
    (979, "Gegrilde ananas met vanille-ijs en karamelsaus", KG, "Zoet & desserts", None),
    # Op hete kolen (p. 29-38)
    (1122, "Italiaanse gehaktballen met pesto", KG, "Hoofdgerecht", None),
    (1167, "Ovenpasta met gerookte ham", KG, "Hoofdgerecht", None),
    (1201, "Knapperige lunchsalade met spek", KG, "Salade", None),
    (1230, "Snel vispannetje met gnocchi", KG, "Hoofdgerecht", None),
    (1255, "Procureursteaks met café-de-Parissaus", KG, "Hoofdgerecht", None),
    (1291, "Supersnelle snijbiet-paprikafrittata", KG, "Hoofdgerecht", None),
    (1327, "Luchtig kaasbrood", KG, "Bijgerecht", None),
    (1349, "Rode-uienconfituur", KG, "Bijgerecht", None),
    (1368, "Kipspiesjes van de barbecue", KG, "Hoofdgerecht", None),
    (1391, "Gevulde procureur met peterselie", KG, "Hoofdgerecht", None),
    (1433, "Couscous-fetasalade", KG, "Salade", None),
    (1478, "Zomerse ciderbowl", KG, "Drank", None),
    (1493, "Gegrilde zalm op cederhout", KG, "Hoofdgerecht", None),
    (1527, "Mangoguacamole", KG, "Bijgerecht", None),
    # Koken met cola (p. 41-43)
    (1708, "Ribeye met colasaus", KG, "Hoofdgerecht", None),
    (1752, "Colagoulash", KG, "Hoofdgerecht", None),
    (1791, "Zelfgebakken colabrood", KG, "Bijgerecht", None),
    (1831, "Currywurst met frisse salade", KG, "Hoofdgerecht", None),
    (1852, "Currywurstsaus met cola", KG, "Bijgerecht", None),
    # Antihooikoorts (p. 45-46)
    (1887, "Gebakken zalm met Thaise wortelsalade", KG, "Hoofdgerecht", None),
    (1938, "Kwarkbowl met fruit", KG, "Bijgerecht", None),
    (1970, "Turkse yoghurtsoep met köfte", KG, "Soep", None),
    (2011, "Kipfilet met lentegroenten", KG, "Hoofdgerecht", None),
    # Mexico in je mandje (p. 49)
    (2125, "Sweet ‘n’ sticky kip met gebakken mais, kaas en jalapeño", KG, "Hoofdgerecht", None),
    # Rabarbertijd (p. 51-53)
    (2198, "Rabarbercurd", KG, "Bijgerecht", None),
    (2211, "Kipfilet met rabarberchutney", KG, "Hoofdgerecht", None),
    (2241, "Rabarberbowl", KG, "Zoet & desserts", None),
    # Zoete inval (p. 54-55)
    (2262, "Rozencrème-brûlée met frambozensaus", KG, "Zoet & desserts", None),
    (2267, "Limoensorbet", KG, "Zoet & desserts", None),
    (2318, "Aardbei-kokostiramisu", KG, "Zoet & desserts", None),
    (2350, "Zelfgemaakte chocoladecrème", KG, "Zoet & desserts", None),
    # Makkie van 'n bakkie (p. 57-60)
    (2379, "Limoncello-rodebessentulband", KG, "Zoet & desserts", None),
    (2428, "Frambozenrolletjes", KG, "Zoet & desserts", None),
    (2472, "Siciliaans zomergebak met fruit", KG, "Zoet & desserts", None),
    (2510, "Blauwebessencake met ijs", KG, "Zoet & desserts", None),
    (2542, "Maanzaadcake met abrikozencompote", KG, "Zoet & desserts", None),
    # Lekker voor erbij (p. 62, coverrecept) and the cheesecake feature (p. 65)
    (2611, "Aardappelsalade met kwarteleitjes en dille", KG, "Salade", None),
    (2694, "Limoencheesecake met kumquat", KG, "Zoet & desserts", None),
]

HEADING_AS = {}

# one wide photo holds the photos of two recipes side by side; the captions are
# printed next to each other, so the combined caption is the key here
CAPTION_SPLIT = {
    "Currywurst met frisse salade Currywurstsaus met cola": [
        "Currywurst met frisse salade", "Currywurstsaus met cola"],
    "Ribeye met colasaus Colagoulash": ["Ribeye met colasaus", "Colagoulash"],
}

OVERRIDES = {
    # these recipes carry their quantities inside the running text, so the
    # parser finds no ingredient box; the lists below are read out of the text
    "IJskoude caipirinha": {
        "ingredients": [
            "4 bio-limoenen", "8 el lichte basterdsuiker", "crushed ijs",
            "3 el cachaça (Braziliaanse sterke drank, bij de slijter)",
        ],
        "instructions": [
            "Was 4 bio-limoenen en snijd ze in partjes. Verdeel de limoen en 8 el lichte basterdsuiker over 4 glazen. Plet de limoenpartjes goed met een (cocktail)stamper. Vul de glazen met crushed ijs en schenk in elk glas 3 el cachaça (Braziliaanse sterke drank, bij de slijter). Serveer ijskoud.",
            "Liever alcoholvrij? Vervang de cachaça dan door gingerale.",
        ],
    },
    # the closing bracket of the yield is lost in the PDF's text layer
    "Zomerse rode wijn ‘Tinto de verano’": {
        "yield": "6 glazen (à ca. 250 ml)",
        "ingredients": [
            "1 bio-citroen", "750 ml droge rode wijn",
            "750 ml goed gekoelde citroenlimonade", "ijsblokjes",
        ],
        "instructions": [
            "Was 1 bio-citroen met heet water en snijd hem in parten. Vul 6 glazen tot de helft met ijsblokjes. Verdeel 750 ml droge rode wijn over de glazen. Schenk 750 ml goed gekoelde citroenlimonade erbij. Versier met de citroenpartjes.",
        ],
    },
    "Tomatendip met amandelen": {
        "ingredients": [
            "50 g gezouten amandelen", "4 takjes tijm",
            "350 g zongedroogde tomaten op olie (pot)", "75 ml olie",
            "50 g pitloze zwarte olijven", "2 el tomatenpuree", "150 g roomkaas",
            "5 el water", "zout en peper",
        ],
        "instructions": [
            "Hak 50 g gezouten amandelen grof. Was 4 takjes tijm en hak de blaadjes fijn. Laat 350 g zongedroogde tomaten op olie (pot) uitlekken en vang hierbij 75 ml olie op. Hak de tomaten grof. Hak 50 g pitloze zwarte olijven klein. Pureer de tomaten, de olijven, de tijm en de olie. Voeg 2 el tomatenpuree, 150 g roomkaas en 5 el water toe en roer goed door elkaar. Breng op smaak met zout en peper. Roer de gezouten amandelen erdoorheen.",
        ],
    },
    "Rode-uienconfituur": {
        "ingredients": [
            "1 kg rode uien", "5 el olijfolie", "1 tl zout", "150 ml rode wijn",
            "200 ml balsamicoazijn", "½ tl gedroogde tijm",
            "½ tl gemalen komijnzaad", "½ tl gerooktepaprikapoeder",
            "50 g geleisuiker 2:1",
        ],
        "instructions": [
            "Pel 1 kg rode uien en snijd in partjes. Verhit 5 el olijfolie in een pan en voeg de ui en 1 tl zout toe. Bak de ui glazig. Blus af met 150 ml rode wijn en 200 ml balsamicoazijn en breng aan de kook. Roer ½ tl gedroogde tijm, ½ tl gemalen komijnzaad en ½ tl gerooktepaprikapoeder erdoorheen en laat met het deksel op de pan ca. 10 minuten smoren. Roer 50 g geleisuiker 2:1 erdoorheen. Breng opnieuw aan de kook en laat al roerend ca. 4 minuten flink koken. Doe de confituur in gesteriliseerde potjes, sluit af en laat een nacht afkoelen.",
        ],
    },
    "Kipspiesjes van de barbecue": {
        "ingredients": [
            "1,2 kg kipfilet", "75 ml teriyakisaus", "1 middelgrote ananas",
            "2 courgettes (à ca. 200 g)", "2 el ahornsiroop", "3 el olie",
            "zeezout en peper",
        ],
        "instructions": [
            "Laat 16 houten spiesjes ca. 2 uur in koud water weken. Dep 1,2 kg kipfilet droog en snijd in blokjes van ca. 2 cm. Meng met 75 ml teriyakisaus en laat ca. 2 uur marineren. Schil 1 middelgrote ananas, snijd hem in kwarten en verwijder de stronk. Snijd de ananas in stukjes. Was 2 courgettes (à ca. 200 g) en schaaf met een dunschiller in de lengte in dunne plakken. Laat de spiesjes uitlekken. Prik de ananas en de helft van de kip afwisselend aan de helft van de spiesjes en bestrijk de ananas met 2 el ahornsiroop. Steek de courgette waaiervormig en de rest van de kip afwisselend aan de rest van de spiesjes. Bestrijk de courgette met ca. 3 el olie en bestrooi met zeezout en peper. Gril de spiesjes op de directe hitte van de barbecue in ca. 5 minuten per zijde goudbruin en gaar.",
        ],
    },
    "Zomerse ciderbowl": {
        "ingredients": [
            "500 g aardbeien", "250 g frambozen", "250 g rode bessen",
            "350 ml crème de cassis", "2 bio-citroenen", "3 bio-limoenen",
            "5 takjes melisse (of gebruik munt)", "1,5 l gekoelde appelcider",
            "ijsblokjes",
        ],
        "instructions": [
            "Was 500 g aardbeien, 250 g frambozen en 250 g rode bessen en doe ze in een grote kom of pot. Schenk 350 ml crème de cassis erbij en laat ca. 3 uur trekken. Was 2 bio-citroenen en 3 bio-limoenen en snijd ze in dunne plakjes. Was 5 takjes melisse (of gebruik munt) en neem de blaadjes van de takjes. Doe de citroen, de limoen en de melisse in de kom en schenk 1,5 l gekoelde appelcider erbij. Verdeel voor het serveren ijsblokjes over glazen en schenk de ciderbowl erop.",
        ],
    },
    # running text as well; the block also holds the crossword page that follows
    # it, whose clue lines used to end up in the ingredients
    "Mangoguacamole": {
        "ingredients": [
            "1 avocado", "1 mango", "1 teentje knoflook", "1 rode chilipeper",
            "75 g Griekse yoghurt", "2 el limoensap", "zout en peper",
            "2 el krokante nootjes",
        ],
        "instructions": [
            "Halveer 1 avocado, verwijder de pit en schep het vruchtvlees uit de schil. Snijd het vruchtvlees in blokjes. Schil 1 mango, snijd het vruchtvlees van de pit en snijd het in blokjes. Pel en snipper 1 teentje knoflook. Snijd 1 rode chilipeper in de lengte in, verwijder de zaadlijsten, was de peper en hak hem fijn. Roer de avocado, de knoflook, de chilipeper, 75 g Griekse yoghurt, 2 el limoensap, zout en peper door elkaar; druk daarbij de avocado fijn met een vork. Roer de mango door de guacamole. Breng de guacamole nogmaals op smaak. Hak 2 el krokante nootjes grof en strooi over de guacamole.",
        ],
    },
    # the sauce kader is printed between this recipe's ingredients and its steps,
    # so both recipes lost their own text to the other one
    "Currywurst met frisse salade": {
        "ingredients": [
            "400 g ovenfriet (diepvries)", "½ krop ijsbergsla", "1 wortel",
            "zout en peper", "2 el appelazijn", "1 tl + 1-2 el olie",
            "2 el crème fraîche", "1 el mayonaise", "2 takjes peterselie",
            "4 braadworsten (à ca. 100 g)",
            "400 ml currywurstsaus met cola (zie kader hierboven)",
        ],
        "instructions": [
            "VOOR DE FRIET Verdeel de friet over een met bakpapier beklede bakplaat. Bak de friet volgens de aanwijzingen op de verpakking gaar in de oven.",
            "VOOR DE SALADE Was de ijsbergsla en snijd hem in fijne reepjes. Schrap de wortel en rasp hem fijn. Kneed de ijsbergsla, de wortel en een snufje zout kort door elkaar. Roer de azijn en 1 tl olie erdoorheen. Roer de crème fraîche glad met de mayonaise. Was de peterselie en hak hem grof. Spatel de peterselie en het mayonaisemengsel door de sla.",
            "VOOR DE WORST Verhit 1-2 el olie in een koekenpan op middelhoog vuur en bak de worsten rondom in 5-8 minuten gaar erin. Serveer de friet met de worst en de saus. Geef de salade erbij.",
        ],
    },
    "Currywurstsaus met cola": {
        "ingredients": [
            "500 ml cola", "500 ml ketchup", "8 el appelmoes",
            "3 el worcestershiresaus", "een paar druppels tabasco", "2 el curry",
            "2 tl limoensap", "zout",
        ],
        "instructions": [
            "Breng 500 ml cola in een pan en de kook en laat inkoken tot ca. 100 ml. Voeg 500 ml ketchup, 8 el appelmoes, 3 el worcestershiresaus, een paar druppels tabasco en 2 el curry toe, roer door elkaar en verhit kort. Breng de saus op smaak met 2 tl limoensap en zout.",
        ],
    },
    "Rabarbercurd": {
        "ingredients": [
            "500 g rabarber (bijv. rode)", "50 g suiker", "5 el water",
            "4 verse eidooiers", "150 g suiker", "1 vanillestokje",
            "1 snufje zout", "1 citroen", "2 el maizena", "110 g koude boter",
        ],
        "instructions": [
            "Was 500 g rabarber (bijv. rode) en snijd klein. Breng met 50 g suiker en 5 el water aan de kook en laat ca. 4 minuten zachtjes koken. Pureer de rabarber en laat even afkoelen. Klop 4 verse eidooiers, 150 g suiker, het merg van 1 vanillestokje, een snufje zout, het sap van 1 citroen en 2 el maizena au bain-marie romig. Voeg het eimengsel toe aan de rabarberpuree en verhit al roerend. Roer 110 g koude boter in stukjes erdoorheen, tot je een dikke crème hebt. Doe de rabarbercurd in gesteriliseerde potjes. Sluit de potjes af en laat afkoelen.",
        ],
    },
    "Rabarberbowl": {
        "ingredients": [
            "1 kg aardbeien", "150 g suiker", "8 g vanillesuiker",
            "1 l gekoelde rabarbernectar (online verkrijgbaar, of gebruik cranberrysap)",
            "750 ml gekoelde witte wijn", "3 takjes citroenmelisse",
            "750 ml gekoelde prosecco",
        ],
        "instructions": [
            "Was 1 kg aardbeien, verwijder de kroontjes en snijd de aardbeien klein. Doe de aardbeistukjes in een grote glazen kom en bestrooi met 150 g suiker en 8 g vanillesuiker. Laat de aardbeien ca. 1 uur trekken. Schenk 1 l gekoelde rabarbernectar (online verkrijgbaar, of gebruik cranberrysap) en 750 ml gekoelde witte wijn erbij en zet de bowl ca. 30 minuten in de koelkast om op smaak te komen. Was 3 takjes citroenmelisse en neem de blaadjes van de takjes. Voeg voor het serveren de melisse toe aan de bowl en vul aan met 750 ml gekoelde prosecco.",
        ],
    },
    # the two recipes on page 54 sit in columns the engine interleaved, so both
    # get their own text back (read from the page's column order)
    "Limoensorbet": {
        "ingredients": [
            "100 g lichte basterdsuiker", "200 g suiker", "8 limoenen",
            "4 el witte rum", "3 takjes munt", "1 vers eiwit",
            "1 bio-limoen (alleen de schil, geraspt)",
        ],
        "instructions": [
            "Breng 450 ml water met de basterdsuiker en de suiker kort aan de kook tot de suiker is gesmolten. Laat afkoelen. Pers de limoenen uit en meet 300 ml sap af. Doe met de suikersiroop en de rum in een metalen kom en roer goed door elkaar. Zet de kom in een ijswaterbad en laat al roerend afkoelen.",
            "Was de munt en neem de blaadjes van de takjes. Hak de helft van de blaadjes fijn. Klop het eiwit stijf. Spatel het eiwit, de fijngehakte munt en de helft van de limoenschil door het suikermengsel. Zet de kom in de diepvries en vries ca. 3 uur in. Roer het mengsel daarbij elke ca. 30 minuten goed door. Maak bolletjes van het ijs en zet nog ca. 30 minuten in de diepvries. Bestrooi de sorbet met de rest van de munt en de rest van de limoenschil.",
        ],
    },
    "Rozencrème-brûlée met frambozensaus": {
        "ingredients": [
            "400 ml slagroom", "150 ml melk", "5 verse eidooiers",
            "50 g + 6 el suiker",
            "5-6 el rozenwater (bij de toko of grotere supermarkt)",
            "400 g frambozen",
        ],
        "instructions": [
            "VOOR DE CRÈME BRÛLÉE Roer de slagroom, de melk, de eidooiers, 3 el rozenwater en 50 g suiker goed door elkaar. Schenk het mengsel door een zeef in vier kleine ovenschaaltjes (à ca. 250 ml inhoud).",
            "Verwarm de oven voor (elektrisch: 160°C / hetelucht: 140°C). Zet de ovenschaaltjes in een grote ovenschaal en schenk er heet water bij tot de vormpjes voor de helft onder staan. Bak ca. 1 uur in de oven, tot de crème gestold is. Neem uit de oven, laat even afkoelen en zet minimaal 6 uur in de koelkast.",
            "VOOR DE SAUS Maak de frambozen schoon. Pureer ⅔ van de frambozen en druk ze door een zeef. Roer de frambozenpuree, 2 el suiker en 2-3 el rozenwater door elkaar. Spatel de rest van de frambozen erdoorheen. Bestrooi elke crème brûlée met 1 el suiker en karamelliseer goudbruin met een gasbrandertje. Serveer de crème brûlée met de frambozensaus.",
        ],
    },
}
