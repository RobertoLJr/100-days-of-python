# Day 36 Project: Stock Trading News Alert

## Concept

This program makes use of various API calls to:

1. Check yesterday's and the day before yesterday's closing stock price for a given NASDAQ code for a company.
2. Get the most recent 3 news from more than 80.000 sources (see resources for News API) that cite the company's name.
3. Send a Telegram notification via bot with the percent difference of yesterday's and the day before yesterday's closing stock price, the headlines, descriptions and sources for each news.

As of the current implementation, the program runs in search of the Tesla Inc. company (NASDAQ TSLA). Prior to its
execution, the user should also provide their own API keys as environment variables for the AlphaVantage API, the News API and the Telegram Bot API (see resources below).

## Resources

### APIs

- [AlphaVantage API](https://www.alphavantage.co) - Stock Market API
- [News API](https://newsapi.org/) - News API
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)

### Miscellanea

- [How to create a Telegram bot, and send messages with Python](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)
- [NASDAQ Stock Screener](https://www.nasdaq.com/market-activity/stocks/screener) - Check other companies' NASDAQ codes.