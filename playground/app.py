from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/welcome/<string:student_name>')
def student(student_name):
    return render_template("welcome.html", student_name=student_name)


@app.route('/roster/<int:grade_view>')
def roster(grade_view):
    grade_view = (grade_view == 0) or (grade_view == 1) or (grade_view == 2)
    class_roster =
    [("Paisley", "F", "Junior"),
    ("Ariel", "C", "Junior"),
    ("Ashley", "D", "Sophomore"),
    ("Shanelle", "B", "Sophmore"),
    ("Chloe", "F", "Freshman"),
    ("Amber", "D", "Senior"),
    ("Hayden", "B", "Freshman")]
    return render_template("roster.html", grade_view=grade_view, class_roster=class_roster)


if __name__ == '__main__':
    app.run()
