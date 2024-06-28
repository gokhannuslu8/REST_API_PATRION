from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from services.auth_services import User
from utils.token import generate_token

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    factory_name = data['factory_name']

    if User.find_by_username(username):
        return jsonify({'message': 'User already exists'}), 400

    user = User(username, password, factory_name)
    user.save()

    return jsonify({'message': 'User and factory created successfully'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = User.find_by_username(username)
        if user and User.check_password(user['password_hash'], password):
            token = generate_token(username)
            return jsonify({'token': token}), 200

        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        import traceback
        return jsonify({
            'message': 'Internal Server Error',
            'error': str(e),
            'trace': traceback.format_exc()
        }), 500



@auth_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    try:
        users = User.get_all_users()
        return jsonify(users), 200
    except Exception as e:
        import traceback
        return jsonify({
            'message': 'Internal Server Error',
            'error': str(e),
            'trace': traceback.format_exc()
        }), 500


