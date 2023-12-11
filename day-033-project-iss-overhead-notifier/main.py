import requests
import smtplib
import time
from datetime import datetime

# Coordinates for Edinburgh
MY_LAT = 55.953251
MY_LNG = -3.188267

# Email and password for notification
EMAIL = "email@domain.com"
PASSWORD = "password"
HOST_DOMAIN = "domain.com"


# Fetch data from ISS Current Location
def is_overhead():
    """Return if ISS latitude and longitude are less than or equal to 5 from my position."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LNG - 5 <= iss_longitude <= MY_LNG + 5)


def is_nighttime():
    """Return if the current hour is greater than sunset hour or lesser than sunrise hour of my position."""
    # Fetch data from Sunrise Sunset API
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise


while True:
    time.sleep(60)
    print("test")

    # Send an email notification in case the ISS is overhead and it is nighttime.
    if is_overhead() and is_nighttime():
        connection = smtplib.SMTP(f"smtp.{HOST_DOMAIN}")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Look Up 🔭\n\nThe ISS is above you in the sky."
        )
