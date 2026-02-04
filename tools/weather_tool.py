
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherTool:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENWEATHER_API_KEY not found in environment variables")
    def getweather(self,city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
        }
        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=10,
        )
        if response.status_code != 200:
            raise Exception(
                f"Weather API error: {response.status_code} - {response.text}"
            )
        data = response.json()
        return {
            "city": data.get("name"),
            "temperature_celsius": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
        }
