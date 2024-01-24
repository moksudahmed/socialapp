from flask import Blueprint, request, jsonify
from app.models.photo import Photo
from app import db

photos_bp = Blueprint('photos', __name__)

@photos_bp.route('/photos', methods=['POST'])
def upload_photo():
    print("Test")
    # Upload photo logic
