from flask import Flask, request, abort
from flask.ext.sqlalchemy import SQLAlchemy

import boto
boto.config.load_from_path('./boto.cfg')

db = SQLAlchemy()

def create_app(config):
    global db

    app = Flask(__name__)
    app.config.from_object('config')
    app.config.from_object(config)

    db.init_app(app)

    from blindr.api import Api
    Api(app)

    return app


