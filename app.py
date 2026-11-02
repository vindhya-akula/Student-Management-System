from flask import Flask, redirect, render_template, request, url_for

from db_connection import get_connection
from student_operations import (
    add_student,
    delete_student,
    get_student_by_id,
    update_student,
    view_students,
)

app = Flask(__name__)


def read_student_form():
    name = request.form.get("name", "").strip()
    age_text = request.form.get("age", "").strip()
    marks_text = request.form.get("marks", "").strip()

    if not name:
        return None, "Please enter the student's name."
    if len(name) > 100:
        return None, "Name must be 100 characters or fewer."
    try:
        age = int(age_text)
        marks = int(marks_text)
    except ValueError:
        return None, "Enter a whole number for age and marks."
    if not 1 <= age <= 120:
        return None, "Age must be between 1 and 120."
    if not 0 <= marks <= 100:
        return None, "Marks must be between 0 and 100."
    return (name, age, marks), None


@app.route("/")
def home():
    students = view_students()
    total_students = len(students)
    average_marks = round(sum(student[3] for student in students) / total_students, 1) if total_students else 0
    top_student = max(students, key=lambda student: student[3]) if students else None
    return render_template(
        "index.html",
        students=students,
        total_students=total_students,
        average_marks=average_marks,
        top_student=top_student,
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        student, error = read_student_form()
        if error:
            return render_template("add_student.html", error=error), 400
        add_student(*student)
        return redirect(url_for("home"))
    return render_template("add_student.html")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    student_record = get_student_by_id(id)
    if student_record is None:
        return redirect(url_for("home"))

    if request.method == "POST":
        student, error = read_student_form()
        if error:
            return render_template("update_student.html", student=student_record, error=error), 400
        update_student(id, *student)
        return redirect(url_for("home"))
    return render_template("update_student.html", student=student_record)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    if get_student_by_id(id) is not None:
        delete_student(id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    connection = get_connection()
    connection.close()
    app.run(debug=True, use_reloader=False, port=5001)
