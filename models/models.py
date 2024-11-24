import logging
import re
from fastapi import HTTPException
from pydantic import BaseModel,validator,conint

class DateQuery(BaseModel):
    date: str

    @validator("date")
    def validate_date(cls, date: str) -> str:
        return validate_date_format(date)

class BookingRequest(BaseModel):
    car_id: int
    date: str

    @validator("date")
    def validate_date(cls, date: str) -> str:
        return validate_date_format(date)

def validate_date_format(date: str) -> str:
    DATE_REGEX = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    if not re.match(DATE_REGEX, date):
        logging.error(f"Invalid date format: {date}. Expected format: YYYY-MM-DD.")
        raise HTTPException(status_code=400, detail=f"Invalid date format: {date}. Expected format: YYYY-MM-DD.")
    return date