from blindr import db


class Match(db.Model):
    __tablename__ = 'matches'

    match_from_id = 	db.Column(db.String, db.ForeignKey('users.id'))
    match_to_id =	db.Column(db.String, db.ForeignKey('users.id'))
    mutual =		db.Column(db.Boolean)

    __table_args__ = (db.PrimaryKeyConstraint('match_from_id', 'match_to_id'),)
