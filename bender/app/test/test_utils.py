""" Unit Test for utils functions """
from unittest import TestCase
from app.controllers.mt_utils import is_jira_key
from app.controllers.mt_utils import classify_issue


class UtilsUnitTest(TestCase):
    """ Test cases for utils functions """
    def test_jira_key(self):
        """ test normal string, expect false """
        result = is_jira_key('randomstring')
        assert result is False

    def test_jira_lower(self):
        """ test jira key lower case, expect false """
        result = is_jira_key('abc-123')
        assert result is False

    def test_jira_valid(self):
        """ test jira valid key, expect true """
        result = is_jira_key('TEST-111')
        assert result is True

    def test_classification(self):
        """ test classification, expect classified dict """
        result = classify_issue("idlzdlivestg1.iddc Free disk space is less than 12% on volume /")
        expected_result = {
            'project': 'BUG',
            'issuetype': 'Bug',
            'component': 'Infrastructure',
            'priority': 'P2',
            'team': 'z_infra_auto_alerting'
        }
        self.assertDictEqual(result, expected_result)

    def test_classify_db_free_space(self):
        """ test classification for free space on db, expect classified dict """
        result = classify_issue("mylzdlivemtdb1.shdc Free disk space is less than 12% on volume /")
        expected_result = {
            'project': 'BUG',
            'issuetype': 'Bug',
            'component': 'Infrastructure',
            'priority': 'P1',
            'team': 'infra_db_team'
        }
        self.assertDictEqual(result, expected_result)

    def test_classify_default_space(self):
        """ test classification for free space, expect classifiied dict """
        result = classify_issue("Free disk space")
        expected_result = {
            'project': 'BUG',
            'issuetype': 'Bug',
            'component': 'Infrastructure',
            'priority': 'P1',
            'team': 'infra_system_team_tier_1'
        }
        self.assertDictEqual(result, expected_result)
