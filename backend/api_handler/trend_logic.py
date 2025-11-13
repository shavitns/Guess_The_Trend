# backend/api_handler/trend_logic.py
"""
trend_logic.py
--------------
Contains general comparison logic for trends.
"""

from datetime import datetime, timedelta
from api_handler.crypto_api import get_crypto_price, get_crypto_price_on_date


def compare_crypto(coin_id="bitcoin", vs_currency="usd", period="day"):
    """
    Compares crypto price between now and a previous time period.
    period options: 'day', 'month', 'year'
    """

    today = get_crypto_price(coin_id, vs_currency)

    if period == "day":
        prev_date = datetime.now() - timedelta(days=1)
    elif period == "month":
        prev_date = datetime.now() - timedelta(days=30)
    elif period == "year":
        prev_date = datetime.now() - timedelta(days=365)
    else:
        raise ValueError("Invalid period. Choose 'day', 'month', or 'year'.")

    previous = get_crypto_price_on_date(coin_id, prev_date, vs_currency)

    if previous is None:
        return {"error": f"No data available for {period} ago."}

    trend = "up" if today > previous else "down"

    return {
        "coin": coin_id,
        "currency": vs_currency,
        "period": period,
        "trend": trend,
        "today": today,
        "previous": previous,
        "change": round((today - previous) / previous * 100, 2)
    }
