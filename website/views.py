from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Category
from . import db
import json
# For showing date in local timezone
import pytz
from pytz import timezone

views = Blueprint('views', __name__)

# / is the homepage
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    local_timezone = timezone('Australia/Melbourne')
    
    return '<h1>Hello</h1>'