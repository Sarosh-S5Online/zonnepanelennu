# Zonnepanelen-artikelen. Cijfers zijn bewust "indicatief" of rekenvoorbeelden met genoemde aannames.
ARTS = []


def A(slug, title, cat, desc, keys, body, faq, rel):
    ARTS.append(dict(slug=slug, title=title, cat=cat, desc=desc, keys=keys, body=body, faq=faq, rel=rel))


A("wat-kosten-zonnepanelen-in-2025",
  "Wat kosten zonnepanelen? Prijzen, aantal panelen en btw",
  "Kosten & rendement",
  "Wat kosten zonnepanelen inclusief installatie? Indicatieve prijzen per aantal panelen, wat de prijs bepaalt en hoe u offertes vergelijkt.",
  ["Voor een gemiddelde woning kosten zonnepanelen indicatief tussen ongeveer € 3.000 en € 9.000, inclusief installatie.",
   "Op woningen geldt voor zonnepanelen op dit moment 0% btw.",
   "De prijs per paneel daalt naarmate de installatie groter is.",
   "Vergelijk offertes op vermogen (Wp), merk, garantie en wat er precies is inbegrepen."],
  """<h2>Indicatieve prijzen</h2>
<p>Onderstaande bedragen zijn richtprijzen voor een complete installatie op een woning, inclusief omvormer, montage en aansluiting. Uw offerte kan hoger of lager uitvallen.</p>
<table><thead><tr><th>Aantal panelen (± 400 Wp)</th><th>Vermogen</th><th>Indicatieve prijs</th></tr></thead><tbody>
<tr><td>6</td><td>2,4 kWp</td><td>± € 2.800 – € 3.800</td></tr>
<tr><td>10</td><td>4,0 kWp</td><td>± € 4.000 – € 5.500</td></tr>
<tr><td>14</td><td>5,6 kWp</td><td>± € 5.500 – € 7.500</td></tr>
<tr><td>20</td><td>8,0 kWp</td><td>± € 7.500 – € 10.000</td></tr>
</tbody></table>
<div class="callout"><b>Btw.</b> Voor zonnepanelen op of bij een woning geldt op dit moment 0% btw. Regels kunnen wijzigen, dus laat u actueel informeren.</div>
<h2>Wat bepaalt de prijs?</h2>
<ul><li><b>Aantal panelen en vermogen:</b> meer panelen kosten meer, maar de prijs per paneel daalt meestal.</li>
<li><b>Merk en kwaliteit:</b> A-merken zijn vaak wat duurder, met betere garantie en degradatiegegevens.</li>
<li><b>Type dak:</b> een plat dak vraagt om een montagesysteem, een schuin dak om haken of rails. Een moeilijk bereikbaar dak kost meer werk.</li>
<li><b>Omvormer:</b> een string-omvormer of optimizers/micro-omvormers. Dat beïnvloedt prijs en prestaties bij schaduw.</li>
<li><b>Aansluiting en meterkast:</b> soms is een aanpassing nodig.</li>
<li><b>Extra’s:</b> monitoring, een thuisbatterij of een voorbereiding daarop.</li></ul>
<h2>Wat moet er in een offerte staan?</h2>
<ul><li>Aantal panelen, merk, type en vermogen in Wp.</li><li>Type en merk omvormer, inclusief garantie.</li><li>Wat er is inbegrepen: montage, aansluiting, afvoer van afval, monitoring.</li><li>Garantie op de installatie en op de producten.</li><li>Een verwachte jaaropbrengst in kWh, gebaseerd op uw dak.</li></ul>
<h2>Wanneer verdient u het terug?</h2>
<p>Dat hangt af van hoeveel stroom u zelf gebruikt. Na de salderingsregeling is zelf gebruiken belangrijker geworden. Lees meer in <a href="/zijn-zonnepanelen-nog-zinvol-om-in-te-investeren/">Zijn zonnepanelen nog zinvol?</a></p>""",
  [("Waarom verschillen offertes zo sterk?", "Vaak door merk, garantie, montagemethode en wat er is inbegrepen. Vergelijk daarom niet alleen het totaalbedrag, maar de onderdelen."),
   ("Is duurder altijd beter?", "Niet altijd, maar een zeer lage prijs kan betekenen dat er op kwaliteit, garantie of service is bespaard. Vraag altijd om een specificatie.")],
  ["zijn-zonnepanelen-nog-zinvol-om-in-te-investeren", "hoeveel-zonnepanelen-heb-je-nodig-voor-5000-kwh-een-gids-van-zonnepanelennu", "waar-op-letten-bij-aankoop-van-zonnepanelen-een-complete-gids"])

