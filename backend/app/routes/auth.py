from flask import Blueprint, request, jsonify
from app import db, bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user import User
from app.schemas.user_schema import UserSchema
from marshmallow import ValidationError

auth_bp = Blueprint('auth', __name__)

user_schema = UserSchema()

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Validate user data
        errors = user_schema.validate(data)
        if errors:
            return jsonify({'errors': errors}), 422

        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user:
            return jsonify({'error': 'Username already taken'}), 400

        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(username=data['username'], password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        access_token = create_access_token(identity=new_user.id)
        return jsonify(access_token=access_token), 201

    except ValidationError as e:
        return jsonify({'errors': e.messages}), 422
        
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        login_data = user_schema.load(data, partial=('username',))

        user = User.query.filter_by(username=login_data['username']).first()

        if user and bcrypt.check_password_hash(user.password, login_data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401

    except ValidationError as e:
        return jsonify({'errors': e.messages}), 422
