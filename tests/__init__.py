from sqlalchemy import orm
import sqlalchemy
Session = orm.scoped_session(orm.sessionmaker())

engine = sqlalchemy.create_engine('sqlite://')
Session.configure(bind=engine)


