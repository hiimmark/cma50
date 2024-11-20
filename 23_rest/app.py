'''
Mark Ma
Topher - Mark, Tawab
Softdev
K23 - Rest API from Nasa
2024-11-20
time spent: 1
'''

from flask import Flask, render_template, request, session, redirect
import urllib.request, urllib.parse
import json


app = Flask(__name__)

@app.route('/')
def render():
    secret_key = open("key_nasa.txt", "r").read().strip().rstrip()
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2022-10-31" 
    url += "&api_key=" + secret_key
    url += "&camera=fhaz"
    req = urllib.request.Request(url=url)

    l = []
    with urllib.request.urlopen(req) as response:
        parsed_page = json.loads(response.read())
        photos = parsed_page['photos']
        for x in photos:
            cam = x['camera']
            name = x['camera']['full_name']
            image_url = x['img_src']
            l.append([image_url, name])
    
    return render_template('main.html', images=l)

if __name__ == "__main__":
    app.run()

