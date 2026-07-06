from flask import Flask
from flask import request
from flask import jsonify
from dotenv import load_dotenv
import os
import requests
import redis
import json

# python3 -m venv api_env create environment
# source api_env/bin/activate enter the environment
# pip freeze > requirements.txt 

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)

# Create Route
@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    if city is None:
        return jsonify({"error": "City not listed"}), 400
    else:
        info = r.get(city)
        if info is not None:
            return jsonify(json.loads(info))
        else:
            url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={API_KEY}&contentType=json"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json() # call the function
                r.set(city, json.dumps(data), ex=3600) # converts into a string
                return jsonify(data)
            else:
                return jsonify({"error": "Could not fetch weather data"}), response.status_code



if __name__ == "__main__":
    app.run(debug=True)