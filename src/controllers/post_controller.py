from flask import Blueprint, request, jsonify, abort, render_template, url_for, redirect
from schemas.PostSchema import post_schema, posts_schema
from schemas.ProfileSchema import profile_schema, profiles_schema
from models.Profiles import Profiles
from main import db
from models.Users import Users
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_services import verify_user
from models.Post import Post
from sqlalchemy.sql import func, label
from sqlalchemy.orm import joinedload
from flask_login import login_required, current_user

posts = Blueprint("post", __name__, url_prefix="/post")

@posts.route("/", methods=["GET"])
def post_index():
    post = db.session.query(Post).order_by(Post.post_name).all()
    #return jsonify(posts_schema.dump(post))
    return render_template("post_index.html", posts= post)

@posts.route("/new", methods=["GET"])
@login_required
def new_post():
    return render_template("new_post.html")


# @posts.route("/", methods=["POST"])
# @jwt_required
# @verify_user
# def post_create(user=None):
#     user_id=get_jwt_identity()
#     post_fields = post_schema.load(request.json)
#     profile=Profiles.query.get(user_id)

#     new_post = Post()
#     new_post.post_name = post_fields["post_name"]
#     new_post.post_description = post_fields["post_description"]

#     profile.post.append(new_post)

#     db.session.add(new_post)
#     db.session.commit()

#     return jsonify(post_schema.dump(new_post))

@posts.route("/", methods=["POST"])
@login_required
def post_create():

    post_name = request.form.get("post_name")
    post_description = request.form.get("post_description")
    profile = Profiles.query.filter_by(user_id=current_user.id).first()
    new_post = Post()
    new_post.post_name = post_name
    new_post.post_description = post_description
    new_post.profile_id = profile.profileid

    #profile.post.append(new_post)

    db.session.add(new_post)
    db.session.commit()

    # return jsonify(post_schema.dump(new_post))
    return redirect(url_for('post.post_index'))

@posts.route("/<int:id>", methods=["GET"])
def post_show(id):
    #Return a single user
    post = Post.query.filter_by(postid = id).first()
    #return jsonify(post_schema.dump(post))
    return render_template("post.html", post=post)

@posts.route("/<int:id>", methods=["PUT", "PATCH"])
#@jwt_required
#@verify_user
def post_update(id):
    #Update a user
    # post = Post.query.filter_by(post_name = post_name)
    post = Post.query.get(id)
    post_fields = post_schema.load(request.json)

    if post.count() != 1:
        return abort(401, description="Unauthorised to update this user")
    post.update(post_fields)

    db.session.commit()

    # return jsonify(post_schema.dump(post[0]))
    return render_template("post.html", post=post)

@posts.route("/delete/<int:id>", methods=["GET"])
@login_required
def post_delete(id):
    #Delete a User
    # post = Post.query.filter_by(postid=postid).first()
    post = Post.query.get(id)
    
    #post = db.session.query(Post).filter(Post.post_name == post_name).first()

    if not post:
        return abort(400, description="Unauthorised to delete user")

    db.session.delete(post)
    db.session.commit()

    #return jsonify(post_schema.dump(post))
    return redirect(url_for("post.post_index"))