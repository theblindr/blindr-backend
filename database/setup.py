from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, CHAR, TIMESTAMP
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id =	Column(Integer, primary_key=True)

    OAuth = 	Column(String)
    fake_name =	Column(String(50), nullable = False)
    gender =	Column(CHAR, nullable = False)
    last_poll =	Column(TIMESTAMP)

class Match(Base):
    __tablename__ = 'matches'

    id =            	Column(Integer, primary_key=True)

    match_from_id = 	Column(Integer, ForeignKey('users.id'))
    match_to_id =	Column(Integer, ForeignKey('users.id'))
    mutual =		Column(Boolean)

engine = create_engine("postgresql://qcdqbomfqypdrm:BVwns35kY0XWQ1t3hDPYQij3GY@ec2-107-21-104-188.compute-1.amazonaws.com/d1hl252nm66p21", echo=True)

Base.metadata.create_all(engine)
