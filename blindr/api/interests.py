from flask.ext import restful
from flask import request
from blindr.common.authenticate import authenticate
import facebook

from blindr.models.event import Event
from blindr.models.user import User
from blindr import db

class Interests(restful.Resource):
    method_decorators=[authenticate]

    def post(self):
        interested_in= request.form.get('interested_in')

        self.user.looking_for = interested_in
        db.session.commit()

        return jsonify(status="ok")



