import json
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

TEST_CARS_JSON = [
    {"id": 1,"model": "Toyota Corolla", "bookings": ["2024-12-24","2024-12-25"]},
    {"id": 2,"model": "Honda Civic", "bookings": ["2024-12-24"]},
    {"id": 3,"model": "Ford Focus", "bookings": ["2024-12-24"]}
]

@pytest.fixture(autouse=True)
def mock_cars_file(monkeypatch, tmp_path):
    mock_path = tmp_path / "cars.json"
    with open(mock_path, "w") as mock_file:
        json.dump(TEST_CARS_JSON, mock_file)
    
    monkeypatch.setattr("services.services.CARS_JSON_PATH", str(mock_path))

def test_get_available_cars():
    response = client.get("/cars", params={"date": "2024-12-24"})
    assert response.status_code == 200
    assert response.json() == [], "Expected no cars to be available."

def test_get_available_cars_no_available():
    response = client.get("/cars", params={"date": "2024-12-25"})
    assert response.status_code == 200
    assert response.json() == [2,3], "Expected cars 2 and 3 to be available."

def test_get_available_cars_invalid_date():
    response = client.get("/cars", params={"date": "25-12-2024"})
    assert response.status_code == 400, "Invalid date format should return 400 status."
    assert response.json()["detail"] == "Invalid date format: 25-12-2024. Expected format: YYYY-MM-DD."

def test_create_booking_success():
    response = client.post("/booking", json={"car_id": 2, "date": "2024-12-25"})
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "message": "Booking created successfully"
    }

def test_create_booking_car_does_not_exist():
    response = client.post("/booking", json={"car_id": 999, "date": "2024-12-25"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Car ID 999 not found."
    }

def test_create_booking_car_already_booked():
    response = client.post("/booking", json={"car_id": 2, "date": "2024-12-24"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Car ID 2 is already booked on 2024-12-24."
    }

def test_create_booking_invalid_car_id():
    response = client.post("/booking", json={"car_id": -9, "date": "2024-12-25"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Car ID must be a positive integer greater than 0."
    }