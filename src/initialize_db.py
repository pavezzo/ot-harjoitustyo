from db_connection import get_db_connection

connection = get_db_connection()

def create_tables():
    cursor = connection.cursor()

    cursor.execute('''
        create table highscores (
            score int primary key,
            username text
        );
    ''')

    connection.commit()


if __name__ == "__main__":
    create_tables()