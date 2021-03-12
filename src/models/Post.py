from main import db

class Post(db.Model):
    __tablename__ = 'post'

    postid =db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.String(), nullable=False)
    post_description= db.Column(db.String(), nullable=False)
    
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.profileid"))
    # profile = db.relationship(
    #     "Profile",
    #     backref="post",
    #     cascade="all, delete"
    # )           #added

def __repr__(self):
    return f"<Post {self.post}>"
