
from flask import Flask, render_template, request, url_for, redirect, flash, session


app = Flask(__name__)  # __name__ refers to the module name
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.app_context().push()


@app.route('/')  # Python decorator, new syntax
def index():

    return render_template("index.html")
