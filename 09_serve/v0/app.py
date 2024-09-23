# Mark Ma
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          #  Initializes a flask object

@app.route("/")                # Assigns the function below to route "/", the home directory.
def hello_world():
    print(__name__)            # print flask server info to terminal
    return "No hablo queso!"   # return this text to the route (and display it) 

app.run()                      # run the flask object
                
