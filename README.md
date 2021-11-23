# Miinaharavatyyppinen peli
Sovellus on miinaharavatyyppinen peli, jossa tulisi olla samat perus toiminnot kuten originaalipelissä.

### Linkki vaatimusmäärittelyn dokumenttiin: 
https://github.com/AmnellEmil/ot-harjoitustyo/blob/master/laskarit/viikko1/vaatimusmaarittely.md

### Linkki työaikakirjanpitoon: 
https://github.com/AmnellEmil/ot-harjoitustyo/blob/master/laskarit/viikko1/Ty%C3%B6naikakirjanpito.txt

## Ongelmatilanne
Tarvittujen pakettien asennus ei toimi poetryn kautta. Poetry on kyllä asennettu oikein ja poetryyn on asennettu python3, pytest, invoke ja coverage, mutta en pysty asentamaan poetryyn numpy tai random pakkauksia, joten poetryn invoke kommennot kuten start, test ja coverage-report eivät toimi poetryn virtuaaliympäristössä koska pakkauksia numpy ja random ei löydy. Kuitenkin virtuaaliympäristön ulkopuolella sovelluksen voi käynnistää ja sillä on yksi testi tällä hetkellä.

## Asennus
Riippuvuudet asennetaan komennolla:
```bash
poetry install
```

## Komentorivitoiminnot
### Ohjelman käynnistys
Sovelluksen voi käynnistää komennolla:
```bash
python3 src/Board.py
``` 

### Testaus
Sovellusta voi testata komennolla:
```bash
pytest src
```

### Testikattavuus (jos numpy ja random toimisivat poetryn kautta)
Testikattavuusraportin voi generoida komennolla:
```bash
poetry run invoke coverage-report
```
Raportti generoituu _htmlcov_-hakemistoon.
