from flask.ext import restful
from authenticate import authenticate
from flask import request, abort, jsonify
import time
from itertools import permutations
from sqlalchemy.exc import IntegrityError

import config
from models import Event
from models import User, Match

class Like(restful.Resource):
    method_decorators=[authenticate]

    def get(self):
        matches = config.session.query(Match).filter(
            (Match.match_from_id == self.user.id) |
            ((Match.match_to_id == self.user.id) & (Match.mutual == True))).all()

        return map(lambda m: {
                'other': m.match_to_id if m.match_from_id == self.user.id else m.match_from_id,
                'mutual': bool(m.mutual)
            }, matches)

    def post(self):
        # Create DB Match entry
        dst_id = request.form.get('dst_user')
        session = config.session

        other = session.query(User).filter(User.id==dst_id).first()
        if not other:
            abort(422)

        # Target already liked, trigger "match"
        match = session.query(Match).filter_by(
                match_from_id= dst_id,
                match_to_id= self.user.id).first()

        if match:
            participants = sorted([self.user, other])
            base = {
                'type': 'match',
                'participants': '{}:{}'.format(*[p.id for p in participants])
            }

            for (dst, src) in permutations(participants):
                base.update({
                    'dst': 'user:{}'.format(dst.id),
                    'src': src.id,
                    'src_real_name': src.real_name
                })
                Event.create(base)

            match.mutual = True
        else:
            match = Match(match_from_id= self.user.id, match_to_id= dst_id)
            session.add(match)


        try:
            session.commit()
        except IntegrityError:
            abort(500)

        return jsonify(status="ok")
