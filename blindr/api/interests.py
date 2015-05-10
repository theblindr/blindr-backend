from flask.ext import restful
from flask import request, abort
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
        try:
            db.session.commit()
        except IntegrityError:
            abort(500)
	
        return jsonify(status="ok")



