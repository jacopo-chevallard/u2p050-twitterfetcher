from flask import Flask, redirect
from config import DevelopmentConfig, ProductionConfig, TestConfig
import os
from .auth.auth import valid_auth_required
from .dash.cache import init_cache

def init_app():
    """Initialize the core application

    :return:
    """

    app = Flask(__name__, static_folder="./static", template_folder="./static/layouts")

    # Set up the config variables
    app.config.from_object(DevelopmentConfig)

    if os.getenv("FLASK_ENV") == "production":
        print("You are in Production Mode")
        app.config.from_object(ProductionConfig)
    elif os.getenv("FLASK_ENV") == "testing":
        print("You are in Testing Mode")
        app.config.from_object(TestConfig)

    cache, app = init_cache(app)

    with app.app_context():
        from .auth import auth_bp
        app.register_blueprint(auth_bp, url_prefix="/auth")

        from .api import api_bp
        app.register_blueprint(api_bp, url_prefix="/api")

        # Import Dash application
        from .dash.dash_app import init_dash

        app = init_dash(server=app, cache=cache)

        @app.route("/version")
        @valid_auth_required
        def version():
            base_dir = os.path.dirname(os.path.abspath(__file__))
            version_file_path = os.path.join(base_dir, '..', 'VERSION')

            with open(version_file_path, "r") as f:
                app_version = f.read().strip()

            return {"version": app_version}

        @app.route("/")
        @valid_auth_required
        def serve_home():
            """
            :return:
            """
            return redirect("/u2p050twitterfetcher/dashboard")

        @app.shell_context_processor
        def make_shell_context():
            """
            :return:
            """
            return {}

    return app
