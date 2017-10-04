""" Data model for Opsgenie """
from opsgenie.swagger_client import AlertApi
from opsgenie.swagger_client import configuration
from opsgenie.swagger_client.rest import ApiException
from opsgenie.swagger_client.models import *
from app.controllers.mt_config_handler import MTConfigHandler


configuration.api_key['Authorization'] = MTConfigHandler().get_config_section('opsgenie')['apikey']
configuration.api_key_prefix['Authorization'] = 'GenieKey'


class MTOpsgenie(object):
    """ Class model for opsgenie """
    __opsgenie = None

    def __init__(self):
        if not self.__opsgenie:
            self.__opsgenie = AlertApi()

    def get_alert_from_id(self, alert_id):
        """ Get opsgenie alert from given alert ID """
        try:
            response = AlertApi().get_alert(identifier=alert_id)
            return response.data.__dict__
        except ApiException as err:
            raise err

    def get_alert_from_tiny_id(self, tiny_id):
        """ Get opsgenie alert from given tiny ID """
        try:
            response = AlertApi().get_alert(identifier=tiny_id, identifier_type='tiny')
            return response.data.__dict__
        except ApiException as err:
            raise err

    def get_alert_from_alias(self, alias):
        """ Get Opsgenie alert from given alias """
        try:
            response = AlertApi().get_alert(identifier=alias, identifier_type='alias')
            return response.data.__dict__
        except ApiException as err:
            raise err

    def add_tags(self, alert_id=None, tags=None):
        """ Add the list of tags to opsgenie alert """
        try:
            body = AddAlertTagsRequest(tags=tags)
            response = AlertApi().add_tags(identifier=alert_id, body=body)
            return response.result
        except ApiException as err:
            raise err
