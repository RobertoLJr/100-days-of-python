import os
import requests

# Setup API keys as environment variables
TELEGRAM_BOT_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")
OPEN_WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
MY_LATITUDE = 55.953251
MY_LONGITUDE = -3.188267

# Call Telegram API to fetch user chat ID
telegram_response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/getUpdates")
telegram_response.raise_for_status()
telegram_data = telegram_response.json()
telegram_chat_id = telegram_data["result"][0]["message"]["chat"]["id"]

# Setup location parameters and API key for OpenWeather API
weather_parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": OPEN_WEATHER_API_KEY,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    telegram_parameters = {
        "chat_id": telegram_chat_id,
        "text": "Weather forecast for the day is rainy. Bring an Umbrella!"
    }

    response = requests.get(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/sendMessage",
        params=telegram_parameters
    )
    response.raise_for_status()
