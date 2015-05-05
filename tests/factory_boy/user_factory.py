import factory
from blindr.models.user import User
from tests import Session

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = tests.Session

    id = factory.Sequence(lambda n: n)

    fake_name = 'Fakename'
    real_name = 'Realname'
    gender = 'm'
