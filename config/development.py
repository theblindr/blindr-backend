import logging

DEBUG = True
SQLALCHEMY_ECHO = True

LOGGING_ENABLED = True
LOGGING_LEVEL = logging.DEBUG

SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/blindr.db'

import boto
boto.config.load_credential_file('./boto.cfg')

