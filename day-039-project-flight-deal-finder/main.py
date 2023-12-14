from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "EDI"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

for item in sheet_data:
    if item["iataCode"] == "":
        item["iataCode"] = flight_search.get_destination_iata_code(item["city"])
        data_manager.update_iata_code(item["id"], item["iataCode"])

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.search_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        date_from=tomorrow,
        date_to=six_months_from_today
    )

    if flight is not None and flight.price <= destination["lowestPrice"]:
        notification_manager.send_notification(
            price=flight.price,
            departure_city_name=flight.origin_city,
            departure_airport_code=flight.origin_airport,
            arrival_city_name=flight.destination_city,
            arrival_airport_code=flight.destination_airport,
            outbound_date=flight.out_date,
            inbound_date=flight.return_date
        )
