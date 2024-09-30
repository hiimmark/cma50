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
def randocc():
    with open("data/occupations.csv", "r") as file:
        arr = list(csv.reader(file))[1:-2] #omit first and last lines
    for i in arr:
        d.update({i[0]:float(i[1])})
    d.update({"Ducky":0.2}) #make the total 100%
    random_occ = random.choices(list(d.keys()), list(d.values()))[0]
    return random_occ

@app.route("/wdywtbwygp")
def load_site():
    return render_template('tablified.html', rand_occupation = randocc(), table=d)


if __name__ == "__main__":
    app.debug = True
    app.run()
