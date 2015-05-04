from flask.ext import restful
from blindr import app
from . import me, auth, events, message, like, dislike, pictures, history

api = restful.Api(app)

api.add_resource(me.Me, '/me')
api.add_resource(auth.Auth, '/auth')
api.add_resource(events.Events, '/events')
api.add_resource(message.Message, '/events/message')
api.add_resource(like.Like, '/events/like')
api.add_resource(dislike.Dislike, '/events/dislike')
api.add_resource(pictures.Pictures, '/events/pictures')
api.add_resource(history.History, '/events/<string:other_id>')

