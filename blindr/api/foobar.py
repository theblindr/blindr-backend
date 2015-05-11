from flask.ext import restful
from flask import current_app

class Foobar(restful.Resource):
    def get(self):
        current_app.logger.info('[Foobar] test')
        return 1/0
