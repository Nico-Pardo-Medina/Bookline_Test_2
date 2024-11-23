from fastapi import APIRouter
from pydantic import BaseModel
import json

router = APIRouter()

CARS_JSON_PATH = "domain/cars.json"

class BookingRequest(BaseModel):
    car_id: int
    date: str

@router.post("/bookings")
def create_booking(booking: BookingRequest):
    with open(CARS_JSON_PATH, "r") as file:
        cars = json.load(file)

    for car in cars:
        if car["id"] == booking.car_id:
            car["bookings"].append(booking.date)  # Add the booking date
            break
    
    with open(CARS_JSON_PATH, "w") as file:
        json.dump(cars, file)