from flask.ext import restful
from authenticate import authenticate
from flask import request, abort
import time

from models import Event

class Message(restful.Resource):
    method_decorators=[authenticate]

    def post(self):
        dst_city = request.form.get('dst_city')
        dst_user = request.form.get('dst_user')
        message = request.form.get('message')
        dest = None
        if dst_city:
            dest = 'city:{}'.format(dst_city)
        elif dst_user:
            dest = 'user:{}'.format(dst_user)

        if dest is None:
            abort(422)

        if not message:
            abort(422)

        data = {
                'type': 'message',
                'dest': dest,
                'src': self.user,
                'message': message
        }
        success = Event.create(data)

        if not success:
            abort(500)

        return data
