# backend/api_handler/manager.py
"""
manager.py
-----------
Routes requests to the right data handler based on the 'type' parameter.
"""
from datetime import datetime, timedelta
from .crypto_api import get_crypto_price, get_crypto_price_on_date
from .weather_api import get_weather, get_weather_on_date
from .stocks_api import get_stock_price, get_stock_price_on_date
import time


def compare_trend(data_type="crypto", **kwargs):
    """
    Compare trends for different data types.
    Supported: crypto, weather
    """
    if data_type == "crypto":
        coin = kwargs.get("coin", "bitcoin")
        vs = kwargs.get("vs", "usd")
        period = kwargs.get("period", "day")

        today = get_crypto_price(coin, vs)
        delta = {"day": 1, "month": 30, "year": 365}[period]
        previous_date = datetime.now() - timedelta(days=delta)
        time.sleep(0.5)  # delay for prevent blocking
        prev = get_crypto_price_on_date(coin, previous_date, vs)

        trend = "up" if today > prev else "down"
        return {
            "type": "crypto",
            "coin": coin,
            "vs": vs,
            "trend": trend,
            "today": today,
            "previous": prev,
            "change": round((today - prev) / prev * 100, 2)
        }

    elif data_type == "weather":
        lat = float(kwargs.get("lat", 31.78))  # default: Jerusalem
        lon = float(kwargs.get("lon", 35.22))
        period = kwargs.get("period", "day")

        today = get_weather(lat, lon)
        delta = {"day": 1, "month": 30, "year": 365}[period]
        previous_date = datetime.now() - timedelta(days=delta)
        prev = get_weather_on_date(lat, lon, previous_date)

        trend = "up" if today > prev else "down"
        return {
            "type": "weather",
            "location": f"{lat}, {lon}",
            "trend": trend,
            "today": today,
            "previous": prev,
            "change": round((today - prev), 2)
        }
    elif data_type == "stocks":
        symbol = kwargs.get("symbol", "AAPL")
        period = kwargs.get("period", "day")

        today = get_stock_price(symbol)
        delta = {"day": 1, "month": 30, "year": 365}[period]
        prev_date = datetime.now() - timedelta(days=delta)
        prev = get_stock_price_on_date(symbol, prev_date)

        if prev is None:
            return {"error": f"No data for {symbol} on that date."}

        trend = "up" if today > prev else "down"

        return {
            "type": "stocks",
            "symbol": symbol,
            "trend": trend,
            "today": today,
            "previous": prev,
            "change": round((today - prev) / prev * 100, 2)
        }

    else:
        return {"error": f"Unsupported data type '{data_type}'"}
