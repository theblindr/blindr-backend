from flask.ext import restful
from authenticate import authenticate
from flask import request, abort, jsonify
import time
from itertools import permutations
from sqlalchemy.exc import IntegrityError
import facebook

import config
from models import Event
from models import User, Match

class Pictures(restful.Resource):
    method_decorators=[authenticate]

    def get(self):
        dst_id = request.args.get('dst_id')
        match = config.session.query(Match).filter(
            (Match.match_from_id == self.user.id) |
            ((Match.match_to_id == self.user.id) & (Match.mutual == True)))

        if match is not None: #matches found, serve pictures

            target_user = config.session.query(User).filter(User.id==dst_id).first()
            facebook.GraphAPI(target_user.OAuth)
            graph = facebook.GraphAPI(target_user.OAuth)
            target_user_albums = graph.get_connections(target_user.id, 'albums')['data']
            profile_pictures_album = target_user_albums[0]
            profile_picture_album_id = profile_pictures_album['id']
            photos = graph.get_connections(profile_picture_album_id, 'photos')
            urls = []
            numberFetched = 0
            for x in photos['data']
                urls.append(x['images'][0]['source'])
                numberFetched = numberFetched + 1
                if numberFetched >= 5
                    return urls
            return urls
        else:
            abort(500)




