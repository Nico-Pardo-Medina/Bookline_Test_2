import logging
from fastapi import APIRouter,HTTPException
from services.services import add_booking
from models.models import BookingRequest

router = APIRouter()

@router.post("/booking")
def create_booking(booking: BookingRequest):
    logging.info(f"Attempting to book car ID {booking.car_id} on {booking.date}")
    try:
        add_booking(booking.car_id, booking.date)
        logging.info(f"Successfully booked car ID {booking.car_id} on {booking.date}")
        return {"status": "success", "message": "Booking created successfully"}
    except Exception as e:
        logging.error(f"Failed to book car ID {booking.car_id} on {booking.date}: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")