import traceback

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.auth_services import User
from utils.token import generate_token

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    """
       Performs the registration process.

       This function is used to register users or other entities. The specific
       implementation may involve adding a user to a database or handling
       similar registration tasks.

       Details of how the function works:
       - Expected parameters and their validation rules.
       - Values or outputs returned upon successful execution.
       - Potential errors and exceptions.
       """
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
    """
       Handles the login process for users.

       This function is responsible for authenticating users based on their
       credentials. It typically involves verifying a username and password
       against stored records and managing user sessions or tokens.

       Details of how the function works:
       - Expected parameters, such as username and password.
       - Validation and authentication procedures.
       - Session or token creation upon successful login.
       - Error handling for invalid credentials or other login issues.
       """
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
    """
       Retrieves a list of users from the database.

       This function fetches and returns a list of user records from the database.
       It may include options for pagination, filtering, or sorting depending on
       the implementation details.

       Details of how the function works:
       - Any parameters for filtering or pagination (if applicable).
       - The format of the data returned, such as a list of dictionaries.
       - Handling of cases where no users are found.

       Returns:
           list: A list of dictionaries, where each dictionary represents a user
                 record with relevant user information.

       Raises:
           DatabaseError: Raised if there is an issue connecting to or querying
                          the database.
       """
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


@auth_bp.route('/users/<users_id>', methods=['DELETE'])
@jwt_required()
def delete_users(users_id):
    """
        Deletes users from the database based on the provided user IDs.

        This function removes one or more user records from the database using
        the specified user IDs. It may handle single or multiple IDs depending
        on the implementation.

        Details of how the function works:
        - `users_id`: A list or single ID representing the user(s) to be deleted.
        - Validation of the provided IDs to ensure they exist in the database.
        - Handling of cases where some or all IDs are invalid or not found.
        """
    users = User.users_get_by_id(users_id)
    print(users)
    if not users:
        return jsonify({'message': 'Users not found'}), 404

    User.users_delete(users["_id"])
    return jsonify({'message': 'Users deleted successfully'}), 200


@auth_bp.route('/users/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    """
        Updates the details of a user identified by the provided user ID.

        This function modifies the user record in the database based on the
        provided `user_id`. The specific fields to be updated and the new values
        are typically passed as part of the request or through additional parameters.

        Details of how the function works:
        - `user_id`: The unique identifier of the user whose details are to be updated.
        - The fields and values to be updated, which should be specified or passed
          alongside the function call.
        - Validation of the `user_id` to ensure the user exists in the database.
        - Handling of cases where the update operation fails or the `user_id` is not found.
        """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    factory = data.get('factory_name')

    try:
        user = User.find_by_id(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        User.update(user_id, username, password, factory)
        return jsonify({'message': 'User updated successfully'}), 200
    except Exception as e:
        return jsonify({
            'message': 'Internal Server Error',
            'error': str(e),
            'trace': traceback.format_exc()
        }), 500

