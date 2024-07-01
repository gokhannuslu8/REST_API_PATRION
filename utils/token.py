from flask_jwt_extended import create_access_token, decode_token
from datetime import timedelta

def generate_token(username):
    """
       Generates an authentication or session token for the specified username.

       This method creates a token that can be used to authenticate or identify the
       user with the given `username`. The generated token may be used for session management
       or API authentication purposes.
       """
    expires = timedelta(days=1)
    return create_access_token(identity=username, expires_delta=expires)

def decode_jwt(token):
    """
      Decodes a JSON Web Token (JWT) and returns the payload data.

      This method takes a JWT as input, verifies its signature, and decodes it to
      extract the payload information. The payload typically contains claims or user
      information encoded in the token.
      """
    return decode_token(token)
