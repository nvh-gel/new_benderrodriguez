""" View for Opsgenie """
from app.controllers.mt_opsgenie_handler import MTOpsgenieHandler


class Opsgenie(object):
    """ View for opsgenie route """
    def return_view(self, payload=None):
        """ Return status message for posted request to opsgenie route """
        if not payload:
            return "Bad request!\n", 400
        else:
            try:
                return MTOpsgenieHandler().mt_opsgenie_queue(payload)
            except KeyError:
                return "Bad request!\n", 400
