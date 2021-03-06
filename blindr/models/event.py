from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex
from boto.dynamodb2.types import NUMBER
import uuid
import time
from datetime import timedelta

# Indexes must support 2 query type:
#  * Query events to a user since last poll
#  * Query all message between two user
events = Table('blindr_events', schema=[
    HashKey('dst'),
    RangeKey('sent_at', data_type=NUMBER)
], throughput={
    'read': 10,
    'write': 10
}, global_indexes=[
    GlobalAllIndex('participants-index', parts=[
        HashKey('participants'),
        RangeKey('sent_at', data_type=NUMBER)
    ], throughput={
        'read':10,
        'write':10
    })
])

_ADJUSTED_DELAY = 5

class Event(object):

    @staticmethod
    def create(data):
        data['sent_at'] = time.time()
        data['event_id'] = str(uuid.uuid4())
        return events.put_item(data=data)

    @staticmethod
    def fetch(user=None, city=None, since=60):
        adjusted_since = since - 60
        dst = ''

        if user:
            dst = 'user:{}'.format(user)
        if city:
            dst = 'city:{}'.format(city)

        resultset = events.query_2(
            dst__eq=dst,
            sent_at__gte=adjusted_since)

        items = [dict(item) for item in resultset]
        for item in items:
            item['sent_at'] = float(item['sent_at'])

        return items

    @staticmethod
    def fetch_history(user, other,since=0):
        resultset = events.query_2(
            participants__eq= '{}:{}'.format(*sorted([user,other])),
            index= 'participants-index',
            sent_at__gte=since)

        items = [dict(item) for item in resultset]
        for item in items:
            item['sent_at'] = float(item['sent_at'])

        return list(items)

