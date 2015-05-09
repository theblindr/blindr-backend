from sqlalchemy import orm
import sqlalchemy

import boto
boto.config.load_from_path('./boto.cfg')
Session = orm.scoped_session(orm.sessionmaker())

engine = sqlalchemy.create_engine('sqlite://')
Session.configure(bind=engine)


