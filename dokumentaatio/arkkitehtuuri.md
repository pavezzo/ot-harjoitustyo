## Pelin rakenne
```mermaid
 classDiagram
      UI -- Main
      GameLogic -- GameView
      GameView -- UI
      HighScoreRepository -- HighScoreView
      HighScoreRepository -- SaveScoreView
      MenuView -- UI
      HighScoreView -- UI
      SaveScoreView -- UI
```

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