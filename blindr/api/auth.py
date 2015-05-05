from flask.ext import restful
from flask import current_app, request, abort
import itsdangerous
from blindr.models.user import User

class Auth(restful.Resource):
    def post(self):
        fb_token = request.form.get('fb_token')
        user = User.from_facebook(fb_token)
        if not user:
            abort(401)

        s = itsdangerous.Signer(current_app.config['AUTH_SECRET'])
        return {'token': s.sign(user.id.encode()).decode('utf-8')}

