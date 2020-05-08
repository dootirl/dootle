from dootle.database import db


class Room(db.Model):
	id = db.Column(db.String(), primary_key=True)
	drawing = db.Column(db.String())
	state = db.Column(db.String())
	time = db.Column(db.String())
	word = db.Column(db.String())
	users = db.relationship('User', backref='room')


class User(db.Model):
	id = db.Column(db.String(), primary_key=True)
	name = db.Column(db.String(32), index=True)
	score = db.Column(db.Integer)
	room_id = db.Column(db.String(), db.ForeignKey('room.id'))
