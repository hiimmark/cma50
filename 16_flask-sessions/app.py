'''
Mark Ma
Ghidorah - Mark, Danny, Marco
SoftDev
K16 - Cookies and Sessions
2024-10-07
time spent: 1
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
from flask import redirect
import os

app = Flask(__name__)    #create Flask object
secret_hehe = os.urandom(32)
app.secret_key = secret_hehe

@app.route("/")
def login_page():
    if "username" in session:
        return redirect("/response")
    return render_template('login.html' , method = request.method)

@app.route("/response", methods=['GET', 'POST']) # , methods=['GET', 'POST'])
def response_page():
    if request.method == "POST":
        # at this point "username" must be in session
        session["username"] = request.form["username"]
    if "username" not in session:
        return redirect("/")
    return render_template('response.html', username=session["username"], method=request.method)

@app.route("/logout", methods = ['POST'])
def logout_page():
    # code to logout page and pop session
    session.pop("username")
    return redirect("/")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
