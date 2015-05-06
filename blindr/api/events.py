from flask.ext import restful
from .authenticate import authenticate
from flask import request, abort
from datetime import datetime
import time

from blindr.models.event import Event
import blindr.utils
import config

class Events(restful.Resource):
    method_decorators=[authenticate]

    def get(self):
        city = request.args.get('city')

        last_poll_at = utils.timestamp(self.user.last_poll)
        events = Event.fetch(
                user= self.user.id,
                since= last_poll_at)

        if city:
            events += Event.fetch(city= city.lower(),
                    since= time.time())

            events = sorted(events, key=lambda e: e['sent_at'])

        self.user.last_poll = datetime.utcnow()
        config.session.commit()

        events = filter(lambda e: e['src'] != self.user.id, events)

        return events