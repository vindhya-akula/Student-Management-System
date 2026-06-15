from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        marks = request.form["marks"]

        print(name, age, marks)

        return "Student received successfully!"

    return render_template("add_student.html")
if __name__ == "__main__":
    app.run(debug=True)
