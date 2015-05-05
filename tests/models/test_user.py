from tests.blindrtest import BlindrTest
from blindr.models.user import User
from unittest import mock

class UserTests(BlindrTest):
    @mock.patch('blindr.models.user.facebook.GraphAPI')
    def test_from_facebook(self, mock_graphapi):
        graph_instance = mock_graphapi.return_value
        graph_instance.get_object.return_value = {
            'id': '123123',
            'name': 'bob',
            'gender': 'male'
        }

        User.from_facebook('234234')

        mock_graphapi.assert_called_with(access_token='234234')


