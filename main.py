from db_connection import get_connection
from student_operations import (
    add_student,
    delete_student,
    get_student_by_id,
    update_student,
    view_students,
)


def menu():
    print("\n╭──────────────────────────────────╮")
    print("│       STUDENT HUB · CONSOLE      │")
    print("├──────────────────────────────────┤")
    print("│  1  Add student                  │")
    print("│  2  View students                │")
    print("│  3  Edit student                 │")
    print("│  4  Delete student               │")
    print("│  5  Exit                         │")
    print("╰──────────────────────────────────╯")


def read_student_details():
    name = input("Student name: ").strip()
    age = int(input("Age (1-120): "))
    marks = int(input("Marks (0-100): "))
    if not name or len(name) > 100:
        raise ValueError("Name is required and must be 100 characters or fewer.")
    if not 1 <= age <= 120:
        raise ValueError("Age must be between 1 and 120.")
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    return name, age, marks


def main():
    connection = get_connection()
    connection.close()

    while True:
        menu()
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                add_student(*read_student_details())
                print("\n✓ Student added.")
            elif choice == "2":
                students = view_students()
                if not students:
                    print("\nNo student records yet.")
                else:
                    print("\nID   NAME                              AGE   MARKS")
                    print("─" * 57)
                    for student in students:
                        print(f"{student[0]:<4} {student[1]:<33} {student[2]:<5} {student[3]}")
            elif choice == "3":
                student_id = int(input("Student ID to edit: "))
                if get_student_by_id(student_id) is None:
                    print("\nNo student found with that ID.")
                    continue
                update_student(student_id, *read_student_details())
                print("\n✓ Student updated.")
            elif choice == "4":
                student_id = int(input("Student ID to delete: "))
                if get_student_by_id(student_id) is None:
                    print("\nNo student found with that ID.")
                    continue
                if input("Are you sure you want to delete this student? (y/N): ").strip().lower() == "y":
                    delete_student(student_id)
                    print("\n✓ Student deleted.")
                else:
                    print("\nDelete cancelled.")
            elif choice == "5":
                print("\nGoodbye!")
                break
            else:
                print("\nChoose a number from 1 to 5.")
        except ValueError as exc:
            print(f"\nPlease check your input: {exc}")


if __name__ == "__main__":
    main()
