from flask import Flask
import flask_sqlalchemy

from .models import db
from . import config


def create_app():
    flask_app = Flask(__name__)
    flask_app.config["SQLALCHMY_DATABSE_URI"] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    return flask_app
