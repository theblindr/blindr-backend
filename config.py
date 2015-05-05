DEBUG = False
SQLALCHEMY_ECHO = False

secret = 'f4babeae21e325df1ff6656d79a5ff0ceac02635'

import boto
boto.config.load_from_path('./boto.cfg')
