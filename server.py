from flask import Flask, request
from flask.ext import restful
import itsdangerous

from api import *
import config

app = Flask(__name__)
api = restful.Api(app)

class Me(restful.Resource):
    method_decorators=[authenticate.authenticate]
    def get(self):
        return {'id': self.user}

class Auth(restful.Resource):
    def post(self):
        fb_token = request.form.get('fb_token')
        # Request user from fb_token
        id = '0'
        s = itsdangerous.Signer(config.secret)
        return {'token': s.sign(id)}

api.add_resource(Me, '/me')
api.add_resource(Auth, '/auth')
api.add_resource(events.Events, '/events')

if __name__ == '__main__':
    app.run(debug=True)
