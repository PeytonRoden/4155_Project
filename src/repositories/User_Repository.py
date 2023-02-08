from src.models.models import db
from src.models.models import User_

class User_Repository:

    def get_all_users(self):
        # TODO get all users from the DB
        return User_.query.all()

    def get_user_by_id(self, user_id):
        # TODO get a single user from the DB using the ID
        user = User_.query.get(user_id)
        return user

    def create_user(self, name, email, user_password):
        # TODO create a new User in the DB

        new_user = User_(name = name, email = email, user_password = user_password)
        db.session.add(new_user)
        db.session.commit()

        return None


    def edit_user(self, user_id, first_name, last_name, username, email, university):
        # TODO create a new User in the DB

        user = self.get_user_by_id(user_id)

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.university = university

        db.session.commit()

        return None

    def change_password(self, user_id, new_password):
        user = self.get_user_by_id(user_id)
        user.user_password = new_password
        db.session.commit()


    def get_user_by_username(self, username):
        return User_.query.filter_by(username = username).first()

    def search_users(self, title):
        # TODO get all Users matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None



    def delete_user(self, user_id):
        #will need to cascade through all the stuff related to user such as tickets they have
        user = self.get_user_by_id(user_id)

        db.session.delete(user)

        db.session.commit()



# Singleton to be used in other modules
user_repository_singleton = User_Repository()
