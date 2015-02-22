from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex
import uuid
import time

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
    def fetch(user, city, since):
        resultset = events.scan(
            dst__in=[
                'user:{}'.format(user),
                'city:{}'.format(city)
            ],
            sent_at__gte=since)

        items = [dict(item) for item in resultset]
        for item in items:
            item['sent_at'] = float(item['sent_at'])

        return sorted(items, key=lambda i: i['sent_at'])


