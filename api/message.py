from flask.ext import restful
from authenticate import authenticate
from flask import request, abort
import time

from models.event import Event
from models.user import User
import config

class Message(restful.Resource):
    method_decorators=[authenticate]

    def post(self):
        dst_city = request.form.get('dst_city')
        dst_user = request.form.get('dst_user')
        message = request.form.get('message')
        dst = None
        if dst_city:
            dst = 'city:{}'.format(dst_city.lower())
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
                'src_gender': self.user.gender,
                'message': message
        }

        if dst_user:
            data['participants'] = '{}:{}'.format(*sorted([self.user.id,dst_user]))
        data['src_real_name'] = self.user.real_name
        data['src_fake_name'] = self.user.fake_name

        success = Event.create(data)

        if not success:
            abort(500)

        return data
