from tests.blindrtest import BlindrTest
from unittest import mock
import json

class MessageTest(BlindrTest):
    @mock.patch('blindr.api.message.Event.create')
    def test_post_message_to_city(self, mock_create_event):
        mock_create_event.return_value = True

        rv = self.auth_post('events/message', data=dict(
            dst_city='Montreal',
            message='Hi!'
        ))

        self.assert_200(rv)
        rv_data = json.loads(rv.data.decode('utf-8'))

        mock_create_event.assert_called_with(dict(
            type='message',
            dst='city:montreal',
            src=self.auth_user.id,
            src_gender=self.auth_user.gender,
            message='Hi!',
            src_real_name=self.auth_user.real_name,
            src_fake_name=self.auth_user.fake_name
        ))

    @mock.patch('blindr.api.message.Event.create')
    def test_post_message_to_user(self, mock_create_event):
        mock_create_event.return_value = True

        rv = self.auth_post('events/message', data=dict(
            dst_user='bob',
            message='Hi!'
        ))

        self.assert_200(rv)
        rv_data = json.loads(rv.data.decode('utf-8'))

        mock_create_event.assert_called_with(dict(
            type='message',
            dst='user:bob',
            src=self.auth_user.id,
            src_gender=self.auth_user.gender,
            message='Hi!',
            src_real_name=self.auth_user.real_name,
            src_fake_name=self.auth_user.fake_name,
            participants='auth_user:bob'
        ))

    def test_post_message_dst_required(self):
        rv = self.auth_post('events/message', data=dict(
            message='Hi!'
        ))
        self.assert_status(rv, 422)

    def test_post_message_message_required(self):
        rv = self.auth_post('events/message', data=dict(
            dst_city='Montreal'
        ))
        self.assert_status(rv, 422)

    @mock.patch('blindr.api.message.Event.create')
    def test_post_message_dynamodb_failure(self, mock_create_event):
        mock_create_event.return_value = False

        rv = self.auth_post('events/message', data=dict(
            dst_user='bob',
            message='Hi!'
        ))

        self.assert_status(rv, 500)

    def test_message_auth(self):
        rv = self.client.post('/events/message')
        self.assert_401(rv)
