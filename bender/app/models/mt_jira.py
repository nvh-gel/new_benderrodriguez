""" Data model for JIRA """
from jira import JIRA
from app.controllers.mt_config_handler import MTConfigHandler


class MTJIRA(object):
    """ Data model for jira """
    _jira = None

    def get_jira(self):
        """ Return jira connection from config
        if not exist init one """
        if not self._jira:
            jira_config = MTConfigHandler().get_config_section('jira')
            self._jira = JIRA(
                jira_config['host'],
                basic_auth=(jira_config['id'], jira_config['password'])
            )
        return self._jira

    def create_jira_ticket(self, issue_dict=None):
        """ Create jira ticket from given dict """
        new_ticket = self.get_jira().create_issue(fields=issue_dict)
        return new_ticket.key

    def add_comment(self, issue, comment):
        """ Add a note to JIRA issue """
        return self.get_jira().add_comment(issue, comment)
