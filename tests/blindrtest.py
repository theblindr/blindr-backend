import unittest
from datetime import datetime
from blindr import create_app, db
from flask.ext.testing import TestCase
from tests.factory_boy.user_factory import UserFactory
import itsdangerous

class BlindrTest(TestCase):
    def create_app(self):
        return create_app('config.test')

    def setUp(self):
        db.create_all()
        self.auth_user = UserFactory(
            id='auth_user',
            fake_name='Foo Bar',
            real_name='Auth User',
            last_poll=datetime(2000,1,1)
        )

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def auth_post(self, *args, **kwargs):
        self._add_header_auth_token(kwargs)
        return self.client.post(*args, **kwargs)

    def auth_get(self, *args, **kwargs):
        self._add_header_auth_token(kwargs)
        return self.client.get(*args, **kwargs)

    def _add_header_auth_token(self, kwargs):
        s = itsdangerous.Signer(self.app.config['AUTH_SECRET'])
        token = s.sign(b'auth_user').decode('utf-8')

        if not 'headers' in kwargs:
            kwargs['headers'] = {}

        kwargs['headers']['X-User-Token'] = token

