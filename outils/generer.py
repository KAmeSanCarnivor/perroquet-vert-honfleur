# -*- coding: utf-8 -*-
"""Génère les 6 versions du site (fr à la racine, en/nl/de/es/ko dans leur dossier).
Usage : python outils/generer.py   (à relancer après toute modification des textes ou du gabarit)"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["fr", "en", "nl", "de", "es", "ko"]
LABEL = {"fr": "FR", "en": "EN", "nl": "NL", "de": "DE", "es": "ES", "ko": "한국어"}
HTMLLANG = {"fr": "fr", "en": "en", "nl": "nl", "de": "de", "es": "es", "ko": "ko"}
TEL = "02 31 89 14 19"
TELHREF = "+33231891419"
INSTA = "https://www.instagram.com/perroquet_vert_honfleur"
MAPS = "https://www.google.com/maps/search/?api=1&query=Perroquet+Vert+52+Quai+Sainte-Catherine+Honfleur"

T = {}

T["fr"] = dict(
 title="Le Perroquet Vert · Bar et brunch sur le bassin, Honfleur",
 desc="Le Perroquet Vert, quai Sainte-Catherine à Honfleur : petit-déjeuner, brunch, planches, cocktails, une soixantaine de bières, billard et fléchettes face au bassin. Ouvert de 8 h à 1 h.",
 nav=["Le lieu", "La carte", "L'histoire", "Infos"],
 kicker="Honfleur · Quai Sainte-Catherine",
 h1="Du premier café au dernier verre, face au bassin.",
 lead="Un bar de quai ouvert à tous, avec sa salle de jeux, sa cave à bières et sa terrasse sur l'eau.",
 cta=["Voir la carte", "Venir nous voir"],
 s1=["Le lieu", "Un bar de quai, ouvert à tous",
     "Petit-déjeuner en terrasse, brunch face aux bateaux, planche à partager, bière pression ou cocktail le soir : le Perroquet Vert suit la journée du bassin, heure après heure.",
     "Le café du matin, la promenade de l'après-midi, le dernier verre : chaque moment a son public, et tous partagent le même quai."],
 feat=[("Billard", "Une table sous les poutres, les fenêtres sur le port."),
       ("Fléchettes", "Pour une partie entre amis, à toute heure."),
       ("Terrasse sur le quai", "Agrandie chaque été, d'avril à fin octobre."),
       ("Wi-Fi et prises", "Pour travailler un moment ou recharger le téléphone.")],  # masqué en français (voir build)
 c=["La carte", "À toute heure, de quoi boire et manger",
    "Une carte simple, qui suit la journée. La carte complète se découvre sur place."],
 m=[("Petit-déjeuner", "Café, jus d'orange pressé, viennoiseries : les formules du matin se prennent en terrasse ou en salle."),
    ("Déjeuner et brunch", "Salades, club sandwich, croque et burger, servis à l'heure du déjeuner."),
    ("Planches", "Charcuteries, andouille de Vire et pain frais, à partager à l'heure de l'apéritif."),
    ("Cocktails", "Du spritz aux verres plus gourmands, à siroter en terrasse ou à l'intérieur.")],
 veg="Options végétariennes",
 b=["Les bières", "Une soixantaine de bières, de Normandie, de Belgique et d'ailleurs",
    "Trois bières pression, dont l'une change régulièrement pour faire découvrir de nouvelles brasseries. En bouteille, la sélection voyage dans de nombreux pays. Et la maison a sa propre bière : la Bière du Perroquet."],
 h=["L'histoire", "Depuis 1975, au bord du bassin",
    "Le Perroquet Vert tient son quai depuis 1975. Pierre apparente, poutres sombres, fenêtres ouvertes sur les bateaux : le lieu a gardé sa matière et s'est mis au goût du jour, sans rien perdre de sa chaleur.",
    "Les habitués de Honfleur et les voyageurs du monde entier poussent la même porte, à toutes heures. Du café du matin au dernier verre, chacun y trouve sa place.",
    "Une équipe de quatre à dix personnes selon la saison fait vivre la maison, du petit-déjeuner jusqu'à une heure du matin."],
 i=["Infos pratiques", "Venir au Perroquet Vert"],
 info=[("Adresse", "52 quai Sainte-Catherine<br>14600 Honfleur"),
       ("Horaires", "Tous les jours, de 8 h à 1 h<br><small>Horaires susceptibles de varier selon la saison.</small>"),
       ("Téléphone", "Pas de réservation en général. Pour une occasion particulière, un appel suffit."),
       ("Accès", "Quai piéton."),
       ("Sur place", "Terrasse, salle intérieure, billard, fléchettes, animaux acceptés, options végétariennes."),
       ("Langues parlées", "Français, anglais.")],
 map="Ouvrir dans Maps", insta="Instagram",
 alc="L'abus d'alcool est dangereux pour la santé. À consommer avec modération.",
 alt=["Terrasse du Perroquet Vert face au bassin de Honfleur", "Petit-déjeuner en terrasse face au bassin", "Sandwich au saumon fumé et salade", "Planche de charcuteries et bières face au port", "Cocktails sur une table de bois", "Bière trappiste devant la vitrine de bières", "Table de billard sous les poutres"],
)

T["en"] = dict(
 title="Le Perroquet Vert · Bar and brunch on the harbour, Honfleur",
 desc="Le Perroquet Vert, quai Sainte-Catherine in Honfleur: breakfast, brunch, sharing boards, cocktails, around seventy beers, pool and darts facing the old harbour. Open 8 am to 1 am.",
 nav=["The place", "The menu", "Our story", "Info"],
 kicker="Honfleur · Quai Sainte-Catherine",
 h1="From the first coffee to the last drink, right on the harbour.",
 lead="A quayside bar for everyone, with a games room, a beer cellar and a terrace on the water.",
 cta=["See the menu", "Come and visit"],
 s1=["The place", "A quayside bar, open to all",
     "Breakfast on the terrace, brunch facing the boats, a board to share, a draught beer or a cocktail in the evening: Le Perroquet Vert follows the rhythm of the harbour, hour after hour.",
     "The morning coffee, the afternoon stroll, the last drink: each moment has its own crowd, and everyone shares the same quay."],
 feat=[("Pool", "A table under the beams, with windows onto the harbour."),
       ("Darts", "A game with friends, at any hour."),
       ("Quayside terrace", "Extended every summer, from April to the end of October."),
       ("Wi-Fi and sockets", "To work for a while or to charge your phone.")],
 c=["The menu", "Something to drink and eat, at any hour",
    "A simple menu that follows the day. The full menu is waiting for you on the spot."],
 m=[("Breakfast", "Coffee, fresh orange juice, pastries: morning sets are served on the terrace or inside."),
    ("Lunch and brunch", "Salads, club sandwich, croque and burger, served at lunchtime."),
    ("Sharing boards", "Charcuterie, andouille de Vire and fresh bread, to share at aperitif time."),
    ("Cocktails", "From the spritz to richer, more indulgent glasses, to sip on the terrace or indoors.")],
 veg="Vegetarian options",
 b=["The beers", "Around seventy beers, from Normandy, Belgium and beyond",
    "Three draught beers, one of which changes regularly to introduce new breweries. In bottles, the selection travels across many countries. And the house has its own beer: the Bière du Perroquet."],
 h=["Our story", "Since 1975, beside the harbour",
    "Le Perroquet Vert has held its spot on the quay since 1975. Exposed stone, dark beams, windows opening onto the boats: the place has kept its character and moved with the times, without losing any of its warmth.",
    "Honfleur regulars and travellers from all over the world walk through the same door, at all hours. From the morning coffee to the last drink, everyone finds their place.",
    "A team of four to ten people, depending on the season, runs the house from breakfast until one in the morning."],
 i=["Practical information", "Finding Le Perroquet Vert"],
 info=[("Address", "52 quai Sainte-Catherine<br>14600 Honfleur, France"),
       ("Opening hours", "Every day, 8 am to 1 am<br><small>Hours may vary with the season.</small>"),
       ("Telephone", "We do not usually take bookings. For a special occasion, a phone call will do."),
       ("Access", "Pedestrian quay."),
       ("On site", "Terrace, indoor room, pool, darts, Wi-Fi, charging sockets, pets welcome, vegetarian options."),
       ("Languages spoken", "French, English.")],
 map="Open in Maps", insta="Instagram",
 alc="Excessive alcohol consumption is harmful to your health. Please drink responsibly.",
 alt=["The terrace of Le Perroquet Vert facing Honfleur harbour", "Breakfast on the terrace facing the harbour", "Smoked salmon sandwich and salad", "Charcuterie board and beers facing the harbour", "Cocktails on a wooden table", "Trappist beer in front of the beer display", "Pool table under the beams"],
)

T["nl"] = dict(
 title="Le Perroquet Vert · Bar en brunch aan de haven, Honfleur",
 desc="Le Perroquet Vert, quai Sainte-Catherine in Honfleur: ontbijt, brunch, borrelplanken, cocktails, een zeventigtal bieren, pool en darts met uitzicht op de haven. Open van 8.00 tot 1.00 uur.",
 nav=["De plek", "De kaart", "Het verhaal", "Info"],
 kicker="Honfleur · Quai Sainte-Catherine",
 h1="Van de eerste koffie tot het laatste glas, aan het water.",
 lead="Een bar aan de kade, voor iedereen, met een speelzaal, een bierkelder en een terras aan het water.",
 cta=["Bekijk de kaart", "Kom langs"],
 s1=["De plek", "Een bar aan de kade, open voor iedereen",
     "Ontbijt op het terras, brunch met zicht op de boten, een plank om te delen, een tapbiertje of een cocktail 's avonds: Le Perroquet Vert volgt de dag aan de haven, uur na uur.",
     "De ochtendkoffie, de wandeling in de middag, het laatste glas: elk moment heeft zijn eigen publiek, en iedereen deelt dezelfde kade."],
 feat=[("Pool", "Een tafel onder de balken, met ramen op de haven."),
       ("Darts", "Een potje met vrienden, op elk uur."),
       ("Terras aan de kade", "Elke zomer uitgebreid, van april tot eind oktober."),
       ("Wifi en stopcontacten", "Om even te werken of je telefoon op te laden.")],
 c=["De kaart", "Op elk uur iets te drinken en te eten",
    "Een eenvoudige kaart die de dag volgt. De volledige kaart ontdekt u ter plaatse."],
 m=[("Ontbijt", "Koffie, verse jus d'orange, gebak: de ochtendmenu's worden op het terras of binnen geserveerd."),
    ("Lunch en brunch", "Salades, clubsandwich, croque en burger, geserveerd rond de lunch."),
    ("Borrelplanken", "Charcuterie, andouille de Vire en vers brood, om te delen rond het aperitief."),
    ("Cocktails", "Van spritz tot rijkere glazen, om te nippen op het terras of binnen.")],
 veg="Vegetarische opties",
 b=["De bieren", "Een zeventigtal bieren uit Normandië, België en daarbuiten",
    "Drie tapbieren, waarvan er één regelmatig wisselt om nieuwe brouwerijen te laten ontdekken. Op fles reist de selectie door tal van landen. En het huis heeft zijn eigen bier: de Bière du Perroquet."],
 h=["Het verhaal", "Sinds 1975 aan de haven",
    "Le Perroquet Vert staat al sinds 1975 op zijn plek aan de kade. Zichtbare natuursteen, donkere balken, ramen met uitzicht op de boten: de plek heeft zijn karakter behouden en is met zijn tijd meegegaan, zonder iets van zijn warmte te verliezen.",
    "Vaste gasten uit Honfleur en reizigers uit de hele wereld stappen door dezelfde deur, op alle uren. Van de ochtendkoffie tot het laatste glas vindt iedereen hier zijn plek.",
    "Een team van vier tot tien mensen, afhankelijk van het seizoen, houdt het huis draaiende, van het ontbijt tot één uur 's nachts."],
 i=["Praktische informatie", "Naar Le Perroquet Vert"],
 info=[("Adres", "52 quai Sainte-Catherine<br>14600 Honfleur, Frankrijk"),
       ("Openingstijden", "Elke dag van 8.00 tot 1.00 uur<br><small>De uren kunnen per seizoen variëren.</small>"),
       ("Telefoon", "Wij werken meestal niet met reserveringen. Voor een bijzondere gelegenheid volstaat een telefoontje."),
       ("Bereikbaarheid", "Voetgangerskade."),
       ("Ter plaatse", "Terras, binnenzaal, pool, darts, wifi, oplaadpunten, huisdieren welkom, vegetarische opties."),
       ("Gesproken talen", "Frans, Engels.")],
 map="Openen in Maps", insta="Instagram",
 alc="Overmatig alcoholgebruik is schadelijk voor de gezondheid. Geniet met mate.",
 alt=["Het terras van Le Perroquet Vert met uitzicht op de haven van Honfleur", "Ontbijt op het terras met uitzicht op de haven", "Sandwich met gerookte zalm en salade", "Charcuterieplank en bieren met uitzicht op de haven", "Cocktails op een houten tafel", "Trappistenbier voor de bierkast", "Pooltafel onder de balken"],
)

T["de"] = dict(
 title="Le Perroquet Vert · Bar und Brunch am Hafen, Honfleur",
 desc="Le Perroquet Vert, Quai Sainte-Catherine in Honfleur: Frühstück, Brunch, Vesperplatten, Cocktails, rund siebzig Biere, Billard und Darts mit Blick auf das Hafenbecken. Täglich von 8 bis 1 Uhr geöffnet.",
 nav=["Das Haus", "Die Karte", "Die Geschichte", "Infos"],
 kicker="Honfleur · Quai Sainte-Catherine",
 h1="Vom ersten Kaffee bis zum letzten Glas, direkt am Hafenbecken.",
 lead="Eine Bar am Kai für alle, mit Spielzimmer, Bierkeller und einer Terrasse am Wasser.",
 cta=["Zur Karte", "Besuchen Sie uns"],
 s1=["Das Haus", "Eine Bar am Kai, offen für alle",
     "Frühstück auf der Terrasse, Brunch mit Blick auf die Boote, eine Platte zum Teilen, ein Bier vom Fass oder abends ein Cocktail: Das Perroquet Vert begleitet den Tag am Hafen, Stunde um Stunde.",
     "Der Morgenkaffee, der Spaziergang am Nachmittag, das letzte Glas: Jeder Moment hat sein eigenes Publikum, und alle teilen sich denselben Kai."],
 feat=[("Billard", "Ein Tisch unter den Balken, mit Fenstern zum Hafen."),
       ("Darts", "Eine Partie unter Freunden, zu jeder Stunde."),
       ("Terrasse am Kai", "Jeden Sommer erweitert, von April bis Ende Oktober."),
       ("WLAN und Steckdosen", "Zum Arbeiten oder um das Handy aufzuladen.")],
 c=["Die Karte", "Zu jeder Stunde etwas zu trinken und zu essen",
    "Eine schlichte Karte, die dem Tag folgt. Die vollständige Karte entdecken Sie vor Ort."],
 m=[("Frühstück", "Kaffee, frisch gepresster Orangensaft, Gebäck: Die Frühstücksmenüs werden auf der Terrasse oder drinnen serviert."),
    ("Mittagessen und Brunch", "Salate, Club Sandwich, Croque und Burger, zur Mittagszeit serviert."),
    ("Vesperplatten", "Aufschnitt, Andouille de Vire und frisches Brot zum Teilen zur Aperitifzeit."),
    ("Cocktails", "Vom Spritz bis zu üppigeren Gläsern, zum Genießen auf der Terrasse oder drinnen.")],
 veg="Vegetarische Optionen",
 b=["Die Biere", "Rund siebzig Biere aus der Normandie, aus Belgien und aus aller Welt",
    "Drei Biere vom Fass, von denen eines regelmäßig wechselt, um neue Brauereien vorzustellen. Bei den Flaschenbieren reist die Auswahl durch viele Länder. Und das Haus hat sein eigenes Bier: das Bière du Perroquet."],
 h=["Die Geschichte", "Seit 1975 am Hafenbecken",
    "Das Perroquet Vert steht seit 1975 an seinem Platz am Kai. Sichtbarer Naturstein, dunkle Balken, Fenster mit Blick auf die Boote: Das Haus hat seinen Charakter bewahrt und ist mit der Zeit gegangen, ohne etwas von seiner Wärme zu verlieren.",
    "Stammgäste aus Honfleur und Reisende aus aller Welt treten durch dieselbe Tür, zu jeder Tageszeit. Vom Morgenkaffee bis zum letzten Glas findet hier jeder seinen Platz.",
    "Ein Team von vier bis zehn Personen, je nach Saison, führt das Haus, vom Frühstück bis ein Uhr nachts."],
 i=["Praktische Informationen", "So finden Sie das Perroquet Vert"],
 info=[("Adresse", "52 Quai Sainte-Catherine<br>14600 Honfleur, Frankreich"),
       ("Öffnungszeiten", "Täglich von 8 bis 1 Uhr<br><small>Die Zeiten können je nach Saison variieren.</small>"),
       ("Telefon", "In der Regel nehmen wir keine Reservierungen an. Für einen besonderen Anlass genügt ein Anruf."),
       ("Anfahrt", "Fußgängerkai."),
       ("Vor Ort", "Terrasse, Innenraum, Billard, Darts, WLAN, Ladesteckdosen, Haustiere willkommen, vegetarische Optionen."),
       ("Gesprochene Sprachen", "Französisch, Englisch.")],
 map="In Maps öffnen", insta="Instagram",
 alc="Übermäßiger Alkoholkonsum ist gesundheitsschädlich. Bitte genießen Sie verantwortungsvoll.",
 alt=["Die Terrasse des Perroquet Vert mit Blick auf das Hafenbecken von Honfleur", "Frühstück auf der Terrasse mit Blick auf den Hafen", "Sandwich mit Räucherlachs und Salat", "Aufschnittplatte und Biere mit Blick auf den Hafen", "Cocktails auf einem Holztisch", "Trappistenbier vor der Bierauslage", "Billardtisch unter den Balken"],
)

T["es"] = dict(
 title="Le Perroquet Vert · Bar y brunch en el puerto, Honfleur",
 desc="Le Perroquet Vert, quai Sainte-Catherine en Honfleur: desayuno, brunch, tablas para compartir, cócteles, unas setenta cervezas, billar y dardos frente a la dársena. Abierto de 8:00 a 1:00.",
 nav=["El local", "La carta", "La historia", "Información"],
 kicker="Honfleur · Quai Sainte-Catherine",
 h1="Del primer café a la última copa, frente a la dársena.",
 lead="Un bar de muelle abierto a todos, con sala de juegos, una selección de cervezas y una terraza junto al agua.",
 cta=["Ver la carta", "Venga a vernos"],
 s1=["El local", "Un bar de muelle, abierto a todos",
     "Desayuno en la terraza, brunch frente a los barcos, una tabla para compartir, una caña o un cóctel por la noche: Le Perroquet Vert sigue el ritmo del puerto, hora tras hora.",
     "El café de la mañana, el paseo de la tarde, la última copa: cada momento tiene su público, y todos comparten el mismo muelle."],
 feat=[("Billar", "Una mesa bajo las vigas, con ventanas al puerto."),
       ("Dardos", "Una partida entre amigos, a cualquier hora."),
       ("Terraza en el muelle", "Ampliada cada verano, de abril a finales de octubre."),
       ("Wifi y enchufes", "Para trabajar un rato o cargar el móvil.")],
 c=["La carta", "A cualquier hora, algo para beber y comer",
    "Una carta sencilla que sigue el ritmo del día. La carta completa se descubre en el local."],
 m=[("Desayuno", "Café, zumo de naranja natural, bollería: los desayunos se sirven en la terraza o en el interior."),
    ("Almuerzo y brunch", "Ensaladas, club sándwich, croque y hamburguesa, a la hora del almuerzo."),
    ("Tablas", "Embutidos, andouille de Vire y pan fresco, para compartir a la hora del aperitivo."),
    ("Cócteles", "Del spritz a copas más golosas, para saborear en la terraza o en el interior.")],
 veg="Opciones vegetarianas",
 b=["Las cervezas", "Unas setenta cervezas de Normandía, Bélgica y otros países",
    "Tres cervezas de barril, una de las cuales cambia con regularidad para dar a conocer nuevas cervecerías. En botella, la selección viaja por numerosos países. Y la casa tiene su propia cerveza: la Bière du Perroquet."],
 h=["La historia", "Desde 1975, junto a la dársena",
    "Le Perroquet Vert ocupa su lugar en el muelle desde 1975. Piedra vista, vigas oscuras, ventanas abiertas a los barcos: el local ha conservado su carácter y se ha puesto al día, sin perder nada de su calidez.",
    "Los habituales de Honfleur y los viajeros de todo el mundo cruzan la misma puerta, a todas horas. Del café de la mañana a la última copa, cada uno encuentra aquí su sitio.",
    "Un equipo de cuatro a diez personas, según la temporada, mantiene la casa en marcha, desde el desayuno hasta la una de la madrugada."],
 i=["Información práctica", "Cómo llegar a Le Perroquet Vert"],
 info=[("Dirección", "52 quai Sainte-Catherine<br>14600 Honfleur, Francia"),
       ("Horario", "Todos los días, de 8:00 a 1:00<br><small>El horario puede variar según la temporada.</small>"),
       ("Teléfono", "Normalmente no se reserva. Para una ocasión especial, basta con una llamada."),
       ("Acceso", "Muelle peatonal."),
       ("En el local", "Terraza, sala interior, billar, dardos, wifi, enchufes para cargar, se admiten mascotas, opciones vegetarianas."),
       ("Idiomas", "Francés, inglés.")],
 map="Abrir en Maps", insta="Instagram",
 alc="El abuso del alcohol es perjudicial para la salud. Consuma con moderación.",
 alt=["La terraza de Le Perroquet Vert frente a la dársena de Honfleur", "Desayuno en la terraza frente al puerto", "Sándwich de salmón ahumado y ensalada", "Tabla de embutidos y cervezas frente al puerto", "Cócteles sobre una mesa de madera", "Cerveza trapense frente a la vitrina de cervezas", "Mesa de billar bajo las vigas"],
)

T["ko"] = dict(
 title="르 페로케 베르 · 옹플뢰르 항구의 바 & 브런치",
 desc="옹플뢰르 생트카트린 부두의 르 페로케 베르(Le Perroquet Vert). 아침 식사, 브런치, 안주 플래터, 칵테일, 약 70종의 맥주, 당구와 다트를 항구를 바라보며 즐기세요. 매일 오전 8시부터 새벽 1시까지.",
 nav=["공간", "메뉴", "이야기", "안내"],
 kicker="옹플뢰르 · 생트카트린 부두",
 h1="첫 커피부터 마지막 한 잔까지, 항구 바로 앞에서.",
 lead="누구에게나 열려 있는 부둣가의 바. 게임룸과 맥주 셀렉션, 물가의 테라스가 있습니다.",
 cta=["메뉴 보기", "찾아오시는 길"],
 s1=["공간", "누구에게나 열려 있는 부둣가의 바",
     "테라스에서 즐기는 아침 식사, 배를 바라보며 먹는 브런치, 함께 나누는 플래터, 저녁의 생맥주 한 잔과 칵테일. 르 페로케 베르는 항구의 하루를 시간마다 따라갑니다.",
     "아침 커피, 오후의 산책, 마지막 한 잔. 시간마다 찾아오는 손님은 다르지만, 모두가 같은 부두를 함께 나눕니다."],
 feat=[("당구", "항구가 내다보이는 창가, 들보 아래의 당구대."),
       ("다트", "친구들과 함께하는 한 게임, 언제든지."),
       ("부두 테라스", "매년 4월부터 10월 말까지 확장됩니다."),
       ("와이파이와 충전", "잠시 일을 하거나 휴대폰을 충전하세요.")],
 c=["메뉴", "언제든 마시고 먹을 수 있는 곳",
    "하루의 흐름에 맞춘 간결한 메뉴입니다. 전체 메뉴는 매장에서 확인하실 수 있습니다."],
 m=[("아침 식사", "커피, 갓 짠 오렌지 주스, 빵. 아침 세트는 테라스나 실내에서 드실 수 있습니다."),
    ("점심 & 브런치", "샐러드, 클럽 샌드위치, 크로크, 버거를 점심시간에 즐기실 수 있습니다."),
    ("플래터", "샤퀴트리, 비르산 앙두이으, 신선한 빵. 아페리티프 시간에 함께 나누세요."),
    ("칵테일", "가벼운 스프리츠부터 달콤하고 풍성한 잔까지, 테라스와 실내에서 즐기세요.")],
 veg="채식 메뉴",
 b=["맥주", "노르망디, 벨기에, 그리고 세계 각지의 맥주 약 70종",
    "생맥주 세 종류 중 하나는 새로운 양조장을 소개하기 위해 정기적으로 바뀝니다. 병맥주는 여러 나라의 맥주로 구성되어 있습니다. 그리고 이 집만의 맥주, 비에르 뒤 페로케도 있습니다."],
 h=["이야기", "1975년부터, 항구 곁에서",
    "르 페로케 베르는 1975년부터 이 부두를 지켜 왔습니다. 드러난 돌벽, 짙은 색의 들보, 배가 보이는 창. 공간은 본연의 질감을 간직한 채 오늘의 감각으로 다듬어졌고, 따뜻함은 그대로입니다.",
    "옹플뢰르의 단골손님과 세계 각지의 여행자가 하루 중 언제든 같은 문을 열고 들어옵니다. 아침 커피부터 마지막 한 잔까지, 누구나 이곳에서 자기 자리를 찾습니다.",
    "계절에 따라 4명에서 10명으로 이루어진 팀이 아침 식사부터 새벽 1시까지 이곳을 운영합니다."],
 i=["이용 안내", "르 페로케 베르 찾아오시는 길"],
 info=[("주소", "52 quai Sainte-Catherine<br>14600 Honfleur, 프랑스"),
       ("영업시간", "매일 오전 8시 ~ 새벽 1시<br><small>계절에 따라 달라질 수 있습니다.</small>"),
       ("전화", "일반적으로 예약은 받지 않습니다. 특별한 날에는 전화로 문의해 주세요."),
       ("오시는 길", "보행자 전용 부두."),
       ("편의시설", "테라스, 실내 홀, 당구, 다트, 와이파이, 충전 콘센트, 반려동물 동반 가능, 채식 메뉴."),
       ("사용 언어", "프랑스어, 영어.")],
 map="지도에서 열기", insta="인스타그램",
 alc="과도한 음주는 건강에 해롭습니다. 적당히 즐기세요.",
 alt=["옹플뢰르 항구를 마주한 르 페로케 베르의 테라스", "항구를 바라보는 테라스의 아침 식사", "훈제 연어 샌드위치와 샐러드", "항구 앞의 샤퀴트리 플래터와 맥주", "나무 테이블 위의 칵테일", "맥주 진열장 앞의 트라피스트 맥주", "들보 아래의 당구대"],
)

ML={"fr":"Mentions légales","en":"Legal notice (in French)","nl":"Wettelijke vermeldingen (in het Frans)","de":"Impressum (auf Französisch)","es":"Aviso legal (en francés)","ko":"법적 고지 (프랑스어)"}

PAGE = """<!doctype html>
<html lang="{hl}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0e100e">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="{p}img/terrasse.jpg">
<link rel="icon" href="{p}img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Jost:wght@300;400;500&family=Noto+Serif+KR:wght@400;600&family=Noto+Sans+KR:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<div class="rail" aria-hidden="true"><span class="ball"><i>8</i></span></div>
<header class="top">
  <a class="brand" href="#haut" aria-label="Le Perroquet Vert"><img src="{p}img/logo.png" alt="Le Perroquet Vert Honfleur" width="150" height="104"></a>
  <nav aria-label="Menu">
    <a href="#lieu">{n0}</a><a href="#carte">{n1}</a><a href="#histoire">{n2}</a><a href="#infos">{n3}</a>
  </nav>
  <div class="langs" role="navigation" aria-label="Langue">{langs}</div>
