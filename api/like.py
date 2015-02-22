from flask.ext import restful
from authenticate import authenticate
from flask import request, abort
import time

from models import Event

class Like(restful.Resource):
    method_decorators=[authenticate]

    def post(self):
        # Create DB Match entry
        pass
