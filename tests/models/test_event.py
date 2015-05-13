import tests.utils.fake_dynamodb
import unittest
from unittest.mock import MagicMock
from freezegun import freeze_time
import time
import boto

from blindr.models.event import Event, events

class EventTests(unittest.TestCase):
    @freeze_time('2015-01-01')
    def test_create(self):
        events.put_item = MagicMock(return_value = 'put_item_ret')

        event = Event.create({'foo': 'bar'})
        event_data = events.put_item.call_args[1]['data']
        self.assertEqual(event, 'put_item_ret')
        self.assertEqual(event_data['sent_at'], time.time())
        self.assertIsNotNone(event_data['event_id'])
        self.assertEqual(event_data['foo'], 'bar')

    def test_fetch_adjust_since(self):
        events.query_2 = MagicMock(return_value = [])
        Event.fetch(since=100060)

        self.assertEqual(100000, events.query_2.call_args[1]['sent_at__gte'])

    def test_fetch_city(self):
        events.query_2 = MagicMock(return_value = [])
        Event.fetch(city='some_city')

        city = events.query_2.call_args[1]['dst__eq']
        self.assertEqual('city:some_city', city)

    def test_fetch_user(self):
        events.query_2 = MagicMock(return_value = [])
        Event.fetch(city='some_user')

        user = events.query_2.call_args[1]['dst__eq']
        self.assertEqual('city:some_user', user)

    def test_fetch_float_sent_at(self):
        events.query_2 = MagicMock(return_value = [{'sent_at':'1.23'}])
        event = Event.fetch()[0]

        self.assertIs(type(event['sent_at']), float)

    def test_fetch_history_sort_participants_id(self):
        events.query_2 = MagicMock(return_value = [])

        Event.fetch_history('123','456')
        participants = events.query_2.call_args[1]['participants__eq']
        self.assertEqual('123:456', participants)

        Event.fetch_history('321','123')
        participants = events.query_2.call_args[1]['participants__eq']
        self.assertEqual('123:321', participants)

    def test_fetch_history_since(self):
        events.query_2 = MagicMock(return_value = [])

        Event.fetch_history('123','456', since=12300)
        events.query_2.assert_called_with(
                participants__eq='123:456',
                sent_at__gte=12300,
                index='participants-index')

    def test_fetch_history_float_sent_at(self):
        events.query_2 = MagicMock(return_value = [{'sent_at':'1.23'}])
        event = Event.fetch_history('123','321')[0]

        self.assertIs(type(event['sent_at']), float)

