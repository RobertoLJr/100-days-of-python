from bs4 import BeautifulSoup
import os
import requests
import smtplib

PROD_URL = ("https://www.amazon.co.uk/Resurrectionist-Lost-Writings-Spencer-Black/dp/1594746168/ref=tmm_hrd_swatch_0"
            "?_encoding=UTF8&qid=1702921590&sr=1-1")

PRICE_CUT = 18

# SMTP information
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
SENDER_HOST_DOMAIN = "gmail.com"

# Web Scrape the Amazon website for the desired product
response = requests.get(url=PROD_URL, headers={"User-Agent": "Defined"})
response.raise_for_status()
product_html = response.text
soup = BeautifulSoup(product_html, "html.parser")

product_name = soup.find(name="span", id="productTitle").text.strip()
product_price = float(soup.find(name="span", id="price").text[1:])

# Send email notification in case the product's price goes below the PRICE_CUT
if product_price <= PRICE_CUT:
    with smtplib.SMTP(f"smtp.{SENDER_HOST_DOMAIN}", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=SENDER_EMAIL,
            msg=f"Subject:Automated Amazon Price Tracker"
                f"\n\nThe product {product_name} is now £{product_price}. Below your target price. Buy it now!"
                f"\n\nLink: {PROD_URL}"
            .encode(encoding="utf-8")
        )
