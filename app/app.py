from fastapi import FastAPI, HTTPException
import requests
import os
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Initialize Instrumentator to collect metrics
Instrumentator().instrument(app).expose(app)

# OpenWeatherMap API Key (store this in environment variables for security)
API_KEY = "386b525bed5796c7d5db34e3d5b9da87"

@app.get("/weather/{city}")
async def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        error_detail = response.json().get("message", "City not found or API error")
        raise HTTPException(status_code=response.status_code, detail=error_detail)


    data = response.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
    }
