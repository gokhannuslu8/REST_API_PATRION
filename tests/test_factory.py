import requests
import json

def test_create_factory():
    url = 'http://127.0.0.1:5000/factories'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTgyOTQ4MiwianRpIjoiNWVjMDQwZGQtMzYzYy00ODFlLWE3YmEtZDMxMDI4NjA3YWU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imdva2hhbiB1c2x1IiwibmJmIjoxNzE5ODI5NDgyLCJleHAiOjE3MTk5MTU4ODJ9.WF6S-JGmeuWkh76_HQ6uCw1eh2u3hE8O1wTrcs6I7Go'
    }

    data = {
        'name': 'newfactory99',
        'location': 'trabzon',
        'capacity': 333
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    assert response.status_code == 201, f"Expected 201, but got {response.status_code}"
    response_data = response.json()
    assert 'message' in response_data, "The key 'message' was not found in the response"
    assert response_data['message'] == 'Factory created successfully', f"Expected message 'Factory created successfully', but got {response_data['message']}"

test_create_factory()

def test_get_factories():
    url = 'http://127.0.0.1:5000/factories'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTgyOTQ4MiwianRpIjoiNWVjMDQwZGQtMzYzYy00ODFlLWE3YmEtZDMxMDI4NjA3YWU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imdva2hhbiB1c2x1IiwibmJmIjoxNzE5ODI5NDgyLCJleHAiOjE3MTk5MTU4ODJ9.WF6S-JGmeuWkh76_HQ6uCw1eh2u3hE8O1wTrcs6I7Go'
    }

    response = requests.get(url, headers=headers)

    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    response_data = response.json()
    assert 'factories' in response_data, "The key 'factories' was not found in the response"
    assert 'pagination' in response_data, "The key 'pagination' was not found in the response"

test_get_factories()

def test_update_factory(factory_id):
    url = f'http://127.0.0.1:5000/factories/{factory_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTgyOTQ4MiwianRpIjoiNWVjMDQwZGQtMzYzYy00ODFlLWE3YmEtZDMxMDI4NjA3YWU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imdva2hhbiB1c2x1IiwibmJmIjoxNzE5ODI5NDgyLCJleHAiOjE3MTk5MTU4ODJ9.WF6S-JGmeuWkh76_HQ6uCw1eh2u3hE8O1wTrcs6I7Go'
    }

    data = {
        'name': 'newfactory59',
        'location': 'hakkari',
        'capacity': 500
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))

    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    response_data = response.json()
    assert 'message' in response_data, "The key 'message' was not found in the response"
    assert response_data['message'] == 'Factory updated successfully', f"Expected message 'Factory updated successfully', but got {response_data['message']}"

test_update_factory('66828d222c2ab2efb53d8620')

def test_delete_factory(factory_id):
    url = f'http://127.0.0.1:5000/factories/{factory_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTgyOTQ4MiwianRpIjoiNWVjMDQwZGQtMzYzYy00ODFlLWE3YmEtZDMxMDI4NjA3YWU1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imdva2hhbiB1c2x1IiwibmJmIjoxNzE5ODI5NDgyLCJleHAiOjE3MTk5MTU4ODJ9.WF6S-JGmeuWkh76_HQ6uCw1eh2u3hE8O1wTrcs6I7Go'
    }

    response = requests.delete(url, headers=headers)


    print('Status Code:', response.status_code)
    print('Response Body:', response.json())

    d
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    response_data = response.json()
    assert 'message' in response_data, "The key 'message' was not found in the response"
    assert response_data['message'] == 'Factory deleted successfully', f"Expected message 'Factory deleted successfully', but got {response_data['message']}"


test_delete_factory('66828b8b988e7d0ea07dce90')
