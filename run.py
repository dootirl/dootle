import os, sys


sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


from dootle.app import create_app, socketio


app = create_app()
socketio.run(app, host='0.0.0.0', port=80)
