from flask.ext import restful
from blindr.models.user import User

class Auth(restful.Resource):
    def post(self):
        fb_token = request.form.get('fb_token')
        user = User.from_facebook(fb_token)
        if not user:
            abort(401)
        s = itsdangerous.Signer(config.secret)
        return {'token': s.sign(user.id)}