A("zijn-zonnepanelen-nog-zinvol-om-in-te-investeren",
  "Zijn zonnepanelen nog zinvol? Rendement na de salderingsregeling",
  "Kosten & rendement",
  "Loont het nog om zonnepanelen te nemen nu de salderingsregeling stopt? Een eerlijk rekenvoorbeeld met aannames, en wanneer een batterij helpt.",
  ["Op 1 januari 2027 stopt de salderingsregeling, voor iedereen. Stroom die u direct zelf gebruikt blijft even voordelig.",
   "Volgens de Rijksoverheid verdienen zonnepanelen zich ook zonder salderingsregeling nog terug.",
   "Hoeveel u zelf gebruikt, bepaalt het rendement. Een batterij kan dat aandeel verhogen.",
   "Reken met uw eigen verbruik, niet met een gemiddelde."],
  """<h2>Wat verandert er?</h2>
<p>Tot en met 31 december 2026 mag u teruggeleverde stroom wegstrepen tegen wat u afneemt. Vanaf 1 januari 2027 stopt dat. Teruggeleverde stroom wordt dan apart vergoed, en tot 2030 moet die vergoeding minimaal 50% van het kale leveringstarief zijn. Dat is minder dan wat u betaalt voor stroom uit het stopcontact. Lees het volledige overzicht op onze pagina <a href="/salderingsregeling-2027/">Salderingsregeling 2027</a>.</p>
<h2>Een rekenvoorbeeld (met aannames)</h2>
<p>Stel: 10 panelen leveren samen ongeveer 3.400 kWh per jaar. U gebruikt daarvan 40% direct zelf, de rest levert u terug. We rekenen met een stroomprijs van € 0,28 per kWh en een terugleververgoeding van € 0,08 per kWh. Dit zijn <b>aannames</b>, uw tarieven kunnen anders zijn.</p>
<table><thead><tr><th>Onderdeel</th><th>Berekening</th><th>Per jaar</th></tr></thead><tbody>
<tr><td>Zelf gebruikt (40%)</td><td>1.360 kWh × € 0,28</td><td>± € 380</td></tr>
<tr><td>Teruggeleverd (60%)</td><td>2.040 kWh × € 0,08</td><td>± € 165</td></tr>
<tr><td><b>Totaal voordeel</b></td><td></td><td><b>± € 545</b></td></tr>
</tbody></table>
<p>Met een thuisbatterij kunt u een groter deel zelf gebruiken. Gebruikt u bijvoorbeeld 30% méér van uw eigen opbrengst zelf (1.020 kWh extra), dan scheelt dat ongeveer 1.020 × (€ 0,28 − € 0,08) = € 204 extra per jaar. Daar staan de kosten van de batterij tegenover, dus of dat loont, hangt van de prijs af. Zie <a href="/wat-kost-een-accu-voor-zonnepanelen/">Wat kost een thuisbatterij?</a></p>
<div class="callout"><b>Waarom geen vaste beloftes?</b> Uw verbruik, uw dak en uw contract bepalen het rendement. Bedragen zoals “€ 1.500 per jaar besparen met 10 panelen” hangen af van veel aannames. Wij rekenen liever met uw eigen meterstanden.</div>
<h2>Voor wie is het extra interessant?</h2>
<ul><li>Huishoudens met veel verbruik overdag (thuiswerken, airco, elektrische auto laden).</li><li>Huishoudens met een warmtepomp of elektrische auto.</li><li>Huishoudens die een batterij overwegen om ’s avonds meer zelf te gebruiken.</li></ul>
<h2>Voor wie minder?</h2>
<ul><li>Zeer weinig verbruik, waardoor de installatie klein en weinig rendabel blijft.</li><li>Een dak met veel schaduw of een ongunstige oriëntatie.</li><li>Een dak dat binnenkort vervangen moet worden (zie ons artikel over <a href="/nadelen-van-zonnepanelen-op-een-plat-dak-wat-u-moet-weten/">daken</a>).</li></ul>
<h2>Terugverdientijd</h2>
<p>Indicatief ligt de terugverdientijd voor veel woningen tussen ongeveer 7 en 10 jaar. Bij weinig eigen verbruik kan het langer duren. Panelen gaan vaak 25 jaar of langer mee, dus na de terugverdientijd levert een installatie nog jarenlang voordeel op.</p>""",
  [("Hoeveel levert een paneel per jaar op?", "Grofweg 300 tot 375 kWh per paneel van ± 400 Wp, afhankelijk van oriëntatie, hellingshoek en schaduw. Uw offerte bevat een verwachting voor uw dak."),
   ("Wordt mijn bestaande installatie minder waard?", "Uw panelen blijven stroom opwekken. Alleen de waarde van teruggeleverde stroom daalt. Meer zelf gebruiken, eventueel met een batterij, helpt.")],
  ["wat-kosten-zonnepanelen-in-2025", "de-voordelen-van-een-thuisbatterij-voor-zonnepanelen", "hoeveel-zonnepanelen-heb-je-nodig-voor-5000-kwh-een-gids-van-zonnepanelennu"])

