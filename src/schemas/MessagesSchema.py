from main import ma
from marshmallow.validate import Length
from models.Messages import Messages
from schemas.PostSchema import PostSchema

class MessagesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Messages
   
    messages = ma.String(required=True, validate=Length(min=1))

message_schema = MessagesSchema()
messages_schema = MessagesSchema(many=True)