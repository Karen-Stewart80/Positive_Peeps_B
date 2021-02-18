from main import ma
from models.Profiles import Profiles
from marshmallow.validate import Length
from schemas.UsersSchema import UsersSchema

class ProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Profiles

    username = ma.String(required=True, validate=Length(min=1))
    fname = ma.String(required=True, validate=Length(min=1))
    lname = ma.String(required=True, validate=Length(min=1))
    account_active = ma.Boolean(required=True)
    
    user = ma.Nested(UsersSchema)


profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)