from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Category
from . import db
import json
# For showing date in local timezone
import pytz
from pytz import timezone

views = Blueprint('views', __name__)


# @current user allows access to the user model 
# @login_required decorator makes it so user cannot access logout route unless logged in

# / is the homepage
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    local_timezone = timezone('Australia/Melbourne')
    
    if request.method == 'POST': 
        note = request.form.get('note')# Gets the data from the HTML form
        category_text = request.form.get('category')

        # Note must be longer than 1 character
        if len(note) < 1:
            flash('Note is too short', category='error') 
        else:
            # Create a new Note object with the provided note text and the current user's ID
            new_note = Note(data=note, user_id=current_user.id)  
            # Check if a category was provided, and add it to the note
            if category_text:
                new_note.category = Category(description=category_text)

            #adding the note to the database 
            db.session.add(new_note) 
            db.session.commit()
            flash('Note added', category='success')

    return render_template("home.html", user=current_user,  local_timezone=local_timezone)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # request.data is the JSON from the deleteNote function (index.js) 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note successfully deleted.', 'success')
    # Returns empty json object to signify completion of function
    return jsonify({})
