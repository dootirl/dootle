from flask import request

from dootle.room import create_room, ROOM_CAPACITY

def matchmake():
	
	most = 0
	
	for id, room in rooms.items():
		if len(room['users']) > most:
			dest = id
			most = len(room['users'])
	if most == 0:
		dest = create_room()

	return dest
