from flask import Flask
from controllers.auth import auth_bp
from controllers.users import users_bp
from controllers.posts import posts_bp
from flask_jwt_extended import JWTManager
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError
from flask import jsonify
from dotenv import load_dotenv
from models.db import db
from models.user import Users
from models.post import Posts
from models.like import Likes
import os


load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_DOCKER_URL")
jwt = JWTManager(app)
db.init_app(app)

try:
    with app.app_context():
        db.create_all()
        print("Tablas creadas con éxito.")
except Exception as e:
    print("Error al crear tablas:", str(e))


@app.route("/")
def index():
    return jsonify({"message": "Hello world"})


@app.errorhandler(InvalidSignatureError)
def handle_auth_error(e):
    return jsonify({"message": "Wrong token"}), 401


@app.errorhandler(ExpiredSignatureError)
def handle_auth_error(e):
    return jsonify({"message": "Token expired"}), 401


app.register_blueprint(auth_bp, url_prefix="/auth")

app.register_blueprint(users_bp, url_prefix="/users")

app.register_blueprint(posts_bp, url_prefix="/posts")

if __name__ == "__main__":
    app.run(debug=True)
