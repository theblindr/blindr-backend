from flask_restful import Resource
from blindr import db
from tests.blindrtest import BlindrTest
from unittest import mock
import json

class AuthenticateTest(BlindrTest):
    def test_success_auth(self):
        rv = self.auth_get('/me')
        self.assert_200(rv)

    def test_no_x_token(self):
        rv = self.client.get('/me')
        self.assert_401(rv)

    def test_invalid_x_token(self):
        rv = self.client.get('/me', headers={'X-User-Token': 'foobar'})
        self.assert_401(rv)

    def test_invalid_user(self):
        db.session.expunge(self.auth_user)
        rv = self.auth_get('/me')
        self.assert_401(rv)

