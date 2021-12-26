# Arkkitehtuurikuvaus

# Rakenne
Rakenne on seuraava:
- ui sisältää game loopin ja käyttöliittymään liittyviä asioita
- luokat Minefield, Square ja Board sisältävät sovelluslogiikan
- sheets sisältää yhteyden google sheetsiin ja funktion jolla tulokset lähetetään sinne

## Käyttöliittymä
Käyttöliittymä sisältää 4 erilaista näkymää:
- Main menu
- Pelin asetuksien menu
- Säätimet
- Varsinainen miinaharavapeli

Lisäksi käyttöliittymä sisältää Button luokan ja funktiota jotka piirtävät tekstiä ja ruutuja tietokoneruudulle.

Miinaharvapelillä on erillinen game looppi, muut näkymät ovat samassa loopissa. Näkymien välillä navigoidaan ruudulla olevien nappien avulla ja esc napin avulla. 

## Sovelluslogiikka

### Luokkakaavio
Minefield luokan ainoa tehtävä on generoida oikean kokoinen satunnainen miiharavakenttä ja sen arvot.

Square oliot sisältävät kaiken relevantin tiedon pelin ruudusta kuten sen arvon, jos en on paljastettu, tiedon graaffiesta esityksestä etc. Square olio toimii siltana käyttöliittymän ja sovelluslogiikan välillä.

Board olio on sovelluslogiikan master olio. Se sisältää kentän parametrit, pelin ruudut (Square oliot) ja kaikki sovelluslogiikan funktiot, jotka tarvitaan kun pelaaja klikkaa asioita käyttöliittymässä miinaharavapelin gameloopissa.

![alt text](https://yuml.me/75b3b04d.png)

## Tuloksien talletus google shetsiin
Minulla on käytössä googlen api sheetsille ja driveille. Tämän ja pygsheets pakkauksen avulla miinaharvapelin high score lista toteutuu


## Esimerrki yhdestä toiminnalisuudesta

### Miinaharvapelin kentän generointi
Kun uusi peli aloitetaan, niin satunnainen miinaharvakenttä generoidaan parametrien mukaan. Seuraava kaavio näyttää miten Board olio generoi kentän.

![](./kuvat/sekvenssikaavio.png)

### Ruudun klikkaaminen
Kun klikataan ruutua, niin board olion metodi reveal paljastaa eri määrän ruutuja riippuen siitä mikä arvo klikatulla ruudulla on. Metodi palauttaa klikatun ruudun arvon. Juuri tämän jälkeen pelin koodissa tarkastetaan, jos klikattu ruutu oli pommi, eli palautettu arvo oli -1. Jos näin on, niin board olion lose metodi ajetaan.

![](./kuvat/reveal.png)
