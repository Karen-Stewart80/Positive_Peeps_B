from main import ma
from models.Post import Post
from marshmallow.validate import Length
from schemas.ProfileSchema import ProfileSchema

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post

    post_name = ma.String(required=True, validate=Length(min=5))
    post_description = ma.String(required=True, validate=Length(min=5))
    account_active = ma.Boolean(required=True)
    front_end = ma.Boolean(required=True)
    back_end = ma.Boolean(required=True)
    full_stack = ma.Boolean(required=True)
    completed = ma.Boolean(required=True)
    post_github = ma.String(required=True, validate=Length(min=5))
    profile = ma.Nested(ProfileSchema)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)