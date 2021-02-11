from main import db
from models.ProfileImage import ProfileImage
from models.Post import Post
from models.Messages import Messages
from sqlalchemy.orm import backref

class Profiles(db.Model):
    __tablename__ = 'profiles'

    profileid =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    account_active = db.Column(db.Boolean(), default = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    profile_image = db.relationship("ProfileImage", backref="profile", uselist=False)
    post = db.relationship("Post", backref="profile", lazy="dynamic")
  
    messages = db.relationship("Messages", backref="profile")
    post = db.relationship("Post", cascade="all, delete")
    admin = db.Column(db.Boolean(), default=False)

def __repr__(self):
    return f"<Profile {self.username}>"
