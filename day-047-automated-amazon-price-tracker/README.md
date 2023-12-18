# Day 47 Project: Automated Amazon Price Tracker

## Concept

This program makes use of web scraping to get hold of a certain product in Amazon Website. As of the current implementation,
the program works for the book [The Resurrectionist: The Lost Work and Writings of Dr. Spencer Black](https://www.amazon.co.uk/Resurrectionist-Lost-Writings-Spencer-Black/dp/1594746168/ref=tmm_hrd_swatch_0?_encoding=UTF8&qid=1702921590&sr=1-1)
in Amazon UK, which can be changed inside the code as of the current implementation. Once the program is executed, it
verifies if the current product price is equal to or less a price cut also set up within the code. If this is true,
then the program sends an email notification containing the product name, price, and link for the user to buy it.

## Requirements

- An [App Password](https://myaccount.google.com/apppasswords) set up in your Google account.
- An email account and the app password as environment variables to provide the SMTP connection.

## Usage

1. First, replace the `PROD_URL` with the URL of the product you wish to track.
2. Then, replace the `PRICE_CUT` with the maximum price of the product for the notification to be sent.
3. Set up a sender email and app password as environment variables and verify if the `SENDER_HOST_DOMAIN` corresponds to the domain of the sender email.
4. Run the program.

## Resources

### Libraries and modules

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [os module](https://docs.python.org/3/library/os.html)
- [Requests: HTTP for Humans Documentation](https://requests.readthedocs.io/en/latest/)
- [smtplib - SMTP protocol client](https://docs.python.org/3/library/smtplib.html)
