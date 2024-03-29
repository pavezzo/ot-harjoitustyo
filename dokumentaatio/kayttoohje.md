# Käyttöohje
Lataa ohjelman uusin [release](https://github.com/pavezzo/ot-harjoitustyo/releases/tag/Loppupalautus).
## Asennus
1. Asenna riippuvuudet:
```bash
poetry install
```
2. Alusta tietokanta:
```bash
poetry run invoke initialize
```
3. Käynnistä peli
```bash
poetry run invoke start
```

## Aloitusvalikko
Sovellus käynnistyy alkuvalikkoon:\
![](./kuvat/aloitusnäyttö.png)\
Alkuvalikosta pääsee aloittamaan uuden pelin tai tarkastelemaan parhaimpia tuloksia. Pelin ruudukon kokoa voi vaihtaa näppäimillä 2-9, eli pienin ruudukko 2x2 ja suurin 9x9.
## Pelinäkymä
Pelaaminen tapahtuu pelinäkymässä. Näytölle piirtyy ruudukko ja ruudukon soluihin numeroita. Numeroita voi liikuttaa nuolinäppäimillä ja aina kun kaksi saman suuruista numeroa kohtaavat ne yhdistyvät. Numeroiden yhdistyminen kasvattaa pistemäärää, joka näkyy vasemmassa yläkulmassa. Pelin voi missä kohtaa tahansa aloittaa alusta välilyönnillä.\
![](./kuvat/pelin%C3%A4kym%C3%A4.png)

## Pelin päättyminen
Pelin päätyttyä ruudulle ilmestyy valikko:\
![](./kuvat/peliohi.png)\
Valikosta voidaan siirtyä aloitusvalikkoon, aloittaa peli uudelleen tai tallentaa tulos tietokantaan.

## Tuloksen tallentaminen
Pelistä saaman tuloksen voi pelin loputtua tallentaa. Tallennusnäkymä lukee käyttäjän näppäinsyötettä ja painamalla save nappia tai enteriä ohjelma tallentaa tuloksen.\
![](./kuvat/tallennusn%C3%A4kym%C3%A4.png)

## Tuloksien tarkastelu
Parhaimpia pelistä saatuja tuloksia voi tarkastella päävalikon kautta.\
![](./kuvat/huipputulokset.png)