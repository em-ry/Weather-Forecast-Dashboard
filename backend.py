import requests
import streamlit as st


def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={st.secrets['API_KEY']}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content["list"]
    # tot data provided for 5 days 3 hourly = 40, ie 8 per day
    requested_days = 8 * forecast_days
    filtered_content = filtered_content[:requested_days]
    return filtered_content


if __name__ == "__main__":
    print(get_data(place="enugu", forecast_days=2))
