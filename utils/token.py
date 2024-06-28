from flask_jwt_extended import create_access_token, decode_token
from datetime import timedelta

def generate_token(username):
    expires = timedelta(days=1)
    return create_access_token(identity=username, expires_delta=expires)

def decode_jwt(token):
    return decode_token(token)
