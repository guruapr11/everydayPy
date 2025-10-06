from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Database instances
db = SQLAlchemy()
migrate = Migrate()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .views import main_bp
    app.register_blueprint(main_bp)

    # Create DB tables if not using migrations
    with app.app_context():
        from . import models  # noqa: F401 - ensure models are registered
        db.create_all()

    return app
