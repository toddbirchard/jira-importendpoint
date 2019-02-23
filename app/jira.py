import os
import requests
import json
import pprint
import arrow
import pandas as pd
from . import r

issues_df = pd.DataFrame(columns=['key', 'assignee', 'summary', 'status', 'priority', 'issuetype', 'epic_name', 'updated', 'rank', 'timestamp', 'project'])


class JiraExporter:
    """Extract Issues from JORA instance."""

    issuecount = 0
    max_results = 100

    @classmethod
    def add_issues_to_df(cls, issues):
        """Create a JSON body for each ticket."""
        global issues_df
        for issue in issues:
            print(issue['fields']['updated'])
            date = arrow.get(issue['fields']['updated'])
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
                'updated': issue['fields']['updated'],
                'timestamp': date.timestamp
            }
            issues_df = issues_df.append(body, ignore_index=True)
            print('df = ', issues_df)

    @classmethod
    def fetch_public_jira_issues_by_page(cls, num_start, num_end):
        """Fetch all public-facing issues from JIRA instance."""
        global issues_df
        endpoint = r.get('jira_base_url')
        jql = r.get('jira_query')
        username = r.get('jira_user')
        password = r.get('jira_pass')
        headers = {
            "Accept": "application/json"
            }

        params = {
            "jql": jql,
            'maxResults': num_end,
            'startAt': num_start
        }
        req = requests.get(endpoint,
                           headers=headers,
                           params=params,
                           auth=(username, password)
                           )
        response = req.json()
        total_results = response['total']
        results_pulled = len(response['issues'])
        cls.add_issues_to_df(response['issues'])
        # Check
        cls.issuecount = cls.issuecount + results_pulled
        if cls.issuecount < total_results:
            if total_results - cls.issuecount < 100:
                end_at = total_results - cls.issuecount
                cls.fetch_public_jira_issues_by_page(cls.issuecount, end_at)
            else:
                cls.fetch_public_jira_issues_by_page(cls.issuecount, 100)
        else:
            return issues_df
