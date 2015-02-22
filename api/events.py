from flask.ext import restful
from authenticate import authenticate
from flask import request, abort
import time

from models import Event
import utils

class Events(restful.Resource):
    method_decorators=[authenticate]
    def get(self):
        last_poll_at = utils.timestamp(self.user.last_poll)
        return Event.fetch(
                user= self.user.id,
                city= request.args.get('city'),
                since= last_poll_at)

