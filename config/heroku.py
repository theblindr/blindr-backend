from os import environ

ENV = 'heroku'
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
SECRET = environ.get('SECRET')
AUTH_SECRET = environ.get('AUTH_SECRET')
ROLLBAR_ACCESS_TOKEN = environ.get('ROLLBAR_ACCESS_TOKEN')
