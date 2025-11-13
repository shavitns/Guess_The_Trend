# backend/app.py
from flask import Flask, jsonify, request
from api_handler.manager import compare_trend

app = Flask(__name__)
from flask_cors import CORS
CORS(app)


@app.route("/api/trend", methods=["GET"])
def trend():
    """
    General API for comparing trends.
    Examples:
      /api/trend?type=crypto&coin=bitcoin&period=month
      /api/trend?type=weather&lat=31.78&lon=35.22&period=year
    """
    data_type = request.args.get("type", "crypto")
    kwargs = request.args.to_dict()  # all params
    result = compare_trend(data_type, **kwargs)
    return jsonify(result)

if __name__ == "__main__":
    print("🚀 Server ready:")
    print("http://127.0.0.1:5000/api/trend?type=crypto&coin=bitcoin")
    print("http://127.0.0.1:5000/api/trend?type=weather&lat=31.78&lon=35.22&period=day")
    app.run(debug=True)
