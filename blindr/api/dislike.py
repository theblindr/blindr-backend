from flask.ext import restful
from blindr.common.authenticate import authenticate
from flask import request, abort
import time

from blindr import db
from blindr.models.event import Event
from blindr.models.match import Match
from blindr.models.user import User

class Dislike(restful.Resource):
    method_decorators=[authenticate]

    def post(self):
        # Create DB Match entry
        dst_id = request.form.get('dst_user')

        # User unliking previously like target. Remove row.
        Match.query.filter(
            ((Match.match_from_id == self.user.id) & (Match.match_to_id == dst_id)) |
            ((Match.match_from_id == dst_id) & (Match.match_to_id == self.user.id))
        ).delete()

        db.session.commit()

        return {'ignore': dst_id}

