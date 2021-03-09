from main import db
from sqlalchemy.orm import backref
from models.Profiles import Profiles
from flask_login import UserMixin    #added

def get_user(user_id):                                  #added
    user=Users.query.filter_by(id=user_id).first()
    return user

class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    profile = db.relationship("Profiles", backref=backref("user", uselist=False))

    def __repr__(self):
        return f"<Users {self.email}>"