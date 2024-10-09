'''
Mark Ma
Ghidorah - Mark, Danny, Amanda
SoftDev
K15 - Flask Forms
2024-10-07
time spent: 0.5
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object

@app.route("/")
def disp_loginpage():
    return render_template( 'login.html' , method = request.method)


@app.route("/response", methods=['GET', 'POST']) # , methods=['GET', 'POST'])
def authenticate():
    user = ""
    if request.method == "GET":
        user = request.args['username']
    else:
        user = request.form['username']
    return render_template('response.html', username=user, method=request.method)


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
