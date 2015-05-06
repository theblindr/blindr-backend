from tests.blindrtest import BlindrTest
from unittest import mock
import json

class MeTest(BlindrTest):

    def test_post_first_like(self):
        rv = self.auth_get('/me')

        rv_data = json.loads(rv.data.decode('utf-8'))
        self.assert_200(rv)

        self.assertEqual(self.auth_user.id, rv_data['id'])
        self.assertEqual(self.auth_user.gender, rv_data['gender'])

    def test_auth(self):
        rv = self.client.get('/me')
        self.assert_401(rv)

