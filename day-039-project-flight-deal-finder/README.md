# Day 39 Project: Flight Deal Finder

## Concept

This program functions making many API calls to check flight deals from more than 750 carriers against a personal
Google sheet containing travel destinations. If any search matches any destination from the sheet and the deal's price
is lower than the one provided by the user, a Telegram bot sends a notification to them with the flight data. See
requirements and resources for proper usage. As of the current implementation, modifications are expected to be
made in-code, so there is room for improvement in the future via GUIs and entries.

## Requirements

- A Google Sheets doc with the columns `City`, `IATA Code`, and `Lowest Price` (see [template](./template_sheet/Flight%20Deals.xlsx)).
- A Sheety account with the Google Sheet doc set up as a project.
- Kiwi Partners Flight Search API Key (Free Signup, Credit Card not required) (see resources).
- Telegram Bot API Key (see resources).

## Usage

1. First, update the Google Sheet doc with at least city names in the City column and a value for the lowest acceptable price for notifications.
2. In code, the user should provide the following data for constants:

   - `ORIGIN_CITY_IATA` in `main.py` with the IATA code for origin destination (see resources for codes).
   - `TEQUILA_API_KEY` in `flight_search.py` with the API Key provided by Kiwi Partners Flight Search API.
   - `CURRENCY` in `flight_search.py` with the desired currency for search (default is GBP).
   - `SHEETY_ENDPOINT` in `data_manager.py` with the endpoint for the sheet in Sheety.
   - `TELEGRAM_BOT_API_KEY` in `notification_manager.py` with the Telegram Bot API Key provided when setting up the bot.

3. Then, update the Google Sheet doc with at least the city name and the desired lowest price for notifications.

4. Then, run the `main.py` file. The program will automatically search and fill the IATA Codes for every city in the City column from the Google Sheet doc.

5. Next, the program will search for flight deals using the updated IATA codes. If a deal is found and costs equal to or lesser than the lowest price in the sheet, a Telegram bot will send a notification with the flight data.


## Resources

### APIs

- [Sheety API Documentation](https://sheety.co/docs)
- [Tequila Flight Search API Documentation](https://tequila.kiwi.com/portal/docs/tequila_api)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)

### Miscellanea

- [IATA Codes for cities with multiple airports](https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_airports)
- [More about Kiwi Partners Flight Search](https://partners.kiwi.com/) - From the creators of the Tequila Flight Search API.
- [How to create a Telegram bot, and send messages with Python](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)
