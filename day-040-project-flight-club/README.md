# Day 40 Project: Flight Club

## Concept

This program functions very similarly to the [Day 39 Project: Flight Deal Finder](/day-039-project-flight-deal-finder). However,
it addresses some exceptions that might be raised. In addition, it offers a menu in the console when first executed. This version
is capable of adding more users to the Google Sheet doc to also send a notification via email whenever a flight deal is found.
Also, whenever no flight is found with no stopover, the program will look for flight deals with one stopover to the destination.

## Requirements

- A Google Sheets doc with the columns `City`, `IATA Code`, and `Lowest Price` (see [template](./template_sheet/Flight%20Deals.xlsx)).
- Another sheet in the same doc with the name `users` with the columns `First Name`, `Last Name`, and `Email`.
- A Sheety account with the Google Sheet doc set up as a project.
- Kiwi Partners Flight Search API Key (Free Signup, Credit Card not required) (see resources).
- Telegram Bot API Key (see resources).

## Usage

1. First, update the Google Sheet doc with at least one city name in the City column and a value for the lowest acceptable price for notifications. The sheet `users` need the column names, but does not require more data.
2. In code, the user should provide the following data for constants:

   - `ORIGIN_CITY_IATA` in `main.py` with the IATA code for origin destination (see resources for codes).
   - `TEQUILA_API_KEY` in `flight_search.py` with the API Key provided by Kiwi Partners Flight Search API.
   - `CURRENCY` in `flight_search.py` with the desired currency for search (default is GBP).
   - `SHEETY_ENDPOINT` in `data_manager.py` with the endpoint for the sheet in Sheety.
   - `TELEGRAM_BOT_API_KEY` in `notification_manager.py` with the Telegram Bot API Key provided when setting up the bot.
   - `EMAIL_PROVIDER_SMTP_ADDRESS` in `notification_manager.py` if other than `gmail.com` (default).
   - `MY_EMAIL` in `notification_manager.py` with the email account that will send the notification.
   - `MY_PASSWORD` in `notification_manager.py` with the app password set up from the email account that will send the notification.

3. Then, update the Google Sheet doc with at least the city name and the desired lowest price for notifications.

4. Then, run the `main.py` file. Enter a number corresponding to the menu option for `Add a new user` or `Send notification to current members`.

   - When adding a new user, provide a first name, a last name, en email account and the same email as validation when prompted.

5. The program will automatically search and fill the IATA Codes for every city in the City column from the Google Sheet doc, if not there already.

6. Next, the program will search for flight deals using the updated IATA codes. If a deal is found and costs equal to or lesser than the lowest price in the sheet, an email notification with the flight data will be sent to the users from the account set in the code. A Telegram bot will also send a notification with the flight data.

## Resources

### APIs

- [Sheety API Documentation](https://sheety.co/docs)
- [Tequila Flight Search API Documentation](https://tequila.kiwi.com/portal/docs/tequila_api)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)

### Modules and libraries

- [os](https://docs.python.org/3/library/os.html)
- [requests](https://requests.readthedocs.io/en/latest/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)

### Miscellanea

- [IATA Codes for cities with multiple airports](https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_airports)
- [More about Kiwi Partners Flight Search](https://partners.kiwi.com/) - From the creators of the Tequila Flight Search API.
- [How to create a Telegram bot, and send messages with Python](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)
