import requests
import json

def test_create_entity():
    url = 'http://127.0.0.1:5000/entities'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTgyOTQ4MiwianRpIjoiNWVjMDQwZGQtMzYzYy00ODFlLWE3YmEtZDMxMDI4NjA3YWU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imdva2hhbiB1c2x1IiwibmJmIjoxNzE5ODI5NDgyLCJleHAiOjE3MTk5MTU4ODJ9.WF6S-JGmeuWkh76_HQ6uCw1eh2u3hE8O1wTrcs6I7Go'  # Add your JWT token here
    }

    data = {
        'name': 'newentity99',
        'description': 'Description of the new entity',
        'value': 100
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    assert response.status_code == 201, f"Expected 201, but got {response.status_code}"
    response_data = response.json()
    assert 'message' in response_data, "The key 'message' was not found in the response"
    assert response_data['message'] == 'Entity created successfully', f"Expected message 'Entity created successfully', but got {response_data['message']}"

test_create_entity()

def test_get_entities():
    url = 'http://127.0.0.1:5000/entities'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTgyOTQ4MiwianRpIjoiNWVjMDQwZGQtMzYzYy00ODFlLWE3YmEtZDMxMDI4NjA3YWU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imdva2hhbiB1c2x1IiwibmJmIjoxNzE5ODI5NDgyLCJleHAiOjE3MTk5MTU4ODJ9.WF6S-JGmeuWkh76_HQ6uCw1eh2u3hE8O1wTrcs6I7Go'  # Add your JWT token here
    }

    response = requests.get(url, headers=headers)

    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    response_data = response.json()
    assert 'entities' in response_data, "The key 'entities' was not found in the response"
    assert 'pagination' in response_data, "The key 'pagination' was not found in the response"

test_get_entities()

def test_update_entity(entity_id):
    url = f'http://127.0.0.1:5000/entities/{entity_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTgyOTQ4MiwianRpIjoiNWVjMDQwZGQtMzYzYy00ODFlLWE3YmEtZDMxMDI4NjA3YWU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imdva2hhbiB1c2x1IiwibmJmIjoxNzE5ODI5NDgyLCJleHAiOjE3MTk5MTU4ODJ9.WF6S-JGmeuWkh76_HQ6uCw1eh2u3hE8O1wTrcs6I7Go'  # Add your JWT token here
    }

    data = {
        'name': 'updatedentity59',
        'description': 'Updated description of the entity',
        'value': 500
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))

    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    response_data = response.json()
    assert 'message' in response_data, "The key 'message' was not found in the response"
    assert response_data['message'] == 'Entity updated successfully', f"Expected message 'Entity updated successfully', but got {response_data['message']}"

test_update_entity('66828d222c2ab2efb53d8620')

def test_delete_entity(entity_id):
    url = f'http://127.0.0.1:5000/entities/{entity_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTgyOTQ4MiwianRpIjoiNWVjMDQwZGQtMzYzYy00ODFlLWE3YmEtZDMxMDI4NjA3YWU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imdva2hhbiB1c2x1IiwibmJmIjoxNzE5ODI5NDgyLCJleHAiOjE3MTk5MTU4ODJ9.WF6S-JGmeuWkh76_HQ6uCw1eh2u3hE8O1wTrcs6I7Go'  # Add your JWT token here
    }

    response = requests.delete(url, headers=headers)

    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    response_data = response.json()
    assert 'message' in response_data, "The key 'message' was not found in the response"
    assert response_data['message'] == 'Entity deleted successfully', f"Expected message 'Entity deleted successfully', but got {response_data['message']}"

test_delete_entity('66828b8b988e7d0ea07dce90')
