from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash(f"Login succesfully as {user.first_name}", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('User does not exist', category='error')        
    return render_template('login.html', text="Hello Romeo", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
@auth.route('/delete_account')
def delete_account():
    current_user.delete_me()
    Note.query.filter_by(user_id=current_user.id)
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print("-----------entered so far")
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than  character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Passoword length must be greater than 7 charcetrs', category='error')
        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created succesfully', category='success')
            return redirect(url_for('views.home'))
    return render_template('sign_up.html', user=current_user)