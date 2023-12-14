# This class is responsible for sending Telegram notifications with the deal flight details.
import os
import requests

TELEGRAM_BOT_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")


class NotificationManager:

    def fetch_telegram_chat_id(self):
        telegram_response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/getUpdates")
        telegram_response.raise_for_status()
        telegram_data = telegram_response.json()
        return telegram_data["result"][0]["message"]["chat"]["id"]

    def send_notification(self, price, departure_city_name, departure_airport_code, arrival_city_name,
                          arrival_airport_code, outbound_date, inbound_date):
        telegram_chat_id = self.fetch_telegram_chat_id()

        telegram_parameters = {
            "chat_id": telegram_chat_id,
            "text": f"""Low price alert! Only {price} to fly from {departure_city_name}-{departure_airport_code} to 
{arrival_city_name}-{arrival_airport_code}, from {outbound_date} to {inbound_date}."""
        }

        response = requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/sendMessage",
            params=telegram_parameters
        )
        response.raise_for_status()
