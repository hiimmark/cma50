"""
Mark Ma
Ghidorah
SoftDev
K12 - Flask site with roster and template
2024-09-29
time spent: 0.5
"""

from flask import Flask, render_template
import random
import csv

app = Flask(__name__)

d = {}

def select_random():
    perc = random.uniform(0, 99.8)
    for key, values in d.items():
        if perc - values[0] <= 0:
            return [key, values[1]]
        perc -= values[0]
    return "N/A"

@app.route("/wdywtbwygp")
def load_site():
    return render_template('tablified.html', rand_occupation = select_random(), table=d)

if __name__ == "__main__":
    with open("data/occupations.csv", "r") as file:
        arr = list(csv.reader(file))[1:-2] #omit first and last lines
    for i in arr:
        d.update({i[0]:[float(i[1]), i[2]]})

    app.debug = True
    app.run()
