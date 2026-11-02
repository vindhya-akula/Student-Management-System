import mysql.connector
from getpass import getpass

_password = None
_password_loaded = False

def get_connection():
    global _password, _password_loaded

    if not _password_loaded:
        _password = getpass("MySQL password: ")
        _password_loaded = True

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=_password,
        database="student_db"
    )