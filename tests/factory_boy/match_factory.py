import factory.alchemy
from tests.factory_boy.user_factory import UserFactory
from blindr.models.match import Match
from blindr import db

class MatchFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Match
        sqlalchemy_session = db.session

    @staticmethod
    def mutual_match(user1,user2):
        MatchFactory(
            match_to_id=user2.id,
            match_from_id=user1.id,
            mutual=True
        )
        MatchFactory(
            match_to_id=user1.id,
            match_from_id=user2.id,
            mutual=True
        )

    match_from_id = factory.SubFactory(UserFactory)
    match_to_id = factory.SubFactory(UserFactory)
    mutual = False

