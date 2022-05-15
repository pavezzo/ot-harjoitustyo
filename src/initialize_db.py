from venv import create
from db_connection import get_db_connection
from db_connection import get_testdb_connection


def create_tables(connection):
    """Alustaa tietokantayhteyden avulla tietokannan
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table highscores (
            username text,
            score int,
            size int
        );
    ''')

    connection.commit()

def drop_tables(connection):
    """Poistaa vanhan datan tietokannasta
    """
    cursor = connection.cursor()

    cursor.execute('drop table if exists highscores;')
    connection.commit()

def initialize_db(testing=False):
    """Suorittaa tietokannan tyhjennyksen ja uudelleen luonnin. Jos käytetään testauksessa niin suorittaa nämä testitietokannassa.
    """
    connection = get_db_connection()
    if testing:
        connection = get_testdb_connection()
    drop_tables(connection)
    create_tables(connection)   


if __name__ == "__main__":
    initialize_db()
