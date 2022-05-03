# Arkkitehtuurikuvaus
## Rakenne
Koodin pakkausrakenne on seuraavanlainen:
```mermaid
 classDiagram
      ui ..> logic
      ui ..> repositories
```
Pakkaus ui sisältää pelingrafiikan, sekä käyttöliittymän, logic pelilogiikan ja repositories tietokantatoiminnoista vastaavan koodin.

## Käyttöliittymä

Käyttöliittymä sisältää neljä erilaista näkymää:

- Alkuvalikko
- Pelinäkymä
- Tulosten tarkastelu
- Tuloksen tallentaminen

Pelinäkymä pitää myös sisällään pelin loppuessa ilmestyvän valikon. Jokainen näistä näkymistä on omina luokkinaan ja niiden hallinnoimisesta ja näyttämisestä vastaa Ui-luokka.

## Sovelluslogiikka

Pelin toimintalogiikka on mallinnettu 2d-listana, jossa jokainen alkio merkkaa yhtä peliruudukon ruutua. Tämän hallinnasta vastaa Game-luokka. Kun GameView-luokka lukee käyttäjältä näppäimenpainalluksen, välittää se sen Game-luokalle joka tekee muutoksen ruudukkoon näppäinpainalluksen mukaan. Kun GameView-luokka seuraavaksi haluaa piirtää uuden pelitilan, pyytää se 2d-listan Game-luokalta ja piirtää sen perusteella uuden tilan näytölle. 

## Päätoiminnallisuudet
### Pelin pelaaminen
Pelaaminen tapahtuu nuolinäppäimillä, jotka GameView-luokka lukee ja välittää edelleen pelilogiikasta vastaavalle Game-luokalle. Tämän jälkeen piirretään pelin tilanne uudelleen käyttäjälle:
```mermaid
sequenceDiagram
      actor User
      participant UI
      participant GameView
      participant Game
      UI ->> GameView: event_handler()
      User ->> GameView: keypress up
      GameView ->> Game: new_keypress("up")
      Game -->> GameView: onnistui / epäonnistui
      UI ->> GameView: update_game()
```
### Tuloksen tallentaminen
Tuloksen tallentaminen tapahtuu päättyneen pelin jälkeen jolloin Game-luokan pistemäärä ja käyttäjän antama nimi viedään HighscoresRepository-luokalle joka hoitaa sen tallentamisen.

```mermaid
sequenceDiagram
      actor User
      participant Ui
      participant GameView
      participant Game
      participant SaveScoreView
      participant HighscoresRepository
      Ui ->> GameView: get_score()
      GameView ->> Game: get_score()
      Game -->> GameView: score
      GameView -->> Ui: score
      Ui ->> SaveScoreView: set_score(score)
      User ->> SaveScoreView: Kirjoittaa käyttäjänimen
      SaveScoreView ->> HighscoresRepository: new_score(score, username)

```