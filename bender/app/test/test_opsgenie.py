""" Test cases for Opsgenie """
from unittest import TestCase
import json
from app.app import BENDER as app
from app.controllers.mt_opsgenie_handler import MTOpsgenieHandler
from opsgenie.swagger_client.models import Alert


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

    def test_opsgenie_valid_create(self):
        """ Test post with valid create payload """
        payload = {
            "action": "Create",
            "actorUserId": "477266bd-da69-4ec5-95ca-f08508fbe4bb",
            "alert": {
                "alertId": "68cbcf70-3d39-4b99-9b79-0eb1e85a205c",
                "alertType": 0,
                "alias": "68cbcf70-3d39-4b99-9b79-0eb1e85a205c",
                "createdAt": 1507738044302,
                "entity": "",
                "insertedAt": 1507738044302000106,
                "message": "[Zabbix] idlzdlivedb6.iddc - Number of concurrent connections for bob_live superior to 25",
                "priority": 4,
                "recipients": [],
                "source": "Zabbix",
                "tags": [],
                "teams": [],
                "tinyId": "8373",
                "updatedAt": 1507738044302000106,
                "userFullName": "Zabbix",
                "userId": "477266bd-da69-4ec5-95ca-f08508fbe4bb",
                "username": "Zabbix"
            },
            "alertFlowContext": {
                "content": {},
                "requestId": "b93928c9-b29b-4b4c-a1fe-7619d83a7355",
                "traceId": "b93928c9-b29b-4b4c-a1fe-7619d83a7355"
            },
            "integrationId": "45b429ca-da65-4700-bb4c-aa3b4aacfce2",
            "integrationName": "MT Bender Rodriguez OUT",
            "integrationType": "Webhook",
            "source": {
                "name": "web",
                "type": "API"
            }
        }
        response = self.app.post('/opsgenie', data=json.dumps(payload))
        assert response.status_code == 202

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
        assert response.status_code == 202

    def test_addtojira_with_tag_payload(self):
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
                "tags": ["BUG-123"],
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
        assert response.data.decode('utf-8') == "Already created JIRA ticket.\n"

    def test_get_opsgenie_alert_by_id(self):
        """ Test get alert from opsgenie by id, expect dict """
        alert_id = 'ce07a005-dcfd-4aaf-bfff-2b9ca00cdfd5'
        alert = MTOpsgenieHandler().get_alert(alert_id=alert_id)
        assert isinstance(alert, Alert)

    def test_get_alert_by_tinyid(self):
        """ Test get alert from tiny id, expect dict """
        tiny_id = '1'
        alert = MTOpsgenieHandler().get_alert(tiny_id=tiny_id)
        assert isinstance(alert, Alert)

    def test_opsgenie_add_tag(self):
        """ Test add tag to opsgenie alert, expect success message """
        alert_id = 'ce07a005-dcfd-4aaf-bfff-2b9ca00cdfd5'
        response = MTOpsgenieHandler().add_tags(alert_id=alert_id, tags='test_tag')
        assert response == "Request will be processed"

    def test_opsgenie_add_note(self):
        """ Test opsgenie alert add note handling, expect success message """
        payload = {
            "action": "AddNote",
            "actorUserId": "477266bd-da69-4ec5-95ca-f08508fbe4bb",
            "alert": {
                "alertId": "ce07a005-dcfd-4aaf-bfff-2b9ca00cdfd5",
                "alertType": 0,
                "alias": "ce07a005-dcfd-4aaf-bfff-2b9ca00cdfd5",
                "createdAt": 1506933923196,
                "entity": "",
                "insertedAt": 1506933923196000109,
                "message": "[Zabbix] mylzdlivemtdb1.shdc - Free disk space is less than 12% on volume /",
                "note": "test something",
                "priority": 2,
                "source": "Zabbix",
                "tags": [
                    "BUG-10",
                    "BUG-11",
                    "BUG-12",
                    "BUG-13",
                    "BUG-14",
                    "BUG-15",
                    "BUG-16",
                    "BUG-17",
                    "BUG-18",
                    "BUG-19",
                    "BUG-20",
                    "BUG-21",
                    "BUG-22",
                    "BUG-23",
                    "BUG-24",
                    "BUG-25",
                    "BUG-26",
                    "BUG-27",
                    "BUG-28",
                    "BUG-29"
                ],
                "tinyId": "6757",
                "updatedAt": 1507352982389000159,
                "userFullName": "Hien Nguyen",
                "userId": "477266bd-da69-4ec5-95ca-f08508fbe4bb",
                "username": "nvhien2703@outlook.com"
            },
            "alertFlowContext": {
                "content": {
                    "alertId": "ce07a005-dcfd-4aaf-bfff-2b9ca00cdfd5"
                },
                "requestId": "fa1ffd45-4695-4b5a-9f68-4b10d5379960",
                "traceId": "fa1ffd45-4695-4b5a-9f68-4b10d5379960"
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
        assert response.status_code == 202
