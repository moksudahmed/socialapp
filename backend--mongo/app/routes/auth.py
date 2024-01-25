from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app import bcrypt, jwt, mongo
from app.models.user import User
from marshmallow import ValidationError
from app.schemas.user import UserSchema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        # Access the 'users' collection
        users_collection = mongo.db.users

        # Validate and deserialize the request JSON data
        user_data = UserSchema().load(request.json)

        # Check if the username already exists
        existing_user = User.query.filter_by(username=user_data['username']).first()
        if existing_user:
            return jsonify({'error': 'Username already exists'}), 400

        # Hash the password before storing it
        hashed_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')

        # Create a new user instance
        new_user = User(
            username=user_data['username'],
            password=hashed_password,
            # Other user fields...
        )

        # Add the new user to the SQLAlchemy session
        mongo_user = {
            'username': new_user.username,
            'password': new_user.password,
            # Other user fields...
        }
        users_collection.insert_one(mongo_user)

        # Commit changes to the database
        mongo.db.session.commit()

        return jsonify({'message': 'Registration successful'}), 201

    except ValidationError as e:
        return jsonify({'errors': e.messages}), 422

def register2():
    data = request.get_json()
    print(data)
    # Validate input data against User schema
    try:
        user_schema = UserSchema()
        new_user = user_schema.load(data)
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 422

    # Check if the username already exists in the database
    existing_user = User.query.filter_by(username=new_user.username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 409

    # Hash the password before storing it
    hashed_password = bcrypt.generate_password_hash(new_user.password).decode('utf-8')

    # Create a new User instance
    user = User(username=new_user.username, password=hashed_password)

    # Save the new user to the MongoDB users collection
    mongo.db.users.insert_one(user.to_dict())

    return jsonify({'message': 'Registration successful'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Find the user by username in the MongoDB users collection
    user = User.query.filter_by(username=data['username']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        # Create an access token for the user
        access_token = create_access_token(identity=user.username)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid username or password'}), 401