A("waar-op-letten-bij-aankoop-van-zonnepanelen-een-complete-gids",
  "Zonnepanelen kopen: waar let u op? De checklist",
  "Advies & aanschaf",
  "Zonnepanelen kopen zonder spijt: checklist voor offertes, merken, garantie, installateur en de meest gemaakte fouten.",
  ["Laat altijd een opname aan huis doen voordat u een offerte accepteert.",
   "Vergelijk offertes op vermogen (Wp), merk, garantie en wat er is inbegrepen, niet alleen op prijs.",
   "Kies een installateur met aantoonbare ervaring, reviews en duidelijke garantievoorwaarden.",
   "Vermijd grote vooruitbetalingen en tijdsdruk."],
  """<h2>1. Begin met uw verbruik en uw dak</h2>
<p>Bepaal eerst hoeveel stroom u gebruikt en wanneer. Kijk daarna naar uw dak: oriëntatie, hellingshoek, schaduw en de staat van het dak. Een goede installateur doet dit ter plaatse en niet alleen via een satellietfoto.</p>
<h2>2. Kies de installatie, niet alleen de panelen</h2>
<p>Het gaat om het geheel: panelen, omvormer, montagesysteem en bekabeling. Vraag naar de omvormer, want die moet meestal één of twee keer vervangen worden tijdens de levensduur van de panelen. Overweeg direct of u een batterij wilt, of dat u de installatie er op voorbereid wilt hebben.</p>
<h2>3. Let op merk en garantie</h2>
<ul><li><b>Productgarantie</b> op panelen (vaak 12 tot 25 jaar).</li><li><b>Prestatiegarantie</b> (vaak rond 25 tot 30 jaar, met een minimale opbrengst).</li><li><b>Omvormergarantie</b> (vaak 10 tot 12 jaar of langer).</li><li><b>Installatiegarantie</b> van de installateur zelf. Vraag wat dat precies dekt, bijvoorbeeld lekkage.</li></ul>
<h2>4. Beoordeel de installateur</h2>
<ul><li>Zijn er onafhankelijke reviews (bijvoorbeeld Google)?</li><li>Werkt het bedrijf met gecertificeerde vakmensen en erkende keurmerken?</li><li>Blijft het bedrijf bereikbaar na oplevering, met een duidelijke storingsservice?</li><li>Komen ze langs voor een opname, of is er alleen een online offerte?</li></ul>
<h2>5. Lees de offerte goed</h2>
<p>Controleer of aantal panelen, Wp per paneel, merk en type, omvormer, montage, aansluiting, afvoer van afval en monitoring worden genoemd. Kijk ook naar de betalingsvoorwaarden. Een kleine aanbetaling is gebruikelijk, een groot bedrag vooruit is een waarschuwingssignaal.</p>
<h2>Veelgemaakte fouten</h2>
<ul><li>Alleen op de laagste prijs kiezen.</li><li>Te weinig of te veel panelen kiezen zonder naar verbruik te kijken.</li><li>Schaduw of de leeftijd van het dak negeren.</li><li>Geen rekening houden met een latere batterij of extra verbruik (warmtepomp, elektrische auto).</li><li>Beslissen onder tijdsdruk (“alleen vandaag deze prijs”).</li></ul>
<h2>Welke panelen zijn het beste?</h2>
<p>Er is niet één beste paneel. Kies een A-merk met een sterke garantie en een verwachte opbrengst die past bij uw dak. Een goede installateur legt uit waarom hij voor een bepaald merk kiest, en welke alternatieven er zijn.</p>""",
  [("Is een gratis opname aan huis gebruikelijk?", "Bij serieuze installateurs wel. Zo kunnen ze dak, meterkast en verbruik beoordelen en een offerte maken die klopt."),
   ("Hoeveel offertes moet ik opvragen?", "Twee of drie is meestal genoeg. Vergelijk ze op onderdelen en garantie, niet alleen op totaalprijs.")],
  ["wat-kosten-zonnepanelen-in-2025", "hoeveel-zonnepanelen-heb-je-nodig-voor-5000-kwh-een-gids-van-zonnepanelennu", "mag-je-zelf-zonnepanelen-plaatsen-een-uitgebreide-gids"])

