import os
from flask import Flask, render_template

app = Flask(__name__)

# global variables
chan = ['test']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flack')
def channels():
    return render_template('channels.html', chan=chan)

@app.route('/channels/<chnl>')
def channel(chnl):
    return render_template('channels.html', chnl=chnl)
