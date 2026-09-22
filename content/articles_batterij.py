# Batterij-artikelen (kern van de nieuwe blog). Cijfers zijn bewust "indicatief" en te bevestigen door de klant.
ARTS = []


def A(slug, title, cat, desc, keys, body, faq, rel):
    ARTS.append(dict(slug=slug, title=title, cat=cat, desc=desc, keys=keys, body=body, faq=faq, rel=rel))


A("de-voordelen-van-een-thuisbatterij-voor-zonnepanelen",
  "Thuisbatterij: voordelen en wanneer het loont",
  "Thuisbatterij",
  "Wat doet een thuisbatterij, welke voordelen heeft hij en voor wie loont hij? Eerlijk overzicht, ook voor de tijd na de salderingsregeling.",
  ["Een thuisbatterij bewaart zonnestroom die u overdag niet gebruikt, zodat u hem ’s avonds zelf gebruikt.",
   "Na de salderingsregeling (1 januari 2027) is zelf gebruiken meestal voordeliger dan terugleveren.",
   "Of een batterij loont, hangt vooral af van uw avondverbruik, uw panelen en uw energiecontract.",
   "In veel gevallen kan een batterij ook bij bestaande zonnepanelen."],
  """<h2>Wat doet een thuisbatterij?</h2>
<p>Zonnepanelen leveren de meeste stroom rond het middaguur, terwijl uw huishouden juist ’s ochtends en ’s avonds het meeste verbruikt. Wat u overdag niet gebruikt, gaat zonder batterij naar het net. Een thuisbatterij slaat dat overschot op, zodat u het later zelf kunt gebruiken. U koopt daardoor minder stroom in.</p>
<h2>De belangrijkste voordelen</h2>
<h3>1. Minder stroom inkopen</h3>
<p>Elke kilowattuur uit uw eigen batterij is een kilowattuur die u niet van uw leverancier hoeft te kopen. Dat is het kernvoordeel, en het werkt het best als u ’s avonds veel verbruikt: koken, wassen, verlichting, tv, en eventueel het opladen van een elektrische auto of een warmtepomp.</p>
<h3>2. Minder afhankelijk van terugleververgoedingen</h3>
<p>Op 1 januari 2027 stopt de salderingsregeling. Teruggeleverde stroom wordt dan apart afgerekend, en tot 2030 moet uw leverancier minimaal 50% van het kale leveringstarief vergoeden. Dat is doorgaans minder dan wat u betaalt voor stroom uit het stopcontact. Ook rekenen sommige leveranciers terugleverkosten. Een batterij verkleint de hoeveelheid stroom die u tegen die lagere vergoeding moet terugleveren. Lees meer in ons artikel over de <a href="/salderingsregeling-2027/">salderingsregeling 2027</a>.</p>
<h3>3. Slim laden en ontladen</h3>
<p>Bij een dynamisch energiecontract verschilt de stroomprijs per uur. Een slimme batterij kan laden wanneer stroom goedkoop is en ontladen wanneer stroom duur is. Het voordeel daarvan hangt sterk af van uw contract en de prijsverschillen op de markt, dus reken niet met een vast bedrag.</p>
<h3>4. Optioneel: noodstroom</h3>
<p>Sommige systemen kunnen bij een stroomstoring doorleveren aan (een deel van) uw huis. Niet elk model kan dit, en het vraagt om een geschikte installatie. Wilt u dit, bespreek het dan vooraf.</p>
<h3>5. Inzicht in uw energie</h3>
<p>Via een app ziet u hoeveel uw panelen opwekken, wat u verbruikt en wat de batterij doet. Dat maakt het makkelijker om bewuster met stroom om te gaan.</p>
<h2>Wanneer loont een thuisbatterij?</h2>
<table><thead><tr><th>Situatie</th><th>Kans dat een batterij loont</th></tr></thead><tbody>
<tr><td>Veel verbruik ’s avonds en ’s nachts</td><td>Groter</td></tr>
<tr><td>Grote overschotten overdag (veel panelen, weinig verbruik overdag)</td><td>Groter</td></tr>
<tr><td>Warmtepomp, elektrische auto of elektrisch koken</td><td>Groter</td></tr>
<tr><td>Dynamisch contract of hoge terugleverkosten</td><td>Groter</td></tr>
<tr><td>Weinig verbruik en weinig overschot</td><td>Kleiner</td></tr>
<tr><td>Alleen verbruik overdag (bijvoorbeeld thuiswerken)</td><td>Kleiner</td></tr>
</tbody></table>
<div class="callout"><b>Eerlijk advies.</b> Een batterij is geen wondermiddel. Bij sommige huishoudens loont hij niet, of pas na lange tijd. Daarom rekenen wij vooraf met uw eigen verbruik door, en zeggen we ook als een batterij (nog) niet slim is.</div>
<h2>Kan een batterij bij mijn bestaande zonnepanelen?</h2>
<p>In veel gevallen wel. Het hangt af van uw omvormer, uw meterkast en de manier waarop uw installatie is aangesloten. Bij een bestaande installatie wordt vaak gekozen voor een batterij die achter de omvormer wordt geplaatst. Tijdens een adviesgesprek bekijken we uw situatie ter plaatse.</p>
<h2>Wat kost het, en welke maat heeft u nodig?</h2>
<p>Dat verschilt per merk, capaciteit en installatie. In ons artikel <a href="/wat-kost-een-accu-voor-zonnepanelen/">Wat kost een thuisbatterij?</a> zetten we prijzen en terugverdientijd op een rij, en in <a href="/thuisbatterij-of-thuisaccu-voor-zonnepanelen-hoeveel-kwh-heb-ik-nodig/">Hoeveel kWh heb ik nodig?</a> leest u hoe u de juiste maat bepaalt.</p>""",
  [("Is een thuisbatterij verplicht na de salderingsregeling?", "Nee. Het is een keuze. Zonnepanelen blijven ook zonder batterij zinvol als u veel stroom zelf gebruikt. Een batterij is vooral interessant als u veel overschot heeft en ’s avonds veel verbruikt."),
   ("Kan ik een batterij later toevoegen?", "In veel gevallen wel. Bij het ontwerpen van een nieuwe installatie kunnen we er rekening mee houden, zodat u later makkelijk kunt uitbreiden."),
   ("Hoe lang gaat een thuisbatterij mee?", "Dat hangt af van het model en het gebruik. Fabrikanten geven vaak rond de 10 jaar garantie. De precieze voorwaarden verschillen per merk, dus vraag altijd naar de garantievoorwaarden.")],
  ["wat-kost-een-accu-voor-zonnepanelen", "thuisbatterij-of-thuisaccu-voor-zonnepanelen-hoeveel-kwh-heb-ik-nodig", "zijn-zonnepanelen-nog-zinvol-om-in-te-investeren"])

