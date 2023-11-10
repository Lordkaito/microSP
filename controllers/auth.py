from models.user import Users
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = Users.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username, expires_delta=timedelta(days=30))
        return jsonify(
            {
                "message": "Logged in successfully",
                "user": user.username,
                "access_token": access_token,
            }
        )

    return jsonify({"message": "Wrong credentials"})


@auth_bp.route("/signup", methods=["POST"])
def signup():
    print(request.json)
    username = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")

    user = Users.query.filter_by(email=email).first()
    if user:
        return jsonify(
            {
                "message": f"Users with email {email} already exists",
                "user": user.username,
            }
        )
    else:
        hashed_password = generate_password_hash(password)
        user = Users(username=username, password=hashed_password, email=email)
        user.save()
        return jsonify(
            {
                "message": "Users created successfully",
                "user": user.username,
            }
        )


@auth_bp.route("/users", methods=["GET"])
def users():
    users = Users.query.all()
    return jsonify({"users": "List of users"})


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