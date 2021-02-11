from flask import Blueprint, request, jsonify, abort
from models.Messages import Messages
from main import db
from models.Users import Users
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_services import verify_user
from models.Messages import Messages
from schemas.MessagesSchema import message_schema, messages_schema
from sqlalchemy.sql import label, func


messages = Blueprint("messages", __name__, url_prefix="/messages")

@messages.route("/", methods=["GET"])
def messages_index():
    messages = Messages.query.all()
    return jsonify(messages_schema.dump(messages))

@messages.route("/messaging", methods=["GET"])
def messages_messaging():
    query = db.session.query(Messages.profile_id, label('profile_messages', func.count(Messages.message_id))).group_by(Messages.profile_id).all()
  
    return jsonify(query)

    #messages = query.filter(Messages.)
   # return jsonify(messages_schema.dump(messages))

# @messages.route("/", methods=["POST"])
# @jwt_required
# @verify_user
# def messages_create(user=None):
#     user_id=get_jwt_identity()
#     messages_fields = message_schema.load(request.json)
#     messages=Messages.query.get(user_id)

#     new_message = Messages()
#     new_message.messages= messages_fields["messages"]
   
#     db.session.add(new_message)
#     db.session.commit()

#     return jsonify(messages_schema.dump(new_message))