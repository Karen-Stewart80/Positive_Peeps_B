from main import db
# from models.Profiles import Profiles
# from models.Post import Post
from datetime import datetime

class Messages(db.Model):
    __tablename__ = 'messages'

    message_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.postid"), nullable=True)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.profileid"), nullable=True)
    messages = db.Column(db.String(), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)



def __repr__(self):
    return f"<Messages {self.message_id}>"