A("hoeveel-zonnepanelen-heb-je-nodig-voor-5000-kwh-een-gids-van-zonnepanelennu",
  "Hoeveel zonnepanelen heeft u nodig? Rekenvoorbeelden",
  "Advies & aanschaf",
  "Hoeveel zonnepanelen heeft uw huis nodig? Zo rekent u het uit, met voorbeelden voor 2.500 tot 7.000 kWh per jaar.",
  ["Een paneel van ± 400 Wp levert grofweg 300 tot 375 kWh per jaar op.",
   "Voor een verbruik van 5.000 kWh heeft u ongeveer 14 tot 16 panelen nodig als u alles wilt dekken.",
   "Na de salderingsregeling hoeft u niet per se alles te dekken: kijk naar uw eigen verbruik en overschot.",
   "Oriëntatie, hellingshoek en schaduw beïnvloeden de opbrengst aanzienlijk."],
  """<h2>De basisformule</h2>
<p>Deel uw jaarverbruik in kWh door de opbrengst per paneel. Een paneel van ongeveer 400 Wp levert op een goed gelegen Nederlands dak grofweg 300 tot 375 kWh per jaar. We rekenen hieronder met ± 340 kWh.</p>
<table><thead><tr><th>Jaarverbruik</th><th>Aantal panelen (± 400 Wp)</th></tr></thead><tbody>
<tr><td>2.500 kWh</td><td>± 7 – 8</td></tr>
<tr><td>3.500 kWh</td><td>± 10 – 11</td></tr>
<tr><td>5.000 kWh</td><td>± 14 – 16</td></tr>
<tr><td>7.000 kWh</td><td>± 20 – 22</td></tr>
</tbody></table>
<p>Dit zijn richtwaarden voor een dak op ongeveer zuid, met een gangbare helling en weinig schaduw.</p>
<h2>Wat beïnvloedt de opbrengst?</h2>
<ul><li><b>Oriëntatie:</b> zuid is optimaal, oost-west levert ongeveer 10 tot 20% minder per paneel op, maar spreidt de opbrengst over de dag.</li><li><b>Hellingshoek:</b> rond de 30 tot 40 graden is gunstig, platte daken gebruiken vaak een lagere hoek.</li><li><b>Schaduw:</b> bomen, schoorstenen en dakkapellen kunnen de opbrengst verlagen.</li><li><b>Kwaliteit en omvormer:</b> beïnvloeden het rendement en het gedrag bij schaduw.</li></ul>
<h2>Moet u alles dekken?</h2>
<p>Voorheen was het slim om zoveel mogelijk panelen te leggen, omdat saldering overschot wegstreepte. Na 1 januari 2027 loont het vooral om te kijken naar wat u zelf gebruikt. Een installatie die iets kleiner is dan uw jaarverbruik, of die met een batterij is gecombineerd, kan verstandiger zijn dan zoveel mogelijk panelen. Lees meer in <a href="/zijn-zonnepanelen-nog-zinvol-om-in-te-investeren/">Zijn zonnepanelen nog zinvol?</a></p>
<h2>Zijn 8 panelen genoeg?</h2>
<p>Voor een huishouden met ongeveer 2.500 tot 3.000 kWh en weinig extra verbruik kunnen 8 panelen een logische keuze zijn. Heeft u een warmtepomp of elektrische auto, dan is het verbruik hoger en heeft u er meer nodig.</p>
<h2>Houd rekening met de toekomst</h2>
<p>Komt er binnenkort een elektrische auto, warmtepomp of airco? Bespreek dat vooraf. Ook is het slim om te kijken of er ruimte is om later een thuisbatterij toe te voegen.</p>""",
  [("Hoeveel ruimte neemt een paneel in?", "Een paneel is ongeveer 1,7 bij 1,1 meter. Voor 10 panelen heeft u dus ruwweg 18 tot 20 vierkante meter dakvlak nodig."),
   ("Kan ik later uitbreiden?", "Vaak wel, afhankelijk van de omvormer en de beschikbare ruimte. Houd hier bij het ontwerp rekening mee.")],
  ["wat-kosten-zonnepanelen-in-2025", "zijn-zonnepanelen-nog-zinvol-om-in-te-investeren", "hoe-werken-zonnepanelen"])

