ENV='test'
SQLALCHEMY_DATABASE_URI = "sqlite://"
TESTING = True

LOGGING_ENABLED = False

import boto
if not boto.config.has_section('Credentials'):
    boto.config.add_section('Credentials')
boto.config.set('Credentials','aws_access_key_id','foobar')
boto.config.set('Credentials','aws_secret_access_key','bizbuz')
