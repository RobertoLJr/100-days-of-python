import os
import requests

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")


# This class is responsible for talking to the Google sheet
class DataManager:
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        return response.json()["prices"]

    def update_iata_code(self, row_id, iata_code):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(f"{SHEETY_ENDPOINT}/{row_id}", json=body)
        response.raise_for_status()
