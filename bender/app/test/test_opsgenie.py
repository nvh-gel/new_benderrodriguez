""" Test cases for Opsgenie """
import unittest
import json
from app.app import BENDER as app


class BenderOpsgenieUnitTest(unittest.TestCase):
    """ Unit test for /opsgneie route """
    def setUp(self):
        super(BenderOpsgenieUnitTest, self).setUp()
        app.testing = True
        self.app = app.test_client()

    def test_get_opsgenie_route(self):
        """ Test get /opsgenie, expect 405 """
        response = self.app.get('/opsgenie')
        assert response.status_code == 405

    def test_post_opsgenie_route(self):
        """ Test post with empty payload to /opsgenie, expect 400 """
        payload = {}
        response = self.app.post('/opsgenie', data=json.dumps(payload))
        assert response.status_code == 400

    def test_post_opsgenie_not_valid(self):
        """ Test post with not valid field in payload """
        payload = {
            "test": "test"
        }
        response = self.app.post('/opsgenie', data=json.dumps(payload))
        assert response.status_code == 400

    def test_opsgenie_without_action(self):
        """ Test post with payload not contains action """
        payload = {
            "alert": {}
        }
        response = self.app.post('/opsgenie', data=json.dumps(payload))
        assert response.status_code == 400


if __name__ == '__main__':
    unittest.main()
