""" Test basic page """
import unittest
from app import BENDER as app


class BenderHomeUnitTest(unittest.TestCase):
    """ For unit testing bender homepage """
    def setUp(self):
        super(BenderHomeUnitTest, self).setUp()
        app.testing = True
        self.app = app.test_client()

    def test_home_code(self):
        """ Test home response code, expect 200 """
        response = self.app.get('/')
        assert response.status_code == 200

    # def test_home_response(self):
    #     """ Test home page response, exect content """
    #     response = self.app.get('/')
    #     assert "Hello world" in response.text


if __name__ == '__main__':
    unittest.main()
