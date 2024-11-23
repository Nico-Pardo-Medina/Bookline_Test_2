from fastapi import FastAPI
from routers import cars, booking

app = FastAPI()
app.include_router(cars.router)
app.include_router(booking.router)

