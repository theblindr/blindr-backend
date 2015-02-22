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
        dst = None
        if dst_city:
            dst = 'city:{}'.format(dst_city)
        elif dst_user:
            dst = 'user:{}'.format(dst_user)

        if dst is None:
            abort(422)

        if not message:
            abort(422)

        data = {
                'type': 'message',
                'dst': dst,
                'src': self.user.id,
                'message': message
        }

        if dst_user:
            data['participants'] = '{}:{}'.format(*sorted([self.user.id,dst_user]))

        success = Event.create(data)

        if not success:
            abort(500)

        return data
