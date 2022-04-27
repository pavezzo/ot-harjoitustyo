# Ohjelmistotekniikan harjoitustyö: 2048 peli
Sovellus on minun versio suositusta 2048 pelistä. Peliä pelataan nuolinäppäimillä. Vaihda main.py UI width ja height sopivaksi omalle näytölle.
## Dokumentaatio
[tuntikirjanpito](https://github.com/pavezzo/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)\
[vaatimusmäärittely](https://github.com/pavezzo/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)\
[changelog](https://github.com/pavezzo/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)\
[arkkitehtuurikuvaus](https://github.com/pavezzo/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Asenna riippuvuudet:
```bash
poetry install
```
2. Alusta tietokanta:
```bash
poetry run invoke initialize
```
3. Käynnistä peli:
```bash
poetry run invoke start
```
## Testaus
Testit suoritetaan komennolla:
```bash
poetry run invoke test
```
Testikattavuusraportin saa komennolla:
```bash
poetry run invoke coverage-report
```
## Pylint
Pylint tarkistukset suoritetaan komennolla:
```bash
poetry run invoke lint
```
