from db_connection import get_connection

def add_student(name, age, marks):
    # Only database insertion
    conn = get_connection()
    cursor = conn.cursor()


    sql = "INSERT INTO students (name, age, marks) VALUES (%s, %s, %s)"
    values = (name, age, marks)

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Marks: {row[3]}")

    cursor.close()
    conn.close()


def update_student():
    conn = get_connection()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to update: "))

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Marks")

    choice = input("Enter choice: ")

    if choice == "1":
        new_name = input("Enter new name: ")
        sql = "UPDATE students SET name = %s WHERE id = %s"
        values = (new_name, student_id)

    elif choice == "2":
        new_age = int(input("Enter new age: "))
        sql = "UPDATE students SET age = %s WHERE id = %s"
        values = (new_age, student_id)

    elif choice == "3":
        new_marks = int(input("Enter new marks: "))
        sql = "UPDATE students SET marks = %s WHERE id = %s"
        values = (new_marks, student_id)

    else:
        print("Invalid choice")
        return

    cursor.execute(sql, values)
    conn.commit()

    print("✅Student updated successfully!")

    cursor.close()
    conn.close()



def delete_student():
    conn = get_connection()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to delete: "))

    confirm = input("Are you sure? (yes/no): ")

    if confirm.lower() == "yes":
        sql = "DELETE FROM students WHERE id = %s"
        values = (student_id,)

        cursor.execute(sql, values)
        conn.commit()

        print("✅Student deleted successfully!")
    else:
        print("Delete cancelled.❌")

    cursor.close()
    conn.close()
    
