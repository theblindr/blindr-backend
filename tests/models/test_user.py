from datetime import datetime
from freezegun import freeze_time
from unittest import mock
from tests.blindrtest import BlindrTest

from blindr.models.user import User

class UserTests(BlindrTest):

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

        with freeze_time('2015-01-01'):
            User.from_facebook('oauth_234234')

            mock_graphapi.assert_called_with(access_token='oauth_234234')
            graph_instance.get_object.assert_called_with(id='me')

            user = User.query.first()

            self.assertEqual('123123', user.id)
            self.assertEqual('oauth_234234', user.OAuth)
            self.assertEqual('m', user.gender)
            self.assertEqual(datetime(2015, 1, 1), user.last_poll)
            self.assertEqual('bob', user.real_name)
            self.assertEqual('Fake Name', user.fake_name)
            self.assertEqual('', user.facebook_urls)

