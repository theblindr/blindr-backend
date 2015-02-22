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
