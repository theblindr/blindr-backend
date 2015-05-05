import factory.alchemy
from blindr.models.user import User
from blindr import db

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: str(n))

    fake_name = 'Fakename'
    real_name = 'Realname'
    gender = 'm'
