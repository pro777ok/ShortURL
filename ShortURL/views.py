from flask import render_template, request
from ShortURL import app
import json
import random

@app.route('/')
def index():
    return render_template('ShortURL/index.html')

@app.route('/re', methods=['GET'])
def other1():
    print('GETデータ受け取ったので処理します')
    req1 = request.args.get('id')
    print(req1)
    f = open('data.json', 'r')
    json_dict = json.load(f)
    url = json_dict.get(req1, "NotFound")
    return render_template('ShortURL/url.html', url=url)

@app.route('/sampleform-post', methods=['POST'])
def sample_form_temp():
    print('POSTデータ受け取ったので処理します')
    req1 = request.form['data']
    f = open('data.json', 'r')
    json_dict = json.load(f)
    rand = random.randint(11111,99999)
    json_dict[rand] = req1
    json_str = json.dumps(json_dict)
    f2 = open('data.json', 'w')
    json.dump(json_dict, f2)


    return f'URL: {req1} <br><br>ShortURL: {rand}'