A("wat-kost-een-accu-voor-zonnepanelen",
  "Wat kost een thuisbatterij? Prijzen, capaciteit en terugverdientijd",
  "Thuisbatterij",
  "Wat kost een thuisbatterij en wanneer verdient hij zich terug? Indicatieve prijzen, wat de prijs bepaalt en hoe u een eerlijke offerte herkent.",
  ["Indicatief ligt de investering voor een thuisbatterij tussen ongeveer € 4.000 en € 10.000, inclusief installatie.",
   "De prijs hangt af van capaciteit (kWh), merk, type omvormer en de installatie.",
   "De terugverdientijd ligt indicatief tussen 5 en 10 jaar, maar verschilt sterk per huishouden.",
   "Vraag altijd een offerte op maat en laat uw eigen verbruik doorrekenen."],
  """<h2>Wat kost een thuisbatterij?</h2>
<p>Voor een complete thuisbatterij, inclusief installatie, gaat het indicatief om ongeveer € 4.000 tot € 10.000. Een kleinere batterij met weinig capaciteit zit aan de onderkant, een grote batterij met veel vermogen en extra functies aan de bovenkant. Dit zijn richtprijzen. Uw offerte kan hoger of lager uitvallen.</p>
<div class="callout"><b>Let op btw.</b> Voor zonnepanelen op een woning geldt op dit moment 0% btw. Voor thuisbatterijen geldt doorgaans het gewone tarief. Regels kunnen veranderen, dus controleer dit bij de Belastingdienst of laat u informeren door uw installateur.</div>
<h2>Wat bepaalt de prijs?</h2>
<ul><li><b>Capaciteit (kWh):</b> hoeveel stroom de batterij kan opslaan. Meer capaciteit kost meer.</li>
<li><b>Vermogen (kW):</b> hoeveel stroom de batterij tegelijk kan leveren. Wilt u ook een warmtepomp of kookplaat voeden, dan heeft u meer vermogen nodig.</li>
<li><b>Merk en garantie:</b> A-merken zijn vaak duurder, maar hebben betere garantie en ondersteuning.</li>
<li><b>Omvormer en aansluiting:</b> past uw huidige omvormer, of is een nieuwe nodig?</li>
<li><b>Installatie:</b> afstand tot de meterkast, bekabeling en eventuele aanpassingen.</li>
<li><b>Extra’s:</b> noodstroom, slimme aansturing en monitoring.</li></ul>
<h2>Wanneer verdient een thuisbatterij zich terug?</h2>
<p>Indicatief ligt de terugverdientijd tussen 5 en 10 jaar. Dat is een grote bandbreedte, en dat is bewust: het resultaat hangt af van veel factoren.</p>
<ul><li>hoeveel stroom u ’s avonds gebruikt;</li><li>hoeveel overschot uw zonnepanelen overdag hebben;</li><li>uw energiecontract (vast, variabel of dynamisch) en eventuele terugleverkosten;</li><li>de prijs van de batterij en de verwachte levensduur.</li></ul>
<p>Rekenvoorbeelden uit brochures zijn vaak te rooskleurig. Wij rekenen liever met uw eigen meterstanden.</p>
<h2>Zo herkent u een goede offerte</h2>
<ul><li>Er staat een duidelijke capaciteit in kWh en vermogen in kW.</li><li>Merk, type en garantie zijn concreet benoemd.</li><li>De installatie en aansluiting zijn inbegrepen, zonder verrassingen achteraf.</li><li>U ziet een berekening op basis van uw eigen verbruik, niet alleen een gemiddelde.</li><li>Er wordt eerlijk gezegd als een batterij bij u (nog) niet loont.</li></ul>
<p>Twijfelt u over de maat? Lees dan <a href="/thuisbatterij-of-thuisaccu-voor-zonnepanelen-hoeveel-kwh-heb-ik-nodig/">Hoeveel kWh heb ik nodig?</a></p>""",
  [("Is een goedkope thuisbatterij ook goed?", "Niet per se. Kijk niet alleen naar de prijs, maar ook naar garantie, service, veiligheid en de mogelijkheid om de batterij slim aan te sturen."),
   ("Zit de installatie in de prijs?", "Bij een goede offerte wel. Vraag altijd of installatie, aansluiting en inbedrijfstelling zijn inbegrepen."),
   ("Zijn er subsidies voor een thuisbatterij?", "Regelingen veranderen regelmatig. Vraag uw installateur naar de actuele situatie, en verwacht niet zomaar dat er subsidie beschikbaar is.")],
  ["de-voordelen-van-een-thuisbatterij-voor-zonnepanelen", "thuisbatterij-of-thuisaccu-voor-zonnepanelen-hoeveel-kwh-heb-ik-nodig", "hoe-wordt-een-thuisbatterij-geinstalleerd"])

