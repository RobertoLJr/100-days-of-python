# This class is responsible for sending Telegram and Email notifications with the deal flight details.
import os
import requests
import smtplib

TELEGRAM_BOT_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")
EMAIL_PROVIDER_SMTP_ADDRESS = "gmail.com"
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


class NotificationManager:

    def fetch_telegram_chat_id(self):
        telegram_response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/getUpdates")
        telegram_response.raise_for_status()
        telegram_data = telegram_response.json()
        return telegram_data["result"][0]["message"]["chat"]["id"]

    def send_notification(self, price, departure_city_name, departure_airport_code, arrival_city_name,
                          arrival_airport_code, outbound_date, inbound_date, has_top_overs, stop_overs=0, via_city=""):
        telegram_chat_id = self.fetch_telegram_chat_id()

        telegram_parameters = {
            "chat_id": telegram_chat_id,
            "text": f"""Low price alert! Only {price} to fly from {departure_city_name}-{departure_airport_code} to 
{arrival_city_name}-{arrival_airport_code}, from {outbound_date} to {inbound_date}."""
        }

        if has_top_overs:
            telegram_parameters["text"] += f"\nFlight has {stop_overs} stop over(s), via {via_city}"

        response = requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/sendMessage",
            params=telegram_parameters
        )
        response.raise_for_status()

    def send_emails(self, emails, price, departure_city_name, departure_airport_code, arrival_city_name,
                    arrival_airport_code, outbound_date, inbound_date, has_top_overs, stop_overs=0, via_city=""):
        message = f"""Low price alert! Only {price} to fly from {departure_city_name}-{departure_airport_code} to 
{arrival_city_name}-{arrival_airport_code}, from {outbound_date} to {inbound_date}."""

        with smtplib.SMTP(f"smtp.{EMAIL_PROVIDER_SMTP_ADDRESS}", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
