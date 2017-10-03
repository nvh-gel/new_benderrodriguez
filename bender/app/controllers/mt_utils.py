""" Convenient function """
import re
from app.controllers.mt_config_handler import MTConfigHandler

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
    classifying_array = MTConfigHandler().get_config_section('classification')
    for issuetype in classifying_array:
        if next(iter(issuetype.keys())) in message.lower():
            details_issue = next(iter(issuetype.values()))
            for details_type in details_issue['details']:
                if next(iter(details_type.keys())) in message.lower():
                    return next(iter(details_type.values()))
            return details_issue['default']
    return {'project': 'BUG', 'issuetype': 'Bug', 'component': '911', 'priority': 'P1', 'team': ''}
