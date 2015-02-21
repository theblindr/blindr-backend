from flask.ext import restful
from authenticate import authenticate
from flask import request, abort
import time

from models import Event

class Events(restful.Resource):
    method_decorators=[authenticate]
    def get(self):
        # Get events since last poll
        return Event.fetch('user:1', 1424558599)

    def post(self):
        event_data = request.form.to_dict()
        event_data['src'] = self.user
        event_data['sent_at'] = int(time.time())

        if not Event.create(event_data):
            abort(500)

        return event_data


