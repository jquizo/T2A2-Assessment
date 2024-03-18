from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    # For securing session data
    app.config['SECRET_KEY'] = 'hgdskasfdajhdua'



    # Import blueprints
    from .views import views
    from .auth import auth
    
    # Register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

