from unittest import mock
from boto.dynamodb2.layer1 import DynamoDBConnection

FakeDynamoDBConnection = mock.create_autospec(DynamoDBConnection)
patcher = mock.patch('boto.dynamodb2.layer1.DynamoDBConnection', autospec=True)
patcher.start()
