import facebook
from datetime import datetime
from blindr import db
from blindr.common import name_generator

_fb_gender_map = {
    'male': 'm',
    'female': 'f'
}

class User(db.Model):
    __tablename__ = 'users'

    id =	db.Column(db.String, primary_key=True)

    OAuth = 	db.Column(db.String)
    fake_name =	db.Column(db.String(50), nullable = False)
    real_name =	db.Column(db.String(50))
    gender =	db.Column(db.CHAR, nullable = False)
    looking_for = db.Column(db.String)
    last_poll =	db.Column(db.TIMESTAMP)
    facebook_urls = db.Column(db.String)

    @staticmethod
    def from_facebook(fb_token):
        user = None
        graph = facebook.GraphAPI(access_token=fb_token)
        fb_user = graph.get_object(id='me')

        session = db.session
        user = session.query(User).filter_by(id=fb_user['id']).first()
        if not user:
            user = User(id= fb_user['id'],
                    OAuth= fb_token,
                    fake_name= name_generator.generate_name(),
                    real_name= fb_user['name'],
                    gender= _fb_gender_map[fb_user['gender'] or 'male'],
                    last_poll= datetime.utcnow(),
                    facebook_urls= "",
                    looking_for="")

            session.add(user)

        else:
            user.OAuth= fb_token
            user.gender= _fb_gender_map[fb_user['gender'] or 'male']
            user.last_poll= datetime.utcnow()
            user.real_name= fb_user['name']

        session.commit()
        return user
