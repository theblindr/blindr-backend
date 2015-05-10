from flask.ext import restful
from flask import request, abort
from blindr.common.authenticate import authenticate
import facebook

from blindr.models.event import Event
from blindr.models.user import User
from blindr.models.match import Match
from blindr import db

class Pictures(restful.Resource):
    method_decorators=[authenticate]

    def get(self):
        typeReq = request.args.get('typeReq')

        if typeReq == 'slideshow':
            dst_id = request.args.get('dst_id')
            user = User.query.get(dst_id)
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
			
    def post(self):
        facebookUrls = request.form.get('facebookUrls')
		
        self.user.facebook_urls = facebookUrls
        try:
            db.session.commit()
        except IntegrityError:
            abort(500)
	
        return jsonify(status="ok")



