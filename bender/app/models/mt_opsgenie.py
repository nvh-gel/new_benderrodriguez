""" Data model for Opsgenie """
from opsgenie.swagger_client import AlertApi
from opsgenie.swagger_client import configuration
from opsgenie.swagger_client.rest import ApiException
from app.controllers.mt_config_handler import MTConfigHandler


configuration.api_key['Authorization'] = MTConfigHandler().get_config_section('opsgenie')['apikey']
configuration.api_key_prefix['Authorization'] = 'GenieKey'


class MTOpsgenie(object):
    """ Class model for opsgenie """
    __opsgenie = None

    def __init__(self):
        if not self.__opsgenie:
            self.__opsgenie = AlertApi()

    def get_alert_from_id(self, id):


    def get_alert_from_tiny_id(self, tinyId):
        pass

    def get_alert_from_alias(self, alias):
        pass
