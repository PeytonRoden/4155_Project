
from flask import Flask, render_template, request, url_for, redirect, flash, session


from src.repositories.User_Repository import user_repository_singleton
from src.models.models import User_
from src.models.models import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, LoginManager, login_user, login_required, logout_user
import os


app = Flask(__name__)  # __name__ refers to the module name
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', default = 'postgresql://postgres:password@localhost:5432/4155_project')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#flask-login stuff
#login_manager = LoginManager()
#login_manager.init_app(app)


@app.route('/') 
def index():

    return render_template("index.html")


@app.route('/login') 
def login_page():
    return render_template("login.html")