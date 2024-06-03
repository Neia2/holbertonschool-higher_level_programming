import requests

def test_root_endpoint():
    response = requests.get('http://localhost:8000/')
    assert response.status_code == 200
    assert response.text == "Hello, this is a simple API!"

def test_data_endpoint():
    response = requests.get('http://localhost:8000/data')
    assert response.status_code == 200
    assert response.json() == {"name": "John", "age": 30, "city": "New York"}

def test_status_endpoint():
    response = requests.get('http://localhost:8000/status')
    assert response.status_code == 200
    assert response.text == "OK"

def test_undefined_endpoint():
    response = requests.get('http://localhost:8000/undefined')
    assert response.status_code == 404
    assert response.json() == {"error": "Endpoint not found"}

if __name__ == '__main__':
    test_root_endpoint()
    test_data_endpoint()
    test_status_endpoint()
    test_undefined_endpoint()
    print("All tests passed!")
