from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt  import Bcrypt
from application.config import Config


db = SQLAlchemy()
loginManager = LoginManager()
bcrypt = Bcrypt()

from application.models import Question


def findQuestion(questionId):
    question = Question.query.get(questionId)
    return question.content



def create_app(config_class=Config()):
    # Initialize app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import routes
    from application.models import Question
    from application.auth.routes import auth
    from application.posts.routes import posts
    from application.main.routes import main
    from application.profile.routes import profile

    # Register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(profile)

    # Initialize plugins
    db.init_app(app)
    loginManager.init_app(app)
    bcrypt.init_app(app)

    # Add function to jinja global functions
    app.jinja_env.globals.update(findQuestion=findQuestion)

    # Create all tables
    with app.app_context():
        db.create_all()

    return app
