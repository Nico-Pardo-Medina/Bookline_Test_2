import logging
import re
from fastapi import HTTPException
from pydantic import BaseModel,validator

class DateQuery(BaseModel):
    date: str

    @validator("date")
    def validate_date(cls, date: str) -> str:
        return validate_date_format(date)

class BookingRequest(BaseModel):
    car_id: int
    date: str

    @validator("car_id")
    def validate_car_id(cls, car_id: int) -> int:
        if car_id < 1:
            logging.error(f"Invalid id format: {car_id}. Car ID must be a positive integer greater than 0.")
            raise HTTPException(status_code=400, detail="Car ID must be a positive integer greater than 0.")
        return car_id

    @validator("date")
    def validate_date(cls, date: str) -> str:
        return validate_date_format(date)

def validate_date_format(date: str) -> str:
    DATE_REGEX = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    if not re.match(DATE_REGEX, date):
        logging.error(f"Invalid date format: {date}. Expected format: YYYY-MM-DD.")
        raise HTTPException(status_code=400, detail=f"Invalid date format: {date}. Expected format: YYYY-MM-DD.")
    return date