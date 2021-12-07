# Miinaharavatyyppinen peli
Sovellus on miinaharavatyyppinen peli, jossa tulisi olla samat perus toiminnot kuten originaalipelissä.

### Linkki vaatimusmäärittelyn dokumenttiin: 
https://github.com/AmnellEmil/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md

### Linkki työaikakirjanpitoon: 
https://github.com/AmnellEmil/ot-harjoitustyo/blob/master/dokumentaatio/Ty%C3%B6naikakirjanpito.txt

### Linkki arkitektuuriin:
https://github.com/AmnellEmil/ot-harjoitustyo/blob/master/dokumentaatio/arkitektuuri.md

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



