from db_connection import get_db_connection

class HighscoresRepository:
    def __init__(self):
        self.connection = get_db_connection()

    def new_score(self, score, username):
        cursor = self.connection.cursor()
        cursor.execute(
            'insert into highscores (username, score) values (?, ?)',
            (username, score)
        )
        self.connection.commit()

    def get_top_10(self):
        cursor = self.connection.cursor()
        cursor.execute('select * from highscores order by score desc limit 10')
        data = cursor.fetchall()
        return data
        