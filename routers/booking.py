import logging
import re
from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,validator
from services.services import add_booking
router = APIRouter()

class BookingRequest(BaseModel):
    car_id: int
    date: str

    @validator("date")
    def validate_date(cls, date: str) -> str:
        DATE_REGEX = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
        if not re.match(DATE_REGEX, date):
            logging.error(f"Invalid date format: {date}. Expected format: YYYY-MM-DD.")
            raise HTTPException(status_code=400, detail=f"Invalid date format: {date}. Expected format: YYYY-MM-DD.")
        return date

@router.post("/booking")
def create_booking(booking: BookingRequest):
    logging.info(f"Attempting to book car ID {booking.car_id} on {booking.date}")
    try:
        add_booking(booking.car_id, booking.date)
        logging.info(f"Successfully booked car ID {booking.car_id} on {booking.date}")
        return {"status": "success", "message": "Booking created successfully"}
    except Exception as e:
        logging.error(f"Failed to book car ID {booking.car_id} on {booking.date}: {e}")
        raise HTTPException(status_code=500, detail="Failed to create booking")