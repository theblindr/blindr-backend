from flask.ext import restful
from authenticate import authenticate
from flask import request, abort, jsonify
import time


import config
from models import Event
from models import User, Match

class Like(restful.Resource):
    method_decorators=[authenticate]

    def post(self):
        # Create DB Match entry
        dst_id = request.form.get('dst_user')
        session = config.session

        # Target already liked, trigger "match"
        data_set = session.query(Match).filter_by(match_from_id="%s" % dst_id, match_to_id="%s" % self.user.id).all()
        if len(data_set) > 0:
            pass        # trigger l'event du match ici
        else: #
            try:
                match = Match(match_from_id=self.user.id, match_to_id="%s" % dst_id)
                session.add(match)
                session.commit()
            except IntegrityError:
                abort(500)

        return jsonify(status="ok")
