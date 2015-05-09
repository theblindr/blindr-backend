import unittest
from unittest import mock
from blindr.common import name_generator

class NameGeneratorTest(unittest.TestCase):
    @mock.patch('blindr.common.name_generator.random.choice')
    def test_generate_name(self, mock_random_choice):
        mock_random_choice.side_effect = lambda x: x[0]
        name_generator.nouns = ('foo',)
        name_generator.adjectives = ('bar',)

        self.assertEqual('Bar Foo', name_generator.generate_name())

