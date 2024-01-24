from flask import Blueprint, jsonify
from app.models.comment import Comment
from app import db

comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/comments', methods=['GET'])
def get_comments():
    print("Test")
    # Get comments logic
