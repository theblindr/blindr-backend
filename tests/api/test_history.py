from tests.blindrtest import BlindrTest
from unittest import mock
import json

class MeTest(BlindrTest):

    @mock.patch('blindr.api.history.Event.fetch_history')
    def test_get_history(self, mock_history):
        mock_history.return_value = [dict(foo='bar')]

        rv = self.auth_get('/events/user2', query_string=dict(since=12300))

        rv_data = json.loads(rv.data.decode('utf-8'))
        self.assert_200(rv)

        self.assertEqual([{'foo':'bar'}], rv_data)
        mock_history.assert_called_with(
            user='auth_user',
            other='user2',
            since=12300
        )

    def test_auth(self):
        rv = self.client.get('/events/city:montreal')
        self.assert_401(rv)

