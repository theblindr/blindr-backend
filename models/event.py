from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex

events = Table('blindr_events', schema=[
    HashKey('dest'),
    RangeKey('sent_at')
], global_indexes=[])

class Event(object):

    @staticmethod
    def create(data):
        return events.put_item(data=data)

    @staticmethod
    def fetch(dst, since):
        resultset = events.query_2(
            dest__eq=dst,
            sent_at__gte=since)

        items = [dict(item) for item in resultset]
        for item in items:
            item['sent_at'] = int(item['sent_at'])

        return items


