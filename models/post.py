from flask_sqlalchemy import SQLAlchemy

from models.db import db

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    content = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    likes = db.relationship("Likes", backref="post", lazy=True)

    def __init__(self, title, content, author, user_id):
        self.title = title
        self.content = content
        self.author = author
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "user_id": self.user_id,
            "likes": [like.to_dict() for like in self.likes],
        }