</header>
<main id="haut">
<section class="hero" style="--bg:url('{p}img/terrasse.jpg')">
  <div class="hero-in">
    <img class="hero-logo" src="{p}img/logo.png" alt="" width="260" height="180">
    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <p class="cta"><a class="btn" href="#carte">{cta0}</a><a class="btn ghost" href="#infos">{cta1}</a></p>
  </div>
</section>

<section id="lieu" class="sec">
  <div class="wrap two">
    <div class="txt rv">
      <p class="eyebrow">{s10}</p>
      <h2>{s11}</h2>
      <p>{s12}</p>
      <p>{s13}</p>
    </div>
    <figure class="ph rv"><img src="{p}img/petit-dejeuner.jpg" alt="{alt1}" loading="lazy" width="1080" height="809"></figure>
  </div>
  <ul class="wrap feats n{nfeat}">
{feats}
  </ul>
</section>

<section id="carte" class="sec alt">
  <div class="wrap">
    <div class="head rv">
      <p class="eyebrow">{c0}</p>
      <h2>{c1}</h2>
      <p>{c2}</p>
    </div>
    <div class="cards">
{cards}
    </div>
  </div>
</section>

<section id="bieres" class="beer">
  <div class="wrap two flip">
    <figure class="ph tall rv"><img src="{p}img/biere.jpg" alt="{alt5}" loading="lazy" width="912" height="1510"></figure>
    <div class="txt rv">
      <p class="eyebrow">{b0}</p>
      <h2>{b1}</h2>
      <p>{b2}</p>
    </div>
  </div>
