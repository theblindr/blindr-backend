from freezegun import freeze_time
from tests.blindrtest import BlindrTest
from blindr import db
from unittest import mock
from datetime import datetime
import json

class MeTest(BlindrTest):

    @freeze_time('2015-01-01')
    @mock.patch('blindr.api.events.Event.fetch')
    def test_get_events(self, mock_fetch):
        mock_fetch.return_value = [dict(foo='bar', sent_at=12300, src='user2')]

        rv = self.auth_get('/events')

        rv_data = json.loads(rv.data.decode('utf-8'))

        self.assert_200(rv)

        self.assertEqual([{
            'foo':'bar',
            'sent_at': 12300,
            'src': 'user2'
        }], rv_data)

        db.session.refresh(self.auth_user)
        self.assertEqual(datetime(2015,1,1), self.auth_user.last_poll)

        mock_fetch.assert_called_with(
            user='auth_user',
            since=946684800
        )

    def test_auth(self):
        rv = self.client.get('/events')
        self.assert_401(rv)


