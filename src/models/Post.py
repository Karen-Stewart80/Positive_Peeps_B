from main import db
from models.Messages import Messages


class Post(db.Model):
    __tablename__ = 'post'

    postid =db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.String(), nullable=False)
    post_description= db.Column(db.String(), nullable=False)
    account_active = db.Column(db.Boolean(), nullable=False)
    front_end = db.Column(db.Boolean(), nullable=False)
    back_end = db.Column(db.Boolean(), nullable=False)
    full_stack = db.Column(db.Boolean(), nullable=False)
    completed = db.Column(db.Boolean(), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.profileid"), nullable=False)
    post_github = db.Column(db.String(), nullable=False)
    messages = db.relationship("Messages", backref="post", lazy="dynamic")


def __repr__(self):
    return f"<Post {self.post}>"
