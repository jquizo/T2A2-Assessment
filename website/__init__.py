from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialise database
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    # For securing session data
    app.config['SECRET_KEY'] = 'hgdskasfdajhdua'
    # Tells flask where database is located
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import blueprints
    from .views import views
    from .auth import auth
    
    # Register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import database models
    from .models import User, Note, Category
    
    with app.app_context():
        db.create_all()

    # Redirects to login page if user is not logged in
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # For retrieving user object from database based on provided user id
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# Checks if database exists, if not creates one
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database')