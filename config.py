from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

secret = 'f4babeae21e325df1ff6656d79a5ff0ceac02635'
engine = create_engine(os.environ.get('DATABASE_URL'), echo=True)
session = scoped_session(sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine))

Base = declarative_base()
Base.query = session.query_property()

