import datetime as dt
import pandas as pd
import random
import smtplib

SENDER_EMAIL = "sender_email@domain.com"
SENDER_EMAIL_PASSWORD = "sender_email_password"
SENDER_EMAIL_PROVIDER_ID = "domain.com"

# Letter files configuration
PLACEHOLDER_NAME = "[NAME]"
PLACEHOLDER_SENDER = "[SENDER]"
SENDER = "Your Name"

# Load data and record today's day/month
data = pd.read_csv("data/birthdays.csv")
date_today = f"{dt.datetime.now().day}/{dt.datetime.now().month}"

# Iterate over dataframe rows
for index, row in data.iterrows():
    person_name = row["name"]
    person_email = row["email"]
    person_birthday = f"{row["day"]}/{row["month"]}"

    # Check if any person's birthday matches today's date
    if date_today == person_birthday:
        with open(f"data/letter_{random.randrange(1, 4)}.txt") as letter_file:
            template = letter_file.read()
            birthday_letter = template.replace(PLACEHOLDER_NAME, person_name).replace(PLACEHOLDER_SENDER, SENDER)

        # Send mail
        with smtplib.SMTP(f"smtp.{SENDER_EMAIL_PROVIDER_ID}", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=person_email,
                msg=f"Subject:Happy Birthday!\n\n{birthday_letter}"
            )
