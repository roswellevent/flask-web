import unittest
import app


class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_case1(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def test_case2(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data, b'This is a simple Python Web for Demo Use')



