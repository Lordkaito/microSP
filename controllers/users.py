from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from models.user import Users
from models.post import Posts

users_bp = Blueprint("users", __name__)

# @users_bp.route("/users", methods=["GET"])
# # @jwt_required() we will think about this later
# def users():
#     return jsonify({"users": "List of users"})

@users_bp.route("/", methods=["GET"])
def index():
    users = Users.query.all()
    return jsonify({"users": [user.to_dict() for user in users]})


@users_bp.route("/users/<int:id>", methods=["GET"])
# @jwt_required()
def user(id):
    return jsonify({"user": "User"})

@users_bp.route("/posts", methods=["GET"])
def posts(user_id):
    posts = Posts.query.filter_by(user_id=user_id).all()
    return jsonify({"posts": posts, "message": f"List of posts from user {user_id}"})
