# backend/api_handler/stocks_api.py
"""
stocks_api.py
---------------
Fetches stock price data using Yahoo Finance (yfinance).
"""

import yfinance as yf
from datetime import datetime, timedelta


def get_stock_price(symbol: str) -> float:
    """
    Fetch current stock price.
    Example: get_stock_price("AAPL")
    """
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    return round(data["Close"].iloc[-1], 2)


def get_stock_price_on_date(symbol: str, date: datetime) -> float:
    """
    Fetch historical stock closing price for a given date.
    If no data found (weekend or holiday), tries a few days earlier.
    """
    import datetime as dt
    ticker = yf.Ticker(symbol)

    for i in range(5):  # last 5 days
        start = (date - timedelta(days=i)).strftime("%Y-%m-%d")
        end = (date - timedelta(days=i-1)).strftime("%Y-%m-%d")
        data = ticker.history(start=start, end=end)
        if not data.empty:
            return round(data["Close"].iloc[-1], 2)
    return None
