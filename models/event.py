from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex
import uuid
import time
from datetime import timedelta

events = Table('blindr_events', schema=[
    HashKey('dst'),
    RangeKey('sent_at')
], throughput={
    'read': 1,
    'write': 1
}, global_indexes=[])

class Event(object):

    @staticmethod
    def create(data):
        data['sent_at'] = time.time()
        data['event_id'] = str(uuid.uuid4())
        return events.put_item(data=data)

    @staticmethod
    def fetch(user=None, city=None, since=15):
        adjusted_since = since - 15
        filters = []
        if user:
            filters.append('user:{}'.format(user))
        if city:
            filters.append('city:{}'.format(city))

        resultset = events.scan(
            dst__in=filters,
            sent_at__gte=adjusted_since)

        items = [dict(item) for item in resultset]
        for item in items:
            item['sent_at'] = float(item['sent_at'])

        return sorted(items, key=lambda i: i['sent_at'])


