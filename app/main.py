from fastapi import FastAPI
from pydantic import BaseModel


description = """

This is a DoorDash (really downgraded) copycat API made for Jedha's students

Made with ❤️ by Jedha
"""

app = FastAPI(
    title="🍔 DoorDash Delivery API",
    description=description,
    version="0.1",
    contact={
        "name": "Jedha",
        "url": "https://jedha.co",
    }
)

class DeliveryFeeRequest(BaseModel):
    distance_km: float
    weight_kg: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the DoorDash Delivery Fee Service API"}

@app.post("/calculate-fee/")
def calculate_fee(request: DeliveryFeeRequest):
    """
    Calculate delivery fees
    """
    base_fee = 5.00
    fee_per_km = 1.50
    fee_per_kg = 0.50
    delivery_fee = base_fee + (fee_per_km * request.distance_km) + (fee_per_kg * request.weight_kg)
    return {"delivery_fee": delivery_fee}

@app.get("/estimate-time/{distance_km}")
def estimate_delivery_time(distance_km: float):
    """
    Estimate time for delivery
    """
    base_time = 10  # Base time in minutes
    time_per_km = 5  # Time in minutes per kilometer
    estimated_time = base_time + (time_per_km * distance_km)
    return {"estimated_delivery_time_minutes": estimated_time}

@app.get("/status/")
def service_status():
    return {"status": "Service is up and running"}
