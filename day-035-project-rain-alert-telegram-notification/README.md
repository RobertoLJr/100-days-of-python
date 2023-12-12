# Day 35 Project: Rain Alert Telegram Notification

## Concept

This program works by making API calls to check the forecast for the day and send the user a message via Telegram if
the forecast is rainy. Check the resources for the APIs used.

Prior to executing the program, the user should provide the following info:

- In the code: provide the latitude and longitude of your location (see resources).
- As environment variables: provide the API keys for your own Telegram bot and for the OpenWeather API (see resources).

To make this program properly useful on the occasion of the current implementation, you can upload the code to
PythonAnywhere (see resources) and schedule the time for its execution as in the early morning, for example. Then,
whenever the forecast for the day is rainy, the bot will send you the message `Weather forecast for the day is rainy.
Bring an Umbrella!`

## Resources

### APIs

- [OpenWeather 5-day weather forecast API Documentation](https://openweathermap.org/forecast5)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)

### Modules and libraries

- [os](https://docs.python.org/3/library/os.html)
- [requests](https://docs.python-requests.org/en/latest/)

### Miscellanea

- [How to create a Telegram bot, and send messages with Python](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)
- [LatLong.net](https://www.latlong.net/) - You can find the latitude/longitude for any place by location name/address here.
- [Online JSON Viewer](https://jsonviewer.stack.hu/) - Awesome for reading extensive JSON data.
- [PythonAnywhere](https://www.pythonanywhere.com/) - Free Cloud service to upload and run your code at any scheduled time (one scheduled execution per free account).