# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)

# Importing Config from the config module
from config.Config import Config
app.config.from_object(Config)

# MongoDB setup
mongo = PyMongo(app)

# Other setups (Bcrypt, JWT, etc.)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Import blueprints at the end of the file
from app.routes.auth import auth_bp
from app.routes.job_postings import job_postings_bp

app.register_blueprint(auth_bp)
app.register_blueprint(job_postings_bp)