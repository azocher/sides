import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# global variables
channel_list = {1 : 'test', 2 : 'another test'}

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/channels', methods=['GET'])
def channels():
    return jsonify(channel_list)

@app.route('/add_channel', methods=['POST'])
def new_channel():
    # get new_channel name from API request
    new_channel = request
    # figure out key value for pair
    count = len(channel_list)
    channel_list[count+1] = new_channel.data
    return 'success!'

@app.route('/channels/<channel>', methods=['GET'])
def channel():
    return render_template('channel.html')
