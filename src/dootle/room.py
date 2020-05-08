import uuid

from src.dootle.models import Room, User


ROOM_CAPACITY = 8


def create_room():
	while Room.query.get(id := uuid.uuid4().hex):
		pass
	r = Room(
		id = id,
		drawing = '',
		state = 'WAITING',
		time = 120,
		word = '',
	)
	return r


def delete_room(room):
	if room:
		db.session.delete(room)
		db.session.commit()
