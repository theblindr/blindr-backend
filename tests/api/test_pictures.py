from tests.blindrtest import BlindrTest
from tests.factory_boy.user_factory import UserFactory
from unittest import mock
import json

class PicturesTest(BlindrTest):

    def test_get_slideshow(self):
        UserFactory(
            id='user2',
            facebook_urls='http://image.url,http://foobar.com'
        )

        rv = self.auth_get('/pictures', query_string=dict(dst_id='user2'))

        self.assert_200(rv)
        rv_data = json.loads(rv.data.decode('utf-8'))

        self.assertEqual(['http://image.url', 'http://foobar.com'], rv_data)

    def test_auth(self):
        rv = self.client.get('/pictures')
        self.assert_401(rv)
