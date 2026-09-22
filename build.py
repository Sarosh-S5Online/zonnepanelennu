#!/usr/bin/env python3
"""Bouwt de ZonnepanelenNu-demo: alle pagina's uit één layout + contentdata.
Gebruik:  python build.py   (schrijft <slug>/index.html, spiegelt de WordPress-permalinks)"""
import os, sys, shutil, html, json

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://zonnepanelennu.nl"
TEL, TEL_HREF, MAIL = "0182 – 60 79 48", "+31182607948", "info@zonnepanelennu.nl"
STRAAT, PLAATS = "Marconistraat 70G", "2809 PE Gouda"
ADRES = f"{STRAAT}, {PLAATS}"
KVK = "85470406"
TIJD = "2 weken"           # live site zegt 2 weken / 4 weken / 1 maand door elkaar: klant laten kiezen
RATING, NREV = "4,8", 43   # Google-bedrijfsprofiel, sept 2026

CITIES = ["Gouda", "Rotterdam", "Den Haag", "Zoetermeer", "Alphen aan den Rijn",
          "Bodegraven", "Nieuwerkerk aan den IJssel", "Waddinxveen", "Woerden"]
CITY_SLUG = {"Alphen aan den Rijn": "alphen-aan-den-rijn", "Bodegraven": "bodegraven", "Nieuwerkerk aan den IJssel": "nieuwerkerk-aan-den-ijssel"}
slug = lambda c: CITY_SLUG.get(c) or "zonnepanelen-" + c.lower().replace(" ", "-")
e = html.escape

import re
from html.parser import HTMLParser

MND = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]
def nl_date(d): y, m, dd = d.split("-"); return f"{int(dd)} {MND[int(m) - 1]} {y}"
def load(name): return json.load(open(os.path.join(ROOT, "content", name), encoding="utf-8"))
def plain(h): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()

STOP = set("de het een en van voor op in met te is zijn je u uw of wat hoe waar dat die dit om bij aan als ook naar door over nog niet meer wordt worden kunt kan".split())
def words(t): return {w for w in re.findall(r"[a-zà-ÿ]{4,}", t.lower()) if w not in STOP}

CATS = [("Thuisbatterij", ("batterij", "accu", "thuisaccu")),
        ("Kosten & rendement", ("kost", "terugverdien", "rendabel", "subsidie", "scheelt", "zinvol", "investeren", " zin", "energierekening")),
        ("Advies & aanschaf", ("aanschaf", "letten", "leverancier", "fouten", "zelf", "hoeveel", "beste", "dak", "bitumen", "airco", "verandert", "moment", "nadelen"))]
def cat_of(t):
    tl = t.lower()
    for name, keys in CATS:
        if any(k in tl for k in keys): return name
    return "Zonne-energie"

LEGAL = load("legal.json")
sys.path.insert(0, os.path.join(ROOT, "content"))
from articles_batterij import ARTS as _A1
from articles_zonnepanelen import ARTS as _A2
OLD_POSTS = {x["slug"]: x for x in load("posts.json")}      # de 39 oude artikelen (voor datum + redirects)
UPDATED = "2026-09-21"
POSTS = []
for art in _A1 + _A2:
    old = OLD_POSTS[art["slug"]]
    q = dict(art)
    q.update(date=old["date"], modified=UPDATED, path=f"/{art['slug']}/", excerpt=art["desc"],
             html=art["body"], mins=max(2, round(len(plain(art["body"]).split()) / 200)), w=words(art["title"]))
    POSTS.append(q)
BY_SLUG = {q["slug"]: q for q in POSTS}

# oude URL's -> nieuwe URL (301). Onderwerp-clusters: 24 oude artikelen gaan naar 15 sterke.
REDIRECTS = {
    "waarom-juist-zonnepanelen-in-het-voorjaar-plaatsen": "wat-is-het-beste-moment-om-zonnepanelen-te-installeren",
    "zonnepanelen-trends-en-ontwikkelingen-in-2025": "/salderingsregeling-2027/",
    "wat-verandert-er-in-2024-voor-zonnepanelen": "/salderingsregeling-2027/",
    "hoeveel-zonnepanelen-heb-ik-nodig-voor-mijn-woning-in-rotterdam": "hoeveel-zonnepanelen-heb-je-nodig-voor-5000-kwh-een-gids-van-zonnepanelennu",
    "hebben-8-zonnepanelen-zin": "hoeveel-zonnepanelen-heb-je-nodig-voor-5000-kwh-een-gids-van-zonnepanelennu",
    "hoeveel-kosten-10-zonnepanelen": "wat-kosten-zonnepanelen-in-2025",
    "wat-kost-het-om-zonnepanelen-te-laten-plaatsen": "wat-kosten-zonnepanelen-in-2025",
    "hoeveel-subsidie-krijg-je-in-2024-voor-zonnepanelen": "wat-kosten-zonnepanelen-in-2025",
    "de-voordelen-van-zonnepanelen-in-een-stedelijke-omgeving-zoals-rotterdam": "/blog/",
    "waarom-is-rotterdam-centraal-duurzaam": "/blog/",
    "zonnepanelen-op-een-bitumen-dak-wat-zijn-de-mogelijkheden": "nadelen-van-zonnepanelen-op-een-plat-dak-wat-u-moet-weten",
    "hoe-oud-mag-je-dak-zijn-voor-zonnepanelen": "nadelen-van-zonnepanelen-op-een-plat-dak-wat-u-moet-weten",
    "is-een-thuisaccu-rendabel-een-duidelijke-uitleg": "wat-kost-een-accu-voor-zonnepanelen",
    "waar-moet-u-op-letten-bij-de-aanschaf-van-zonnepanelen": "waar-op-letten-bij-aankoop-van-zonnepanelen-een-complete-gids",
    "de-meest-gemaakte-fouten-bij-zonnepanelen-hoe-ze-te-voorkomen": "waar-op-letten-bij-aankoop-van-zonnepanelen-een-complete-gids",
    "wat-is-de-beste-zonnepanelen-leverancier": "waar-op-letten-bij-aankoop-van-zonnepanelen-een-complete-gids",
    "wat-zijn-de-beste-zonnepanelen-van-2024-een-gids-van-zonnepanelennu": "waar-op-letten-bij-aankoop-van-zonnepanelen-een-complete-gids",
    "hoe-snel-verdien-ik-mijn-zonnepanelen-terug-in-2024": "zijn-zonnepanelen-nog-zinvol-om-in-te-investeren",
    "hoeveel-scheelt-zonnepanelen-op-je-energierekening": "zijn-zonnepanelen-nog-zinvol-om-in-te-investeren",
    "is-het-nog-rendabel-om-zonnepanelen-te-plaatsen": "zijn-zonnepanelen-nog-zinvol-om-in-te-investeren",
    "waarom-investeren-in-zonnepanelen": "zijn-zonnepanelen-nog-zinvol-om-in-te-investeren",
    "is-het-slim-om-een-accu-te-plaatsen-voor-je-zonnepanelen": "de-voordelen-van-een-thuisbatterij-voor-zonnepanelen",
    "accu-om-zonne-energie-op-te-slaan-hoe-werkt-het": "de-voordelen-van-een-thuisbatterij-voor-zonnepanelen",
    "is-de-productie-van-zonnepanelen-milieuvriendelijk": "is-het-gebruik-van-een-thuisbatterij-goed-voor-het-milieu",
}
REDIRECTS = {f"/{k}/": (v if v.startswith("/") else f"/{v}/") for k, v in REDIRECTS.items()}
assert set(OLD_POSTS) == {k.strip("/") for k in REDIRECTS} | set(BY_SLUG), set(OLD_POSTS) ^ ({k.strip("/") for k in REDIRECTS} | set(BY_SLUG))
assert all(d in {f"/{q['slug']}/" for q in POSTS} or d in ("/blog/", "/salderingsregeling-2027/") for d in REDIRECTS.values())

# ------------------------------------------------------------------ media
PH = {1: "woning-baksteen", 2: "dakkapel-zwart", 4: "rijtjeswoningen", 6: "bedrijfspand-a", 7: "pannendak-close",
      8: "steiger-installateurs", 9: "omvormer", 12: "team-steiger", 14: "installateurs-platdak", 15: "installateur-werk",
      16: "woning-hoek", 18: "dakramen-panelen", 19: "rijtjeswoning", 22: "platdak-sneeuw", 25: "industrieel-dak",
      26: "woning-blauwe-lucht", 28: "woning-rood", 29: "woning-zonnig", 30: "woning-modern", 32: "dakkapel-woning",
      11: "meterkast", 33: "bedrijfspand-b", 35: "aeg-batterij-1", 36: "aeg-batterij-2", 3: "platdak-opstelling", 10: "platdak-grind",
      37: "zonnepanelen-bodegraven", 38: "zonnepanelen-nieuwerkerk", 39: "myreserve-accu"}
def img(n, small=False): return f"/assets/img/f/{n:02d}-{PH[n]}{'-s' if small else ''}.webp"

ICONS = {
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "star": '<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 "battery": '<rect x="2" y="7" width="16" height="10" rx="2"/><path d="M22 11v2M6 11v2M10 11v2"/>',
 "home": '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>',
 "building": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2"/>',
 "euro": '<path d="M18 7a6 6 0 0 0-9.5 2M18 17a6 6 0 0 1-9.5-2M5 10h9M5 14h9"/>',
 "trend": '<path d="M3 17l6-6 4 4 8-8M15 7h6v6"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "tool": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 "help": '<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>',
 "user": '<circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M16 11l2 2 4-4"/>',
 "zap": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "cal": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M9 16l2 2 4-4"/>',
}
def ic(n): return f'<svg class="i" viewBox="0 0 24 24" aria-hidden="true">{ICONS[n]}</svg>'

REVIEWS = [
    ("Michel van Wissen", "Het gehele traject van intake, schouwen, advies aan huis, ontwerp, offerte, installeren en in bedrijfstellen is zeer professioneel en plezierig verlopen. Met aandacht voor onze maatwerk wensen. Helemaal top gedaan."),
    ("Sander Vijverberg", "Snelle reactie op de online aanvraag, advies aan huis en binnen 5 weken zeer strak gelegd. De klantgerichtheid van Abdel is super en maakt het hele proces soepel."),
    ("Mark Overeijnder", "Vanaf het eerste contact een goed gevoel. Vriendelijk, deskundig, flexibel. Panelen konden snel geplaatst worden. Kan Abdel zeker aanbevelen!"),
    ("Cyril Brink", "Afspraak was snel gemaakt en deal snel beklonken. Binnen paar weken lagen de panelen op het dak. Ze hebben ons zeker niet teleurgesteld. Van begin tot eind in één woord: top!"),
    ("Irfanos", "Deze mannen doen wat ze beloven! Vakkundig advies gehad en geïnstalleerd!"),
    ("Angelique Gauger", "Top bedrijf, zeker een aanrader! Snel en fijn contact. Vakkundig en aardig personeel. We zijn goed geadviseerd over de mogelijkheden en zijn super blij met onze zonnepanelen."),
]

