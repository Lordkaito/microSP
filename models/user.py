from flask_sqlalchemy import SQLAlchemy

from models.db import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    posts = db.relationship("Post", backref="user", lazy=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def save(self):
        db.session.add(self)
        db.session.commit()
