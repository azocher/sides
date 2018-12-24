import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# global variables
channel_list = {1 : 'test', 2 : 'another test'}

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/channels', methods=['POST'])
def channels():
    return jsonify(channel_list)

@app.route('/add_channel', methods=['POST'])
def new_channel():

    new_channel = request.form.get('form_new_channel')
    print(new_channel)
    # figure out key value for pair
    count = len(channel_list)
    channel_list[count+1] = new_channel

    return "success!"