BLOG = [
    ("waarom-juist-zonnepanelen-in-het-voorjaar-plaatsen", "Waarom juist zonnepanelen in het voorjaar plaatsen?", "18 maart 2025", "De zon begint weer te schijnen, de dagen worden langer en de lente is in aantocht. Het ideale moment om aan zonnepanelen te denken."),
    ("hoe-werken-zonnepanelen", "Hoe werken zonnepanelen?", "6 februari 2025", "Heb je je ooit afgevraagd hoe zonnepanelen eigenlijk werken? Je bent zeker niet de enige."),
    ("zonnepanelen-trends-en-ontwikkelingen-in-2025", "Zonnepanelen: trends en ontwikkelingen in 2025", "30 januari 2025", "De wereld van zonnepanelen verandert razendsnel. Technologieën verbeteren en de vraag naar duurzame energie groeit."),
    ("hoeveel-zonnepanelen-heb-ik-nodig-voor-mijn-woning-in-rotterdam", "Hoeveel zonnepanelen heb ik nodig voor mijn woning in Rotterdam?", "23 januari 2025", "Zonnepanelen zijn niet meer weg te denken uit ons straatbeeld. Maar hoeveel heeft u er nodig?"),
    ("wat-kosten-zonnepanelen-in-2025", "Wat kosten zonnepanelen in 2025?", "23 januari 2025", "Als je aan zonnepanelen denkt, is de eerste vraag vaak: wat gaat het kosten? Dat is ook logisch."),
    ("de-voordelen-van-zonnepanelen-in-een-stedelijke-omgeving-zoals-rotterdam", "De voordelen van zonnepanelen in een stedelijke omgeving zoals Rotterdam", "15 januari 2025", "Wat betekenen zonnepanelen in een stedelijke omgeving? We zetten de voordelen op een rij."),
    ("wat-is-het-beste-moment-om-zonnepanelen-te-installeren", "Wat is het beste moment om zonnepanelen te installeren?", "19 december 2024", "Steeds meer huishoudens en bedrijven stappen over op zonnepanelen. Maar wanneer is het beste moment?"),
    ("nadelen-van-zonnepanelen-op-een-plat-dak-wat-u-moet-weten", "Nadelen van zonnepanelen op een plat dak: wat u moet weten", "12 december 2024", "Een plat dak biedt veel voordelen, zoals een vrije plaatsingshoek. Toch zijn er ook nadelen om rekening mee te houden."),
]

FAQ = [
 ("Loont het nog om zonnepanelen te nemen nu de salderingsregeling stopt?",
  "In veel gevallen wel. De salderingsregeling stopt op 1 januari 2027. Stroom die u direct zelf gebruikt blijft even voordelig, en voor wat u teruglevert ontvangt u een vergoeding (tot 2030 minimaal 50% van het kale leveringstarief). Daarom ontwerpen we uw installatie op uw verbruik en bespreken we of een thuisbatterij zinvol is. Zelfs zonder saldering verdienen zonnepanelen zich volgens de Rijksoverheid nog terug."),
 ("Wat kosten zonnepanelen en hoe snel verdien ik ze terug?",
  "Dat hangt af van uw dak en uw verbruik. Voor een gemiddelde woning ligt de terugverdientijd indicatief tussen 7 en 10 jaar. Voor particulieren geldt bij aankoop voor de eigen woning op dit moment 0% btw. In het gratis adviesgesprek rekenen we het voor uw situatie uit."),
 ("Hoe snel liggen de panelen op mijn dak?",
  f"Na uw aanvraag nemen we contact op voor een afspraak aan huis. Na akkoord op de offerte kan de installatie binnen {TIJD} worden uitgevoerd. De installatie zelf is vaak op één dag klaar."),
 ("Is mijn dak geschikt? Ik heb een plat dak, dakkapel of dakramen.",
  "Meestal wel. We werken op schuine én platte daken, ook rondom dakramen en dakkapellen (zie onze projecten). Tijdens de dakscan beoordelen we oriëntatie, schaduw en dakconstructie, zodat u vooraf weet wat er kan."),
 ("Welke garantie krijg ik?",
  "5 jaar garantie op onze installatie en tot 25 jaar fabrieksgarantie op de A-merken waarmee we werken."),
 ("En als er iets niet werkt?",
  "Dan lossen wij het op. Onderhoud en storingsservice zijn onderdeel van onze dienstverlening, en via de app op uw smartphone ziet u direct hoe uw installatie presteert (monitoring is inbegrepen)."),
 ("Heb ik een thuisbatterij nodig?",
  "Niet altijd. Een batterij is vooral interessant als u overdag veel teruglevert en ’s avonds veel verbruikt. In het adviesgesprek rekenen we beide varianten voor u door, zodat u niet meer betaalt dan nodig."),
 ("Wat kost de dakscan en zit ik ergens aan vast?",
  "De dakscan en het adviesgesprek zijn gratis en vrijblijvend. U beslist pas na het zien van de offerte."),
]


FAQ_BATT = [
 ("Loont een thuisbatterij nog nu de salderingsregeling stopt?",
  "In veel gevallen wel, en juist dan. Vanaf 1 januari 2027 ontvangt u voor teruggeleverde stroom een lagere vergoeding (tot 2030 minimaal 50% van het kale leveringstarief), terwijl stroom die u ’s avonds inkoopt duur blijft. Een batterij bewaart uw overschot zodat u het zelf gebruikt. Of het bij u loont, hangt af van uw verbruik en energiecontract. Dat rekenen we vooraf voor u door."),
 ("Wat kost een thuisbatterij?",
  "Dat hangt af van de capaciteit, het merk en de installatie. Indicatief ligt de investering tussen ongeveer € 4.000 en € 10.000. Na het adviesgesprek ontvangt u een offerte met de exacte prijs, zonder verplichtingen."),
 ("Hoe snel verdien ik een thuisbatterij terug?",
  "Indicatief tussen de 5 en 10 jaar, maar dat verschilt sterk per huishouden. Uw avondverbruik, uw zonnepanelen en uw energiecontract bepalen het resultaat. Daarom rekenen we het voor uw situatie uit en beloven we geen standaardcijfers."),
 ("Kan een batterij bij mijn bestaande zonnepanelen?",
  "In veel gevallen wel. Het hangt af van uw omvormer en installatie. Tijdens het adviesgesprek bekijken we uw meterkast en omvormer en zeggen we eerlijk of het kan en of het loont."),
 ("Welke capaciteit (kWh) heb ik nodig?",
  "Dat hangt af van hoeveel stroom u ’s avonds en ’s nachts gebruikt en hoeveel uw panelen overdag overhouden. Te klein laat opbrengst liggen, te groot kost onnodig geld. We berekenen de juiste maat voor u."),
 ("Werkt de batterij ook bij stroomuitval?",
  "Dat hangt van het systeem af. Sommige thuisbatterijen kunnen als noodstroom dienen, andere niet. We bespreken vooraf wat u wilt en welk model daarbij past."),
 ("Is een thuisbatterij veilig?",
  "Moderne thuisbatterijen hebben ingebouwde beveiligingen. Wij werken met A-merken en laten de batterij installeren door gecertificeerde vakmannen."),
 ("Welke garantie krijg ik?",
  "5 jaar garantie op onze installatie, plus de fabrieksgarantie van het gekozen merk (bij thuisbatterijen vaak 10 jaar). De exacte voorwaarden hangen af van het model dat we voor u kiezen."),
]
FAQ_HOME = FAQ_BATT[:5] + [("Hoe snel is alles geïnstalleerd?", f"Na uw aanvraag komen we langs voor een adviesgesprek. Na akkoord op de offerte kan de installatie binnen {TIJD} worden uitgevoerd."),
                            FAQ[7]]

NAV = [("dd:Thuisbatterij", "batt"), ("dd:Zonnepanelen", "zon"), ("/werkwijze/", "Werkwijze"), ("/projecten/", "Projecten"),
       ("dd:Kennis", "kennis"), ("/over-ons/", "Over ons"), ("/contact/", "Contact")]
DD = {"batt": [("/thuisbatterij/", "Thuisbatterij"), ("/zonnepanelen-met-batterij-accu-kopen/", "Zonnepanelen met batterij")],
      "zon": [("/zonnepanelen-thuis/", "Zonnepanelen thuis"), ("/zonnepanelen-zakelijk/", "Zonnepanelen zakelijk")],
      "kennis": [("/salderingsregeling-2027/", "Salderingsregeling 2027"), ("/blog/", "Blog")]}


def nav_html(path):
    out = []
    for href, label in NAV:
        if href.startswith("dd:"):
            items = DD[label]
            on = " class=on" if any(path == h for h, _ in items) else ""
            out.append(f'<div class="dd"><a href="{items[0][0]}"{on}>{href[3:]}</a><ul>' + "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in items) + "</ul></div>")
        else:
            out.append(f'<a href="{href}"{" class=on" if path == href else ""}>{label}</a>')
    return "".join(out)


def jsonld(path, faq=None, extra=None):
    org = {"@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "name": "ZonnepanelenNu B.V.",
           "url": SITE, "telephone": "+31182607948", "email": MAIL, "image": SITE + img(7),
           "address": {"@type": "PostalAddress", "streetAddress": STRAAT, "postalCode": "2809PE", "addressLocality": "Gouda", "addressCountry": "NL"},
           "areaServed": {"@type": "Country", "name": "Nederland"}, "identifier": f"KvK {KVK}",
           "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": str(NREV)}}
    out = [org] + (extra or [])
    if faq:
        out.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    return "".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in out)


def layout(path, title, desc, body, faq=None, og=None, extra=None, noindex=False):
    cities = "".join(f'<li><a href="/{slug(c)}/">Zonnepanelen {c}</a></li>' for c in CITIES[:6])
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{path}">{'<meta name="robots" content="noindex,follow">' if noindex else ""}
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website"><meta property="og:image" content="{SITE}{og or img(7)}">
<link rel="icon" href="/assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&family=Roboto+Slab:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
{jsonld(path, faq, extra)}
</head>
<body{' class="home"' if path == "/" else ""}>
<a class="skip" href="#main">Ga naar de inhoud</a>
<header><div class="bar">
 <a class="logo" href="/"><img src="/assets/img/logo.png" alt="ZonnepanelenNu" width="90" height="46"></a>
 <button class="burger" aria-label="Menu" aria-expanded="false">☰</button>
 <nav>{nav_html(path)}</nav>
 <div class="actions"><a class="tel" href="tel:{TEL_HREF}">{ic("phone")}{TEL}</a><a class="btn btn-amber btn-sm" href="#offerte">Gratis advies</a></div>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap cols">
 <div><img src="/assets/img/logo-footer.png" alt="ZonnepanelenNu" width="150" height="36"><p>Uw specialist in zonnepanelen voor woning en bedrijf, met persoonlijk advies aan huis.<br><br>{STRAAT}<br>{PLAATS}<br>KvK {KVK}</p></div>
 <div><h4>Pagina’s</h4><ul><li><a href="/over-ons/">Over ons</a></li><li><a href="/werkwijze/">Werkwijze</a></li><li><a href="/projecten/">Projecten</a></li><li><a href="/salderingsregeling-2027/">Salderingsregeling 2027</a></li><li><a href="/blog/">Blog</a></li><li><a href="/contact/">Contact</a></li></ul></div>
 <div><h4>Diensten</h4><ul>{"".join(f'<li><a href="{h}">{l}</a></li>' for h, l in DD["batt"] + DD["zon"])}</ul></div>
 <div><h4>Plaatsen</h4><ul>{cities}</ul><br><a href="tel:{TEL_HREF}"><b style="color:#fff">{TEL}</b></a><br><a href="mailto:{MAIL}">{MAIL}</a></div>
