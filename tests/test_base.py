import unittest
from app import app

class TestBase(unittest.TestCase):
    def setUp(self):
        # this statement will be executed before testing
        self.app = app.test_client()
    # def tearDown(self):
        # this statement will be executed after testing