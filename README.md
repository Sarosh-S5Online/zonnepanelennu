# ZonnepanelenNu – demo (statisch)

Lokaal draaien: `python -m http.server 8130` in deze map (of preview-config `zonnepanelennu`).
Opnieuw bouwen na een wijziging in `build.py` of `content/`: `python build.py`

## Opbouw
- `build.py` – layout + alle pagina-inhoud, schrijft `<slug>/index.html` (= WordPress-permalinks)
- `content/` – 39 blogartikelen + 3 juridische pagina's (van de live site, ongewijzigd)
- `assets/style.css`, `assets/main.js` – stijl en gedrag (formulier, blogfilter, cookiebanner)
- `assets/img/f/` – klantfoto's uit Google-bedrijfsprofiel (webp)
- `sitemap.xml`, `robots.txt`, `404.html` worden gegenereerd

## Pagina's (66)
Home, thuis, zakelijk, thuisbatterij, zonnepanelen-met-batterij-accu-kopen, salderingsregeling-2027 (nieuw),
werkwijze, over-ons, projecten, contact, blog + 39 artikelen, 9 stadspagina's, offerte-aanvragen,
laten-installeren, privacyverklaring, algemene-voorwaarden, cookie-policy, bedankt (noindex), 404.

## Nog te doen vóór live
1. Formulier koppelen: `window.ZNN_FORM = {accessKey: "…"}` (Web3Forms) of WPForms in WordPress.
2. Tracking: GTM/GA4/Ads/Pixel achter de cookiebanner hangen (events `lead_submit`, `consent_update` staan al in `dataLayer`).
3. Klant laten bevestigen: installatietijd (`TIJD`), certificeringen, Abdel (rol/foto), WhatsApp-nummer, stadsteksten.
4. Oude blogartikelen (2024/2025) inhoudelijk actualiseren; ze tonen nu een notitie richting /salderingsregeling-2027/.
5. Redirects: `/zonnepanelen-offerte-010-aanvragen/` (noindex) en oude Elementor-URL's controleren.
6. Google-reviews: `RATING`/`NREV` in `build.py` (nu 4,8 / 43, bron GBP sept 2026) periodiek bijwerken.
7. Daarna: omzetten naar WordPress (Elementor-JSON of hybride thema), zie chat.

## Demo-deploy
`vercel.json` zet `noindex` op de hele demo (canonicals wijzen naar de live domeinnaam). Verwijder die header bij livegang.
