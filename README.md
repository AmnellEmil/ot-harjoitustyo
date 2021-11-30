# Miinaharavatyyppinen peli
Sovellus on miinaharavatyyppinen peli, jossa tulisi olla samat perus toiminnot kuten originaalipelissä.

### Linkki vaatimusmäärittelyn dokumenttiin: 
https://github.com/AmnellEmil/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md

### Linkki työaikakirjanpitoon: 
https://github.com/AmnellEmil/ot-harjoitustyo/blob/master/dokumentaatio/Ty%C3%B6naikakirjanpito.txt

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
poetry run invoke start
``` 

### Testaus
Sovellusta voi testata komennolla:
```bash
poetry run invoke test
```

### Testikattavuus 
Testikattavuusraportin voi generoida komennolla:
```bash
poetry run invoke coverage-report
```
Raportti generoituu _htmlcov_-hakemistoon.

### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:`
```bash
poetry run invoke lint
```