A("hoe-werken-zonnepanelen",
  "Hoe werken zonnepanelen? Uitleg in gewone taal",
  "Zonnepanelen",
  "Hoe zetten zonnepanelen zonlicht om in stroom? Uitleg over panelen, omvormer, meter en wat er gebeurt met stroom die u niet gebruikt.",
  ["Zonnepanelen zetten zonlicht om in gelijkstroom, een omvormer maakt daar wisselstroom van.",
   "Stroom die u opwekt, gebruikt u eerst zelf. Wat overblijft gaat naar het net of naar een batterij.",
   "Panelen werken ook bij bewolking, alleen met minder opbrengst.",
   "Onderhoud is beperkt: houd het dak schoon en bekijk de opbrengst via de app."],
  """<h2>Van zonlicht naar stroom</h2>
<p>Een zonnepaneel bestaat uit zonnecellen van silicium. Als daglicht op die cellen valt, komt er elektrische stroom vrij (het fotovoltaïsche effect). Die stroom is gelijkstroom. Uw huis werkt op wisselstroom, dus een <b>omvormer</b> zet de stroom om.</p>
<h2>Wat gebeurt er met de stroom?</h2>
<ol><li>Uw huishouden gebruikt eerst de stroom die op dat moment wordt opgewekt.</li><li>Is er meer opbrengst dan verbruik, dan gaat het overschot naar een batterij (als u die heeft) of naar het net.</li><li>Is er te weinig opbrengst, bijvoorbeeld ’s avonds, dan gebruikt u stroom uit de batterij of het net.</li></ol>
<p>Een <b>slimme meter</b> registreert wat u afneemt en levert. Vanaf 1 januari 2027 stopt de salderingsregeling, waardoor het voordeliger wordt om meer van uw eigen stroom zelf te gebruiken. Lees meer op <a href="/salderingsregeling-2027/">Salderingsregeling 2027</a>.</p>
<h2>Werken panelen ook bij bewolking?</h2>
<p>Ja, maar met minder opbrengst. Ook in de winter en bij regen wekken panelen stroom op, alleen aanzienlijk minder dan op een heldere zomerdag. Over het hele jaar telt de som.</p>
<h2>Onderhoud en levensduur</h2>
<ul><li>Panelen gaan vaak 25 jaar of langer mee. Hun opbrengst neemt langzaam af.</li><li>De omvormer moet meestal één of twee keer vervangen worden.</li><li>Regen houdt panelen meestal schoon genoeg. Laat ze zo nodig door een vakman reinigen.</li><li>Via de app ziet u direct of de opbrengst klopt en of er een storing is.</li></ul>
<h2>En als u ’s avonds ook zonnestroom wilt?</h2>
<p>Dan is een thuisbatterij het antwoord. Die bewaart uw overschot van overdag. Lees <a href="/de-voordelen-van-een-thuisbatterij-voor-zonnepanelen/">Thuisbatterij: voordelen en wanneer het loont</a>.</p>""",
  [("Wat is het verschil tussen kWp en kWh?", "kWp (kilowattpiek) is het maximale vermogen van uw installatie. kWh is de hoeveelheid stroom die u opwekt of verbruikt."),
   ("Werken zonnepanelen bij stroomuitval?", "Standaard niet. Een omvormer schakelt uit voor de veiligheid. Voor noodstroom heeft u een speciaal systeem nodig, bijvoorbeeld met een batterij.")],
  ["hoeveel-zonnepanelen-heb-je-nodig-voor-5000-kwh-een-gids-van-zonnepanelennu", "zijn-zonnepanelen-nog-zinvol-om-in-te-investeren", "is-het-gebruik-van-een-thuisbatterij-goed-voor-het-milieu"])

