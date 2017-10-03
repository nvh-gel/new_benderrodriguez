""" Unit Test for JIRA handler """
from unittest import TestCase
from jira import JIRA
from app.controllers.mt_jira_handler import MTJIRAHandler
from app.controllers.mt_utils import is_jira_key


class JIRAUnitTest(TestCase):
    """ Test cases for jira """
    def test_get_jira(self):
        """ Test getting jira, expect JIRA object """
        result = MTJIRAHandler().get_jira()
        assert isinstance(result, JIRA)

    # def test_jira_create_simple_ticket(self):
    #     """ Test creating jira, expect jira ticket key """
    #     result = MTJIRAHandler().create_jira_ticket('New Ticket')
    #     assert is_jira_key(result) is True

    # def test_jira_create_ticket_details(self):
    #     """ Test create jira ticket with detail,
    #     expect jira ticket key """
    #     result = MTJIRAHandler().create_jira_ticket('New detailed ticket',
    #                                                 project='BUG',
    #                                                 issuetype='Task',
    #                                                 priority='P3',
    #                                                 component='911',
    #                                                 labels=['test'],
    #                                                 description="this is just for testing")
    #     assert is_jira_key(result) is True
