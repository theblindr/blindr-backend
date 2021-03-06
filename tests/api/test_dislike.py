from tests.blindrtest import BlindrTest
from tests.factory_boy.match_factory import MatchFactory
from tests.factory_boy.user_factory import UserFactory
from blindr.models.match import Match
from unittest import mock
import json

class DislikeTest(BlindrTest):

    def test_post_dislike(self):
        MatchFactory(
            match_from_id=self.auth_user.id,
            match_to_id=UserFactory(id='user2').id,
            mutual=True
        )

        rv = self.auth_post('/events/dislike', data=dict(dst_user='user2'))

        rv_data = json.loads(rv.data.decode('utf-8'))
        self.assert_200(rv)
        self.assertEqual('user2', rv_data['ignore'])
        self.assertIsNone(Match.query.get((self.auth_user.id,'user2')))

    def test_dislike_auth(self):
        rv = self.client.post('/events/dislike', data=dict(dst_user='user2'))
        self.assert_401(rv)

