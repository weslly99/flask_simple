from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from config import app_config

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)

    from .auth import auth as auth_blueprint
    from .book import book as book_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(book_blueprint)

    return app
