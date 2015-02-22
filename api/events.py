from flask.ext import restful
from authenticate import authenticate
from flask import request, abort
from datetime import datetime

from models import Event
import utils
import config

class Events(restful.Resource):
    method_decorators=[authenticate]
    def get(self):
        last_poll_at = utils.timestamp(self.user.last_poll)
        events = Event.fetch(
                user= self.user.id,
                city= request.args.get('city'),
                since= last_poll_at)

        self.user.last_poll_at = datetime.utcnow()
        import pdb;pdb.set_trace()
        config.session.add(self.user)
        config.session.commit()

        return events