A("mag-je-zelf-zonnepanelen-plaatsen-een-uitgebreide-gids",
  "Mag u zelf zonnepanelen plaatsen? Regels, risico’s en alternatief",
  "Advies & aanschaf",
  "Mag u zelf zonnepanelen leggen? Wat de regels zijn, welke risico’s er zijn voor veiligheid, garantie en verzekering, en wanneer u beter een vakman inschakelt.",
  ["Zelf zonnepanelen plaatsen is niet verboden, maar het brengt risico’s mee.",
   "De elektrische aansluiting moet veilig en volgens de voorschriften gebeuren.",
   "Werken op het dak brengt valgevaar en kans op lekkage met zich mee.",
   "Garantie en verzekering kunnen vervallen als het werk niet door een erkend vakman is gedaan."],
  """<h2>Mag het?</h2>
<p>Het is niet verboden om zelf zonnepanelen te plaatsen. In de praktijk zijn er wel veel voorwaarden en risico’s. Denk aan veiligheid, garantie, verzekering en aanmelding bij uw netbeheerder.</p>
<h2>De belangrijkste risico’s</h2>
<ul><li><b>Elektrische veiligheid:</b> panelen leveren gelijkstroom die lang en zwaar kan zijn. Een slechte aansluiting kan tot storingen of brand leiden.</li>
<li><b>Werken op hoogte:</b> vallen van het dak is een reëel risico. Professionals werken met borging en een steiger of hoogwerker.</li>
<li><b>Lekkage en dakschade:</b> een verkeerde bevestiging kan het dak beschadigen. Bij dakdoorvoeren is zorgvuldig werk nodig.</li>
<li><b>Garantie:</b> fabrikanten en dakleveranciers kunnen garantie laten vervallen als het werk niet door een erkende installateur is gedaan.</li>
<li><b>Verzekering:</b> meld uw installatie bij uw verzekeraar en vraag welke eisen ze stellen.</li></ul>
<h2>Regels en vergunningen</h2>
<p>Zonnepanelen op een dak zijn vaak vergunningvrij, maar er zijn uitzonderingen, bijvoorbeeld bij monumenten, beschermd stadsgezicht of een VvE. Controleer dit vooraf bij uw gemeente. Meld uw installatie ook aan bij uw netbeheerder.</p>
<h2>Wat u zelf wel kunt doen</h2>
<ul><li>Uw verbruik uitzoeken en een goede opname laten maken.</li><li>Offertes vergelijken, zie onze <a href="/waar-op-letten-bij-aankoop-van-zonnepanelen-een-complete-gids/">checklist voor aankoop</a>.</li><li>Uw dak vooraf laten beoordelen op leeftijd en draagkracht.</li></ul>
<div class="callout"><b>Ons advies.</b> Laat zonnepanelen en zeker een thuisbatterij plaatsen door gecertificeerde vakmensen. Zo weet u zeker dat het veilig, verzekerbaar en gegarandeerd is, en heeft u een aanspreekpunt als er iets misgaat.</div>""",
  [("Wat kost het om het zelf te doen?", "U bespaart op arbeid, maar loopt risico op kosten door fouten, extra materiaal en het vervallen van garanties. Vaak valt het besparingsbedrag in de praktijk tegen."),
   ("Mag ik zelf een batterij installeren?", "Voor batterijen geldt dat nog meer: het gaat om veel energie op een klein oppervlak. Laat dit door een gecertificeerde installateur doen.")],
  ["waar-op-letten-bij-aankoop-van-zonnepanelen-een-complete-gids", "zijn-thuisbatterijen-brandgevaarlijk-de-feiten-op-een-rij", "wat-kosten-zonnepanelen-in-2025"])

