from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods=["GET"])
# @jwt_required() we will think about this later
def users():
    return jsonify({"users": "List of users"})

@users_bp.route("/users/<int:id>", methods=["GET"])
# @jwt_required()
def user(id):
    return jsonify({"user": "User"})


