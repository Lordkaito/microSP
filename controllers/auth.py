from models.user import Users
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET"])
@jwt_required()
def index():
    id = get_jwt_identity()
    print(id, "id for user")
    return jsonify({"message": "Hello world"})


@auth_bp.route("/login", methods=["POST"])
def login():
    name = request.json.get("name")
    password = request.json.get("password")

    user = Users.query.filter_by(name=name).first()
    if user and check_password_hash(user.password, password):
        # we need to create the identity with the id of the user
        # this is so we can easily find the user posts and more using the relation in the db
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=30))
        return jsonify(
            {
                "message": "Logged in successfully",
                "user": user.name,
                "access_token": access_token,
            }
        )

    return jsonify({"message": "Wrong credentials"})


@auth_bp.route("/signup", methods=["POST"])
def signup():
    print(request.json)
    name = request.json.get("name")
    password = request.json.get("password")
    email = request.json.get("email")

    user = Users.query.filter_by(email=email).first()
    if user:
        return jsonify(
            {
                "message": f"User with email {email} already exists",
                "user": {
                    "name": user.name,
                    "email": user.email,
                }
            }
        )
    else:
        hashed_password = generate_password_hash(password)
        user = Users(name=name, password=hashed_password, email=email)
        user.save()
        return jsonify(
            {
                "message": "Users created successfully",
                "user": {
                    "name": user.name,
                    "email": user.email,
                    "id": user.id,
                    "posts": [post.to_dict() for post in user.posts] if user.posts else [],
                }
            }
        )


# @auth_bp.route("/users", methods=["GET"])
# def users():
#     users = Users.query.all()
#     return jsonify({"users": "List of users"})


@auth_bp.route("/validate", methods=["POST"])
@jwt_required()
def validate():
    user = get_jwt_identity()
    if user:
        return jsonify(
            {
                "message": "Valid token",
                "user": user,
            }
        )
    else:
        return jsonify(
            {
                "message": "Invalid token",
            }
        )