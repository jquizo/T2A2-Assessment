from os import path
from flask import Flask


def create_app():
    app = Flask(__name__)
    # For securing session data
    app.config['SECRET_KEY'] = 'hgdskasfdajhdua'

    return app

