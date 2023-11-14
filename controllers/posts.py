from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

posts_bp = Blueprint("posts", __name__)

@posts_bp.route("/", methods=["GET"])
def index():
    return jsonify({"posts": "List of posts"})

@posts_bp.route("/posts/<int:id>", methods=["GET"])
def post(id):
    return jsonify({"post": "Post"})

@posts_bp.route("/posts", methods=["POST"])
@jwt_required()
def create_post():
    id = get_jwt_identity()
    return jsonify({"message": "Post created successfully"})
