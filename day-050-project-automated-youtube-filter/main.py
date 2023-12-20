import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

MUSIC_STYLE = "synthwave"

# Set up web browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(3)

# Begin search for the MUSIC_STYLE
search = driver.find_element(By.NAME, value="search_query")
search.send_keys(MUSIC_STYLE)
search.send_keys(Keys.ENTER)
time.sleep(3)

# Select filter for This Week
button_filter = driver.find_element(By.ID, value="filter-button")
button_filter.click()
time.sleep(3)
this_week = driver.find_element(By.XPATH, value='/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search'
                                                '-filter-options-dialog-renderer/div['
                                                '2]/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer['
                                                '3]/a')
this_week.click()
time.sleep(3)

# Open the first video
first_video = driver.find_element(By.XPATH, value="//*[@id='video-title']/yt-formatted-string")
first_video.click()

user_input = input("Press any key to close the browser.")
driver.quit()
