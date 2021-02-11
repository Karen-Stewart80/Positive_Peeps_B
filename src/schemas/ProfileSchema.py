from main import ma
from models.Profiles import Profiles
from marshmallow.validate import Length
from schemas.UsersSchema import UsersSchema

class ProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Profiles
        load_only =["admin"]
    username = ma.String(required=True, validate=Length(min=1))
    fname = ma.String(required=True, validate=Length(min=1))
    lname = ma.String(required=True, validate=Length(min=1))
    account_active = ma.Boolean(required=True)
    github = ma.String(required=False, validate=Length(min=1))
    user = ma.Nested(UsersSchema)
    front_end = ma.Boolean(required=True)
    back_end = ma.Boolean(required=True)
    full_stack = ma.Boolean(required=True)
    admin = ma.Boolean()


profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)