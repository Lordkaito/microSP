from models.user import User
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
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

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify(
            {
                "message": f"User with email {email} already exists",
                "user": user.username,
            }
        )
    else:
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password, email=email)
        user.save()
        return jsonify(
            {
                "message": "User created successfully",
                "user": user.username,
            }
        )
