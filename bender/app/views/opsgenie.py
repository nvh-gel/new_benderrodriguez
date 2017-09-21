""" View for Opsgenie """
from app.controllers.mt_opsgenie_handler import mt_opsgenie_queue


class Opsgenie(object):
    """ View for opsgenie route """
    def return_view(self, payload=None):
        """ Return status message for posted request to opsgenie route """
        if not payload:
            return "Bad request!", 400
        else:
            return mt_opsgenie_queue(payload)
