from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, CHAR, TIMESTAMP
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Match(Base):
    __tablename__ = 'matches'

    id =            	Column(Integer, primary_key=True)

    match_from_id = 	Column(Integer, ForeignKey('users.id'))
    match_to_id =	Column(Integer, ForeignKey('users.id'))
    mutual =		Column(Boolean)
