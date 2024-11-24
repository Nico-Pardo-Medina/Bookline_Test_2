import logging
from fastapi import APIRouter,Depends
from services.services import list_available_cars
from models.models import DateQuery

router = APIRouter()

@router.get("/cars", response_model=list[int])
def get_available_cars(query: DateQuery = Depends()):
    logging.debug(f"Received query to list available cars for date: {query.date}")
    available_cars = list_available_cars(query.date)
    if len(available_cars) < 1:
        logging.info(f"No cars available on {query.date}.")
    else:
        logging.info(f"Available cars on {query.date}: {available_cars}")
    return available_cars