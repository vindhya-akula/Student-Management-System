from flask import Flask, render_template, request, redirect
from student_operations import add_student
from db_connection import get_connection

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Add Student page
@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        marks = int(request.form["marks"])

        add_student(name, age, marks)

        return "Student Added Successfully!"

    return render_template("add_student.html")

@app.route('/view')
def view_student():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('view_students.html',students = data)



if __name__ == "__main__":
    app.run(debug=True)



