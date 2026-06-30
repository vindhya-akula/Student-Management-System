from db_connection import get_connection

def add_student(name, age, marks):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = "INSERT INTO students (name, age, marks) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, age, marks))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

    return True

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()



def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = "SELECT * FROM students WHERE id = %s"
        cursor.execute(sql, (student_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()
    

def update_student(student_id, name, age, marks):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = """
        UPDATE students
        SET name = %s,
            age = %s,
            marks = %s
        WHERE id = %s
        """
        cursor.execute(sql, (name, age, marks, student_id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = "DELETE FROM students WHERE id = %s"
        cursor.execute(sql, (student_id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
