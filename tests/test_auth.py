import requests
import json

def test_login():
    url = 'http://127.0.0.1:5000/login'
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    response_data = response.json()
    assert 'access_token' in response_data, "The key 'access_token' was not found in the response"
    assert 'refresh_token' in response_data, "The key 'refresh_token' was not found in the response"
    assert 'token_type' in response_data, "The key 'token_type' was not found in the response"
    assert response_data['token_type'] == 'Bearer', f"Expected token_type 'Bearer', but got {response_data['token_type']}"

test_login()

def test_refresh_token(refresh_token):
    url = 'http://127.0.0.1:5000/refresh'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {refresh_token}'
    }

    response = requests.post(url, headers=headers)

    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    response_data = response.json()
    assert 'access_token' in response_data, "The key 'access_token' was not found in the response"
    assert 'token_type' in response_data, "The key 'token_type' was not found in the response"
    assert response_data['token_type'] == 'Bearer', f"Expected token_type 'Bearer', but got {response_data['token_type']}"

# To use this function, you need to obtain a refresh token from the login function
# Example:
# refresh_token = 'your_refresh_token_here'
# test_refresh_token(refresh_token)

def test_protected_endpoint(access_token):
    url = 'http://127.0.0.1:5000/protected'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    response_data = response.json()
    assert 'message' in response_data, "The key 'message' was not found in the response"
    assert response_data['message'] == 'Access granted', f"Expected message 'Access granted', but got {response_data['message']}"

# To use this function, you need to obtain an access token from the login function
# Example:
# access_token = 'your_access_token_here'
# test_protected_endpoint(access_token)
