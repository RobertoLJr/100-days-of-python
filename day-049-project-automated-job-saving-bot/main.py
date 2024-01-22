from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import os

LINKEDIN_USERNAME = os.environ.get("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

# Set up Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3789144643&distance=25&f_AL=true&f_E=1%2C2&f_WT=2"
           "&geoId=101165590&keywords=Data%20Engineer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")
driver.maximize_window()
time.sleep(2)

# Find and click the login button
button_login = driver.find_element(By.CLASS_NAME, value="nav__button-secondary.btn-md.btn-secondary-emphasis")
button_login.click()
time.sleep(2)

# Fill credentials and log into LinkedIn
username = driver.find_element(By.ID, value="username")
username.send_keys(LINKEDIN_USERNAME)
password = driver.find_element(By.ID, value="password")
password.send_keys(LINKEDIN_PASSWORD)

button_submit_login = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
button_submit_login.click()
time.sleep(2)

# Start saving all jobs in first page
jobs_containers = driver.find_elements(By.CLASS_NAME, value="job-card-container--clickable")
print("Opening job lists...")

for job_container in jobs_containers:
    print(f"Saving {job_container.text} job...")
    job_container.click()
    time.sleep(2)

    try:
        button_save_job = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
        button_save_job.click()
        time.sleep(2)

        print(f"Job from {job_container.text.split()[1]} saved successfully.")
    except NoSuchElementException:
        print(f"No saving button was found. Skipped application to {job_container.text} job.")
        continue

print("Done.")

driver.quit()
