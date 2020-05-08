from flask import request
from flask_socketio import emit, send

from dootle.app import socketio
from dootle.game import matchmake
from dootle.user import create_user, delete_user


@socketio.on('connect')
def on_connect():
	user = create_user()
	print(request.sid)
	print(user)
	# room = matchmake()

	# for i in drawing:
	#	emit('drawing', i)


@socketio.on('disconnect')
def on_disconnect():
	pass


@socketio.on('message')
def on_message(data):
	print(data)


@socketio.on('drawing')
def on_drawing(data):
	user = users[request.sid]
	room = rooms[user['room']]

	room['drawing'].append(data)
	emit('drawing', data, broadcast=True)


@socketio.on('scoreboard')
def on_scoreboard():
	pass
