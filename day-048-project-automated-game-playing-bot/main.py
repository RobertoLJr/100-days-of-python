from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()

# Timer for scheduled checks and break
timeout = time.time() + 5
five_min_mark = time.time() + 60 * 5

# Select English language
time.sleep(1)
driver.find_element(By.ID, value="langSelect-EN").click()
time.sleep(1)

# Get big cookie element
big_cookie = driver.find_element(By.ID, value="bigCookie")

while True:
    if time.time() >= five_min_mark:
        break

    big_cookie.click()
    if time.time() > timeout:
        cookies = driver.find_element(By.ID, value="cookies").text.split()[0].replace(",", "")
        products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")

        products_prices = []
        if len(products) > 0:
            for product in products:
                products_prices.append(int(product.text.split()[1].replace(",", "")))
            most_expensive_index = products_prices.index(max(products_prices))
            products[most_expensive_index].click()

        timeout = time.time() + 5

time.sleep(5)
cookies_per_sec = driver.find_element(By.ID, value="cookiesPerSecond")
print(f"Cookies {cookies_per_sec.text}")

driver.quit()
