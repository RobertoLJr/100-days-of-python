from flight_data import FlightData
import os
import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
CURRENCY = "GBP"


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        self.headers = {"apikey": TEQUILA_API_KEY}

    def get_destination_iata_code(self, city):
        query = {"term": city}
        response = requests.get(f"{TEQUILA_ENDPOINT}/locations/query", headers=self.headers, params=query)
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def search_flights(self, origin_city_code, destination_city_code, date_from, date_to):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": CURRENCY
        }

        response = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", headers=self.headers, params=query)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £ {flight_data.price}")
        return flight_data
