from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

r = FlaskRedis()
db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Set Global Session Variables
        r.init_app(app, charset="utf-8", decode_responses=True)
        r.set('sqlalchemy_uri', app.config['SQLALCHEMY_DATABASE_URI'])
        r.set('jira_base_url', app.config['JIRA_BASE_URL'])
        r.set('jira_user', app.config['JIRA_USERNAME'])
        r.set('jira_pass', app.config['JIRA_PASSWORD'])
        r.set('jira_query', app.config['JIRA_QUERY'])

        db.init_app(app)

        from . import routes
        from . import jira

        return app
