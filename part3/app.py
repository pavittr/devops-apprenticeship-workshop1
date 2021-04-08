# save this as app.py
from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/films/list')
def list():
    return render_template('filmlist_template.html')


@app.route('/films/table')
def table():
    films = []
    filter = request.args.get('stars')
    print(f"filter is {filter}")
    with open('films.csv', "r") as f:
        for line in f.readlines():
            print(f"Processing {line}")
            parts = line.split(", ")
            if filter is None or filter == parts[1].strip():
                films.append({'title': parts[0], 'rating': parts[1]})
    return render_template('filmtable_template.html', films = films)

@app.route('/films/submit', methods = ['GET'])
def get_submission_form():
    return render_template('filmsubmit_template.html')

@app.route('/films/submit', methods = ['POST'])
def create_submission():
    title = request.form['film_name']
    stars = request.form['rating']
    print(f"{title}, {stars}")
    with open("films.csv", "a") as f:
        f.write(f"{title}, {stars}\n")
    return table()