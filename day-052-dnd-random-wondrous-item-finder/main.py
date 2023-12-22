import re
import time
from random import shuffle

from selenium import webdriver
from selenium.webdriver.common.by import By
from WondrousItem import WondrousItem

# Rarity tabs
RARITY_TABS = 8

# Greet the user
print("=== WELCOME TO VOLO'S WHEEL OF WONDERS! ===\n")
print("Please hold while we fetch the treasure hoard from the dragon...\n")
time.sleep(3)

# Set up web browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://dnd5e.wikidot.com/wondrous-items")

# Get all wondrous items from website
items_list_per_rarity = []
all_items = []

for _ in range(RARITY_TABS):
    rarity_tab_items = driver.find_element(By.ID, value=f'wiki-tab-0-{_}')
    display_prop = rarity_tab_items.value_of_css_property("display")
    if display_prop == "none":
        driver.execute_script("arguments[0].style.display = 'block';", rarity_tab_items)

    items_list_per_rarity.append(rarity_tab_items.text.split("\n")[1:])

for items_list in items_list_per_rarity:
    for item_info in items_list:
        item_name = re.split(" - | Attuned ", item_info)[0]
        if " ".join(item_name.split(" ")[-2:]) == "Wondrous Item":
            all_items.append(" ".join(item_name.split(" ")[:-2]))
        else:
            all_items.append(" ".join(item_name.split(" ")[:-1]))

# Prompt user for a random choice
lower_limit = 0
upper_limit = len(all_items) - 1

number = int(input(f"There! Please, choose a number between {0} and {upper_limit} to get a random wondrous item! -> "))
while number < lower_limit or number > upper_limit:
    number = int(input(f"Come now, don't be stubborn. Choose a number between {lower_limit} and {upper_limit} (or "
                       f"any nonnumerical key to end the program altogether). -> "))

shuffle(all_items)
print(f"OK, {number}! Very bold! Please, wait while we organize the Bag of Holding...\n")
time.sleep(3)

# Open the item info web page
print(f"Congratulations! You got a {all_items[number]}! See the browser for more information!\n")

wondrous_item = WondrousItem(all_items[number], driver)
wondrous_item.print_info()

input("Press any key to close the browser and end the program. Go on! Shoo now!\n")

driver.quit()
