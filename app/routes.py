import json
import requests
from flask import current_app as app
from flask import make_response, request
from . import db
from . import r
from . import jira


@app.route('/', methods=['GET'])
def get_issues():
    """Get details of current user."""
    issues = jira.JiraExporter.fetch_public_jira_issues_by_page(0, 100)
    print('issues_df = ', issues)
    # return make_response(str(response), 200)
