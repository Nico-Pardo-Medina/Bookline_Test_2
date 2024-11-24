import logging
import re
from fastapi import APIRouter,HTTPException,Depends
from pydantic import BaseModel,validator
from services.services import list_available_cars

router = APIRouter()

class Car(BaseModel):
    id: int
    model: str
    bookings: list[str]

class DateQuery(BaseModel):
    date: str

    @validator("date")
    def validate_date(cls, date: str) -> str:
        DATE_REGEX = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
        if not re.match(DATE_REGEX, date):
            logging.error(f"Invalid date format: {date}. Expected format: YYYY-MM-DD.")
            raise HTTPException(status_code=400, detail=f"Invalid date format: {date}. Expected format: YYYY-MM-DD.")
        return date


@router.get("/cars", response_model=list[int])
def get_available_cars(query: DateQuery = Depends()):
    logging.debug(f"Received query to list available cars for date: {query.date}")
    available_cars = list_available_cars(query.date)
    if len(available_cars) < 1:
        logging.info(f"No cars available on {query.date}.")
    else:
        logging.info(f"Available cars on {query.date}: {available_cars}")
    return available_cars