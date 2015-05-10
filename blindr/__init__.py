from flask import Flask, request, abort
from flask.ext.sqlalchemy import SQLAlchemy
from blindr.plugins import rollbar

db = SQLAlchemy()

def create_app(config=None):
    global db

    app = Flask(__name__)
    app.config.from_object('config')
    if config:
        app.config.from_object(config)

    db.init_app(app)

    rollbar.init_rollbar(app)

    from blindr.api import Api
    Api(app)

    app.logger.info('App created')

    return app


