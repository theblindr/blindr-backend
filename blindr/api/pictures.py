from flask.ext import restful
from flask import request, abort
from blindr.common.authenticate import authenticate
import facebook

from blindr.models.event import Event
from blindr.models.user import User
from blindr.models.match import Match
from blindr import db

class Pictures(restful.Resource):
    method_decorators=[authenticate]

    def get(self):
        dst_id = request.args.get('dst_id')
        user = User.query.get(dst_id)
        if user:
            return user.facebook_urls.split(",")
        else:
            abort(422)

    def post(self):
        facebookUrls = request.form.get('facebookUrls')

        self.user.facebook_urls = facebookUrls
        db.session.commit()

        return {}

