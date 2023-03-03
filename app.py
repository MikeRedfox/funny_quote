from flask import Flask, render_template
import requests
from urllib.request import urlopen
import json
import random


url = 'https://raw.githubusercontent.com/MikeRedfox/funny_quote/main/quotes.json'
response = urlopen(url)
json_data = response.read().decode('utf-8', 'replace')
d = json.loads(json_data)


app = Flask(__name__)

width = 800
height = 900


@app.route('/')
def home():
    return render_template('index.html',size=f'{str(width)}x{str(height)}', quote=d['_default'][str(random.randint(1,len(d['_default'])))]['quote'])





if __name__ == '__main__':
    app.run(debug=True)
