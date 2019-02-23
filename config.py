import os


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = os.environ["TESTING"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    FLASK_DEBUG = os.environ["FLASK_DEBUG"]
    SESSION_TYPE = os.environ["SESSION_TYPE"]
    REDIS_URL = os.environ["REDIS_URL"]

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_ECHO = os.environ["SQLALCHEMY_ECHO"]
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]

    # JIRA
    JIRA_BASE_URL = os.environ.get('JIRA_BASE_URL')
    JIRA_USERNAME = os.environ.get('JIRA_USERNAME')
    JIRA_PASSWORD = os.environ.get('JIRA_PASSWORD')
    JIRA_QUERY = os.environ.get('JIRA_QUERY')
