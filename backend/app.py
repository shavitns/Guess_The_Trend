# backend/app.py
from flask import Flask, jsonify, request
from api_handler.trend_logic import compare_crypto

app = Flask(__name__)

@app.route("/api/crypto-trend", methods=["GET"])
def crypto_trend():
    """
    Example usage:
    /api/crypto-trend?coin=bitcoin&vs=usd&period=year
    """
    coin = request.args.get("coin", "bitcoin")
    vs = request.args.get("vs", "usd")
    period = request.args.get("period", "day")
    result = compare_crypto(coin, vs, period)
    return jsonify(result)

if __name__ == "__main__":
    print("🚀 Flask server running... Visit:")
    print("http://127.0.0.1:5000/api/crypto-trend?coin=bitcoin&vs=usd&period=day")
    app.run(debug=True)
# backend/app.py
from flask import Flask, jsonify, request
from api_handler.trend_logic import compare_crypto

app = Flask(__name__)

@app.route("/api/crypto-trend", methods=["GET"])
def crypto_trend():
    """
    Example usage:
    /api/crypto-trend?coin=bitcoin&vs=usd&period=year
    """
    coin = request.args.get("coin", "bitcoin")
    vs = request.args.get("vs", "usd")
    period = request.args.get("period", "day")
    result = compare_crypto(coin, vs, period)
    return jsonify(result)

if __name__ == "__main__":
    print("🚀 Flask server running... Visit:")
    print("http://127.0.0.1:5000/api/crypto-trend?coin=bitcoin&vs=usd&period=day")
    app.run(debug=True)
# backend/app.py
from flask import Flask, jsonify, request
from api_handler.trend_logic import compare_crypto

app = Flask(__name__)

@app.route("/api/crypto-trend", methods=["GET"])
def crypto_trend():
    """
    Example usage:
    /api/crypto-trend?coin=bitcoin&vs=usd&period=year
    """
    coin = request.args.get("coin", "bitcoin")
    vs = request.args.get("vs", "usd")
    period = request.args.get("period", "day")
    result = compare_crypto(coin, vs, period)
    return jsonify(result)

if __name__ == "__main__":
    print("🚀 Flask server running... Visit:")
    print("http://127.0.0.1:5000/api/crypto-trend?coin=bitcoin&vs=usd&period=day")
    app.run(debug=True)
