import json

CARS_JSON_PATH = "data/cars.json"

def list_available_cars(date: str) -> list[int]:
    """List car IDs that are not booked on the given date."""
    with open(CARS_JSON_PATH, "r") as file:
        cars = json.load(file)
    return [car["id"] for car in cars if date not in car["bookings"]]

def add_booking(car_id: int, date: str) -> None:
    """Add a booking to a car."""
    with open(CARS_JSON_PATH, "r") as file:
        cars = json.load(file)
    car_found = False
    for car in cars:
        if car["id"] == car_id:
            if date in car["bookings"]:
                raise ValueError(f"Car ID {car_id} is already booked on {date}.")
            car["bookings"].append(date)
            car_found = True
            break
    if not car_found:
        raise ValueError(f"Car ID {car_id} not found.")
    with open(CARS_JSON_PATH, "w") as file:
        json.dump(cars, file)