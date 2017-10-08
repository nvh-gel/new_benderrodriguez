""" Handler for all JIRA action """
from app.models.mt_jira import MTJIRA
from app.controllers.mt_io import print_stderr
from jira import JIRAError


class MTJIRAHandler(object):
    """ Class handler for jira """
    _jira = None
    def get_jira(self):
        """ if jira is not set, init one, else return jira """
        if not self._jira:
            self._jira = MTJIRA()
        return self._jira

    def create_jira_ticket(self, summary, **kwargs):
        """ create jira ticket from given params """
        issue_dict = {
            'project': {
                'key': kwargs['project'] if 'project' in kwargs else 'BUG'
            },
            'summary': summary,
            'issuetype': kwargs['issuetype'] if 'issuetype' in kwargs else 'Bug',
            'priority': {
                'name': kwargs['priority'] if 'priority' in kwargs else 'P1',
            },
            'components': [{'name': kwargs['component']}] if 'component' in kwargs else [],
            'labels': kwargs['labels'] if 'labels' in kwargs else [],
            'description': kwargs['description'] if 'description' in kwargs else ""
        }
        for key, value in kwargs.items():
            if 'custom' in key:
                issue_dict[key] = value
        return self.get_jira().create_jira_ticket(issue_dict)

    def add_comment(self, ticket, comment):
        """ add a comment to jira ticket """
        print_stderr("adding comment {} to {}".format(comment, ticket))
        try:
            self.get_jira().add_comment(ticket, comment)
            return "Comment added.\n", 202
        except JIRAError as err:
            print_stderr(err.message)
            return "Internal error.\n", 500
