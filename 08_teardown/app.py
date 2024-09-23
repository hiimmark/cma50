'''
Mark Ma
Hot Cheetos
SoftDev
K08 -- Suspicious Python File
2024-09-22
time spent: 0.5

DISCO:
Upon running the program, a webpage server is opened up at 127.0.0.1:5000. When
loading the url in the browser, a blank page with No hablo queso is displayed.

QCC:
0. ?
1. The home directory
2. It prints to to terminal.
3. It prints whatever is in the __name__ variable.
4. This might appear in the "/" webpage because app is routed to it.
5. netlogo?
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



