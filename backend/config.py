# config.py

import os

class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/social_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key_here'
    CORS_HEADERS = 'Content-Type'

    # Other configuration options if needed
