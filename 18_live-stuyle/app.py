'''
Mark Ma
Team 54
SoftDev
K18 -- Serve HTML in Flask
2024-10-16
time spent: 0.3
'''

from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
def serve():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
