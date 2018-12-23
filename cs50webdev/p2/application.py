import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# global variables
channel_list = {1 : 'test', 2 : 'another test'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/channels', methods=['GET'])
def channels():
    return jsonify(channel_list)

@app.route('/add_channel', methods=['POST'])
def new_channel(data):
    count = len(channel_list)
    channel_list[count+1] = data
    return channel_list
