import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the form URL and Zillow URL
FORM_URL = "YOUR_FORM_URL"
FORM_INPUT_ADDRESS_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
FORM_INPUT_PRICE_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
FORM_INPUT_LINK_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
FORM_BUTTON_SEND_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
FORM_LINK_SEND_ANOTHER_RESPONSE_XPATH = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

# Get BeautifulSoup Zillow info
response = requests.get(ZILLOW_URL)
response.raise_for_status()
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# Collect listing links, prices, and addresses, and create a dictionary for each listing
listing_cards = soup.find_all(name="li", attrs="ListItem-c11n-8-84-3-StyledListCardWrapper")
listing_links = [card.find(name="a")["href"] for card in listing_cards]
listing_prices = [
    re.split(f"{re.escape("+")}|/", card.find(name="span", attrs="PropertyCardWrapper__StyledPriceLine").text)[0]
    for card in listing_cards
]
listing_addresses = [card.find(name="a").text.strip() for card in listing_cards]

listings = [{"link": listing_links[_], "price": listing_prices[_], "address": listing_addresses[_]}
            for _ in range(len(listing_cards))]

# Set up webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_URL)

# Fill in the form entries for each listing item
for listing in listings:
    # Find and fill the address input
    input_address = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, FORM_INPUT_ADDRESS_XPATH))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", input_address)
    input_address.send_keys(listing["address"])

    # Find and fill the price input
    input_price = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, FORM_INPUT_PRICE_XPATH)))
    driver.execute_script("arguments[0].scrollIntoView(true);", input_price)
    input_price.send_keys(listing["price"])

    # Find and fill the link input
    input_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, FORM_INPUT_LINK_XPATH)))
    driver.execute_script("arguments[0].scrollIntoView(true);", input_link)
    input_link.send_keys(listing["link"])

    # Find and click the button to send response
    button_send = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, FORM_BUTTON_SEND_XPATH)))
    button_send.click()

    # Find and click the link to send another response
    link_send_another = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH,FORM_LINK_SEND_ANOTHER_RESPONSE_XPATH)))
    link_send_another.click()

driver.quit()
