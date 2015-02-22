from flask import Flask, request, abort
from flask.ext import restful
import requests
import itsdangerous

from api import *
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

        # Request user from fb_token
        r = requests.get('https://graph.facebook.com/v2.2/me/?access_token=%s' % fb_token)
        if r.status_code == 200: #good
            jsonObj = r.json()
            if "id" in jsonObj:
                s = itsdangerous.Signer(config.secret)
                return {'token': s.sign(jsonObj["id"])}
            else:
                abort(500)
        else:
            abort(401)

api.add_resource(Me, '/me')
api.add_resource(Auth, '/auth')
api.add_resource(Events, '/events')
api.add_resource(Message, '/events/message')
api.add_resource(Like, '/events/like')

if __name__ == '__main__':
    app.run(debug=True)
