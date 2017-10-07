""" Handler for opsgenie """
# from app.controllers.mt_queue_handler import MTQueueHandler
from app.controllers.mt_jira_handler import MTJIRAHandler
from app.controllers.mt_utils import classify_issue
from app.models.mt_opsgenie import MTOpsgenie
from app.controllers.mt_io import print_stderr
from app.controllers.mt_utils import is_jira_key
from app.controllers.mt_config_handler import MTConfigHandler


class MTOpsgenieHandler(object):
    """ handling all opsgenie request """
    def mt_opsgenie_queue(self, payload=None):
        """ Put task on queue """
        try:
            alert = payload['alert']
            action = 'opsgenie_' + payload['action'].lower()
            # MTQueueHandler().enqueue(action, alert)
            return self.__getattribute__(action)(alert)
        except KeyError as exc:
            raise exc
        # return "Accepted.\n", 202

    def opsgenie_create(self, alert=None):
        """ handle opsgenie alert created event """
        pass

    def opsgenie_addtojira(self, alert=None):
        """ handle opsgenie alert add to jira event """
        try:
            if check_created_jira_ticket(alert):
                return "Already created JIRA ticket.\n", 202
            else:
                jira_dict = self.prepare_jira_detail_dict(alert)
                new_ticket = MTJIRAHandler().create_jira_ticket(alert['message'],
                                                                **jira_dict
                                                               )
                print_stderr("New ticket: " + new_ticket)
                return self.add_tags(alert_id=alert['alertId'], tags=[new_ticket]), 202
        except KeyError as err:
            return "Internal Error {}.\n".format(err.message), 500

    def get_alert(self, **kwargs):
        """ get opsgenie alert from either id, tiny id or alias """
        if 'alert_id' in kwargs:
            return MTOpsgenie().get_alert_from_id(kwargs['alert_id'])
        elif 'tiny_id' in kwargs:
            return MTOpsgenie().get_alert_from_tiny_id(kwargs['tiny_id'])
        elif 'alias' in kwargs:
            return MTOpsgenie().get_alert_from_alias(kwargs['alias'])
        else:
            return None

    def add_tags(self, alert_id=None, tags=None):
        """ add one or more tags into alert """
        if isinstance(tags, str):
            return MTOpsgenie().add_tags(alert_id=alert_id, tags=[tags])
        elif isinstance(tags, list):
            return MTOpsgenie().add_tags(alert_id=alert_id, tags=tags)
        else:
            return False

    def prepare_jira_detail_dict(self, alert=None):
        """ create a dict to create jira ticket """
        classified_dict = classify_issue(alert['message'])
        component = classified_dict['component']
        priority = classified_dict['priority']
        labels = ['push']
        opsgenie_alert = self.get_alert(alert_id=alert['alertId'])
        description = add_jira_opsgenie_syncback(opsgenie_alert.description, alert)
        jira_config = MTConfigHandler().get_config_section('jira')
        alias_field = jira_config['custom_fields']['opsgenie_alias']
        opsgenie_alias = alert['alias']
        jira_dict = {
            'component': component,
            'priority': priority,
            'labels': labels,
            'description': description,
            alias_field: opsgenie_alias
        }
        return jira_dict


def check_created_jira_ticket(alert=None):
    """ check if given alert have jira key tag
    if found return True
    else return False """
    tags = alert['tags']
    for tag in tags:
        if is_jira_key(tag):
            return True
    return False

def add_jira_opsgenie_syncback(description=None, alert=None):
    """ edit opsgenie description when create jira ticket
    to trace back to opsgenie alert """
    if description and alert:
        append = "\n|| Referrer | {}\nhttps://app.opsgenie.com/alert/V2#/show/{}/details"
        append = append.format(alert['userFullName'], alert['alertId'])
        result = description + append
        return result
