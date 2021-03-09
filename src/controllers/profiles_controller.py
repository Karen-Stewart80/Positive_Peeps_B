from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for
import json 
import os
from schemas.ProfileSchema import profile_schema, profiles_schema
from models.Profiles import Profiles
from main import db
from models.Users import Users
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_services import verify_user
from flask_login import login_required, current_user


profiles = Blueprint("profiles", __name__, url_prefix="/profiles")

@profiles.route("/", methods=["GET"])
def profiles_index():
    profiles = Profiles.query.all()
    #return jsonify(profiles_schema.dump(profiles))
    return render_template("profile_index.html", profiles=profiles)

@profiles.route("/", methods=["POST"])
@login_required
def profile_create(user=None):
    username = request.form.get('username')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    # user_id=get_jwt_identity()
    # profile_fields = profile_schema.load(request.json)
    # profile=Profiles.query.get(user_id)

    new_profile = Profiles()
    new_profile.username = username
    new_profile.fname = fname
    new_profile.lname = lname
    new_profile.user_id = current_user.id
    # new_user.account_active = profile_fields["account_active"]
 
    # user.profile.append(new_profile)

    db.session.add(new_profile)
    db.session.commit()

    return redirect(url_for('post.post_index'))

@profiles.route("/new", methods=["get"])
@login_required
def new_profile():
    return render_template("new_profile.html")

@profiles.route("/<string:username>", methods=["GET"])
def profiles_show(username):
    #Return a single user
    profile = Profiles.query.filter_by(username = username).first()
    #return jsonify(profile_schema.dump(profile))
    return render_template("profiles.html", profile=profile)

@profiles.route("/<int:id>", methods=["PUT", "PATCH"])
@login_required
def profiles_update(id):
    #Update a user
    profile = Profiles.query.filter_by(profileid = id, user_id=current_user.id)
    profile_fields = profile_schema.load(request.json)
    print(profile)

    if not profile:
        return abort(401, description="Unauthorised to update")
    profile.update(profile_fields)

    db.session.commit()

    return jsonify(profile_schema.dump(profile[0]))

@profiles.route("/<int:id>", methods=["DELETE"])
@login_required
def profiles_delete(id):
    #Delete a User
    # profile = Profiles.query.filter_by(username=username, user_id=current_user.id).first()
    profile = Profiles.query.get(id)

    if not profile:
        return abort(400, description="Unauthorised to delete user")

    db.session.delete(profile)
    db.session.commit()

    # return jsonify(profile_schema.dump(profile))
    return redirect(url_for('post.post_index'))



