from flask import Flask, request, abort
from flask.ext import restful
import requests
import itsdangerous

from api import *
from models import User
import config

app = Flask(__name__)
api = restful.Api(app)

class Me(restful.Resource):
    method_decorators=[authenticate]
    def get(self):
        return {'id': self.user.id}

class Auth(restful.Resource):
    def post(self):
        fb_token = request.form.get('fb_token')
        user = User.from_facebook(fb_token)
        if not user:
            abort(401)
        s = itsdangerous.Signer(config.secret)
        return {'token': s.sign(user.id)}


api.add_resource(Me, '/me')
api.add_resource(Auth, '/auth')
api.add_resource(Events, '/events')
api.add_resource(Message, '/events/message')
api.add_resource(Like, '/events/like')

if __name__ == '__main__':
    app.run(debug=True)
