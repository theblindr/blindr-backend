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
            user = config.session.query(User).filter(
                User.id==dst_id)
            if user:
                return user.facebook_urls.split(",")
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




