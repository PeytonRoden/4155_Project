
from flask import Flask, render_template, request, url_for, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, LoginManager, login_user, login_required, logout_user


from src.repositories.User_Repository import user_repository_singleton
from src.models.models import User_
from src.models.models import db

import os


app = Flask(__name__)  # __name__ refers to the module name
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', default = 'postgresql://postgres:password@localhost:5432/4155_project')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#flask-login stuff
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/') 
def index():

    return render_template("index.html")


@app.route('/login') 
def login():
    return render_template("login.html")

@app.route('/signup') 
def signup():
    return render_template("signup.html")


@app.post('/signup/new_user' )
def signup_new_user():
    # code to validate and add user to database goes here
    name = request.form.get('name')
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    user_repeat_password = request.form.get('repeat_password')


    # if passwords don't match redirect
    if (user_password != user_repeat_password):
        # TODO: handle this
        flash('Password Does Not Match')
        return signup()

    # if this returns a user, then the email already exists in database
    user = User_.query.filter_by(email=user_email).first()

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return signup()

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    user_repository_singleton.create_user(name, user_email, generate_password_hash(
        user_password, method='sha256'))

    flash('Form Submitted Successfully')


    return index()


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User_.query.get(int(user_id))




@app.post('/login/login_user')  # Python decorator, new syntax
def loginuser():


    email = request.form.get('email')
    password = request.form.get('password')

    user = User_.query.filter_by(email=email).first()
    

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.user_password, password):
        flash('Please check your login details and try again.')
        # if password details don't match reload the page
        return login()

    # if the above check passes, then we know the user has the right credentials
    login_user(user)

    print("logged in :" + current_user.email)

    # if the above check passes, then we know the user has the right credentials
    return index()


@app.post('/logout')
@login_required
def logout():
    session.pop("user", None)
    logout_user()
    return index()

