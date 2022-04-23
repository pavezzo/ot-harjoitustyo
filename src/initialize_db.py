from db_connection import get_db_connection

connection = get_db_connection()

def create_tables():
    cursor = connection.cursor()

    cursor.execute('''
        create table highscores (
            username text,
            score int
        );
    ''')

    connection.commit()

def drop_tables():
    cursor = connection.cursor()

    cursor.execute('drop table if exists highscores;')
    connection.commit()

if __name__ == "__main__":
    drop_tables()
    create_tables()