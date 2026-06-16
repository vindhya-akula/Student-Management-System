import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nihanth_06",  # MySQL password
        database="student_db"
    )
    
