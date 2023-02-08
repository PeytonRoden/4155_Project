from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


class User_(UserMixin, db.Model):

    #serial field that automatically increments
    user_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), nullable = False, unique = True)
    user_password = db.Column(db.String(255), nullable = False)
    account_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.user_id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False



