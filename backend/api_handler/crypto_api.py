# backend/api_handler/crypto_api.py
"""
crypto_api.py
--------------
Handles cryptocurrency data fetching using CoinGecko API.
"""

import requests
from datetime import datetime, timedelta


def get_crypto_price(coin_id: str, vs_currency: str = "usd") -> float:
    """
    Fetches the current price of a cryptocurrency.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": vs_currency}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()[coin_id][vs_currency]


def get_crypto_price_on_date(coin_id: str, date: datetime, vs_currency: str = "usd") -> float:
    """
    Fetches historical price of a cryptocurrency on a given date.
    """
    formatted_date = date.strftime("%d-%m-%Y")
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/history"
    params = {"date": formatted_date}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("market_data", {}).get("current_price", {}).get(vs_currency, None)