</div>
<div class="wrap legal">© 2026 ZonnepanelenNu B.V. · <a href="/privacyverklaring/">Privacyverklaring</a> · <a href="/algemene-voorwaarden/">Algemene voorwaarden</a> · <a href="/cookie-policy/">Cookiebeleid</a> · <a href="#" data-cookie-settings>Cookie-instellingen</a></div></footer>
<div class="cookie" id="cookie" hidden role="dialog" aria-label="Cookies"><p><b>Wij gebruiken cookies</b><br>Voor een goed werkende website en, met uw toestemming, voor statistieken en advertenties. <a href="/cookie-policy/">Lees meer</a></p><div><button class="btn btn-line btn-sm" data-consent="no">Alleen noodzakelijk</button><button class="btn btn-amber btn-sm" data-consent="yes">Accepteren</button></div></div>
<div class="callbar"><a href="tel:{TEL_HREF}">{ic("phone")} Bel ons</a><a href="#offerte">Gratis advies</a></div>
<a class="wa-fab" href="https://wa.me/31634685201?text=Hallo%2C%20ik%20heb%20een%20vraag%20over%20zonnepanelen%2Fthuisbatterij" target="_blank" rel="noopener" aria-label="Stuur ons een WhatsApp-bericht"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg></a>
<script src="/assets/main.js"></script>
</body>
</html>"""


# ------------------------------------------------------------------ blokken
def stars(): return '<span class="stars" aria-label="5 van 5 sterren">★★★★★</span>'


def hero(h1, sub, image, crumb=None, eyebrow=None, pcbar=True, buttons=False):
    cr = f'<div class="crumbs"><a href="/">Home</a> / {crumb}</div>' if crumb else ""
    eb = f'<span class="eyebrow">{eyebrow}</span><br>' if eyebrow else ""
    if pcbar:
        act = f"""<div class="pc" data-pc><input aria-label="Postcode en huisnummer" placeholder="Postcode + huisnummer" autocomplete="postal-code"><button class="btn btn-amber" type="button">Vraag gratis advies</button></div>
  <div class="hnote"><span class="ch">Gratis en vrijblijvend</span><span class="ch">Offerte binnen 24 uur</span><span>{stars()} <b>{RATING}</b> Google-reviews</span></div>"""
    else:
        act = f'<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-amber" href="#offerte">Gratis advies</a><a class="btn btn-ghost" href="tel:{TEL_HREF}">{ic("phone")} {TEL}</a></div>'
    return f"""<section class="hero" style="--hero:url('{image}')"><div class="wrap">
 <div class="hcard">{cr}{eb}<h1>{h1}</h1><p class="sub">{sub}</p>{act}</div>
</div></section>"""


def trust():
    it = [("star", f"{RATING} op Google", "Google-reviews"), ("shield", "Gecertificeerd", "vakmannen met papieren"),
          ("tool", "5 jaar garantie", "tot 25 jaar op panelen"), ("home", "Advies aan huis", "gratis en vrijblijvend")]
    return '<div class="trust"><div class="wrap">' + "".join(f'<div><span class="ic">{ic(i)}</span><span class="txt"><b>{a}</b><small>{b}</small></span></div>' for i, a, b in it) + "</div></div>"


def head(eyebrow, h2, lead="", c=False):
    return f'<div class="head{" c" if c else ""} reveal"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{f"<p class=lead>{lead}</p>" if lead else ""}</div>'


PAINS = [
 ("euro", "Ik krijg straks weinig terug voor mijn overschot", "Vanaf 2027 stopt salderen. Een batterij vangt uw overschot op, zodat u het zelf gebruikt.", "/thuisbatterij/", "Zo werkt een thuisbatterij"),
 ("trend", "Mijn energierekening blijft stijgen", "’s Avonds gebruikt u de meeste stroom, maar dan schijnt de zon niet meer. Een batterij lost dat op.", "/thuisbatterij/", "Bekijk de mogelijkheden"),
 ("battery", "Ik heb al zonnepanelen. Kan er een batterij bij?", "Meestal wel. Wij checken uw omvormer en meterkast, en zeggen eerlijk of het loont.", "#offerte", "Vraag advies aan"),
]

def pain_block():
    cards = "".join(f'<a class="pain reveal" href="{h}"><div class="ic">{ic(i)}</div><h3>{t}</h3><p>{p}</p><span class="more">{l}</span></a>' for i, t, p, h, l in PAINS)
    return f'<section><div class="wrap">{head("Herkent u dit?", "Waar loopt u tegenaan?", "De vragen die we het vaakst horen — met een eerlijk antwoord.")}<div class="grid3" style="margin-bottom:36px">{cards}</div></div></section>'


def how_block(image=15, alt=True):
    return f"""<section class="{'alt' if alt else ''}"><div class="wrap split">
 <div class="ph reveal"><img src="{img(image)}" alt="Installateur van ZonnepanelenNu monteert een zonnepaneel" loading="lazy"></div>
 <div class="reveal"><span class="eyebrow">Zo werkt het</span><h2>Eerst kijken we naar uw situatie. Dan pas praten we over prijs.</h2>
  <p>We komen bij u langs, bekijken meterkast, omvormer en dak en kijken naar uw verbruik. Daarna krijgt u een offerte op maat: de juiste opzet (batterij, panelen of allebei), de verwachte besparing en de terugverdientijd. Duidelijk, zonder kleine lettertjes.</p>
  <p>Akkoord? Dan plannen we de installatie. Onze gecertificeerde vakmannen installeren alles en nemen het afval mee. U hoeft niets te regelen.</p>
  <ul class="list"><li>Advies aan huis is standaard en gratis</li><li>Offerte met verwachte besparing per jaar</li><li>Monitoring via uw smartphone inbegrepen</li></ul>
  <p style="margin-top:26px"><a class="btn btn-amber" href="#offerte">Plan uw adviesgesprek</a></p></div></div></section>"""



def calc_block():
    return f"""<section id="calculator"><div class="wrap">
 {head("Bereken uw batterij", "Wat levert een thuisbatterij u op?", "Vul uw verbruik in en zie direct de geadviseerde capaciteit, de besparing en de terugverdientijd. Duurt 30 seconden, indicatief en vrijblijvend.", True)}
 <div class="calcbox reveal">
  <div class="calc-in">
   <div class="calc-row">
    <label for="c-verbruik">Jaarverbruik <b class="calc-val" id="cv-verbruik">3.500 kWh</b></label>
    <input type="range" id="c-verbruik" min="1500" max="8000" step="100" value="3500">
    <small>Staat op uw jaarafrekening of in uw energie-app.</small>
   </div>
   <div class="calc-row">
    <label for="c-kwp">Zonnepanelen <b class="calc-val" id="cv-kwp">5,0 kWp</b></label>
    <input type="range" id="c-kwp" min="0" max="15" step="0.5" value="5">
    <small id="cv-panelen">≈ 13 panelen (± 400 Wp per paneel)</small>
   </div>
   <div class="calc-checks">
    <label class="ccheck"><input type="checkbox" id="c-ev"> Elektrische auto</label>
    <label class="ccheck"><input type="checkbox" id="c-wp"> Warmtepomp</label>
    <label class="ccheck"><input type="checkbox" id="c-dyn"> Dynamisch energiecontract</label>
    <label class="ccheck"><input type="checkbox" id="c-btw" checked> BTW-teruggave via zonnepanelen</label>
   </div>
   <details class="calc-more"><summary>Details tonen (oriëntatie + aansluiting)</summary>
    <div class="row2">
     <div><label for="c-or">Oriëntatie van uw panelen</label><select id="c-or"><option>Zuid</option><option>Oost-west</option><option>Oost of west</option></select></div>
     <div><label for="c-aan">Aansluiting</label><select id="c-aan"><option>1-fase</option><option>3-fase</option></select></div>
    </div>
   </details>
  </div>
  <div class="calc-out">
   <span class="eyebrow">Geadviseerde batterij</span>
   <div class="calc-battery"><b id="co-kwh">–</b><span>kWh</span></div>
   <p class="calc-model" id="co-model">&nbsp;</p>
   <div class="calc-grid">
    <div><span>Besparing jaar 1</span><b id="co-besparing">–</b></div>
    <div><span>Terugverdientijd</span><b id="co-terug">–</b></div>
    <div><span>Investering (netto)</span><b id="co-investering">–</b></div>
   </div>
   <a class="btn btn-amber" href="#offerte">Persoonlijk advies aanvragen</a>
   <p class="calc-note">Indicatieve berekening op basis van ± 950 kWh opbrengst per kWp per jaar, een stroomprijs van € 0,28 en een terugleververgoeding van € 0,08 per kWh. Geadviseerd op AEG Solarcube-capaciteiten (4,8 / 9,6 / 14,4 kWh). Definitieve cijfers volgen uit een gratis adviesgesprek aan huis.</p>
  </div>
 </div>
