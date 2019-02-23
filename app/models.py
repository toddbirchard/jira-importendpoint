from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from .db import Base
import datetime as dt


class JiraIssue(Base):
    """Create JIRA Record per ticket."""

    __tablename__ = 'jira'
    key = Column(String(20), primary_key=True)
    assignee = Column(String(50), unique=False, nullable=False)
    summary = Column(String(100), unique=False, nullable=False)
    status = Column(String(50), unique=False, nullable=False)
    priority = Column(String(50), unique=False, nullable=False)
    issuetype = Column(Float, unique=False, nullable=False)
    epic_name = Column(String(50), unique=False)
    rank = Column(Integer, unique=False, nullable=False)
    epic_link = Column(String(50), unique=False)
    project = Column(String(50), unique=False)
    updated = Column(DateTime, unique=False)

    def __repr__(self):
        return '<Jira %r>' % self.title
