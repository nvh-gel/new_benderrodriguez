""" Convenient function """
import re
from app.controllers.mt_config_handler import MTConfigHandler
from app.controllers.mt_io import print_stderr


def is_jira_key(key):
    """ Check passed string is jira or not,
    if valid return true
    else return false """
    regex_jira = r'^[A-Z]{1,9}-[0-9]{1,9}$'
    match = re.match(regex_jira, key)
    if match:
        return True
    else:
        return False


def classify_issue(message):
    """ Classify issue type, team, component
    accept alert message
    return dict of classification """
    classifying_dict = MTConfigHandler().get_config_section('classification')
    return browse_classifying_dict(message.lower(), issue_dict=classifying_dict)


def browse_classifying_dict(issue, issue_dict=None):
    """ Keep browsing classfying tree
    till no more details """
    if 'details' not in issue_dict:
        return issue_dict.get('default', {})
    else:
        for issue_details in issue_dict['details']:
            issue_key = next(iter(issue_details.keys()))
            if issue_key in issue:
                print_stderr(issue_key)
                return browse_classifying_dict(issue, issue_dict=issue_details[issue_key])
        return issue_dict.get('default', {})