</div></section>"""


def battery_block():
    st = [("Overdag opladen", "Uw panelen wekken meer op dan u gebruikt. Het overschot gaat in de batterij, in plaats van naar het net."),
          ("’s Avonds gebruiken", "Als de zon weg is, gebruikt u uw eigen opgeslagen stroom. U koopt minder in tegen het hoge avondtarief."),
          ("Slim handelen", "Een slimme batterij laadt op goedkope uren en ontlaadt op dure. Op een dag met grote prijsverschillen kan dat met 10 kWh ruim € 7 opleveren (voorbeeld).")]
    steps = "".join(f"<div class='reveal'><h3>{t}</h3><p>{d}</p></div>" for t, d in st)
    return f"""<section class="alt" id="thuisbatterij"><div class="wrap">
 <div class="split">
  <div class="ph reveal"><img src="{img(35)}" alt="AEG-thuisbatterij naast de meterkast" loading="lazy"></div>
  <div class="reveal"><span class="eyebrow">Thuisbatterij</span><h2>Gebruik ’s avonds uw eigen zonnestroom</h2>
   <p>Zonnepanelen leveren overdag, maar u gebruikt het meest in de ochtend en de avond. Een thuisbatterij overbrugt dat gat. Zo betaalt u minder voor stroom uit het net, en verliest u minder aan teruglevering.</p>
   <ul class="list"><li>Minder stroom inkopen, meer zelf gebruiken</li><li>Minder afhankelijk van terugleververgoedingen</li><li>Ook te combineren met bestaande zonnepanelen (afhankelijk van uw installatie)</li><li>Advies met eerlijke berekening, zonder standaardbeloftes</li></ul>
   <p style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-amber" href="/thuisbatterij/">Alles over de thuisbatterij</a><a class="btn btn-line" href="#offerte">Vraag gratis advies</a></p></div></div>
 <div class="steps" style="margin-top:56px">{steps}</div></div></section>"""

def saldering_block():
    return f"""<section class="dark"><div class="wrap">{head("Salderingsregeling 2027", '<span class="accent">Saldering</span> stopt op 1 januari 2027. Zo haalt u toch het maximale uit uw stroom.')}
 <div class="sal">
  <div class="reveal"><div class="num"><b>1.</b><h3>Een batterij als buffer</h3></div><p>Overdag wekt u veel op, ’s avonds gebruikt u het meest. Een thuisbatterij overbrugt dat gat, in plaats van dat u uw overschot goedkoop teruglevert.</p></div>
  <div class="reveal"><div class="num"><b>2.</b><h3>Zelf gebruiken wint</h3></div><p>Stroom die u direct gebruikt verandert niet: die blijft even voordelig. Een installatie die past bij uw verbruik is daarom belangrijker dan ooit.</p></div>
  <div class="reveal"><div class="num"><b>3.</b><h3>Nog steeds een vergoeding</h3></div><p>Voor wat u teruglevert ontvangt u een vergoeding van uw leverancier: tot 2030 minimaal 50% van het kale leveringstarief.</p></div>
 </div>
 <p style="margin-top:34px"><a class="btn btn-amber" href="/salderingsregeling-2027/">Wat betekent dit voor mij?</a></p>
 <p class="src">Bron: <a href="https://www.rijksoverheid.nl/themas/klimaat-milieu-en-natuur/energie-thuis/salderingsregeling" rel="noopener">Rijksoverheid, salderingsregeling</a></p></div></section>"""


def services_block():
    d = [(35, "Thuisbatterij", "Sla uw zonnestroom op en gebruik hem wanneer u wilt, zonder zorgen over terugleververgoedingen.", "/thuisbatterij/"),
         (9, "Zonnepanelen met batterij", "Panelen en batterij als één geheel, afgestemd op uw verbruik. Eén gesprek, één offerte.", "/zonnepanelen-met-batterij-accu-kopen/"),
         (1, "Zonnepanelen thuis", "Verlaag uw energierekening en word minder afhankelijk van het net, met een installatie die bij uw dak past.", "/zonnepanelen-thuis/")]
    cards = "".join(f'<article class="card reveal"><img src="{img(n, True)}" alt="{t}" loading="lazy"><div class="b"><h3>{t}</h3><p>{p}</p><a class="more" href="{h}">Lees meer</a></div></article>' for n, t, p, h in d)
    return f'<section class="alt"><div class="wrap">{head("Onze diensten", "Eén partner, van advies tot service", "Wat u ook kiest: u praat met dezelfde mensen van eerste gesprek tot storingsservice.")}<div class="grid3">{cards}</div><p style="text-align:center;margin-top:30px;color:var(--mute)">Ook voor bedrijven: <a class="more" href="/zonnepanelen-zakelijk/">zonnepanelen zakelijk</a></p></div></section>'


def why_block():
    return f"""<section><div class="wrap split rev why">
 <div class="reveal"><span class="eyebrow">Waarom ZonnepanelenNu</span><h2>Kwaliteit door jarenlange ervaring</h2>
  <p>We doen dit al meer dan tien jaar, op woningen en bedrijfspanden in de hele regio. Wij werken alleen met A-merken, en als de installatie er eenmaal ligt, blijven we gewoon bereikbaar: geen callcenter, maar hetzelfde vertrouwde team dat u ook aan huis heeft gehad.</p>
  <div class="pillars">
   <div class="pillar"><b class="n">1</b><div><h3>Persoonlijk en professioneel advies</h3><p>Eerst uitgebreid advies aan huis, daarna pas een offerte en een installatie.</p></div></div>
   <div class="pillar"><b class="n">2</b><div><h3>Gecertificeerde vakmannen</h3><p>Al onze vakmannen beschikken over de juiste papieren en certificaten.</p></div></div>
   <div class="pillar"><b class="n">3</b><div><h3>Onderhoud en storingsservice</h3><p>Loopt er iets niet zoals het hoort? Wij lossen het snel en vakkundig op.</p></div></div>
  </div><a class="btn btn-blue" href="/over-ons/">Lees meer over ons</a></div>
 <div class="ph reveal"><img src="{img(12)}" alt="Team van ZonnepanelenNu op de steiger" loading="lazy"></div></div></section>"""


def stats_block():
    it = [("10+", "jaar, erkend installateur"), (RATING, "gemiddeld op Google"), ("1.000+", "tevreden klanten"), ("25 jr", "fabrieksgarantie")]
    return '<section class="dark" style="padding:64px 0"><div class="stats reveal">' + "".join(f"<div><b>{n}</b><span>{l}</span></div>" for n, l in it) + "</div></section>"


GAL_HOME = [(35, "tall", "AEG-thuisbatterij"), (2, "", "Zwarte panelen rond dakkapel"), (36, "", "AEG-batterij"),
            (6, "wide", "Bedrijfspand"), (9, "tall", "Omvormer"), (22, "", "Plat dak, opstelling"), (14, "", "Installatie op plat dak"),
            (12, "wide", "Ons team aan het werk"), (18, "", "Panelen rond dakramen"), (30, "wide", "Woning met dakramen"),
            (26, "", "Woning in de zon"), (8, "tall", "Installateurs op de steiger")]
GAL_THUIS = [(2, "tall", "Zwarte panelen rond dakkapel"), (22, "", "Plat dak, opstelling"), (14, "", "Installatie op plat dak"),
             (30, "", "Woning met dakramen"), (4, "", "Rijtjeswoningen"), (35, "", "AEG-thuisbatterij"), (26, "", "Woning in de zon")]
GAL_BIZ = [(6, "wide", "Bedrijfspand"), (25, "wide", "Industrieel dak")]
GAL_BATT = [(35, "", "AEG-thuisbatterij"), (9, "", "Omvormer"), (36, "", "AEG-batterij")]


def gallery_block(items=None, link=True, cols=4):
    items = items or GAL_HOME
    figs = "".join(f'<figure class="{c} reveal"><img src="{img(i, True)}" alt="{t}" loading="lazy"><figcaption>{t}</figcaption></figure>' for i, c, t in items)
    more = '<p style="text-align:center;margin-top:34px"><a class="btn btn-blue" href="/projecten/">Alle projecten bekijken</a></p>' if link else ""
    return f'<section class="alt"><div class="wrap">{head("Klantverhalen", "Zo ziet het er bij onze klanten uit", "Echte installaties, door ons team gelegd.")}<div class="gal{" c3" if cols == 3 else ""}">{figs}</div>{more}</div></section>'


def reviews_block(n=3, alt=False):
    r = "".join(f'<blockquote class="reveal">{stars()}<span>“{e(t)}”</span><cite><i>{e(a[0])}</i><span>{e(a)}<small>Google-review</small></span></cite></blockquote>' for a, t in REVIEWS[:n])
    return f"""<section class="{'alt' if alt else ''}" id="reviews"><div class="wrap">{head("Reviews", "Wat klanten over ons zeggen")}
 <div class="rate reveal"><span class="big">{RATING}</span><span>{stars()}<br><small style="color:var(--mute)">Google-reviews</small></span></div>
 <div class="rev">{r}</div></div></section>"""


def steps_block():
    return f"""<section id="werkwijze"><div class="wrap">{head("Werkwijze", "In drie stappen naar uw zonnedak", "Duidelijk, persoonlijk en zonder verrassingen.", True)}
 <div class="steps"><div class="reveal"><h3>Adviesgesprek aan huis</h3><p>Zodra u een aanvraag doet, nemen we snel contact op. We komen langs om dak en meterkast te bekijken en stellen een offerte op maat op.</p></div>
 <div class="reveal"><h3>Installatie en controle</h3><p>Na akkoord plannen we de installatie. Onze gecertificeerde vakmannen leggen de panelen vakkundig en nemen al het afval mee.</p></div>
 <div class="reveal"><h3>Service en onderhoud</h3><p>5 jaar garantie op de installatie en tot 25 jaar fabrieksgarantie. Ook voor onderhoud en storingen bent u bij ons aan het juiste adres.</p></div></div></div></section>"""


def brands_block():
    logos = [("lg.png", "LG"), ("jasolar.png", "JA Solar"), ("growatt.png", "Growatt"), ("apsystems.png", "APsystems")]
    imgs = "".join(f'<img src="/assets/img/{f}" alt="{a}" loading="lazy">' for f, a in logos)
    # rij staat 4x achter elkaar (vult ook brede schermen volledig) zodat de -25%-scrollanimatie naadloos herhaalt; nieuwe merken later gewoon aan `logos` toevoegen
    return f'<section style="padding:56px 0"><div class="wrap"><p style="text-align:center;font-weight:700;color:var(--navy);margin-bottom:22px">Wij werken uitsluitend met A-merken</p><div class="brand-strip"><div class="brands" aria-hidden="false">{imgs * 4}</div></div></div></section>'


def faq_block(items=FAQ, alt=True):
    d = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
    return f"""<section class="{'alt' if alt else ''}"><div class="wrap faqwrap">
 <div class="reveal"><span class="eyebrow">Veelgestelde vragen</span><h2>Antwoord op de vragen die u nog heeft</h2><p class="lead">Staat uw vraag er niet tussen? Bel ons gerust op {TEL}.</p><p style="margin-top:22px"><a class="btn btn-line" href="tel:{TEL_HREF}">{ic("phone")} {TEL}</a></p>
  <div class="faq-photo"><img src="{img(37)}" alt="Geplaatste zonnepanelen in Bodegraven" loading="lazy"></div></div>
 <div class="reveal">{d}</div></div></section>"""


def offer_block(title="Ontdek wat een thuisbatterij voor uw woning kan betekenen"):
    return f"""<section id="offerte"><div class="wrap offer">
 <div class="reveal"><span class="eyebrow">Gratis advies</span><h2>{title}</h2>
  <p class="lead" style="margin-bottom:22px">Laat uw gegevens achter en we nemen contact met u op voor een afspraak aan huis. U ontvangt een voorstel op maat.</p>
  <ul class="list"><li>Gratis en vrijblijvend</li><li>Verwachte besparing en terugverdientijd voor uw situatie</li><li>Offerte binnen 24 uur na het adviesgesprek</li><li>Geen verplichtingen, u beslist pas na de offerte</li></ul>
  <div class="person"><div class="av">A</div><div><b>Abdel en team</b><small>Uw aanvraag wordt persoonlijk opgepakt</small></div></div>
  <p style="margin-top:20px;color:var(--mute)">Liever bellen? <a href="tel:{TEL_HREF}" style="color:var(--blue-d);font-weight:700">{TEL}</a></p></div>
 <form class="form reveal" data-form novalidate><div class="fields"><h3 style="font-size:24px;margin-bottom:4px">Vraag uw gratis advies aan</h3><small style="color:var(--mute)">Duurt 1 minuut</small>
  <div class="row2"><div><label for="f-naam">Naam *</label><input id="f-naam" required autocomplete="name"></div><div><label for="f-tel">Telefoon *</label><input id="f-tel" type="tel" required autocomplete="tel"></div></div>
  <label for="f-mail">E-mailadres *</label><input id="f-mail" type="email" required autocomplete="email">
  <div class="row2"><div><label for="f-postcode">Postcode + huisnummer *</label><input id="f-postcode" required autocomplete="postal-code"></div><div><label for="f-dak">Type dak</label><select id="f-dak"><option>Schuin dak</option><option>Plat dak</option><option>Beide / weet ik niet</option></select></div></div>
  <label for="f-opm">Opmerking (optioneel)</label><textarea id="f-opm" placeholder="Bijv. dakkapel, dakramen of een thuisbatterij"></textarea>
  <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" style="display:none"><label class="check"><input type="checkbox" required> <span>Ik ga akkoord met het opslaan en verwerken van mijn gegevens volgens de privacyverklaring. *</span></label>
  <button class="btn btn-amber" type="submit">Verstuur mijn aanvraag</button><p class="note">🔒 Uw gegevens worden niet gedeeld met derden.</p></div>
  <div class="done"><b>Bedankt! ✓</b>We nemen zo snel mogelijk contact met u op om een afspraak in te plannen.</div></form></div></section>"""


GLOSS = [("Salderingsregeling", "Regeling waarbij stroom die u teruglevert wordt weggestreept tegen wat u afneemt. Stopt op 1 januari 2027."),
         ("Terugleveren", "Stroom die u zelf opwekt maar niet direct gebruikt, en aan het elektriciteitsnet levert."),
         ("Zelfverbruik", "Het deel van uw zonnestroom dat u direct zelf gebruikt. Dat is het voordeligste deel."),
         ("Omvormer", "Zet de gelijkstroom van uw panelen om in wisselstroom die uw huis kan gebruiken."),
         ("kWp (kilowattpiek)", "Het maximale vermogen van uw installatie onder ideale omstandigheden."),
         ("Thuisbatterij", "Slaat overtollige zonnestroom op, zodat u die later kunt gebruiken, bijvoorbeeld ’s avonds.")]

def gloss_block():
    d = "".join(f"<div class='reveal'><h3>{a}</h3><p>{b}</p></div>" for a, b in GLOSS)
    return f'<section class="alt"><div class="wrap">{head("Energiebegrippen", "Alles over zonne-energie, in gewone taal")}<div class="gl">{d}</div></div></section>'


def cities_block():
    return f'<section><div class="wrap">{head("Plaatsen", "Zonnepanelen en thuisbatterijen in uw plaats", "Vraag advies aan in uw plaats.")}<div class="cities">' + "".join(f'<a href="/{slug(c)}/">Zonnepanelen {c}</a>' for c in CITIES) + "</div></div></section>"


def cta_block(h="Klaar om uw eigen stroom slimmer te gebruiken?", p="Vraag gratis advies aan. Vrijblijvend, en u weet snel of een thuisbatterij bij u past.", image=29):
    return f'<section style="padding:0 0 92px"><div class="wrap"><div class="cta-band reveal" style="--cta:url(\'{img(image)}\')"><div><h2>{h}</h2><p>{p}</p></div><div class="acts"><a class="btn btn-amber" href="#offerte">Gratis advies</a><a class="btn btn-ghost" href="tel:{TEL_HREF}">{TEL}</a></div></div></div></section>'


def prose(inner, alt=False):
    return f'<section class="{"alt" if alt else ""}"><div class="wrap"><div class="prose">{inner}</div></div></section>'


# ------------------------------------------------------------------ pagina's
def post_card(p):
    return f'<a class="post reveal" href="{p["path"]}" data-cat="{e(p["cat"])}" data-t="{e(p["title"].lower())}"><div class="meta">{e(p["cat"])} · {p["mins"]} min leestijd</div><h3>{e(p["title"])}</h3><p>{e(p["excerpt"])}</p><span class="more">Lees meer</span></a>'


def latest_block(n=3, keys=None, title="Laatste artikelen"):
    sel = [p for p in POSTS if not keys or any(k in p["title"].lower() for k in keys)][:n]
    return f'<section><div class="wrap">{head("Kennis", title, "Antwoorden op vragen over kosten, opbrengst en thuisbatterijen.")}<div class="grid3">{"".join(post_card(p) for p in sel)}</div><p style="text-align:center;margin-top:34px"><a class="btn btn-line" href="/blog/">Alle artikelen</a></p></div></section>'


def related_block(keys, n=3):
    sel = [p for p in POSTS if any(k in p["title"].lower() for k in keys)][:n]
    if not sel:
        return ""
    return f'<section><div class="wrap">{head("Meer lezen", "Gerelateerde artikelen")}<div class="grid3">{"".join(post_card(p) for p in sel)}</div></div></section>'


pages = {}   # pad -> (title, desc, body, faq?)

pages["/"] = ("Thuisbatterij en zonnepanelen | Advies aan huis | ZonnepanelenNu",
 f"Sla uw zonnestroom op met een thuisbatterij en betaal minder. Persoonlijk advies aan huis, gecertificeerde vakmannen en {RATING} op Google. Vraag gratis advies aan.",
 hero("Gebruik uw eigen zonnestroom <span>wanneer u wilt</span>",
      "Per 1 januari 2027 stopt de salderingsregeling. Een thuisbatterij bewaart uw overschot voor de avond, zodat u minder inkoopt en minder verliest bij terugleveren. Wij adviseren, installeren en blijven bereikbaar.",
      img(38), eyebrow="Thuisbatterijen en zonnepanelen")
 + trust() + pain_block() + calc_block() + battery_block() + saldering_block() + how_block(7, False) + services_block() + why_block() + stats_block()
 + gallery_block() + reviews_block(3) + steps_block() + brands_block() + faq_block(FAQ_HOME) + offer_block() + latest_block(3, ("batterij", "accu"), "Alles over thuisbatterijen") + gloss_block() + cities_block() + cta_block(),
 FAQ_HOME)

pages["/zonnepanelen-thuis/"] = ("Zonnepanelen voor thuis | Advies aan huis | ZonnepanelenNu",
 "Lagere energierekening met zonnepanelen op uw woning. Gratis advies aan huis, A-merken met tot 25 jaar garantie en gecertificeerde vakmannen.",
 hero("Zonnepanelen voor uw <span>woning</span>", "Verlaag uw energierekening en word minder afhankelijk van het net. Met een installatie die past bij uw dak en uw verbruik.", img(1), "Zonnepanelen thuis", "Zonnepanelen thuis")
 + trust()
 + prose(f"""<span class="eyebrow">Voor huiseigenaren</span><h2>Bespaar op uw energierekening, ook na 2027</h2>
 <p>Elke kilowattuur die u zelf opwekt en direct gebruikt, hoeft u niet in te kopen. Dat blijft na het stoppen van de salderingsregeling op 1 januari 2027 net zo voordelig. Daarom kijken we bij een advies niet alleen naar uw dak, maar vooral naar wanneer u stroom gebruikt.</p>
 <p>Met een gratis dakscan weet u binnen een minuut of uw dak geschikt is. Daarna komen we bij u langs voor een advies op maat, met de verwachte opbrengst en terugverdientijd.</p>
 <h2>Wat u van ons mag verwachten</h2>
 <ul><li>Gratis advies aan huis, ook voor platte daken, dakkapellen en dakramen</li><li>Alleen A-merken, met tot 25 jaar fabrieksgarantie</li><li>5 jaar garantie op onze installatie</li><li>Monitoring via uw smartphone inbegrepen</li><li>Installatie door gecertificeerde vakmannen, afval nemen we mee</li></ul>""")
 + how_block(8, False) + gallery_block(GAL_THUIS) + reviews_block(3, True) + related_block(("kost", "terugverdien", "energierekening")) + faq_block() + offer_block() + cta_block(),
 FAQ)

pages["/zonnepanelen-zakelijk/"] = ("Zonnepanelen zakelijk | Bedrijfsdak verduurzamen | ZonnepanelenNu",
 "Bespaar op energiekosten met zonnepanelen op uw bedrijfsdak. Advies op maat, A-merken en een vaste partner voor onderhoud en storingen.",
 hero("Zonnepanelen voor uw <span>bedrijf</span>", "Uw bedrijfsdak als energiebron. Verlaag uw energiekosten en versterk uw duurzame imago.", img(6), "Zonnepanelen zakelijk", "Zakelijke zonnepanelen")
 + trust()
 + prose("""<span class="eyebrow">Voor ondernemers</span><h2>Energie is een kostenpost. Uw dak kan er iets aan doen.</h2>
 <p>Een bedrijfsdak is vaak groot, vrij van schaduw en dus ideaal voor zonnepanelen. Overdag, als uw bedrijf het meeste verbruikt, wekt u zelf stroom op. Dat verlaagt uw energiekosten direct.</p>
 <p>We komen altijd eerst ter plaatse om dak, aansluiting en verbruik te beoordelen. Zo krijgt u een offerte die klopt, en geen standaardpakket.</p>
 <ul><li>Oplossingen voor platte, schuine en industriële daken</li><li>Alleen A-merken, met fabrieksgarantie</li><li>Monitoring via smartphone inbegrepen</li><li>Onderhoud en storingsservice na oplevering</li></ul>""")
 + gallery_block(GAL_BIZ, False) + reviews_block(3, True) + faq_block() + offer_block("Wat kunnen zonnepanelen voor uw bedrijf betekenen?") + cta_block(),
 FAQ)


def battery_usp():
    it = [("🌙", "Minder inkopen", "U gebruikt ’s avonds uw eigen stroom in plaats van stroom uit het net."),
          ("💶", "Minder verlies bij teruglevering", "Na de salderingsregeling levert teruggeleverde stroom minder op. Opslaan is dan slimmer."),
          ("📈", "Slim handelen", "Een slimme batterij laadt op goedkope uren en ontlaadt op dure."),
          ("🔌", "Bij bestaande panelen", "In veel gevallen kan een batterij bij uw huidige installatie (afhankelijk van uw omvormer)."),
          ("🛡️", "Optioneel noodstroom", "Sommige modellen kunnen bij stroomuitval doorleveren. We bespreken wat u wilt."),
          ("📱", "Inzicht op uw telefoon", "Volg live wat uw panelen en batterij doen (monitoring is inbegrepen).")]
    return f'<section><div class="wrap">{head("Voordelen", "Waarom een thuisbatterij?")}<div class="usp">' + "".join(
        f'<div class="reveal"><div class="ic">{i}</div><h3>{t}</h3><p>{p}</p></div>' for i, t, p in it) + "</div></div></section>"


def battery_steps():
    return f"""<section class="alt"><div class="wrap">{head("Zo werkt het", "In drie stappen slimmer met uw stroom", "", True)}
 <div class="steps"><div class="reveal"><h3>Overdag opladen</h3><p>Uw panelen wekken meer op dan u gebruikt. Het overschot gaat in de batterij.</p></div>
 <div class="reveal"><h3>’s Avonds gebruiken</h3><p>Als de zon weg is, gebruikt u uw opgeslagen stroom en koopt u minder in.</p></div>
 <div class="reveal"><h3>Slim aansturen</h3><p>De batterij laadt op goedkope momenten en ontlaadt op dure. Op een dag met grote prijsverschillen kan dat met 10 kWh ruim € 7 opleveren (voorbeeld).</p></div></div></div></section>"""

pages["/thuisbatterij/"] = ("Thuisbatterij installeren | Zonnestroom opslaan | ZonnepanelenNu",
 "Sla uw zonnestroom op met een thuisbatterij en gebruik hem wanneer u wilt. Eerlijk advies aan huis en installatie door gecertificeerde vakmannen. Vraag gratis advies aan.",
 hero("Gebruik uw zonnestroom wanneer <span>u</span> wilt", "Een thuisbatterij bewaart uw overschot voor de avond, in plaats van dat u het goedkoop teruglevert.", img(35), "Thuisbatterij", "Thuisbatterij")
 + trust() + battery_usp() + battery_steps() + calc_block()
 + prose("""<span class="eyebrow">Kosten en rendement</span><h2>Wat kost een thuisbatterij, en wanneer verdient hij zich terug?</h2>
 <p>Dat hangt af van de capaciteit, het merk en de installatie. Indicatief ligt de investering tussen ongeveer € 4.000 en € 10.000. De terugverdientijd ligt indicatief tussen 5 en 10 jaar, maar verschilt sterk per huishouden: uw avondverbruik, uw zonnepanelen en uw energiecontract bepalen het resultaat.</p>
 <p>Daarom beloven wij geen standaardcijfers. In een gratis adviesgesprek bekijken we uw meterkast, omvormer en verbruik, en rekenen we uit of een batterij bij u loont. Zo niet, dan zeggen we dat ook.</p>
 <h2>Welke capaciteit heeft u nodig?</h2>
 <p>Te klein laat opbrengst liggen, te groot kost onnodig geld. De juiste maat hangt af van uw verbruik ’s avonds en ’s nachts en van wat uw panelen overdag overhouden.</p>
 <ul><li>Advies of u een batterij nodig heeft, met eerlijke berekening</li><li>Installatie door gecertificeerde vakmannen</li><li>Alleen A-merken, met fabrieksgarantie</li><li>5 jaar garantie op onze installatie</li></ul>""")
 + saldering_block() + gallery_block(GAL_BATT, False, 3) + related_block(("batterij", "accu"), 6) + faq_block(FAQ_BATT) + offer_block("Past een thuisbatterij bij uw situatie?") + cta_block(),
 FAQ_BATT)

pages["/zonnepanelen-met-batterij-accu-kopen/"] = ("Zonnepanelen met thuisbatterij kopen | ZonnepanelenNu",
 "Zonnepanelen én een thuisbatterij in één keer laten plaatsen? Persoonlijk advies aan huis en een offerte op maat van ZonnepanelenNu.",
 hero("Zonnepanelen met <span>thuisbatterij</span>", "Zonnepanelen met batterij plaatsen? Eén adviesgesprek, één offerte, één partner.", img(39), "Zonnepanelen met batterij", "Combinatiepakket")
 + trust() + calc_block()
 + prose("""<span class="eyebrow">Alles in één keer</span><h2>Waarom zonnepanelen en batterij samen?</h2>
 <p>Wanneer u ze tegelijk laat plaatsen, ontwerpen we de installatie als één geheel: het aantal panelen, de omvormer en de batterij zijn op elkaar afgestemd. Dat is praktisch, en u praat met één partner als er iets is.</p>
 <h2>Hoe werkt het samen?</h2>
 <p>Uw panelen wekken stroom op. Wat u direct gebruikt, gebruikt u direct. Wat overblijft, gaat in de batterij en gebruikt u ’s avonds. Alleen wat dan nog over is, levert u terug.</p>
 <h2>Slim handelen op de energiebeurs</h2>
 <p>Een batterij die automatisch wordt aangestuurd, laadt wanneer stroom goedkoop is en ontlaadt wanneer stroom duur is. Energieprijzen worden per uur bepaald op basis van vraag en aanbod, en overdag zijn ze door zonnestroom vaak laag of zelfs negatief.</p>""")
 + related_block(("batterij", "accu")) + faq_block(FAQ_BATT) + offer_block("Offerte voor zonnepanelen met batterij") + cta_block(),
 FAQ_BATT)

pages["/salderingsregeling-2027/"] = ("Salderingsregeling stopt 1 januari 2027: wat betekent dat voor u? | ZonnepanelenNu",
 "De salderingsregeling stopt op 1 januari 2027. Wat verandert er, loont het nog om zonnepanelen te nemen en hoe haalt u meer uit uw eigen stroom?",
 hero("Salderingsregeling stopt op <span>1 januari 2027</span>", "Wat verandert er precies, loont het nog en wat kunt u doen? Een eerlijk overzicht, zonder verkooppraatjes.", img(7), "Salderingsregeling 2027", "Kennis", pcbar=False)
 + prose("""<h2>Wat verandert er?</h2>
 <p>Tot en met 31 december 2026 mag u stroom die u teruglevert wegstrepen tegen wat u afneemt. Dat heet salderen. Vanaf 1 januari 2027 stopt dat, in één keer en voor iedereen. Ook als uw panelen al liggen.</p>
 <p>Elke kilowattuur die u teruglevert wordt daarna apart afgerekend. Uw leverancier moet u tot 2030 minimaal 50% van het kale leveringstarief (zonder belastingen) vergoeden. Dat is minder dan wat u betaalt voor stroom uit het stopcontact.</p>
 <h2>Loont het nog om zonnepanelen te nemen?</h2>
 <p>Ja, in veel gevallen wel. Stroom die u op het moment van opwekken zelf gebruikt, blijft net zo voordelig als nu. Volgens de Rijksoverheid verdienen zonnepanelen zich ook zonder salderingsregeling nog terug. Het verschil zit in hoe goed de installatie past bij uw verbruik.</p>
 <h2>Zo haalt u meer uit uw eigen stroom</h2>
 <ul><li><b>Gebruik overdag meer.</b> Was- en vaatwasser, of het opladen van een elektrische auto, kunt u op zonnige momenten laten draaien.</li><li><b>Kies de juiste omvang.</b> Niet zoveel mogelijk panelen, maar wat bij uw verbruik past.</li><li><b>Overweeg een thuisbatterij.</b> Die bewaart uw overschot voor de avond.</li><li><b>Kijk naar uw energiecontract.</b> Let op terugleverkosten en de vergoeding voor teruglevering.</li></ul>
 <h2>Heeft u al zonnepanelen?</h2>
 <p>Dan verandert er per 1 januari 2027 iets voor u, maar uw panelen blijven waardevol. In een gratis gesprek kijken we of een batterij of een aanpassing in uw verbruik zinvol is.</p>
 <p style="margin-top:28px"><a class="btn btn-amber" href="#offerte">Vraag gratis advies aan</a></p>
 <p style="font-size:14px;color:var(--mute);margin-top:34px">Bronnen: <a href="https://www.rijksoverheid.nl/themas/klimaat-milieu-en-natuur/energie-thuis/salderingsregeling" rel="noopener" style="text-decoration:underline">Rijksoverheid, salderingsregeling</a>. Algemene informatie; uw persoonlijke situatie kan afwijken.</p>""")
 + related_block(("verandert", "subsidie", "rendabel", "zinvol")) + faq_block(FAQ[:2] + FAQ[6:7]) + offer_block() + cta_block(),
 FAQ[:2] + FAQ[6:7])

pages["/werkwijze/"] = ("Onze werkwijze | Van advies tot oplevering | ZonnepanelenNu",
 "In drie stappen naar uw zonnedak: adviesgesprek aan huis, installatie door gecertificeerde vakmannen en service en onderhoud.",
 hero("Van eerste gesprek tot <span>oplevering</span>", "Duidelijk, persoonlijk en zonder verrassingen. Zo werken wij.", img(8), "Werkwijze", "Onze werkwijze", pcbar=False)
 + steps_block() + how_block(15, True) + faq_block(FAQ[2:6], False) + offer_block() + cta_block(), FAQ[2:6])

pages["/over-ons/"] = ("Over ons | ZonnepanelenNu",
 "Al meer dan 10 jaar leggen wij zonnepanelen op woningen en bedrijfspanden. Kwaliteit, A-merken en persoonlijk advies aan huis.",
 hero("Mensen die uw dak <span>zelf</span> aanpakken", "Al meer dan 10 jaar realiseren we zonnepaneleninstallaties voor woningen en bedrijven.", img(12), "Over ons", "Over ZonnepanelenNu", pcbar=False)
 + prose(f"""<span class="eyebrow">Ons verhaal</span><h2>Kwaliteit staat bij ons hoog in het vaandel</h2>
 <p>Wij werken uitsluitend met A-merken. Daarnaast vinden we persoonlijke service belangrijk: we komen altijd langs om de situatie te bekijken en uw wensen te bespreken voordat we een offerte uitbrengen.</p>
 <p>Dat doen we efficiënt, waardoor de installatie binnen {TIJD} na akkoord kan worden uitgevoerd. En als er na de oplevering iets is, bent u niet met een servicenummer aan het bellen: u belt ons.</p>
 <ul><li>Persoonlijk advies aan huis is standaard</li><li>Ruim assortiment aan merken</li><li>Altijd de beste service en garantie</li><li>Monitoring via smartphone inbegrepen</li></ul>""")
 + stats_block() + why_block() + reviews_block(6, True) + brands_block() + offer_block() + cta_block())

pages["/projecten/"] = ("Projecten | Recent opgeleverde zonnepanelen | ZonnepanelenNu",
 "Bekijk onze recent opgeleverde projecten: zonnepanelen en thuisbatterijen op woningen en bedrijfspanden.",
 hero("Recent <span>opgeleverd</span>", "Een greep uit onze laatste installaties.", img(14), "Projecten", "Projecten", pcbar=False)
 + f"""<section><div class="wrap">{head("Projecten", "Benieuwd wat wij voor u kunnen doen?")}<div class="gal">"""
 + "".join(f'<figure class="{c} reveal"><img src="{img(i, True)}" alt="{t}" loading="lazy"><figcaption>{t}</figcaption></figure>' for i, c, t in
           [(2, "tall", "Zwarte panelen rond dakkapel"), (22, "", "Plat dak, opstelling"), (14, "", "Installatie op plat dak"), (6, "wide", "Bedrijfspand"),
            (7, "", "Pannendak, all-black"), (35, "tall", "AEG-thuisbatterij"), (30, "", "Woning met dakramen"), (4, "", "Rijtjeswoningen"),
            (28, "wide", "Woning met zonnepanelen"), (18, "", "Panelen rond dakramen"), (26, "wide", "Woning in de zon")])
 + "</div></div></section>" + reviews_block(3, True) + offer_block("Uw dak als volgend project?") + cta_block())

cats = ["Alle"] + sorted({p["cat"] for p in POSTS})
chips = "".join(f'<button class="chip{" on" if c == "Alle" else ""}" data-chip="{e(c)}">{e(c)}</button>' for c in cats)
pages["/blog/"] = ("Blog | Alles over zonnepanelen en thuisbatterijen | ZonnepanelenNu",
 "Kosten, opbrengst, plaatsing, thuisbatterijen en de salderingsregeling: lees de antwoorden van ZonnepanelenNu in gewone taal.",
 hero("Kennis over <span>zonnepanelen</span>", "Kosten, opbrengst, plaatsing en thuisbatterijen, in gewone taal.", img(7), "Blog", "Blog", pcbar=False)
 + f"""<section><div class="wrap"><div class="filter reveal"><input type="search" data-filter placeholder="Zoek in {len(POSTS)} artikelen…" aria-label="Zoek in artikelen"><div class="chips">{chips}</div></div>
 <div class="grid3" id="posts">{"".join(post_card(p) for p in POSTS)}</div><p id="nores" class="lead" style="display:none;margin-top:30px">Geen artikelen gevonden. Probeer een ander zoekwoord of bel ons: {TEL}.</p></div></section>"""
 + offer_block() + cta_block())

pages["/contact/"] = ("Contact | Gratis offerte aanvragen | ZonnepanelenNu",
 f"Vraag een gratis offerte aan of neem contact op met ZonnepanelenNu. Bel {TEL}.",
 hero("Neem <span>contact</span> op", "Zonnepanelen op uw huis of bedrijf? We ontzorgen u in het hele proces, van installatie tot garantie.", img(15), "Contact", "Contact", pcbar=False)
 + f"""<section style="padding-bottom:0"><div class="wrap"><div class="gl">
 <div class="reveal"><h3>Bel ons</h3><p><a href="tel:{TEL_HREF}" style="font-weight:700;color:var(--navy);font-size:20px">{TEL}</a><br>Voor een snelle vraag of afspraak.</p></div>
 <div class="reveal"><h3>Mail ons</h3><p><a href="mailto:{MAIL}" style="font-weight:700;color:var(--navy)">{MAIL}</a><br>We reageren zo snel mogelijk.</p></div>
 <div class="reveal"><h3>Bezoek ons</h3><p>{STRAAT}<br>{PLAATS}<br>KvK {KVK}</p></div></div></div></section>"""
 + offer_block("Vraag een gratis offerte aan") + faq_block(alt=True) + reviews_block(3) + cities_block(), FAQ)

pages["/bedankt/"] = ("Bedankt voor uw aanvraag | ZonnepanelenNu", "We nemen zo snel mogelijk contact met u op.",
 f'<section><div class="wrap" style="text-align:center;padding:70px 0"><span class="eyebrow">Aanvraag ontvangen</span><h1 style="margin-bottom:16px">Bedankt voor uw aanvraag ✓</h1><p class="lead" style="margin:0 auto 28px">We nemen zo snel mogelijk contact met u op om een afspraak in te plannen. Wilt u nu al iets kwijt? Bel ons gerust op {TEL}.</p><a class="btn btn-blue" href="/">Terug naar home</a></div></section>')

CITY_IMG = [30, 1, 4, 28, 29, 26, 16, 19, 32]
CITY_TXT = {
 "Gouda": ("Ons kantoor zit in Gouda", "Onze vestiging ligt aan de Marconistraat in Gouda. In de oudere wijken zien we vaak kleinere schuine daken met dakkapellen en dakramen: daar bepaalt een goede indeling van de panelen hoeveel u opwekt."),
 "Rotterdam": ("Zonnepanelen op Rotterdamse daken", "In Rotterdam zijn veel daken plat. Bij een plat dak kiezen we een opstelling (zuid of oost-west) die het meeste uit de beschikbare ruimte haalt, en we letten op dakbedekking en windbelasting. Ook voor bedrijfspanden in de regio Rotterdam denken we graag mee."),
 "Den Haag": ("Zonnepanelen in Den Haag", "In Den Haag staan veel rijtjeswoningen en oudere panden. Bij sommige straten en gebouwen gelden regels voor beschermd stadsgezicht of welstand. Dat zoeken we vooraf voor u uit, zodat u niet voor verrassingen komt te staan."),
 "Zoetermeer": ("Zonnepanelen in Zoetermeer", "Zoetermeer is voor een groot deel na 1970 gebouwd, met veel rijtjeswoningen en schuine daken met dakramen. Wij plaatsten hier onder meer een installatie van 12 zonnepanelen. Die ervaring nemen we mee in uw advies."),
 "Alphen aan den Rijn": ("Zonnepanelen in Alphen aan den Rijn", "Ook in Alphen aan den Rijn en omgeving komen we bij u langs voor een advies aan huis. We kijken naar uw dak, de meterkast en uw verbruik, en rekenen door wat een installatie u oplevert."),
 "Bodegraven": ("Zonnepanelen in Bodegraven", "Wilt u zonnepanelen of een thuisbatterij in Bodegraven? We komen bij u langs voor een adviesgesprek, rekenen de opbrengst en besparing door en regelen de installatie."),
 "Nieuwerkerk aan den IJssel": ("Zonnepanelen in Nieuwerkerk aan den IJssel", "In Nieuwerkerk aan den IJssel bestaan veel woningen uit rijtjeshuizen met een schuin dak. We kijken naar oriëntatie en schaduw en stellen een installatie voor die past bij uw verbruik."),
 "Waddinxveen": ("Zonnepanelen in Waddinxveen", "Voor huiseigenaren en ondernemers in Waddinxveen verzorgen we advies, installatie en service. Wij komen bij u langs, ook als u nog twijfelt of uw dak geschikt is."),
 "Woerden": ("Zonnepanelen in Woerden", "Wilt u zonnepanelen in Woerden? We beoordelen uw dak, rekenen de opbrengst voor u door en leggen de panelen. Ook voor een thuisbatterij bent u bij ons aan het juiste adres."),
}
for k, c in enumerate(CITIES):
    h2, txt = CITY_TXT[c]
    near = "".join(f'<a href="/{slug(x)}/">Zonnepanelen {x}</a>' for x in CITIES if x != c)
    cfaq = [(f"Werken jullie ook in {c}?", f"Ja. We plaatsen zonnepanelen en thuisbatterijen in {c} en omgeving. Vraag een gratis dakscan aan om te zien wat er op uw dak kan.")] + FAQ[:4]
    pages[f"/{slug(c)}/"] = (f"Zonnepanelen {c} | Installateur in {c} | ZonnepanelenNu",
     f"Zonnepanelen of thuisbatterij in {c}? ZonnepanelenNu: gecertificeerd, A-merken en advies aan huis. Vraag een gratis dakscan aan.",
     hero(f"Zonnepanelen in <span>{c}</span>", f"Zonnepanelen of een thuisbatterij in {c} laten plaatsen? Wij komen bij u langs voor advies, en leggen ze zelf.", img(CITY_IMG[k]), f"Zonnepanelen {c}", f"Zonnepanelen {c}")
     + trust() + services_block()
     + prose(f"""<span class="eyebrow">Lokaal</span><h2>{h2}</h2>
     <p>{txt}</p>
     <p>Kwaliteit staat centraal: we werken alleen met A-merken en komen altijd langs om de situatie te beoordelen voordat we een offerte opstellen. Zo kan de installatie binnen {TIJD} na akkoord worden uitgevoerd.</p>
     <ul><li>Gratis dakscan en advies aan huis in {c}</li><li>5 jaar garantie op de installatie, tot 25 jaar op de panelen</li><li>Onderhoud en storingsservice na oplevering</li></ul>""")
     + reviews_block(3, True) + faq_block(cfaq) + offer_block()
     + f'<section class="alt"><div class="wrap">{head("Andere plaatsen", "Zonnepanelen en thuisbatterijen in andere plaatsen")}<div class="cities">{near}</div></div></section>' + cta_block(), cfaq)

pages["/zonnepanelen-offerte-aanvragen/"] = ("Zonnepanelen offerte aanvragen | Gratis en vrijblijvend | ZonnepanelenNu",
 f"Vraag een gratis offerte aan voor zonnepanelen. Advies aan huis, offerte binnen 24 uur na het gesprek en 5 jaar garantie. Bel {TEL}.",
 hero("Vraag uw <span>offerte</span> aan", "Gratis en vrijblijvend. U ontvangt een offerte op maat met de verwachte opbrengst voor uw dak.", img(1), "Offerte aanvragen", "Offerte aanvragen")
 + trust() + steps_block() + reviews_block(3, True) + offer_block("Vraag uw gratis offerte aan") + faq_block(FAQ[:5], False) + cta_block(), FAQ[:5])

pages["/zonnepanelen-laten-installeren-door-zonnepanelennu/"] = ("Zonnepanelen laten installeren | Van advies tot service | ZonnepanelenNu",
 "Zonnepanelen laten installeren door gecertificeerde vakmannen. Advies aan huis, alleen A-merken, 5 jaar installatiegarantie en service na oplevering.",
 hero("Zonnepanelen laten <span>installeren</span>", "Van advies tot oplevering en service: alles door hetzelfde team, met vaste aanspreekpunten.", img(8), "Zonnepanelen laten installeren", "Installatie", pcbar=False)
 + prose(f"""<span class="eyebrow">Wat u van ons mag verwachten</span><h2>Zonnepanelen laten installeren zonder gedoe</h2>
 <p>Een goede installatie begint met kijken: naar uw dak, uw meterkast en uw verbruik. Daarna maken we een offerte op maat. Na akkoord plannen we de installatie en leggen onze gecertificeerde vakmannen de panelen. Het afval nemen we mee.</p>
 <ul><li>Advies aan huis, gratis en vrijblijvend</li><li>Alleen A-merken, met tot 25 jaar fabrieksgarantie</li><li>5 jaar garantie op onze installatie</li><li>Monitoring via uw smartphone inbegrepen</li><li>Installatie binnen {TIJD} na akkoord</li></ul>""")
 + steps_block() + gallery_block(GAL_THUIS, False) + faq_block() + offer_block() + cta_block(), FAQ)

# ------------------------------------------------------------------ artikelen, juridisch, 404
PAGE_OPTS = {}
KNOWN = set(pages) | {q["path"] for q in POSTS} | {f"/{x['slug']}/" for x in LEGAL}
ALLOWED = {"h2", "h3", "h4", "p", "ul", "ol", "li", "strong", "em", "a", "br", "table", "thead", "tbody", "tr", "th", "td", "blockquote"}
RENAME = {"h1": "h2", "h5": "h4", "h6": "h4", "b": "strong", "i": "em"}


def rewrite(h):
    if h.startswith(SITE):
        path = h[len(SITE):].split("?")[0].split("#")[0] or "/"
        if not path.endswith("/"):
            path += "/"
        return path if path in KNOWN else h
    return h


class Clean(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.o, self.skip = [], 0

    def handle_starttag(self, t, a):
        if t in ("script", "style"):
            self.skip += 1
            return
        if self.skip:
            return
        t = RENAME.get(t, t)
        a = dict(a)
        if t == "img":
            fn = os.path.basename((a.get("src") or "").split("?")[0])
            if os.path.exists(os.path.join(ROOT, "assets", "img", "blog", fn)):
                self.o.append(f'<img src="/assets/img/blog/{fn}" alt="{e(a.get("alt") or "")}" loading="lazy">')
            return
        if t not in ALLOWED:
            return
        if t == "br":
            self.o.append("<br>")
        elif t == "a":
            h = rewrite(a.get("href", ""))
            self.o.append(f'<a href="{e(h)}"{" rel=noopener" if h.startswith("http") else ""}>')
        else:
            self.o.append(f"<{t}>")

    def handle_endtag(self, t):
        if t in ("script", "style"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        t = RENAME.get(t, t)
        if t in ALLOWED and t != "br":
            self.o.append(f"</{t}>")

    def handle_data(self, d):
        if not self.skip:
            self.o.append(e(d, quote=False))


def clean(h, title=""):
    c = Clean()
    c.feed(h)
    out = "".join(c.o)
    out = re.sub(r"<p>(\s|<br>)*</p>", "", out)
    m = re.match(r"\s*<h2>(.*?)</h2>", out, re.S)
    norm = lambda t: re.sub(r"\W+", "", plain(t).lower())
    if m and norm(m.group(1)) == norm(title):
        out = out[m.end():]
    return out.strip()


def small_hero(crumbs, eyebrow, h1, image):
    return f"""<section class="hero hero-s" style="--hero:url('{image}')"><div class="wrap"><div class="hcard"><div class="crumbs">{crumbs}</div><span class="eyebrow">{eyebrow}</span><br><h1>{h1}</h1></div></div></section>"""


HERO_IMGS = {"Thuisbatterij": [35, 36, 9, 11], "Kosten & rendement": [1, 30, 4], "Advies & aanschaf": [8, 12, 15], "Zonnepanelen": [7, 22, 14, 18]}
import re as _re


def with_toc(body):
    heads = _re.findall(r"<h2>(.*?)</h2>", body)
    ids = []
    for h in heads:
        ids.append(_re.sub(r"[^a-z0-9]+", "-", plain(h).lower()).strip("-"))
    it = iter(ids)
    body = _re.sub(r"<h2>(.*?)</h2>", lambda m: f'<h2 id="{next(it)}">{m.group(1)}</h2>', body)
    toc = "".join(f'<li><a href="#{i}">{plain(h)}</a></li>' for i, h in zip(ids, heads))
    return body, (f'<nav class="toc" aria-label="Inhoud"><b>In dit artikel</b><ol>{toc}</ol></nav>' if len(heads) >= 3 else "")


for i, q in enumerate(POSTS):
    rel_slugs = [x for x in q["rel"] if x in BY_SLUG and x != q["slug"]]
    rel = [BY_SLUG[x] for x in rel_slugs][:3]
    if len(rel) < 3:
        rel += [x for x in sorted((x for x in POSTS if x is not q and x not in rel), key=lambda x: len(q["w"] & x["w"]), reverse=True)][:3 - len(rel)]
    short = q["title"] if len(q["title"]) <= 48 else q["title"][:45].rsplit(" ", 1)[0] + "…"
    hero_img = HERO_IMGS[q["cat"]][i % len(HERO_IMGS[q["cat"]])]
    body_html, toc = with_toc(q["html"])
    keys = "".join(f"<li>{k}</li>" for k in q["keys"])
    faq_html = "".join(f"<details><summary>{fq}</summary><p>{fa}</p></details>" for fq, fa in q["faq"])
    body = (small_hero(f'<a href="/">Home</a> / <a href="/blog/">Blog</a> / {e(short)}', f'{e(q["cat"])} · {q["mins"]} min leestijd', e(q["title"]), img(hero_img))
            + f"""<section><div class="wrap art"><article class="prose">
 <p class="byline">Door het team van ZonnepanelenNu · Bijgewerkt op {nl_date(q["modified"])}</p>
 <div class="keys"><h2>De kern in het kort</h2><ul>{keys}</ul></div>{toc}{body_html}
 <h2 id="veelgestelde-vragen">Veelgestelde vragen</h2><div class="faqlist">{faq_html}</div>
 <div class="artcta"><h3>Wilt u weten wat dit voor u betekent?</h3><p>Vraag gratis advies aan. We komen bij u langs en rekenen het voor u door, met uw eigen verbruik en zonder verplichtingen.</p><a class="btn btn-amber" href="#offerte">Gratis advies</a></div>
 <div class="authorbox"><div class="av">Z</div><div><b>Team ZonnepanelenNu</b><small>Advies en installatie van zonnepanelen en thuisbatterijen. Cijfers in dit artikel zijn indicatief en kunnen afwijken per situatie.</small></div></div></article>
 <aside class="side"><div class="sidecard"><h3>Gratis advies</h3><p>Weten of een thuisbatterij of zonnepanelen bij u passen? Wij komen bij u langs voor een advies op maat.</p><a class="btn btn-amber" href="#offerte">Vraag advies aan</a><a class="btn btn-line" href="tel:{TEL_HREF}">{ic("phone")} {TEL}</a><p class="hnote2">{stars()} {RATING} Google-reviews</p></div></aside></div></section>"""
            + f'<section class="alt"><div class="wrap">{head("Meer lezen", "Gerelateerde artikelen")}<div class="grid3">{"".join(post_card(x) for x in rel)}</div></div></section>'
            + offer_block() + cta_block())
    pages[q["path"]] = (f'{q["title"]} | ZonnepanelenNu', q["desc"], body, q["faq"])
    PAGE_OPTS[q["path"]] = {"og": img(hero_img), "extra": [{
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": q["title"], "datePublished": q["date"],
        "dateModified": q["modified"], "mainEntityOfPage": f"{SITE}{q['path']}", "image": SITE + img(hero_img),
        "author": {"@type": "Organization", "name": "ZonnepanelenNu"},
        "publisher": {"@type": "Organization", "name": "ZonnepanelenNu B.V.", "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo.png"}}}]}

for x in LEGAL:
    path = f"/{x['slug']}/"
    title = html.unescape(x["title"])
    body = (small_hero(f'<a href="/">Home</a> / {e(title)}', "Juridisch", e(title), img(7))
            + f'<section><div class="wrap"><div class="prose">{clean(x["html"], title)}</div></div></section>')
    pages[path] = (f"{title} | ZonnepanelenNu", f"{title} van ZonnepanelenNu B.V., KvK {KVK}.", body)

pages["/404.html"] = ("Pagina niet gevonden | ZonnepanelenNu", "Deze pagina bestaat niet (meer).",
 f'<section><div class="wrap" style="text-align:center;padding:70px 0"><span class="eyebrow">404</span><h1 style="margin-bottom:16px">Deze pagina bestaat niet (meer)</h1><p class="lead" style="margin:0 auto 28px">Mogelijk is de link verouderd. Ga naar de homepage, lees onze artikelen of bel ons op {TEL}.</p><a class="btn btn-blue" href="/">Naar home</a> <a class="btn btn-line" href="/blog/">Naar het blog</a></div></section>')
PAGE_OPTS["/404.html"] = {"noindex": True}
PAGE_OPTS["/bedankt/"] = {"noindex": True}


def write(path, content):
    if path.endswith(".html"):
        with open(os.path.join(ROOT, path.lstrip("/")), "w", encoding="utf-8") as f:
            f.write(content)
        return
    d = ROOT if path == "/" else os.path.join(ROOT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    import datetime
    today = datetime.date.today().isoformat()
    for p, v in pages.items():
        title, desc, body = v[0], v[1], v[2]
        faq = v[3] if len(v) > 3 else None
        o = PAGE_OPTS.get(p, {})
        out = layout(p, title, desc, body, faq, og=o.get("og"), extra=o.get("extra"), noindex=o.get("noindex", False))
        out = re.sub(r'<span class="eyebrow">.*?</span>(<br>)?', '', out)   # sitebreed: geen subkopjes (eyebrows) boven de titels
        if 'id="offerte"' not in out:   # pagina zonder formulier: knoppen naar het formulier op /contact/
            out = out.replace('href="#offerte"', 'href="/contact/#offerte"')
        write(p, out)
    urls = [p for p in pages if not PAGE_OPTS.get(p, {}).get("noindex")]
    mod = {q["path"]: q["modified"] or q["date"] for q in POSTS}
    sm = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{mod.get(p, today)}</lastmod></url>" for p in sorted(urls))
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>')
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\nDisallow: /bedankt/\n\nSitemap: {SITE}/sitemap.xml\n")

    # oude artikelmappen weghalen (die gaan via redirect naar de nieuwe URL)
    for old in REDIRECTS:
        d = os.path.join(ROOT, old.strip("/"))
        if os.path.isdir(d) and old.strip("/") in OLD_POSTS:
            shutil.rmtree(d)
    vj = {"trailingSlash": True,
          "redirects": [{"source": k, "destination": v, "permanent": True} for k, v in sorted(REDIRECTS.items())],
          "headers": [{"source": "/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]}]}
    open(os.path.join(ROOT, "vercel.json"), "w", encoding="utf-8").write(json.dumps(vj, indent=2, ensure_ascii=False) + "\n")
    open(os.path.join(ROOT, "redirects.csv"), "w", encoding="utf-8").write(
        "bron,doel,type\n" + "".join(f"{SITE}{k},{SITE}{v},301\n" for k, v in sorted(REDIRECTS.items())))
    print(f"{len(pages)} pagina's gebouwd ({len(POSTS)} artikelen), {len(urls)} in sitemap")
