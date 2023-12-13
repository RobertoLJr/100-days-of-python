import os
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_KEY = os.environ.get("STOCK_KEY")
NEWS_KEY = os.environ.get("NEWS_KEY")
BOT_KEY = os.environ.get("BOT_KEY")

# Make a call to AlphaVantage API to get the close stock value for yesterday and the day before yesterday
stock_params = {
    "apikey": STOCK_KEY,
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK
}

stock_response = requests.get("https://www.alphavantage.co/query", params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
day_before_yesterday_data = stock_data_list[1]
yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])


def calc_percent_difference():
    """Return the absolute percent difference between yesterday closing price and the day before closing price."""
    global yesterday_closing_price, day_before_yesterday_closing_price

    percent_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
    return (percent_difference / yesterday_closing_price) * 100


# Get the first 3 news pieces for the COMPANY_NAME via News API.
news_params = {
    "apiKey": NEWS_KEY,
    "q": COMPANY_NAME
}

news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
news_response.raise_for_status()
news_data = news_response.json()

articles = news_data["articles"][:3]

# Send a separate message with the percentage change and each article's title and description via Telegram bot.
bot_response = requests.get(f"https://api.telegram.org/bot{BOT_KEY}/getUpdates")
bot_response.raise_for_status()
bot_data = bot_response.json()

bot_chat_id = bot_data["result"][0]["message"]["chat"]["id"]

# Message data
difference = '{:.2f}'.format(calc_percent_difference())

for article in articles:
    bot_params = {
        "chat_id": bot_chat_id,
        "text": f"""
{STOCK}: {"🔺" if yesterday_closing_price > day_before_yesterday_closing_price else "🔻"} {difference}%
Headline: {article["title"]}

Brief: {article["description"]}

Read more at {article["url"]}"""
    }

    response = requests.get(f"https://api.telegram.org/bot{BOT_KEY}/sendMessage", params=bot_params)
    response.raise_for_status()
