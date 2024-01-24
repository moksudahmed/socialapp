# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load configuration from config.py
app.config.from_object('config.Config')

db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Import your models and routes at the end
from app.models import User
from app.routes import auth_bp, posts_bp, comments_bp, likes_bp, photos_bp, other_bp

app.register_blueprint(auth_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(likes_bp)
app.register_blueprint(photos_bp)
app.register_blueprint(other_bp)  # Register the other_bp blueprint
