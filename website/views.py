from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Note
from . import db
import json
views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    if request.method == 'POST':
        data = request.form.get('note')
        if len(data) > 1:
            new_note = Note(data=data, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
        else:
            flash("Note should not be empty", category='error')
    all_notes = Note.query.filter_by(user_id=current_user.id).all()
    number_of_notes = len(current_user.notes)
    return render_template("home.html", user=current_user, notes=[[note.data, note.id] for note in all_notes], number_of_notes=number_of_notes)

@views.route('/delete_note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteid']
    note_to_delete = Note.query.get(note_id)
    if note_to_delete.user_id == current_user.id:
        db.session.delete(note_to_delete)
        db.session.commit()
    return jsonify({})