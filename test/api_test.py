import requests

BASE_URL = "http://localhost:8000"


def test_root_endpoint():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "All routes available"
    assert data["routes"]["health"] == "/health"
    assert data["routes"]["version"] == "/version"
    assert data["routes"]["environment"] == "/environment"


def test_health_endpoint():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "Up"}


def test_version_endpoint():
    response = requests.get(f"{BASE_URL}/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}


def test_environment_endpoint():
    response = requests.get(f"{BASE_URL}/environment")
    assert response.status_code == 200
    assert response.json() == {"environment": "development"}


def test_unknown_endpoint():
    response = requests.get(f"{BASE_URL}/unknown")
    assert response.status_code == 404


def test_health_response_type():
    response = requests.get(f"{BASE_URL}/health")
    assert response.headers["Content-Type"] == "application/json"