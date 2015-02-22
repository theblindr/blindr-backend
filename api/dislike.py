from flask.ext import restful
from authenticate import authenticate
from flask import request, abort, jsonify
import time


import config
from models import Event
from models import User, Match

class Dislike(restful.Resource):
    method_decorators=[authenticate]

    def post(self):
        # Create DB Match entry
        dst_id = request.form.get('dst_user')
        session = config.session

        # User unliking previously like target. Remove row.
        match = session.query(Match).filter_by(match_from_id="%s" % self.user.id, match_to_id="%s" % dst_id).first()
        if match is not None: # Prior like, remove & send ignore callback
            session.delete(match)
        else: # first dislike, send ignore callback
            pass

        session.commit()
        return jsonify(ignore="%s" % dst_id)         
        
