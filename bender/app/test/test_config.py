""" Test config page """
import unittest
from app.app import BENDER as app
import json


class TestConfigPage(unittest.TestCase):
    """ Unit testing config page """
    def setUp(self):
        super(TestConfigPage, self).setUp()
        app.testing = True
        self.app = app.test_client()

    def test_config_response_code(self):
        """ Test response code for /config, expect 200 """
        response = self.app.get('/config')
        assert response.status_code == 200

    def test_config_response_page(self):
        """ Test response page for /config, expect html content """
        response = self.app.get('/config')
        assert response.headers['content-type'] == "text/html; charset=utf-8"

    # def test_post_config_response_code(self):
    #     """ Test posting to /config, expect 202 """
    #     response = self.app.post('/config')
    #     assert response.status_code == 202

    def test_json_config_response_code(self):
        """ Test response code for /config/json, expect 200 """
        response = self.app.get('/config/json')
        assert response.status_code == 200

    def test_json_config_content(self):
        """ Test response code for /config/json, expect dict """
        response = self.app.get('/config/json')
        config = json.loads(response.data)
        assert isinstance(config, dict)
