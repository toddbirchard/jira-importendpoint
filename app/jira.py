import os
import requests
import json
import pprint


def main():
    """Application Entry Point."""
    issues_json = fetch_public_jira_issues()
    for issue in issues_json['issues']:
        make_issue_body(issue)


def make_issue_body(issue):
    """Create a JSON body for each ticket."""
    body = {
        'key': issue['key'],
        'assignee': issue['fields']['assignee']['displayName'],
        'summary': issue['fields']['summary'],
        'status': issue['fields']['status']['name'],
        'priority': issue['fields']['priority']['name'],
        'rank': issue['fields']['priority']['id'],
        'issuetype': issue['fields']['issuetype']['name'],
        'epic_link': issue['fields']['customfield_10008'],
        'project': issue['fields']['project']['name'],
        'updated': issue['fields']['updated']
    }
    print(body)


def fetch_public_jira_issues():
    """Fetch all public-facing issues from JIRA instance."""
    endpoint = "https://hackersandslackers.atlassian.net/rest/api/3/search"
    jql = 'project in ("Hackers and Slackers", DevOps, hackersndslackers-api, linkbox, Roblog, Toddzilla, "Tableau Extraction", ghostthemes.io) AND status != Decline ORDER BY updated DESC'
    username = os.environ.get('JIRA_USERNAME')
    password = os.environ.get('JIRA_PASSWORD')
    print(username)
    print(password)
    headers = {
        "Accept": "application/json"
        }
    params = {
        "jql": jql
    }
    req = requests.get(endpoint,
                       headers=headers,
                       params=params,
                       auth=(username, password)
                       )
    # pp = pprint.PrettyPrinter(indent=4)
    response = req.json()
    return response


main()
