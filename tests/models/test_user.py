from datetime import datetime
from freezegun import freeze_time
from unittest import mock
from tests.blindrtest import BlindrTest
from tests.factory_boy.user_factory import UserFactory

from blindr.models.user import User

class UserTests(BlindrTest):

    @freeze_time('2015-01-01')
    @mock.patch('blindr.models.user.name_generator.generate_name')
    @mock.patch('blindr.models.user.facebook.GraphAPI')
    def test_from_facebook_new_user(self, mock_graphapi, mock_generate_name):
        graph_instance = mock_graphapi.return_value
        graph_instance.get_object.return_value = {
            'id': '123123',
            'name': 'bob',
            'gender': 'male'
        }

        mock_generate_name.return_value = 'Fake Name'

        user = User.query.get('123123')
        self.assertIsNone(user)

        User.from_facebook('oauth_234234')

        mock_graphapi.assert_called_with(access_token='oauth_234234')
        graph_instance.get_object.assert_called_with(id='me')

        user = User.query.get('123123')
        self.assertIsNotNone(user)

        self.assertEqual('123123', user.id)
        self.assertEqual('oauth_234234', user.OAuth)
        self.assertEqual('m', user.gender)
        self.assertEqual(datetime(2015, 1, 1), user.last_poll)
        self.assertEqual('bob', user.real_name)
        self.assertEqual('Fake Name', user.fake_name)
        self.assertEqual('', user.facebook_urls)

    @freeze_time('2015-01-01')
    @mock.patch('blindr.models.user.facebook.GraphAPI')
    def test_from_facebook_update_user(self, mock_graphapi):
        graph_instance = mock_graphapi.return_value
        graph_instance.get_object.return_value = {
            'id': '123123',
            'name': 'bob',
            'gender': 'male'
        }

        UserFactory(
            id='123123',
            OAuth='oauth_old',
            gender='f',
            last_poll=datetime(2000,1,1),
            real_name='Alice'
        )

        user = User.query.get('123123')
        self.assertIsNotNone(user)

        User.from_facebook('oauth_234234')

        mock_graphapi.assert_called_with(access_token='oauth_234234')
        graph_instance.get_object.assert_called_with(id='me')

        user = User.query.get('123123')
        self.assertIsNotNone(user)

        self.assertEqual('123123', user.id)
        self.assertEqual('oauth_234234', user.OAuth)
        self.assertEqual('m', user.gender)
        self.assertEqual(datetime(2015, 1, 1), user.last_poll)
        self.assertEqual('bob', user.real_name)

