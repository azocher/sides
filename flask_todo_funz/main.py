# all credit to @ShadabTweets (Shadab Ansari) - almost all code via tutorial on stackabuse.com

import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World"

@app.route('/item/new', methods=['POST'])
def add_item():

    # Get item from the POST
    req_data = request.get_json()
    item = req_data['item']

    # Add item to list
    res_data = helper.add_to_list(item)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400, mimetype='application/json')
        return response

    # return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

@app.route('/items/all')
def get_all_items():
    #get items from the helper
    res_data = helper.get_all_items()

    #return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/item/status', methods=['GET'])
def get_item():

    #get parameter from URL
    item_name = request.args.get('name')

    #get items from the helper
    status = helper.get_item(item_name)

    # Return 404 if no item found
    if status is None:
        response = Response("{'error': 'Item Not Found - %s'}" % item_name, status=404, mimetype='application/json')
        return Response

    res_data = {
        'status': status
    }

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response

@app.route('/item/update', methods=['PUT'])
