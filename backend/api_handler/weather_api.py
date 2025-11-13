# backend/api_handler/weather_api.py
"""
weather_api.py
---------------
Handles fetching current and historical temperature data from Open-Meteo API.
"""
import requests
from datetime import datetime, timedelta

def get_weather(lat: float, lon: float) -> float:
    """
    Fetch current temperature (°C) for given coordinates.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["current_weather"]["temperature"]

def get_weather_on_date(lat: float, lon: float, date: datetime) -> float:
    """
    Fetch historical daily temperature for given coordinates.
    (using reanalysis data)
    """
    formatted_date = date.strftime("%Y-%m-%d")
    url = "https://archive-api.open-meteo.com/v1/era5"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": formatted_date,
        "end_date": formatted_date,
        "daily": "temperature_2m_max",
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    temps = data.get("daily", {}).get("temperature_2m_max", [])
    return temps[0] if temps else None
