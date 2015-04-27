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
        typeReq = request.args.get('typeReq')
        
        if typeReq == 'slideshow':
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
                urls = [x['images'][0]['source'] for x in graph.get_connections(profile_picture_album_id, 'photos')['data']][:5]
                return urls
            else:
                abort(500)
        elif typeReq == 'all':
            facebook.GraphAPI(self.user.OAuth)
            graph = facebook.GraphAPI(self.user.OAuth)
            target_user_albums = graph.get_connections(self.user.id, 'albums')['data']
            profile_pictures_album = target_user_albums[0]
            profile_picture_album_id = profile_pictures_album['id']
            urls = [x['images'][0]['source'] for x in graph.get_connections(profile_picture_album_id, 'photos')['data']]
            return urls
        else:
            abort(500)




