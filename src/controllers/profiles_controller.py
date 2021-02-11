from flask import Blueprint, request, jsonify, abort
import json 
import os
from schemas.ProfileSchema import profile_schema, profiles_schema
from models.Profiles import Profiles
from main import db
from models.Users import Users
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_services import verify_user
from models.Post import Post
from models.Messages import Messages
from models.ProfileImage import ProfileImage
from schemas.MessagesSchema import messages_schema
from schemas.PostSchema import posts_schema
from schemas.UsersSchema import users_schema
from schemas.ProfileImageSchema import profiles_image_schema




profiles = Blueprint("profiles", __name__, url_prefix="/profiles")

tables = ["messages", "profile_images", "profiles", "post", "users"]
schemas = [messages_schema, profiles_schema, profiles_image_schema, users_schema, posts_schema]




@profiles.route("/dump/all/<int:id>", methods=["GET"])
@jwt_required
@verify_user
def profile_dump(user, id):

    profile = db.session.query(Profiles).filter(Profiles.admin == True).filter_by(profileid = id, user_id=user.id).first()

    if not profile:
        return abort(400, description="Unauthorised to complete")
    i=0
    try:
        os.remove("backup/backup.json")
        print("file successfully deleted")
    except:
        print("file does not exist")


    for table in tables:
        
        query = db.engine.execute(f'SELECT * FROM {table}')
        data = ((schemas[i]).dump(query))

        data = json.dumps(data)
        i+=1
    
        file = open("backup/backup.json", "a")
        file.write(data)
        file.close()

    return "Data backed up"

@profiles.route("/", methods=["GET"])
def profiles_index():
    profiles = Profiles.query.all()
    return jsonify(profiles_schema.dump(profiles))

@profiles.route("/dev", methods=["GET"])

def profiles_index_dev():
   
    profiles = db.session.query(Profiles, Post).join(Post, Profiles.profileid == Post.profile_id).all()
    
    listy_list = []
    for result in profiles:
       listy_list.append(f"Name: {result[0].username} Description: {result[1].post_description}")
    return jsonify(listy_list)



@profiles.route("/back_end", methods=["GET"])

def profiles_back_end():
   
    profiles = db.session.query(Profiles, Post).join(Post, Profiles.profileid == Post.profile_id).all()
   
    listy_list = []
    for result in profiles:
       listy_list.append(f"Name: {result[0].username} Backend: {result[1].back_end}")
    return jsonify(listy_list)


@profiles.route("/front_end", methods=["GET"])

def profiles_front_end():
   
    profiles = db.session.query(Profiles, Post).join(Post, Profiles.profileid == Post.profile_id).all()


    listy_list = []
    for result in profiles:
       listy_list.append(f"Name: {result[0].username} Front_end: {result[1].front_end}")
    return jsonify(listy_list)

@profiles.route("/full_stack", methods=["GET"])

def profiles_full_stack():
   
    profiles = db.session.query(Profiles, Post).join(Post, Profiles.profileid == Post.profile_id).all()
   
    listy_list = []
    for result in profiles:
       listy_list.append(f"Name: {result[0].username} Full_stack: {result[1].full_stack}")
    return jsonify(listy_list)


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
    new_user.github = profile_fields["github"]
    new_user.front_end = profile_fields["front_end"]
    new_user.back_end = profile_fields["back_end"]
    new_user.full_stack = profile_fields["full_stack"]
    new_user.admin = profile_fields["admin"]

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



