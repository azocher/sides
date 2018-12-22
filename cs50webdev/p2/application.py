import os
from flask import Flask, render_template

app = Flask(__name__)

# global variables
channel_list = ('test', 'another test')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/channels', methods=['GET'])
def channels():
    return channel_list
