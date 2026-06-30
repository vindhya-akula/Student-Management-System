from flask import Flask, render_template, request, redirect
from student_operations import (
    add_student,
    get_student_by_id,
    update_student,
    delete_student,
    view_students
)

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    students = view_students()
    return render_template("index.html", students=students)


# Add Student
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        marks = int(request.form["marks"])

        add_student(name, age, marks)

        return redirect("/")

    return render_template("add_student.html")


# Update Student
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        marks = int(request.form["marks"])

        update_student(id, name, age, marks)

        return redirect("/")

    student = get_student_by_id(id)
    return render_template("update_student.html", student=student)


# Delete Student
@app.route("/delete/<int:id>")
def delete(id):
    delete_student(id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)