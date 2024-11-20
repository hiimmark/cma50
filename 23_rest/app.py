'''
Mark Ma

'''

from flask import Flask, render_template, request, session, redirect
import urllib.request, urllib.parse
import json


app = Flask(__name__)

@app.route('/')
def render():
    secret_key = open("key_nasa.txt", "r").read()
    print(secret_key)
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    values = {
            'earth_date' : '2022-04-21',
            'api_key' : secret_key
            }
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page)
    
    return render_template('main.html')

if __name__ == "__main__":
    app.run()

