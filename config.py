from sqlalchemy import create_engine
import os

secret = 'f4babeae21e325df1ff6656d79a5ff0ceac02635'
engine = create_engine(os.environ.get('DATABASE_URL'), echo=True)
