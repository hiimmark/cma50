# Mark Ma
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...") # this prints everytime the webpage is refreshed
    print(__name__) # this prints __main__
    return "No hablo queso!"

app.run()

