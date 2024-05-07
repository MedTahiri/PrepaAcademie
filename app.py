import csv
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/section/<section>')
def section(section=None):
    info_lesson = read_from_file('static/DATA/informatique_lesson.csv')
    info_exercise = read_from_file('static/DATA/informatique_exercise.csv')

    chimie_lesson = read_from_file('static/DATA/chimie_lesson.csv')
    chimie_exercise = read_from_file('static/DATA/chimie_exercise.csv')

    si_lesson = read_from_file('static/DATA/si_lesson.csv')
    si_exercise = read_from_file('static/DATA/si_exercise.csv')

    math_lesson = read_from_file('static/DATA/math_lesson.csv')
    math_exercise = read_from_file('static/DATA/math_exercise.csv')

    physique_lesson = read_from_file('static/DATA/physique_lesson.csv')
    physique_exercise = read_from_file('static/DATA/physique_exercise.csv')

    return render_template("section.html",section=section,
                           info_exercise=info_exercise,
                           info_lesson=info_lesson,
                           chimie_lesson=chimie_lesson,
                           chimie_exercise=chimie_exercise,
                           si_lesson=si_lesson,
                           si_exercise=si_exercise,
                           math_lesson=math_lesson,
                           math_exercise=math_exercise,
                           physique_lesson=physique_lesson,
                           physique_exercise=physique_exercise)

@app.route('/concours')
def concours():
    return render_template("concours.html")

@app.route('/tipe')
def tipe():
    tipe = read_from_file('static/DATA/tipe.csv')
    return render_template("tipe.html",tipe=tipe)

@app.route('/lignes')
def lignes():
    return render_template("lignes.html")

@app.route('/view/<id>')
def view(id):
    return render_template("view.html",id=id)

def read_from_file(file_name):
    l=[]
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            l.append(row)
    return l

if __name__ == '__main__':
    app.run()