A("thuisbatterij-of-thuisaccu-voor-zonnepanelen-hoeveel-kwh-heb-ik-nodig",
  "Hoeveel kWh thuisbatterij heeft u nodig?",
  "Thuisbatterij",
  "Welke capaciteit heeft uw thuisbatterij nodig? Zo bepaalt u de juiste maat op basis van uw avondverbruik en de opbrengst van uw zonnepanelen.",
  ["De juiste capaciteit hangt af van uw verbruik ’s avonds en ’s nachts en van het overschot van uw panelen.",
   "Te klein: u laat opbrengst liggen. Te groot: u betaalt voor capaciteit die u niet benut.",
   "Vermogen (kW) is even belangrijk als capaciteit (kWh), zeker met een warmtepomp of laadpaal.",
   "Een gemeten verbruik (slimme meter) geeft een betere basis dan een gemiddelde."],
  """<h2>Capaciteit en vermogen: wat is het verschil?</h2>
<p>Capaciteit (kWh) zegt hoeveel stroom een batterij kan opslaan. Vermogen (kW) zegt hoeveel stroom de batterij op één moment kan leveren. Een batterij met veel capaciteit maar weinig vermogen kan uw huis ’s avonds niet voeden als u tegelijk kookt, wast en een warmtepomp gebruikt.</p>
<h2>Zo bepaalt u de juiste capaciteit</h2>
<p>Kijk naar twee getallen:</p>
<ol><li><b>Uw verbruik zodra de zon weg is.</b> Hoeveel kWh gebruikt u grofweg tussen zonsondergang en de volgende ochtend? Dat is het maximum dat een batterij per dag zinvol kan leveren.</li>
<li><b>Uw overschot overdag.</b> Hoeveel kWh leveren uw panelen aan het net terug op een gemiddelde zonnige dag? Daarmee laadt u de batterij.</li></ol>
<p>De kleinste van die twee is meestal een goede richtlijn voor de capaciteit. Heeft u bijvoorbeeld ’s avonds en ’s nachts 6 kWh nodig, en houden uw panelen op een zomerdag 10 kWh over, dan is een batterij van ongeveer 6 kWh een logische startmaat.</p>
<div class="callout"><b>Waarom niet gewoon groter?</b> Een grotere batterij kost meer, maar wordt in de praktijk niet altijd vaker vol of leeg. Alleen de extra kWh’s die u ook echt gebruikt, verdienen zich terug.</div>
<h2>Seizoenen maken verschil</h2>
<p>In de zomer is uw overschot groot en zit de batterij snel vol. In de winter wekken panelen veel minder op, dus dan maakt een grote batterij minder verschil. De beste maat kijkt daarom naar het hele jaar, niet naar één perfecte zomerdag.</p>
<h2>Wat als u een warmtepomp, laadpaal of airco heeft?</h2>
<p>Dan stijgt uw avondverbruik en heeft u mogelijk meer capaciteit en vooral meer vermogen nodig. Maak daar vooraf afspraken over met uw installateur, zodat de batterij uw grootste verbruikers ook aankan.</p>
<h2>Gebruik uw slimme meter</h2>
<p>Uw slimme meter en energieleverancier geven vaak inzicht in uw verbruik per uur of per dag. Met die data kunnen we een veel nauwkeuriger advies geven dan met een gemiddelde. Vraag bij ons advies gerust om een berekening.</p>
<p>Meer over prijzen leest u in <a href="/wat-kost-een-accu-voor-zonnepanelen/">Wat kost een thuisbatterij?</a></p>""",
  [("Is 10 kWh genoeg voor een gemiddeld huis?", "Voor veel huishoudens is dat meer dan nodig. De juiste maat hangt af van uw avondverbruik en uw overschot. We rekenen het graag voor u door."),
   ("Kan ik later meer capaciteit toevoegen?", "Bij sommige systemen kunt u later modules toevoegen. Vraag dit vooraf, want het verschilt per merk en model.")],
  ["wat-kost-een-accu-voor-zonnepanelen", "de-voordelen-van-een-thuisbatterij-voor-zonnepanelen", "hoe-wordt-een-thuisbatterij-geinstalleerd"])

