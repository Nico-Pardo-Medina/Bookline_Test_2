from fastapi import APIRouter,Query
from pydantic import BaseModel
import json

router = APIRouter()

class Car(BaseModel):
    id: int
    model: str
    bookings: list[str]

CARS_JSON_PATH = "domain/cars.json"

@router.get("/cars/available", response_model=list[Car])
def list_available_cars(date:str = Query(...)):
    with open(CARS_JSON_PATH, "r") as file:
        cars = json.load(file)
    available_cars = [
        car for car in cars if date not in car["bookings"]
    ]
    return available_cars