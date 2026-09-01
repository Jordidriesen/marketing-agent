---
name: supermarkt-prijsanalyse
description: >
  Analyseer en vergelijk wekelijkse promoties en prijzen van Belgische supermarkten Lidl, Albert Heijn (AH) en Jumbo. Gebruik deze skill wanneer de gebruiker vraagt naar: de beste deals van de week, goedkoopste producten, promo-vergelijkingen, welke winkel het voordeligst is voor een specifiek product, weekaanbiedingen, folder-analyse, supermarktpromoties, of wanneer ze vragen "wat is in promo bij Lidl/AH/Jumbo?", "waar is X het goedkoopst?", "wat zijn de beste deals deze week?", "vergelijk de folders", of "beste value deals". Triggert ook bij vragen als "moet ik naar Lidl of AH gaan voor X?" en elke vraag over boodschappen doen op een budget in België. Gebruik altijd de ACTUELE folder van deze week — haal live data op, gebruik nooit verouderde of gecachte informatie.
---

# Supermarkt Prijsanalyse — België (Lidl, AH, Jumbo)

## Doel
Wekelijkse promoties en prijzen scrapen, analyseren en vergelijken van Belgische supermarkten, met als output: beste value deals, laagste prijs per product, en een gerangschikte aanbevelinglijst. Altijd live data — nooit op geheugen vertrouwen voor prijzen of promo's.

## Gezinscontext (standaard)
- 2 volwassenen + 2 kinderen (3 en 5 jaar)
- Doel: voedseluitgaven verlagen + verspilling minimaliseren
- Budget-gedreven keuzes: promo's op basisproducten hebben prioriteit

---

## Bronnen per winkel

### Lidl België
- **Officiële folder:** https://www.lidl.be/c/nl-BE/folders-magazines/s10008101
- **Promoties overzicht:** https://www.lidl.be/nl-BE/promoties
- **Aggregator (scrapebaar):** https://www.promotiez.be/winkels/lidl/folders-promoties
- **Aggregator 2:** https://www.kimbino.be/lidl/
- **Aggregator 3:** https://winkelfolders.be/lidl/
- **Folder geldigheid:** Maandag t/m zondag — nieuwe folder verschijnt vrijdag/weekend

### Albert Heijn België
- **Officiële Bonusfolder:** https://www.ah.be/bonus/folder
- **Alle promoties:** https://www.ah.be/bonus
- **Acties pagina:** https://www.ah.be/acties
- **Aggregator:** https://www.promotiez.be/winkels/albert-heijn/folders-promoties
- **Folder geldigheid:** Woensdag t/m dinsdag — nieuwe folder verschijnt woensdag

### Jumbo België
- **Officiële aanbiedingen:** https://www.jumbo.com/nl-be/aanbiedingen
- **Homepagina BE:** https://www.jumbo.com/nl-be
- **Folder PDF (patroon):** https://www.jumbo.com/dam/belgie/2024/folder/2026/Jumbo-BE-Instore-Folder-2026-Week-[XX].pdf
  - Vervang [XX] door het huidige weeknummer (bijv. Week-25 voor week 25)
  - Probeer ook [XX-1] als de huidige week nog niet online staat
- **Aggregator:** https://www.promotiez.be/winkels/jumbo/folders-promoties
- **Folder geldigheid:** Woensdag t/m dinsdag — nieuwe folder verschijnt woensdag
- **Let op:** Jumbo heeft slechts ~30 winkels in België (Limburg, Kempen-regio). Controleer of de gebruiker een Jumbo in de buurt heeft voor je het meeneemt in de analyse.

---

## Werkwijze (stap voor stap)

### Stap 0 — Bepaal de actuele week
Gebruik de huidige datum om:
1. Het weeknummer te berekenen
2. Te bepalen welke folders geldig zijn (Lidl start maandag, AH/Jumbo starten woensdag)
3. De juiste Jumbo PDF-URL te construeren

### Stap 1 — Bepaal scope
Vraag indien niet duidelijk:
- Gaat het om een **specifiek product** of een **algemeen weekoverzicht**?
- Alle drie winkels of een subset?
- Focus op food (standaard voor dit gezin) of ook non-food?

### Stap 2 — Haal live folderdata op

**Volgorde van voorkeur per winkel:**

#### Lidl
```
1. web_fetch https://www.lidl.be/c/nl-BE/folders-magazines/s10008101
2. Als leeg/JS-geblokkeerd: web_fetch https://www.promotiez.be/winkels/lidl/folders-promoties
3. Fallback: web_fetch https://www.kimbino.be/lidl/
```

#### Albert Heijn
```
1. web_fetch https://www.ah.be/bonus
2. Als leeg/JS-geblokkeerd: web_fetch https://www.promotiez.be/winkels/albert-heijn/folders-promoties
3. Fallback: web_fetch https://www.ah.be/acties
```

#### Jumbo
```
1. web_fetch https://www.jumbo.com/nl-be/aanbiedingen
2. PDF proberen: https://www.jumbo.com/dam/belgie/2024/folder/2026/Jumbo-BE-Instore-Folder-2026-Week-[XX].pdf
3. Fallback: web_fetch https://www.promotiez.be/winkels/jumbo/folders-promoties
```

