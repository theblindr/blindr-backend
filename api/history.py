from flask.ext import restful
from authenticate import authenticate
from flask import request, abort

from models import Event

class History(restful.Resource):
    method_decorators=[authenticate]

    def get(self, other_id):
        sinceParam = request.args.get('since')
        return Event.fetch_history(user= self.user.id,
                                    other= other_id, since= sinceParam)


