from flask import Flask, request, abort
from flask.ext.sqlalchemy import SQLAlchemy
import itsdangerous
import config

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

import boto
boto.config.load_from_path('./boto.cfg')

import blindr.api

@app.teardown_appcontext
def shutdown_session(exception=None):
    config.session.remove()