**Als Firecrawl beschikbaar is:** gebruik `firecrawl_scrape` in plaats van `web_fetch` — dat levert betere resultaten op voor JS-zware sites zoals lidl.be en ah.be.

**Als scraping volledig mislukt voor een winkel:** zeg dit eerlijk, geef de directe URL mee, en werk verder met de winkels die wel beschikbaar zijn.

### Stap 3 — Verwerk de data

Extraheer per product:
- Productnaam + variant/gramgewicht
- Normale prijs (indien vermeld)
- Actieprijs
- Kortingspercentage (bereken zelf als niet vermeld: `(normaal - actie) / normaal * 100`)
- Type promo (bijv. "2+1 gratis", "2e halve prijs", directe korting)
- Effectieve korting voor "2+1 gratis" = 33,3%, "2e halve prijs" = 25%
- Winkel
- Geldigheid van t/m

### Stap 4 — Analyseer met gezinsfilter

**Prioriteer producten die:**
- Geschikt zijn voor kinderen van 3 en 5 jaar (basisingrediënten, niet te exotisch)
- Weinig verspilling geven (producten die heel het gezin eet)
- Basis zijn voor meerdere gerechten (kip, gehakt, pasta, rijst, eieren, groenten)
- Lang houdbaar of diepvriespbaar zijn (waarde is ook houdbaarheid)

**Best Value Score berekenen:**
- Hoogste kortingspercentage = meest punten
- Basisproducten (vlees, vis, groenten, zuivel, pasta, rijst, eieren) krijgen prioriteit boven snoep/snacks
- Grote verpakkingen met lage prijs per 100g scoren hoger dan kleine verpakkingen

**Deals categoriseren:**
1. 🏆 **Top deals** — >40% korting op dagelijkse producten
2. ✅ **Goede deals** — 20-40% korting
3. 💡 **Aandacht waard** — <20% korting maar op dure/kwalitatieve basisproducten

### Stap 5 — Output

**Formaat voor algemeen weekoverzicht:**

```
## 🛒 Supermarktdeals — Week [X] ([datum t/m datum])
*Data opgehaald op [datum/tijdstip]*

### 🏆 Top picks deze week (gezinsgericht)

| Product | Winkel | Actieprijs | Korting | Geldig t/m |
|---------|--------|------------|---------|------------|
| ...     | Lidl   | €X.XX      | -XX%    | ...        |

### Per winkel — highlight

**Lidl** (geldig ma-zo): beste voor [categorie]
**AH** (geldig wo-di): beste voor [categorie]
**Jumbo** (geldig wo-di): beste voor [categorie] *(check of Jumbo in buurt)*

### 💡 Verspillingsarm inkopen
Producten die in meerdere gerechten bruikbaar zijn én nu in promo:
- [product]: gebruik in [gerecht 1] en [gerecht 2]

### 💡 Slimme winkelstop
Als je maar 1 winkel doet: ga naar [winkel] want [reden]
Als je 2 winkels combineert: [winkel A] voor [X, Y] + [winkel B] voor [Z]
```

**Formaat voor productspecifieke vergelijking:**

```
## Prijsvergelijking: [Product]
*Live data — [datum]*

| Winkel | Prijs   | In promo? | Korting | Type deal   |
|--------|---------|-----------|---------|-------------|
| Lidl   | €X.XX   | ✅ Ja     | -XX%    | Directe korting |
| AH     | €X.XX   | ❌ Nee    | —       | —           |
| Jumbo  | €X.XX   | ✅ Ja     | -XX%    | 2+1 gratis  |

**Goedkoopst deze week:** [Winkel] — €X.XX
**Beste value:** [uitleg, bijv. "Jumbo 2+1 is beter als je 3 nodig hebt"]
```

---

## Koppeling met weekmenu-planner

Als de supermarkt-prijsanalyse gecombineerd wordt met de weekmenu-planner:
- Geef aan welke promo-ingrediënten die week ideaal zijn als basis voor het menu
- Voorbeeld: "Kip in promo bij Lidl → voorstel voor teriyaki, curry en gebakken rijst met kip"
- Koppel aanbiedingen expliciet aan gerechten: verminder de kloof tussen "wat is goedkoop" en "wat eet ik"

---

## Vaste herinneringen

- **Nooit verouderde data gebruiken** — altijd live ophalen
- Lidl folder: start maandag, nieuwe folder elk weekend online → check altijd of je de folder van de lopende week hebt
- AH Bonusfolder: start woensdag, verschijnt woensdag → op maandag/dinsdag nog de folder van vorige week geldig bij AH
- Jumbo BE: soms andere deals dan Jumbo NL — gebruik altijd de /nl-be/ URL
- Lidl "Delicieux" = premiumlijn, minder relevant voor budget-focus
- AH huismerk = structureel goedkoper, ook buiten promo
- Prijzen en promo's kunnen per filiaal verschillen — vermeld dit als disclaimer
