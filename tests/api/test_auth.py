from tests.blindrtest import BlindrTest
from tests.factory_boy.user_factory import UserFactory
from unittest import mock
import json

class AuthTest(BlindrTest):

    @mock.patch('blindr.api.auth.User.from_facebook')
    def test_success_auth(self, mock_user):
        user = UserFactory.create(id='123123')
        mock_user.return_value = user

        rv = self.client.post('/auth', data=dict(fb_token='token_123'))

        mock_user.assert_called_with('token_123')

        rv_data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(200, rv.status_code)
        self.assertEqual('123123.kCcEmo-jm_mfDTcDRRE5JN9R3Vk', rv_data['token'])

    @mock.patch('blindr.api.auth.User.from_facebook')
    def test_failure_auth(self, mock_user):
        mock_user.return_value = None

        rv = self.client.post('/auth', data=dict(fb_token='token_123'))

        rv_data = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(401, rv.status_code)
        self.assertEqual(401, rv_data['status'])
        self.assertEqual('Unauthorized', rv_data['message'])
        self.assertNotIn('token', rv_data)
