'''
Mark Ma
Team 54
SoftDev
K09
2024-09-24
time spent: 0.3
'''

import random
import csv
from flask import Flask
d = {}
def randocc():
    with open("occupations.csv", "r") as file:
        arr = list(csv.reader(file))[1:-2] #omit first and last lines
    for i in arr:
        d.update({i[0]:float(i[1])})
    d.update({"Ducky":0.2}) #make the total 100%
    random_occ = random.choices(list(d.keys()), list(d.values()))[0]
    return random_occ

app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    txt = "Team 54<br>Anastasia, Mark, Brian<br>"
    txt += "<h2> A random occupation is chosen: " + randocc() + "</h2><br><br>"
    txt += "<h3>Here are the list of occupations and their percentages:</h3><br>"
    for key, values in d.items():
        txt += key + '<div align="center">' + str(values) + "</div> <br>"
    return txt

if __name__ == "__main__":      # true if this file NOT imported
                                # meaning that we're running app.py, not another program that imported app.py
    app.debug = True            # enable auto-reload upon code change
    app.run()
