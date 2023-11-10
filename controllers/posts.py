from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required

posts_bp = Blueprint("posts", __name__)

@posts_bp.route("/posts", methods=["GET"])
def posts():
    return jsonify({"posts": "List of posts"})

@posts_bp.route("/posts/<int:id>", methods=["GET"])
def post(id):
    return jsonify({"post": "Post"})

@posts_bp.route("/posts", methods=["POST"])
@jwt_required()
def create_post():
    return jsonify({"message": "Post created successfully"})
