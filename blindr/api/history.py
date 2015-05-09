from flask.ext import restful
from blindr.common.authenticate import authenticate
from flask import request, abort

from blindr.models.event import Event

class History(restful.Resource):
    method_decorators=[authenticate]

    def get(self, other_id):
        sinceParam = int(request.args.get('since'))
        return Event.fetch_history(user= self.user.id,
                                    other= other_id, since= sinceParam)


