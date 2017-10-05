""" Test cases for Opsgenie """
from unittest import TestCase
import json
from app.app import BENDER as app
from app.controllers.mt_opsgenie_handler import MTOpsgenieHandler


class BenderOpsgenieUnitTest(TestCase):
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

    # def test_opsgenie_valid_create(self):
    #     """ Test post with valid create payload """
    #     payload = {
    #         "action": "Create",
    #         "alert": {
    #             "alertId": "89b47797-bb11-4fc1-b611-492cb841e503",
    #             "alertType": 0,
    #             "alias": "Node 10.84.0.2:5550 for service i18n_api SG went down",
    #             "createdAt": 1506008195937,
    #             "entity": "",
    #             "insertedAt": 1506008195937000103,
    #             "message": " Node 10.84.0.2:5550 for service i18n_api SG went down",
    #             "priority": 2,
    #             "recipients": [],
    #             "source": "103.56.127.16",
    #             "tags": [
    #                 "P0",
    #                 "LIVE"
    #             ],
    #             "teams": [],
    #             "tinyId": "1851",
    #             "updatedAt": 1506008195937000103,
    #             "userFullName": "System",
    #             "userId": "",
    #             "username": "System"
    #         },
    #         "alertFlowContext": {
    #             "content": {},
    #             "requestId": "9387e622-33f1-403c-863b-f1af245796b9",
    #             "traceId": "9387e622-33f1-403c-863b-f1af245796b9"
    #         },
    #         "integrationId": "45b429ca-da65-4700-bb4c-aa3b4aacfce2",
    #         "integrationName": "MT Bender Rodriguez OUT",
    #         "integrationType": "Webhook",
    #         "source": {
    #             "name": "",
    #             "type": "API"
    #         }
    #     }
    #     response = self.app.post('/opsgenie', data=json.dumps(payload))
    #     assert response.status_code == 202

    def test_addtojira_payload(self):
        """ test post add to jira payload to /opsgenie """
        payload = {
            "action": "AddToJIRA",
            "actorUserId": "477266bd-da69-4ec5-95ca-f08508fbe4bb",
            "alert": {
                "alertId": "ce07a005-dcfd-4aaf-bfff-2b9ca00cdfd5",
                "alertType": 0,
                "alias": "ce07a005-dcfd-4aaf-bfff-2b9ca00cdfd5",
                "createdAt": 1506933923196,
                "entity": "",
                "insertedAt": 1506933923196000109,
                "message": "[Zabbix] mylzdlivemtdb1.shdc - Free disk space is less than 12% on volume /",
                "priority": 2,
                "source": "Zabbix",
                "tags": [],
                "tinyId": "6757",
                "updatedAt": 1506933926998113946,
                "userFullName": "Hien Nguyen",
                "userId": "477266bd-da69-4ec5-95ca-f08508fbe4bb",
                "username": "nvhien2703@outlook.com"
            },
            "alertFlowContext": {
                "content": {
                "alertId": "ce07a005-dcfd-4aaf-bfff-2b9ca00cdfd5"
                },
                "requestId": "c37b8957-6e7e-4cb8-856e-04a7a5e1deb8",
                "traceId": "c37b8957-6e7e-4cb8-856e-04a7a5e1deb8"
            },
            "integrationId": "45b429ca-da65-4700-bb4c-aa3b4aacfce2",
            "integrationName": "MT Bender Rodriguez OUT",
            "integrationType": "Webhook",
            "source": {
                "name": "",
                "type": "web"
            }
        }
        response = self.app.post('/opsgenie', data=json.dumps(payload))
        assert response == 202

    def test_get_opsgenie_alert_by_id(self):
        """ Test get alert from opsgenie by id, expect dict """
        alert_id = 'ce07a005-dcfd-4aaf-bfff-2b9ca00cdfd5'
        alert = MTOpsgenieHandler().get_alert(alert_id=alert_id)
        assert isinstance(alert, dict)

    def test_get_alert_by_tinyid(self):
        """ Test get alert from tiny id, expect dict """
        tiny_id = '1'
        alert = MTOpsgenieHandler().get_alert(tiny_id=tiny_id)
        assert isinstance(alert, dict)

    def test_opsgenie_add_tag(self):
        """ Test add tag to opsgenie alert, expect success message """
        alert_id = 'ce07a005-dcfd-4aaf-bfff-2b9ca00cdfd5'
        response = MTOpsgenieHandler().add_tags(alert_id=alert_id, tags='test_tag')
        assert response == "Request will be processed"
