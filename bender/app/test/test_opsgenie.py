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

    def test_opsgenie_without_alert(self):
        """ Test post with payload not contain alert """
        payload = {
            "action": "addnote"
        }
        response = self.app.post('/opsgenie', data=json.dumps(payload))
        assert response.status_code == 400

    def test_opsgenie_valid_create(self):
        """ Test post with valid create payload """
        payload = {
            "action": "Create",
            "alert": {
                "alertId": "89b47797-bb11-4fc1-b611-492cb841e503",
                "alertType": 0,
                "alias": "Node 10.84.0.2:5550 for service i18n_api SG went down",
                "createdAt": 1506008195937,
                "entity": "",
                "insertedAt": 1506008195937000103,
                "message": " Node 10.84.0.2:5550 for service i18n_api SG went down",
                "priority": 2,
                "recipients": [],
                "source": "103.56.127.16",
                "tags": [
                "P0",
                "LIVE"
                ],
                "teams": [],
                "tinyId": "1851",
                "updatedAt": 1506008195937000103,
                "userFullName": "System",
                "userId": "",
                "username": "System"
            },
            "alertFlowContext": {
                "content": {},
                "requestId": "9387e622-33f1-403c-863b-f1af245796b9",
                "traceId": "9387e622-33f1-403c-863b-f1af245796b9"
            },
            "integrationId": "45b429ca-da65-4700-bb4c-aa3b4aacfce2",
            "integrationName": "MT Bender Rodriguez OUT",
            "integrationType": "Webhook",
            "source": {
                "name": "",
                "type": "API"
            }
        }
        response = self.app.post('/opsgenie', data=json.dumps(payload))
        assert response.status_code == 202


if __name__ == '__main__':
    unittest.main()