</section>

<section id="histoire" class="sec">
  <div class="wrap two">
    <div class="txt rv">
      <p class="eyebrow">{h0}</p>
      <h2>{h1t}</h2>
      <p>{h2}</p>
      <p>{h3}</p>
    </div>
    <figure class="ph rv"><img src="{p}img/billard.jpg" alt="{alt6}" loading="lazy" width="1080" height="1440"></figure>
  </div>
</section>

<section id="infos" class="sec alt">
  <div class="wrap">
    <div class="head rv"><p class="eyebrow">{i0}</p><h2>{i1}</h2></div>
    <div class="info">
{info}
    </div>
    <p class="links rv"><a class="btn" href="tel:{telh}">{tel}</a><a class="btn ghost" href="{maps}" target="_blank" rel="noopener">{mapl}</a><a class="btn ghost" href="{insta}" target="_blank" rel="noopener">{instal}</a></p>
  </div>
</section>
</main>
<footer>
  <img src="{p}img/logo.png" alt="" width="90" height="62">
  <p>Le Perroquet Vert · 52 quai Sainte-Catherine · 14600 Honfleur</p>
  <p class="alc">{alc}</p>
  <p class="alc"><a href="{p}mentions-legales.html">{ml}</a></p>
</footer>
<script src="{p}site.js" defer></script>
</body>
</html>
"""

def build(lang):
    t = T[lang]
    p = "" if lang == "fr" else "../"
    path = "" if lang == "fr" else lang + "/"
    langs = "".join(
        '<a href="%s" hreflang="%s"%s>%s</a>' % (
            ("%s" % ("./" if lang == "fr" else "../") if l == "fr" else ("%s%s/" % ("" if lang == "fr" else "../", l))),
            l, ' aria-current="true"' if l == lang else "", LABEL[l])
        for l in LANGS)
    alts = "\n".join('<link rel="alternate" hreflang="%s" href="https://CHEMIN-A-DEFINIR/%s">' % (l, "" if l == "fr" else l + "/") for l in LANGS)
    if lang == "fr":  # Wi-Fi et prises : mentionnés seulement pour les visiteurs étrangers
        t = dict(t, feat=t["feat"][:3])
    feats = "\n".join('    <li class="rv"><h3>%s</h3><p>%s</p></li>' % (a, b) for a, b in t["feat"])
    imgs = [("petit-dejeuner", 809, 1080, t["alt"][1]), ("sandwich", 1440, 1080, t["alt"][2]),
            ("planche", 814, 1080, t["alt"][3]), ("cocktails", 1440, 1080, t["alt"][4])]
    cards = []
    for k, ((name, h, w, alt), (mt, md)) in enumerate(zip(imgs, t["m"])):
        veg = '<span class="tag">%s</span>' % t["veg"] if k == 1 else ""
        cards.append('      <article class="card rv"><img src="%simg/%s.jpg" alt="%s" loading="lazy" width="%d" height="%d"><div><h3>%s</h3><p>%s</p>%s</div></article>' % (p, name, alt, w, h, mt, md, veg))
    info = "\n".join('      <div class="rv"><h3>%s</h3><p>%s</p></div>' % (a, b) for a, b in t["info"])
    info = info.replace("</p></div>", "</p></div>", 1)
    ld = ('{"@context":"https://schema.org","@type":"BarOrPub","name":"Le Perroquet Vert","description":"%s",'
          '"telephone":"+33 2 31 89 14 19","address":{"@type":"PostalAddress","streetAddress":"52 quai Sainte-Catherine","postalCode":"14600","addressLocality":"Honfleur","addressCountry":"FR"},'
          '"openingHours":"Mo-Su 08:00-01:00","servesCuisine":"Brunch, planches, bières","sameAs":["%s"],"image":"img/terrasse.jpg"}') % (t["desc"].replace('"', "'"), INSTA)
    out = PAGE.format(
        hl=HTMLLANG[lang], title=html.escape(t["title"]), desc=html.escape(t["desc"]), p=p, path=path, alts=alts, ld=ld,
        n0=t["nav"][0], n1=t["nav"][1], n2=t["nav"][2], n3=t["nav"][3], langs=langs, kicker=t["kicker"], h1=t["h1"], lead=t["lead"],
        cta0=t["cta"][0], cta1=t["cta"][1], s10=t["s1"][0], s11=t["s1"][1], s12=t["s1"][2], s13=t["s1"][3], alt1=t["alt"][1],
        feats=feats, nfeat=len(t["feat"]), c0=t["c"][0], c1=t["c"][1], c2=t["c"][2], cards="\n".join(cards),
        b0=t["b"][0], b1=t["b"][1], b2=t["b"][2], alt5=t["alt"][5],
        h0=t["h"][0], h1t=t["h"][1], h2=t["h"][2], h3=t["h"][3], h4=t["h"][4], alt6=t["alt"][6],
        i0=t["i"][0], i1=t["i"][1], info=info, telh=TELHREF, tel=TEL, maps=MAPS, mapl=t["map"], insta=INSTA, instal=t["insta"], alc=t["alc"], ml=ML[lang])
    d = ROOT if lang == "fr" else os.path.join(ROOT, lang)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(out)

for l in LANGS:
    build(l)
print("ok", LANGS)
