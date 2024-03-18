from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return '<h1>Hello</h1>'


@auth.route('/logout')
@login_required
def logout():
    return '<h1>Logout</h1>'


@auth.route('/register', methods=['GET', 'POST'])
def register():
    return '<h1>logout</h1>'