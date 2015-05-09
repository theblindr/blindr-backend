import unittest

class FailTest(unittest.TestCase):
    def test_fail(self):
        self.assertTrue(False)
