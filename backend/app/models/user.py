from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    profile_picture_url = db.Column(db.String(255))
    bio = db.Column(db.Text)
    website = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"
