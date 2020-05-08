from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


socketio = SocketIO()


def create_app():
	app = Flask(__name__)
	app.config.from_pyfile('settings.py')

	socketio.init_app(app) 

	from dootle.database import db
	db.init_app(app)

	from dootle import views
	app.register_blueprint(views.blueprint)
	return app
