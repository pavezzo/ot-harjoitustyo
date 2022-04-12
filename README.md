# Ohjelmistotekniikan harjoitustyö: 2048 peli
Sovellus on minun versio suositusta 2048 pelistä. 
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
2. Käynnistä peli:
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