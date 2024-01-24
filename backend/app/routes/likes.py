from flask import Blueprint, request, jsonify
from app.models.like import Like
from app import db

likes_bp = Blueprint('likes', __name__)

@likes_bp.route('/likes', methods=['POST'])
def like_post():
    print("Test")
    # Like post logic
