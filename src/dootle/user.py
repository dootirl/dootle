import uuid

from src.dootle.name import generate_name 


def create_user():
	while User.query.get(id := uuid.uuid4().hex):
		pass
	u = User(
		id = id,
		name = name,
		score = 0,
		room_id = None,
	)
	return u


def delete_user(user):
	if user:
		db.session.delete(user)
		db.session.commit()
