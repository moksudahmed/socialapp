from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import mongo

job_postings_bp = Blueprint('job_postings', __name__)

@job_postings_bp.route('/job-postings', methods=['POST'])
@jwt_required()
def create_job_posting():
    current_user_id = get_jwt_identity()
    data = request.get_json()

    # Your job posting creation logic with MongoDB
    return jsonify({'message': 'Job posted successfully'}), 200

@job_postings_bp.route('/job-postings', methods=['GET'])
def get_job_postings():
    # Your job postings retrieval logic with MongoDB
    return jsonify({'job_postings': job_postings_list}), 200
