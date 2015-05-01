import tests.utils.fake_dynamodb
import unittest
from unittest.mock import MagicMock
from models.event import Event, events
from freezegun import freeze_time
import time

class EventTests(unittest.TestCase):
    def test_create(self):
        events.put_item = MagicMock(return_value = 'put_item_ret')

        with freeze_time('2015-01-01'):
            event = Event.create({'foo': 'bar'})
            event_data = events.put_item.call_args[1]['data']
            self.assertEqual(event, 'put_item_ret')
            self.assertEqual(event_data['sent_at'], time.time())
            self.assertIsNotNone(event_data['event_id'])
            self.assertEqual(event_data['foo'], 'bar')

