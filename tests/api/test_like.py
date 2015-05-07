from tests.blindrtest import BlindrTest
from tests.factory_boy.match_factory import MatchFactory
from tests.factory_boy.user_factory import UserFactory
from blindr.models.match import Match
from unittest import mock
import json

class LikeTest(BlindrTest):

    def test_post_first_like(self):
        UserFactory(id='user2')

        rv = self.auth_post('/events/like', data=dict(dst_user='user2'))

        rv_data = json.loads(rv.data.decode('utf-8'))
        self.assert_200(rv)

        match = Match.query.get((self.auth_user.id,'user2'))
        self.assertIsNotNone(match)
        self.assertFalse(match.mutual)

    @mock.patch('blindr.api.like.Event.create')
    def test_post_match(self, mock_create_event):
        MatchFactory(
            match_from_id=UserFactory(id='user2').id,
            match_to_id=self.auth_user.id,
            mutual=False
        )

        rv = self.auth_post('/events/like', data=dict(dst_user='user2'))

        rv_data = json.loads(rv.data.decode('utf-8'))
        self.assert_200(rv)

        match = Match.query.get(('user2',self.auth_user.id))
        self.assertIsNotNone(match)
        self.assertTrue(match.mutual)

        mock_create_event.assert_any_call({
            'type': 'match',
            'participants': 'auth_user:user2',
            'dst': 'user:user2',
            'src': 'auth_user',
            'src_real_name': 'Auth User',
            'src_fake_name': 'Foo Bar'
        })

        mock_create_event.assert_any_call({
            'type': 'match',
            'participants': 'auth_user:user2',
            'dst': 'user:auth_user',
            'src': 'user2',
            'src_real_name': 'Realname',
            'src_fake_name': 'Fakename'
        })

    def test_like_unvalid_user(self):
        rv = self.auth_post('/events/like', data=dict(dst_user='foobar'))
        self.assert_status(rv, 422)

    def test_get_like_from_user(self):
        MatchFactory(
            match_from_id=self.auth_user.id,
            match_to_id=UserFactory(id='user2').id,
            mutual=False
        )

        rv = self.auth_get('/events/like')
        self.assert_200(rv)
        rv_data = json.loads(rv.data.decode('utf-8'))[0]

        self.assertEqual(rv_data, {
            'other': 'user2',
            'other_fake_name': 'Fakename',
            'mutual': False
        })

        self.assertNotIn('other_real_name', rv_data)

    def test_get_like_mutual_like_to_user(self):
        MatchFactory(
            match_from_id=UserFactory(id='user2').id,
            match_to_id=self.auth_user.id,
            mutual=True
        )

        rv = self.auth_get('/events/like')
        self.assert_200(rv)
        rv_data = json.loads(rv.data.decode('utf-8'))[0]

        self.assertEqual(rv_data, {
            'other': 'user2',
            'other_fake_name': 'Fakename',
            'other_real_name': 'Realname',
            'mutual': True
        })

    def test_get_like_non_mutual_like_to_user(self):
        MatchFactory(
            match_from_id=UserFactory(id='user2').id,
            match_to_id=self.auth_user.id,
            mutual=False
        )

        rv = self.auth_get('/events/like')
        self.assert_200(rv)
        rv_data = json.loads(rv.data.decode('utf-8'))

        self.assertEqual(0, len(rv_data))

    def test_like_auth(self):
        rv = self.client.post('/events/like', data=dict(dst_user='user2'))
        self.assert_401(rv)

        rv = self.client.get('/events/like')
        self.assert_401(rv)


