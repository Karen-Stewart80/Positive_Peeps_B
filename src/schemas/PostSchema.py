from main import ma
from models.Post import Post
from marshmallow.validate import Length
from schemas.ProfileSchema import ProfileSchema

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post

    post_name = ma.String(required=True, validate=Length(min=5))
    post_description = ma.String(required=True, validate=Length(min=5))


    profile = ma.Nested(ProfileSchema)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)