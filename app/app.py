from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from app.models import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edusphere.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    CORS(app)
    return app
