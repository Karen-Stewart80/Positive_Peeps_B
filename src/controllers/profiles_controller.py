from flask import Blueprint, request, jsonify, abort
import json 
import os
from schemas.ProfileSchema import profile_schema, profiles_schema
from models.Profiles import Profiles
from main import db
from models.Users import Users
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_services import verify_user


profiles = Blueprint("profiles", __name__, url_prefix="/profiles")

@profiles.route("/", methods=["GET"])
def profiles_index():
    profiles = Profiles.query.all()
    return jsonify(profiles_schema.dump(profiles))


@profiles.route("/", methods=["POST"])
@jwt_required
@verify_user
def profiles_create(user=None):
    user_id=get_jwt_identity()
    profile_fields = profile_schema.load(request.json)
    profile=Profiles.query.get(user_id)

    new_user = Profiles()
    new_user.username = profile_fields["username"]
    new_user.fname = profile_fields["fname"]
    new_user.lname = profile_fields["lname"]
    new_user.account_active = profile_fields["account_active"]
 
    user.profile.append(new_user)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(profile_schema.dump(new_user))

@profiles.route("/<string:username>", methods=["GET"])
def profiles_show(username):
    #Return a single user
    profile = Profiles.query.filter_by(username = username).first()
    return jsonify(profile_schema.dump(profile))

@profiles.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def profiles_update(user, id):
    #Update a user
    profile = Profiles.query.filter_by(profileid = id, user_id=user.id)
    profile_fields = profile_schema.load(request.json)
    print(profile)

    if not profile:
        return abort(401, description="Unauthorised to update")
    profile.update(profile_fields)

    db.session.commit()

    return jsonify(profile_schema.dump(profile[0]))

@profiles.route("/<string:username>", methods=["DELETE"])
@jwt_required
@verify_user
def profiles_delete(username, user=None):
    #Delete a User
    profile = Profiles.query.filter_by(username=username, user_id=user.id).first()

    if not profile:
        return abort(400, description="Unauthorised to delete user")

    db.session.delete(profile)
    db.session.commit()

    return jsonify(profile_schema.dump(profile))



