# Käyttöohje
Lataa projekti release sivulta. Lataa source code zip tiedosto.

## Ohjelman käynnistäminens
Riippuvuudet asennetaan komennolla:
```bash
poetry install
```

Sovelluksen voi tämän jälkeen  käynnistää komennolla:
```bash
poetry run invoke start
``` 

## Pelaaminen
Sovellus käynnistyy main menu näkymään:

![](./kuvat/main_menu.png)

Tästä näkymästä voi siirtyä play napin kautta näkymään, jossa valitaan miinaharavakentän dimensiot

![](./kuvat/play.png)

Kun on valinnut dimensiot miinaharvapeli aloitetaan start napilla. Peli avautuu uuteen ikkunaan.

Menu näkymästä pääsee myös näkymään, jossa kerrotaan pelin säätimet

![](./kuvat/controls.png)

Lopuksi voi painaa leaderboards nappia ja päästä pelin high score listalle, joka sijaitsee google sheetsissä.

![](./kuvat/leaderboards.png)

Kun voittaa pelin, niin pelaajalla on mahdollisuus antaa nimensä ja lähettää aikansa google sheets leaderboardsille

![](./kuvat/victory.png)
