""" Test module for classify view """
import json
from unittest import TestCase
from app.app import BENDER as app
# from app.controllers.mt_io import print_stderr


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

    def test_classify_disk_space(self):
        """ test get classify json, expect classification dict """
        response = self.app.get('/classify?issue=Free disk space&json')
        result = json.loads(response.data)
        expect_result = {
            "component": "Infrastructure",
            "issuetype": "Bug",
            "priority": "P1",
            "project": "BUG",
            "team": "infra_system_team_tier_1"
        }
        self.assertDictEqual(result, expect_result)
