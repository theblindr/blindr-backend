from flask.ext import restful
from authenticate import authenticate
from flask import request, abort
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
        session.query(Match).filter(
            ((Match.match_from_id == self.user.id) & (Match.match_to_id == dst_id)) |
            ((Match.match_from_id == dst_id) & (Match.match_to_id == self.user.id))).delete()

        session.commit()

        return {'ignore': dst_id}