A("hoe-wordt-een-thuisbatterij-geinstalleerd",
  "Hoe wordt een thuisbatterij geïnstalleerd? Stap voor stap",
  "Thuisbatterij",
  "Van adviesgesprek tot inbedrijfstelling: zo verloopt de installatie van een thuisbatterij, waar hij komt te staan en wat u zelf moet regelen.",
  ["De installatie begint met een adviesgesprek waarin meterkast, omvormer en verbruik worden bekeken.",
   "De installatie zelf duurt meestal een dag, afhankelijk van het systeem.",
   "Laat een thuisbatterij altijd door gecertificeerde vakmensen installeren.",
   "Na oplevering krijgt u uitleg over de app en de instellingen."],
  """<h2>Stap 1: adviesgesprek en opname</h2>
<p>We bekijken uw meterkast, omvormer en de plek waar de batterij kan komen. We kijken naar uw verbruik en uw energiecontract en bespreken uw wensen, zoals noodstroom. Zo weten we welk systeem past.</p>
<h2>Stap 2: offerte en planning</h2>
<p>U ontvangt een offerte met merk, capaciteit, vermogen en garantie. Na akkoord plannen we de installatie. Is uw omvormer of meterkast niet geschikt, dan staat dat vooraf in de offerte.</p>
<h2>Stap 3: de installatie</h2>
<p>De installateur monteert de batterij op de afgesproken plek, sluit hem aan op de installatie en de meterkast en koppelt hem aan uw wifi of netwerk. Voor de bekabeling en aansluitingen is vakkennis nodig. Dit is werk voor gecertificeerde vakmensen, niet voor doe-het-zelvers.</p>
<h2>Stap 4: inbedrijfstelling en uitleg</h2>
<p>Na de installatie testen we de werking en stellen we de slimme aansturing in. U krijgt uitleg over de app, zodat u kunt zien wat uw panelen en batterij doen.</p>
<h2>Waar komt de batterij te staan?</h2>
<ul><li>Bij voorkeur dicht bij de meterkast en omvormer, zodat de bekabeling kort blijft.</li><li>Op een droge, goed bereikbare plek met voldoende ruimte en ventilatie, zoals een berging, garage of technische ruimte.</li><li>Niet in een vochtige of extreem koude of warme ruimte, en niet op een plek die vol staat met brandbare spullen.</li></ul>
<p>Voor de exacte eisen volgen we de voorschriften van de fabrikant. Meer over veiligheid leest u in <a href="/zijn-thuisbatterijen-brandgevaarlijk-de-feiten-op-een-rij/">Zijn thuisbatterijen brandgevaarlijk?</a></p>
<h2>Wat regelt u zelf?</h2>
<p>Meestal weinig. Zorg dat de installateur bij de meterkast kan, dat er een werkende internetverbinding is en dat de gekozen plek toegankelijk is. Over eventuele meldingen en aanmeldingen bij uw netbeheerder of leverancier informeert uw installateur u.</p>""",
  [("Hoe lang duurt de installatie?", "Meestal ongeveer een dag, afhankelijk van het systeem en de situatie. Bij complexere installaties kan het langer duren."),
   ("Moet mijn meterkast worden aangepast?", "Soms. Dat bekijken we tijdens het adviesgesprek en staat vooraf in de offerte.")],
  ["zijn-thuisbatterijen-brandgevaarlijk-de-feiten-op-een-rij", "thuisbatterij-of-thuisaccu-voor-zonnepanelen-hoeveel-kwh-heb-ik-nodig", "de-voordelen-van-een-thuisbatterij-voor-zonnepanelen"])

