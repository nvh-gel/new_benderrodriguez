""" Test module for classify view """
from unittest import TestCase
from app.app import BENDER as app


class TestClassify(TestCase):
    """ Test cases for classify view """
    def setUp(self):
        super(TestClassify, self).setUp()
        app.testing = True
        self.app = app.test_client()

    def test_classify_response_code(self):
        """ test get classify view, expect 200 """
        response = self.app.get('/classify')
        assert response.status_code == 200
