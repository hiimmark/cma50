# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__..." ) # prints everytime the webpage is refreshed
    print(__name__)                   # prints __main__ right after the above print statement
    return "No hablo queso!"

app.debug = True # opens a debugger with a pin, but doesn't seem to print anything new at the moment
app.run()