A("nadelen-van-zonnepanelen-op-een-plat-dak-wat-u-moet-weten",
  "Zonnepanelen op een plat dak: mogelijkheden, nadelen en dakleeftijd",
  "Zonnepanelen",
  "Zonnepanelen op een plat of bitumen dak? Wat er kan, welke nadelen er zijn en hoe oud uw dak mag zijn voordat u panelen laat leggen.",
  ["Op platte daken en bitumen daken zijn zonnepanelen goed mogelijk, vaak met een ballastsysteem.",
   "Belangrijk zijn de draagkracht, de staat en de leeftijd van het dak.",
   "Is uw dak binnen ongeveer 10 tot 15 jaar aan vervanging toe, laat het dan eerst renoveren.",
   "Een plat dak geeft vrijheid in opstelling, maar vraagt om aandacht voor wind en gewicht."],
  """<h2>Zonnepanelen op een plat dak</h2>
<p>Een plat dak is prima geschikt voor zonnepanelen. U kunt de panelen op een frame in de gewenste richting plaatsen. Dat geeft vrijheid, zoals een opstelling naar het zuiden of in oost-west.</p>
<h3>Mogelijke montage</h3>
<ul><li><b>Ballast:</b> de panelen worden verzwaard met stenen of tegels, zonder het dak te doorboren. Dat is gangbaar, maar het vraagt om voldoende draagkracht.</li><li><b>Verankering:</b> bevestiging aan de dakconstructie. Dat kan lichter zijn, maar er zijn dakdoorvoeren, die zorgvuldig moeten worden afgedicht.</li></ul>
<h2>De nadelen</h2>
<ul><li><b>Gewicht:</b> ballast maakt een installatie zwaarder. Laat de draagkracht controleren.</li><li><b>Wind:</b> bij een plat dak speelt windbelasting een grote rol, zeker op hoge gebouwen.</li><li><b>Vuil en water:</b> bij een lage hoek blijft vuil of water sneller liggen. Een iets grotere hoek of oost-west helpt.</li><li><b>Onderhoud van het dak:</b> panelen bemoeilijken het inspecteren en repareren van de dakbedekking.</li></ul>
<h2>Bitumen daken</h2>
<p>Op een bitumen dak (dakleer) is een ballastsysteem vaak de voorkeur, omdat het dak dan niet hoeft te worden doorboord. Let op de staat van het dak: scheuren, blazen of vocht moeten eerst worden hersteld.</p>
<h2>Hoe oud mag uw dak zijn?</h2>
<p>Zonnepanelen gaan 25 jaar of langer mee. Ligt uw dak er al lang en moet het binnen ongeveer 10 tot 15 jaar worden vervangen, dan is het slim om dat eerst te doen. Anders moeten de panelen later weer worden verwijderd en teruggelegd, wat extra kosten geeft.</p>
<p>Een dakdekker of installateur kan de staat van het dak beoordelen. Vraag ook naar de garantie van de dakbedekking en of die vervalt na het plaatsen van panelen.</p>
<h2>Onze werkwijze</h2>
<p>Wij komen langs, beoordelen dak, draagkracht en montage en zeggen eerlijk of uw dak nu geschikt is. Meer over de kosten leest u in <a href="/wat-kosten-zonnepanelen-in-2025/">Wat kosten zonnepanelen?</a></p>""",
  [("Zijn er speciale eisen voor een plat dak?", "Ja: draagkracht, windbelasting en de staat van de dakbedekking. Een goede installateur controleert dit vooraf."),
   ("Kan het op een dak met dakramen of lichtkoepels?", "Vaak wel, met een aangepaste opstelling. Dit bekijken we tijdens de opname.")],
  ["wat-kosten-zonnepanelen-in-2025", "wat-is-het-beste-moment-om-zonnepanelen-te-installeren", "hoeveel-zonnepanelen-heb-je-nodig-voor-5000-kwh-een-gids-van-zonnepanelennu"])

A("wat-is-het-beste-moment-om-zonnepanelen-te-installeren",
  "Wat is het beste moment om zonnepanelen (en batterij) te laten plaatsen?",
  "Advies & aanschaf",
  "Is er een beste moment om zonnepanelen of een thuisbatterij te laten plaatsen? Seizoen, planning, wachttijden en wat de salderingsregeling ermee te maken heeft.",
  ["Er is geen slecht moment: panelen wekken op vanaf de dag dat ze liggen, en installatie kan het hele jaar.",
   "De salderingsregeling stopt op 1 januari 2027 voor iedereen, ongeacht wanneer uw panelen zijn geplaatst.",
   "In het voorjaar en de zomer is het druk bij installateurs, dus plan op tijd.",
   "Wacht niet als uw verbruik stijgt (warmtepomp, elektrische auto) of als uw dak wordt gerenoveerd: bespreek het vooraf."],
  """<h2>Is er een beste seizoen?</h2>
<p>Technisch gezien niet. Panelen beginnen te leveren zodra ze zijn aangesloten. Wel kunt u in de zomermaanden veel opbrengst meenemen, dus wie in het voorjaar plaatst, profiteert meteen van de lange dagen. In de winter kunt u prima laten installeren; vaak zijn de wachttijden dan korter.</p>
<h2>De salderingsregeling en uw planning</h2>
<p>Op 1 januari 2027 stopt de salderingsregeling, voor <b>iedereen</b>, ook voor wie nu al panelen heeft. Het is dus <b>niet</b> zo dat u door vóór dat moment te plaatsen de salderingsregeling behoudt. Lees meer op <a href="/salderingsregeling-2027/">Salderingsregeling 2027</a>. Belangrijker is dat uw installatie past bij uw verbruik.</p>
<h2>Wanneer loont plannen wél?</h2>
<ul><li><b>Plan op tijd:</b> in het voorjaar is de vraag groot en kunnen wachttijden oplopen.</li><li><b>Voor een dakrenovatie:</b> laat het dak eerst vernieuwen en plaats daarna de panelen.</li><li><b>Voor een nieuw verbruik:</b> komt er een warmtepomp, elektrische auto of airco, dan is het slim om de installatie daarop af te stemmen.</li><li><b>Met een batterij:</b> laat een batterij bij voorkeur samen met de panelen ontwerpen, of laat de installatie ervoor voorbereiden.</li></ul>
<h2>En als u nog twijfelt?</h2>
<p>Neem de tijd voor een goede berekening. Een gratis adviesgesprek kost niets. Daarna kunt u rustig beslissen, zonder tijdsdruk. Serieuze installateurs werken niet met “vandaag alleen” acties.</p>""",
  [("Kan ik in de winter zonnepanelen laten plaatsen?", "Ja, dat kan gewoon. Bij vorst of storm kan de planning wisselen, maar installatie in de winter is prima mogelijk."),
   ("Blijft de salderingsregeling voor mij gelden als ik nu plaats?", "Nee. De regeling stopt op 1 januari 2027 voor alle huishoudens, ook voor bestaande installaties.")],
  ["salderingsregeling-2027", "zijn-zonnepanelen-nog-zinvol-om-in-te-investeren", "de-voordelen-van-een-thuisbatterij-voor-zonnepanelen"])

