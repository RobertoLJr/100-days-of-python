from datetime import *
import os
import requests

NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.environ.get("NUTRITIONIX_KEY")

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PROJECT = os.environ.get("SHEETY_PROJECT")
SHEETY_SHEET = os.environ.get("SHEETY_SHEET") # Doublecheck this because Sheet sometimes creates an arbitrary value
SHEET_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT}/{SHEETY_SHEET}"

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

# Get data from Nutritionix using user input as natural language
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_input = input("Tell me which exercises you did: ")

HEADER = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY
}

parameters = {
    "query": user_input
}

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=HEADER)
response.raise_for_status()
data = response.json()

# Add rows to a Google Sheet via Sheety API
for exercise in data["exercises"]:
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    sheety_payload = {
        "workout": {
            "date": str(datetime.now().strftime("%d/%m/%Y")),
            "time": str(datetime.now().strftime("%X")),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=SHEET_ENDPOINT, json=sheety_payload, headers=headers)
    response.raise_for_status()
