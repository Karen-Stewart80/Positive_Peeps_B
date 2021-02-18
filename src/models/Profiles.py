from main import db
from models.Post import Post
from sqlalchemy.orm import backref

class Profiles(db.Model):
    __tablename__ = 'profiles'

    profileid =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    account_active = db.Column(db.Boolean(), default = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post = db.relationship("Post", backref="profile", lazy="dynamic")
    post = db.relationship("Post", cascade="all, delete")

def __repr__(self):
    return f"<Profile {self.username}>"
