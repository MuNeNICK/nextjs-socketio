from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
import pymysql
from flask_login import LoginManager, login_user
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)

# CORS(app, supports_credentials=True)
CORS(app)

app.config.from_object('config')

socketio = SocketIO(app, cors_allowed_origins='*')

db = SQLAlchemy(app)

from models import user

login_manager = LoginManager()
login_manager.init_app(app)

import views

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
    
