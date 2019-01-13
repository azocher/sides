import os
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# global variables
channel_list = {
    1 : 'test',
    2 : 'another test',
}

messages = {
    "test" : [],
    "another test" : []
}

users = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', channels=channel_list, current_users=users)

@app.route('/channels', methods=['GET'])
def channels():
    return jsonify(channel_list);

@socketio.on("new user")
def user_on(data):
    message_sender = data['sn']
    sender_emoji = data['emoji']
    users[message_sender] = sender_emoji
    emit('login', {"screename": message_sender, "avatar": sender_emoji}, broadcast=True)

@app.route('/add_channel', methods=['POST'])
def new_channel():

    # get new_channel name from API request
    new_channel = request.data.decode("utf-8")

    # figure out key value for pair
    count = len(channel_list)
    channel_list[count+1] = new_channel
    print("Added a new channel!")
    print(channel_list[count+1])

    # add channel as empty dict for possible messages
    messages[new_channel] = []

    return 'success!'

@app.route('/channels/<channel>', methods=['GET'])
def channel(channel):
    return render_template('channel.html', channel=channel, messages=messages[channel])

@socketio.on("send message")
def new_message(data):
    # get variables from socket message
    channel = data['channel']
    print(channel)
    message = data['message']
    message_sender = data['sn']
    sender_emoji = data['emoji']

    # add message to message array for storage
    messages[channel].append([sender_emoji, message_sender, message])

    # check to see length of message array; delete if >100
    if (len(messages[channel]) > 100):
        del messages[channel][0]

    emit('message received', {"message": message, "screename": message_sender, "avatar": sender_emoji}, broadcast=True)