A("zijn-thuisbatterijen-brandgevaarlijk-de-feiten-op-een-rij",
  "Zijn thuisbatterijen brandgevaarlijk? De feiten op een rij",
  "Thuisbatterij",
  "Hoe veilig is een thuisbatterij? Wat het risico is, welke beveiligingen er zijn en waar u op let bij aankoop en installatie.",
  ["Een goed geïnstalleerde thuisbatterij van een A-merk is voor de meeste huishoudens een veilig apparaat.",
   "Brand ontstaat zelden, en meestal door een productiefout, beschadiging of een foute installatie.",
   "Kies een A-merk, laat installeren door gecertificeerde vakmensen en volg de plaatsingsvoorschriften.",
   "Vraag naar het type batterijcel en de ingebouwde beveiligingen."],
  """<h2>Is een thuisbatterij veilig?</h2>
<p>Thuisbatterijen bevatten veel energie op een klein oppervlak. Dat vraagt om zorgvuldig ontwerp en een goede installatie. Moderne systemen hebben ingebouwde beveiligingen tegen bijvoorbeeld oververhitting, overladen en kortsluiting. Een goed geïnstalleerde batterij van een gerenommeerd merk is voor de meeste huishoudens veilig, maar risico op storing of brand is nooit nul.</p>
<h2>Waar ontstaat het risico?</h2>
<ul><li><b>Productiefouten of beschadiging</b> van de batterijcellen.</li><li><b>Een verkeerde installatie</b>, bijvoorbeeld slechte aansluitingen of onvoldoende ventilatie.</li><li><b>Extreme omstandigheden</b>, zoals vocht of grote hitte.</li><li><b>Goedkope of onbekende merken</b> zonder goede kwaliteitscontrole.</li></ul>
<h2>Welk type batterij is veiliger?</h2>
<p>Er bestaan verschillende celchemieën. Lithium-ijzerfosfaat (LFP) staat bekend als thermisch stabieler dan sommige andere lithium-ionvarianten. Toch bepaalt het type cel niet alleen de veiligheid: ontwerp, beveiligingselektronica en installatie zijn minstens zo belangrijk. Vraag uw leverancier welke techniek in het systeem zit.</p>
<h2>Waar let u op?</h2>
<ol><li>Kies een <b>A-merk</b> met duidelijke garantie- en servicevoorwaarden.</li><li>Laat de batterij installeren door <b>gecertificeerde vakmensen</b>.</li><li>Vraag naar de <b>plaatsingsvoorschriften</b> van de fabrikant en houd u eraan.</li><li>Kies een <b>geschikte plek</b>: droog, ventileerbaar en zonder brandbare spullen eromheen.</li><li>Laat uw <b>verzekering</b> weten dat u een batterij heeft, en vraag of dit gevolgen heeft.</li></ol>
<div class="callout"><b>Ons standpunt.</b> Wij plaatsen alleen batterijen van merken waar we achter staan, en laten ze installeren door gecertificeerde vakmensen. Heeft u zorgen over veiligheid, stel de vraag dan gerust tijdens het adviesgesprek.</div>
<p>Wilt u weten hoe de installatie verloopt? Lees <a href="/hoe-wordt-een-thuisbatterij-geinstalleerd/">Hoe wordt een thuisbatterij geïnstalleerd?</a></p>""",
  [("Mag een thuisbatterij in de woonkamer?", "In de praktijk plaatst men een batterij liever in een berging, garage of technische ruimte. Volg altijd de voorschriften van de fabrikant."),
   ("Moet ik mijn verzekeraar informeren?", "Het is verstandig. Vraag uw verzekeraar of een thuisbatterij gevolgen heeft voor uw polis.")],
  ["hoe-wordt-een-thuisbatterij-geinstalleerd", "is-het-gebruik-van-een-thuisbatterij-goed-voor-het-milieu", "de-voordelen-van-een-thuisbatterij-voor-zonnepanelen"])

