from flask_sqlalchemy import SQLAlchemy

from models.db import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    posts = db.relationship("Posts", backref="user", lazy=True)

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "posts": [post.to_dict() for post in self.posts],
        }
