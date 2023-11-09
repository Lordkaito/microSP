from flask import Flask
from controllers.auth import auth_bp
from models.user import db
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
print(os.getenv("DATABASE_DOCKER_URL"))
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_DOCKER_URL")
jwt = JWTManager(app)
db.init_app(app)
# gunicorn '.venv.lib.python3.11.site-packages.werkzeug.wsgi' --bind=0.0.0.0:8000
try:
    with app.app_context():
        db.create_all()
        print("Tablas creadas con éxito.")
except Exception as e:
    print("Error al crear tablas:", str(e))


@app.route("/")
def index():
    return "Hello, World!"


app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)
