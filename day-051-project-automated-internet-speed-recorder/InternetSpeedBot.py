import csv
import time
from datetime import datetime

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class InternetSpeedBot:
    def __init__(self, timeout=45):
        self.driver_path = "https://www.speedtest.net/"
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0
        self.timeout = timeout

    def countdown(self):
        while self.timeout >= 0:
            mins, secs = divmod(self.timeout, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("\rTime remaining: ", end=timer)
            time.sleep(1)
            self.timeout -= 1

    def get_internet_speed(self):
        print("Starting test...")
        try:
            self.driver.get(self.driver_path)
            time.sleep(2)
            button_start = self.driver.find_element(By.CSS_SELECTOR, value=".js-start-test.test-mode-multi")
            button_start.click()
            print("Test started.")

            self.countdown()

            down = self.driver.find_element(By.CSS_SELECTOR, value=".result-data-large.number.result-data-value"
                                                                   ".download-speed")
            up = self.driver.find_element(By.CSS_SELECTOR, value=".result-data-large.number.result-data-value.upload"
                                                                 "-speed")
            print("\nTest concluded successfully.")
            self.down = float(down.text)
            self.up = float(up.text)

        except NoSuchElementException:
            print("Test aborted. Web elements not found.")
        finally:
            self.driver.quit()

    def record_tests(self):
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        try:
            with open("./data/data.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                with open("./data/data.csv", "a", newline='') as csv_file_appender:
                    csv_writer = csv.writer(csv_file_appender)
                    csv_writer.writerow([current_date, self.down, self.up])
        except FileNotFoundError:
            with open("./data/data.csv", "w", newline='') as writefile:
                csv_writer = csv.writer(writefile)
                csv_writer.writerow(["datetime", "download_speed", "upload_speed"])
                csv_writer.writerow([current_date, self.down, self.up])
        finally:
            print("Test recorded successfully.")
