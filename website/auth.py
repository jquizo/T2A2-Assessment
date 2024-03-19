from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Gets data from HTML form
        email = request.form.get('email')
        password = request.form.get('password')
        # Checks database if email exists in database and returns the first result
        user = User.query.filter_by(email=email).first() 
        if user:
            # Checks if password entered is the same as the hash stored on database.
            if check_password_hash(user.password, password):
                flash('Logged in. Welcome!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


# @login_required decorator requires user to be logged in to access route
@auth.route('/logout')
@login_required
def logout():
    # Logs out current user and redirects to login page
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Takes information from HTML Form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first() # Checks database if email exists in database
        if user: 
            flash('Email is already registered.', category='error')
        # Checks if the information input are valid - if not FLASH error message
        elif len(email) < 1:
            flash('Email must be greater than 1 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 5:
            flash('Password must be at least 5 characters.', category='error')
        else:
            # Adds new user to the database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            # Redirects user to homepage after account creation
            return redirect(url_for('views.home'))

    return render_template("register.html", user=current_user)