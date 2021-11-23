# Miinaharavatyyppinen peli
Sovellus on miinaharavatyyppinen peli, jossa tulisi olla samat perus toiminnot kuten originaalipelissä.

## Linkki vaatimusmäärittelyn dokumenttiin: 
https://github.com/AmnellEmil/ot-harjoitustyo/blob/master/laskarit/viikko1/vaatimusmaarittely.md

##Linkki työaikakirjanpitoon: 
https://github.com/AmnellEmil/ot-harjoitustyo/blob/master/laskarit/viikko1/Ty%C3%B6naikakirjanpito.txt

##Ongelmatilanne
Tarvittujen pakettien asennus ei toimi poetryn kautta. Poetry on kyllä asennettu oikein ja poetryyn on asennettu python3, pytest, invoke ja coverage, mutta en pysty asentamaan poetryyn numpy tai random pakkauksia, joten poetryn invoke kommennot kuten start, test ja coverage-report eivät toimi.

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
