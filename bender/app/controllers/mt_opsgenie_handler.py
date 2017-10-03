""" Handler for opsgenie """
# from app.controllers.mt_queue_handler import MTQueueHandler
from app.controllers.mt_jira_handler import MTJIRAHandler
from app.controllers.mt_utils import classify_issue
from app.models.mt_opsgenie import MTOpsgenie


class MTOpsgenieHandler(object):
    """ handling all opsgenie request """
    def mt_opsgenie_queue(self, payload=None):
        """ Put task on queue """
        try:
            alert = payload['alert']
            action = 'opsgenie_' + payload['action'].lower()
            # MTQueueHandler().enqueue(action, alert)
            self.__getattribute__(action)(alert)
        except KeyError as exc:
            raise exc
        return "Accepted.\n", 202

    def opsgenie_create(self, alert=None):
        """ handle opsgenie alert created event """
        pass

    def opsgenie_addtojira(self, alert=None):
        """ handle opsgenie alert add to jira event """
        try:
            classified_dict = classify_issue(alert['message'])
            opsgenie_alert = MTOpsgenieHandler().get_alert(id=alert['alertId'])
            description = opsgenie_alert['description']
        except KeyError:
            return "Internal Error.\n", 500
        MTJIRAHandler().create_jira_ticket(alert['message'],
                                           component=classified_dict['component'],
                                           priority=classified_dict['priority'],
                                           labels=['push'],
                                           description=description,
                                           opsgenie_alert=alert['alias']
                                          )

    def get_alert(self, *args, **kwargs):
        """ get opsgenie alert from either id, tiny id or alias """
        if 'id' in kwargs:
            return MTOpsgenie().get_alert_from_id(kwargs['id'])
        elif 'tinyId' in kwargs:
            return MTOpsgenie().get_alert_from_tiny_id(kwargs['tinyId'])
        elif 'alias' in kwargs:
            return MTOpsgenie().get_alert_from_alias(kwargs['alias'])
        else:
            return None
