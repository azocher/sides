''' flask app with mongo '''

import os
import json
import datetime
from flask import Flask
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

class JSONEncoder(json.JSONEncoder):
    # extends json-encoder class

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

# declare Flask app
app = Flask(__name__)

# add mongo url to flask config, so that flask_pymongo can use it ot make connection
app.config['MONGO_URI'] = os.environ.get('DB')
mongo = PyMongo(app)

# use the modified encoder class to jsonify our requested response
app.json_encoder = JSONEncoder

from app.controllers import *
