from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, CHAR, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from datetime import datetime
import facebook

import config

Base = declarative_base()

fb_gender_map = {
    'male': 'm',
    'female': 'f'
}

class User(Base):
    __tablename__ = 'users'

    id =	Column(String, primary_key=True)

    OAuth = 	Column(String)
    fake_name =	Column(String(50), nullable = False)
    gender =	Column(CHAR, nullable = False)
    last_poll =	Column(TIMESTAMP)

    @staticmethod
    def from_facebook(fb_token):
        user = None
        graph = facebook.GraphAPI(access_token=fb_token)
        fb_user = graph.get_object(id='me')

        session = config.Session()
        user = session.query(User).filter_by(id=fb_user['id']).first()
        if not user:
            user = User(id= fb_user['id'],
                    OAuth= fb_token,
                    fake_name= 'test {}'.format(id),
                    gender= fb_gender_map[fb_user['gender'] or 'male'],
                    last_poll= datetime.utcnow())

            session.add(user)
            session.commit()

        return user
