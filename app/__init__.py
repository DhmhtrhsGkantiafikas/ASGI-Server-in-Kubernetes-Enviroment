from flask import Flask
from .config import Config
from .routes import main

def create_app():
    app = Flask(__name__)  # αυτόματα βρίσκει templates/ & static/
    app.config.from_object(Config)
    app.register_blueprint(main)
    return app

