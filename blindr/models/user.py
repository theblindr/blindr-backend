from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, CHAR, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from datetime import datetime
import facebook
import blindr.name_generator
from blindr import db

import config

fb_gender_map = {
    'male': 'm',
    'female': 'f'
}

class User(db.Model):
    __tablename__ = 'users'

    id =	Column(String, primary_key=True)

    OAuth = 	Column(String)
    fake_name =	Column(String(50), nullable = False)
    real_name =	Column(String(50))
    gender =	Column(CHAR, nullable = False)
    last_poll =	Column(TIMESTAMP)
    facebook_urls = Column(String)

    @staticmethod
    def from_facebook(fb_token):
        user = None
        graph = facebook.GraphAPI(access_token=fb_token)
        fb_user = graph.get_object(id='me')

        session = config.session
        user = session.query(User).filter_by(id=fb_user['id']).first()
        if not user:
            user = User(id= fb_user['id'],
                    OAuth= fb_token,
                    fake_name= name_generator.generate_name(),
                    real_name= fb_user['name'],
                    gender= fb_gender_map[fb_user['gender'] or 'male'],
                    last_poll= datetime.utcnow(),
                    facebook_urls= "")

            session.add(user)

        else:
            user.OAuth= fb_token
            user.gender= fb_gender_map[fb_user['gender'] or 'male']
            user.last_poll= datetime.utcnow()
            user.real_name= fb_user['name']

        session.commit()
        return user
