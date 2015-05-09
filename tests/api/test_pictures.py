from tests.blindrtest import BlindrTest
from tests.factory_boy.user_factory import UserFactory
from unittest import mock
import json

class PicturesTest(BlindrTest):

    @mock.patch('blindr.models.user.facebook.GraphAPI')
    def test_get_all_pictures(self, mock_graphapi):
        graph_instance = mock_graphapi.return_value
        graph_instance.get_connections.side_effect = [
            {'data':[{'id':'album_123123'}]},
            {'data':[{'images':[{'source':'http://image.url'}]}]}
        ]

        rv = self.auth_get('/pictures', query_string=dict(typeReq='all'))

        self.assert_200(rv)
        rv_data = json.loads(rv.data.decode('utf-8'))

        self.assertEqual(['http://image.url'], rv_data)

    def test_get_slideshow(self):
        UserFactory(
            id='user2',
            facebook_urls='http://image.url,http://foobar.com'
        )

        rv = self.auth_get('/pictures', query_string=dict(typeReq='slideshow', dst_id='user2'))

        self.assert_200(rv)
        rv_data = json.loads(rv.data.decode('utf-8'))

        self.assertEqual(['http://image.url', 'http://foobar.com'], rv_data)

    def test_auth(self):
        rv = self.client.get('/pictures')
        self.assert_401(rv)
