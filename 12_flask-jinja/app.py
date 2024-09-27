"""
Mark Ma
Ghidorah
SoftDev
K12 - Flask Render Template
2024-09-26
time spent: 0.5

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
This will cause an error because render_template is not defined in the test_implt() function since it is not imported.
We expected that the program wouldn't even run. However, it only presented an error when we tried to load /my_foist_template.

Q1:
http://localhost:5000/my_foist_template

Q2:
The first argument is the path to the template (the html file) to be rendered.
The second argument passes "fooooo" into the foo variable in the template file.
The third argument passes the coll array into the collections variable in the template file.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Observed:
When render_template is removed from input, localhost:5000/my_foist_template displays a NameError and a long
erorr message is printed in terminal.

When localhost:5000/my_foist_template is loaded, the title is foooo, and 0 1 1 2 3 5 8 is displayed on
different lines. It seems to us that our prediction in Q3 is correct. "foooo" is assigned the foo variable
in the html template file and passed through the render_template function in app.py, and the collections variable
is assigned the coll array in app.py.
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()

