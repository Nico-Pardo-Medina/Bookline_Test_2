import logging

from fastapi import FastAPI
from routers import cars, booking

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

app = FastAPI()
app.include_router(cars.router)
app.include_router(booking.router)

