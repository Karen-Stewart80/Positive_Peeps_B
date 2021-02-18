from flask import Blueprint, request, jsonify, abort, render_template, url_for
from schemas.PostSchema import post_schema, posts_schema
from models.Profiles import Profiles
from main import db
from models.Users import Users
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_services import verify_user
from models.Post import Post
from sqlalchemy.sql import func, label
from sqlalchemy.orm import joinedload

posts = Blueprint("post", __name__, url_prefix="/post")

@posts.route("/", methods=["GET"])
def post_index():
    post = db.session.query(Post).order_by(Post.post_name).all()
    return jsonify(posts_schema.dump(post))
    #return render_template("home_page.html", posts= post)


@posts.route("/", methods=["POST"])
@jwt_required
@verify_user
def post_create(user=None):
    user_id=get_jwt_identity()
    post_fields = post_schema.load(request.json)
    profile=Profiles.query.get(user_id)

    new_post = Post()
    new_post.post_name = post_fields["post_name"]
    new_post.post_description = post_fields["post_description"]

    profile.post.append(new_post)

    db.session.add(new_post)
    db.session.commit()

    return jsonify(post_schema.dump(new_post))

@posts.route("/<string:post_name>", methods=["GET"])
def post_show(post_name):
    #Return a single user
    post = Post.query.filter_by(post_name = post_name).first()
    return jsonify(post_schema.dump(post))

@posts.route("/<string:post_name>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def post_update(post_name, user=None):
    #Update a user
    post = Post.query.filter_by(post_name = post_name)
    post_fields = post_schema.load(request.json)

    if post.count() != 1:
        return abort(401, description="Unauthorised to update this user")
    post.update(post_fields)

    db.session.commit()

    return jsonify(post_schema.dump(post[0]))

@posts.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def post_delete(user, postid):
    #Delete a User
    #post = Post.query.filter_by(post_name=post_name).first()
    post = Post.query.options(joinedload("profile")).filter_by(postid = postid, profile_id = user.id).first()
    #post = db.session.query(Post).filter(Post.post_name == post_name).first()

    if not post:
        return abort(400, description="Unauthorised to delete user")

    db.session.delete(post)
    db.session.commit()

    return jsonify(post_schema.dump(post))