A("de-perfecte-combinatie-airco-en-zonnepanelen-voor-maximale-energiebesparing",
  "Airco en zonnepanelen: zo combineert u ze slim",
  "Zonnepanelen",
  "Een airco draait het hardst als de zon schijnt, precies wanneer zonnepanelen het meest opwekken. Zo combineert u ze slim, ook met een batterij.",
  ["Een airco wordt meestal gebruikt als het warm is, en dan wekken uw panelen het meest op.",
   "Direct zelf gebruikte zonnestroom is voordeliger dan teruggeleverde stroom.",
   "Een thuisbatterij kan helpen om ook in de avond koel te blijven op eigen stroom.",
   "Kies een zuinige airco en stem de instellingen af op uw opbrengst."],
  """<h2>Waarom past een airco goed bij zonnepanelen?</h2>
<p>Op warme, zonnige dagen wekken uw panelen veel op, en juist dan draait een airco het hardst. Een deel van uw koeling gebruikt dus rechtstreeks uw eigen zonnestroom. Dat is voordelig, zeker na de salderingsregeling, want direct zelf gebruikte stroom blijft even waardevol, terwijl teruggeleverde stroom minder oplevert.</p>
<h2>Hoeveel stroom gebruikt een airco?</h2>
<p>Dat verschilt sterk per model, ruimte en gebruik. Een moderne split-unit gebruikt vaak grofweg enkele honderden watt tot ruim een kilowatt per uur wanneer hij koelt. Kijk naar het energielabel en de efficiëntie (SEER) van het toestel.</p>
<h2>Zo haalt u er het meeste uit</h2>
<ul><li><b>Koel vooruit:</b> laat de airco in de ochtend of vroege middag draaien, terwijl uw panelen veel opwekken, in plaats van pas in de avond.</li><li><b>Kies een zuinig model:</b> een efficiënte inverter-airco gebruikt minder stroom voor dezelfde koeling.</li><li><b>Beperk de warmte:</b> zonwering en ventilatie verlagen de koelvraag.</li><li><b>Meet uw verbruik:</b> met de app of slimme meter ziet u wanneer u het meest zelf gebruikt.</li></ul>
<h2>En als de avond warm blijft?</h2>
<p>Op hete dagen is het ’s avonds nog warm, terwijl de zon weg is. Met een thuisbatterij kunt u dan de stroom van overdag gebruiken. Lees <a href="/de-voordelen-van-een-thuisbatterij-voor-zonnepanelen/">Thuisbatterij: voordelen en wanneer het loont</a>.</p>
<h2>Hoeveel panelen extra?</h2>
<p>Een airco vraagt over een zomer gerekend maar beperkt extra stroom, vaak enkele honderden tot enkele duizenden kWh, afhankelijk van gebruik. Bespreek uw verwachte gebruik bij het ontwerp, zodat uw installatie niet te klein uitvalt. Zie ook <a href="/hoeveel-zonnepanelen-heb-je-nodig-voor-5000-kwh-een-gids-van-zonnepanelennu/">Hoeveel zonnepanelen heeft u nodig?</a></p>""",
  [("Werkt een airco op zonnestroom?", "Ja, een airco gebruikt gewoon de stroom van uw huis. Wekt u op dat moment stroom op, dan gebruikt hij die eerst."),
   ("Is een airco of een warmtepomp beter?", "Een warmtepomp kan verwarmen én koelen. Het hangt af van uw woning en wensen. Laat u daarover adviseren.")],
  ["de-voordelen-van-een-thuisbatterij-voor-zonnepanelen", "hoeveel-zonnepanelen-heb-je-nodig-voor-5000-kwh-een-gids-van-zonnepanelennu", "zijn-zonnepanelen-nog-zinvol-om-in-te-investeren"])
