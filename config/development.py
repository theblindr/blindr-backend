import logging
import os

ENV='development'
DEBUG = True
SQLALCHEMY_ECHO = True

LOGGING_ENABLED = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/instance/blindr.db'.format(os.getcwd())

import boto
boto.config.load_from_path('instance/boto.cfg')

