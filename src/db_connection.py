import os
import sqlite3

dirname = os.path.dirname(__file__)
connection = sqlite3.connect(os.path.join(dirname, "..", "data", "database.sqlite"))
test_connection = sqlite3.connect(os.path.join(dirname, "..", "data", "testdatabase.sqlite"))

def get_db_connection():
    """Palauttaa yhteyden tietokantaan
    """
    return connection

def get_testdb_connection():
    """Palauttaa yhteyden testeissä käytettävään tietokantaan
    """
    return test_connection
