'''
Mark Ma

SoftDev
K09
2024-09-2
time spent: 0.3
'''

import random
from flask import Flask
app = Flask(__name__)           #create instance of class Flask

f = open("occupations.csv", "r").read()
f = f.split("\n")[1:-1]
total = float(f[-1].split(',')[-1]) # the total percentage of the whole thing
f = f[0:-1] # get rid of the last column with the total

occupations = {} # {occupation: percentage}
for x in f:
    y = x.split(',')
    occupations[(",".join(y[:-1])).replace('"','')] = float(y[-1])

def select_random():
    perc = random.uniform(0, total)
    for key, values in occupations.items():
        if perc - values <= 0:
            return key
        perc -= values
    return "null"

@app.route("/")
def hello_world():
    txt = "<h2> A random occupation is chosen: " + select_random() + "</h2><br><br>"
    txt += "<h3>Here are the list of occupations and their percentages:</h3><br>"
    for key, values in occupations.items():
        txt += key + '<div align="center">' + str(values) + "</div> <br>"
    return txt

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
