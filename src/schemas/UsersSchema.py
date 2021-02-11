from main import ma
from models.Users import Users
from marshmallow.validate import Length

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_only = ["password"]
    
    email = ma.String(required=True, validate=Length(min=4))
    password = ma.String(required=True, validate=Length(min=6))

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)