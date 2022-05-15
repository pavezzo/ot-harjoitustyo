from db_connection import get_db_connection
from db_connection import get_testdb_connection
from initialize_db import initialize_db

class HighscoresRepository:
    """Luokka, jolla hallinoidaan uusien tulosten lisäämistä ja hakemista tietokannasta
    """
    def __init__(self, testing=False):
        """Luokan konstruktori, jossa luodaan tietokantaan yhteys
        """
        self._connection = get_db_connection()
        if testing:
            self._connection = get_testdb_connection()
            initialize_db(True)

    def new_score(self, score, username, size):
        """Lisää uuden tuloksen tietokantaan

        Args:
            score (kokonaisluku): käyttäjän saama pistemäärä pelistä
            username (merkkijono): käyttäjän käyttäjänimi
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into highscores (username, score, size) values (?, ?, ?)',
            (username, score, size)
        )
        self._connection.commit()

    def get_top_10(self):
        """Palauttaa 10 suurinta tulosta

        Returns:
            lista käyttäjänimi ja tulos pareja suuruus järjestyksessä
        """
        cursor = self._connection.cursor()
        cursor.execute('select * from highscores order by score desc limit 10')
        data = cursor.fetchall()
        return data
        