A("is-het-gebruik-van-een-thuisbatterij-goed-voor-het-milieu",
  "Is een thuisbatterij goed voor het milieu?",
  "Thuisbatterij",
  "Wat zijn de milieueffecten van een thuisbatterij en van zonnepanelen? Productie, levensduur, recycling en wat u zelf kunt doen.",
  ["Zonnepanelen leveren over hun levensduur veel meer schone energie op dan er voor de productie nodig was.",
   "Een thuisbatterij helpt om meer eigen groene stroom te gebruiken, maar de productie heeft ook een milieu-impact.",
   "Hoe langer een batterij of paneel meegaat en hoe beter het wordt gebruikt, hoe gunstiger de balans.",
   "Zowel panelen als batterijen vallen onder recyclingregels."],
  """<h2>De korte versie</h2>
<p>Zonnepanelen en thuisbatterijen kosten bij de productie energie en grondstoffen. Tegelijk voorkomen ze tijdens hun gebruik veel uitstoot doordat u minder stroom uit het net gebruikt. Over de hele levensduur genomen is de balans meestal gunstig, zeker als u de installatie goed gebruikt.</p>
<h2>Zonnepanelen: snel terugverdiend in energie</h2>
<p>De energie die nodig is om een zonnepaneel te maken, is meestal binnen enkele jaren teruggewonnen. Daarna levert het paneel vele jaren schone stroom. Een paneel gaat vaak 25 jaar of langer mee, en de productie neemt langzaam af.</p>
<h2>De thuisbatterij: wat is de impact?</h2>
<p>Een batterij bevat onder andere lithium en andere metalen, en het winnen en verwerken daarvan heeft een milieu-impact. Toch kan een batterij netto bijdragen, omdat ze uw eigen zonnestroom beter benut. Bij overschot overdag gaat die stroom anders naar het net, waar het op dat moment vaak weinig waard is. Met een batterij gebruikt u hem ’s avonds zelf, en hoeft er minder stroom uit fossiele bronnen te worden geleverd.</p>
<h2>Wat maakt het verschil?</h2>
<ul><li><b>Levensduur:</b> hoe langer het systeem meegaat, hoe kleiner de impact per opgeslagen kWh.</li><li><b>Gebruik:</b> een batterij die dagelijks laadt en ontlaadt, levert meer op dan een batterij die grotendeels stilstaat.</li><li><b>Juiste maat:</b> een te grote batterij is onnodige materiaalinzet.</li><li><b>Kwaliteit:</b> betere producten met langere garantie gaan doorgaans langer mee.</li></ul>
<h2>Recycling</h2>
<p>Voor zowel zonnepanelen als batterijen gelden recyclingregels en inzamelsystemen. Werk bij einde levensduur mee aan een goede afvoer via uw installateur of een erkend inzamelpunt.</p>
<p>Wilt u weten of een batterij bij u past? Lees <a href="/de-voordelen-van-een-thuisbatterij-voor-zonnepanelen/">Thuisbatterij: voordelen en wanneer het loont</a>.</p>""",
  [("Is een thuisbatterij groener dan zonnepanelen alleen?", "Ze vullen elkaar aan. Panelen leveren de schone stroom, de batterij helpt u meer daarvan zelf te gebruiken."),
   ("Wat gebeurt er met een batterij aan het einde van de levensduur?", "Batterijen worden ingezameld en gerecycled. Uw installateur kan u vertellen hoe u dat het best regelt.")],
  ["de-voordelen-van-een-thuisbatterij-voor-zonnepanelen", "hoe-werken-zonnepanelen", "zijn-thuisbatterijen-brandgevaarlijk-de-feiten-op-een-rij"])
