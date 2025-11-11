# backend/api_handler.py
"""
api_handler.py
----------------
This module handles all data fetching and processing for the "Guess the Trend" game.

Currently, it retrieves Bitcoin price data from the CoinGecko API and compares
today's price with yesterday's to determine whether the trend went UP or DOWN.
"""
import requests
from datetime import datetime, timedelta



def get_bitcoin_price():
    """
    Fetches the current Bitcoin price in USD using the CoinGecko API.

    Returns:
        float: The current Bitcoin price in USD.
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url) # Raises an exception if the request failed
    data = response.json()
    return data["bitcoin"]["usd"]

def get_bitcoin_price_on(date):
    """
    Fetches the historical Bitcoin price (USD) for a given date.

    Args:
        date (datetime): A Python datetime object representing the date to fetch.

    Returns:
        float: The Bitcoin price (USD) for that specific date.
    """
    formatted_date = date.strftime("%d-%m-%Y")
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/history"
    params = {"date": formatted_date}

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    # Some days might not have market data (e.g., future date or API limits)
    return data.get("market_data", {}).get("current_price", {}).get("usd", None)


def compare_bitcoin_today_vs_yesterday():
    """
    Compares today's Bitcoin price with yesterday's price.

    Returns:
        dict: {
            "trend": "up" or "down",
            "today": <float>,
            "yesterday": <float>
        }
    """
    today = get_bitcoin_price()

    yesterday = datetime.now() - timedelta(days=1)
    yesterday_price = get_bitcoin_price_on(yesterday)

    # Validate data
    if yesterday_price is None:
        return {"error": "Failed to fetch yesterday's price"}

    trend = "up" if today > yesterday_price else "down"

    return {
        "trend": trend,
        "today": today,
        "yesterday": yesterday_price
    }

if __name__ == "__main__":
    result = compare_bitcoin_today_vs_yesterday()
    print(result)
