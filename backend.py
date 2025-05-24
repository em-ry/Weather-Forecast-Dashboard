import os

from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = ""


def get_data(place, forecast_days=None, option=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={os.getenv('API_KEY')}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content["list"]
    # tot data provided for 5 days 3 hourly = 40, ie 8 per day
    requested_days = 8 * forecast_days
    filtered_content = filtered_content[:requested_days]

    if option.capitalize() == "Temperature":
        filtered_content = [data["main"]["temp"] for data in filtered_content]
    if option.capitalize() == "Clouds":
        filtered_content = [sky_data["weather"][0]["main"] for sky_data in filtered_content]
    return filtered_content


if __name__ == "__main__":
    print(get_data(place="enugu", forecast_days=2, option="temperature"))
