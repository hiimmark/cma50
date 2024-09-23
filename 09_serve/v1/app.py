# Mark Ma
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

'''
The only thing ommitted from this version and the previous is print(__name__). We initially thought
this would cause the server info to not be printed in the terminal, but that's not true. We're not sure what changed from ommitting the print(__name__) statement
'''

