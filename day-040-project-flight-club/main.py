from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Menu
print("Welcome to the Flight Club.\nWe find the best flight deals and email you.")
option = int(input("""
Please, enter the number corresponding to one of the options below:
1. Add a new user to the club.
2. Search flights and send notifications to current members.
3. Quit.\n"""))

if option == 1:
    first_name = input("What is your first name?\n").title()
    last_name = input("What is your last name?\n").title()

    email = input("What is your email?\n").lower()
    email_validation = ""

    while email_validation != email:
        email_validation = input("Type your email again.\n")

    data_manager.add_user(first_name, last_name, email)
    print("You're in the club!")
elif option == 2:
    ORIGIN_CITY_IATA = "EDI"

    if sheet_data[0]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in sheet_data:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )

        if flight is None:
            continue

        if flight.price <= destination["lowestPrice"]:
            users = data_manager.get_user_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]

            notification_manager.send_notification(
                price=flight.price,
                departure_city_name=flight.origin_city,
                departure_airport_code=flight.origin_airport,
                arrival_city_name=flight.destination_city,
                arrival_airport_code=flight.destination_airport,
                outbound_date=flight.out_date,
                inbound_date=flight.return_date,
                has_top_overs=True if flight.stop_overs > 0 else False,
                stop_overs=flight.stop_overs if flight.stop_overs > 0 else False,
                via_city=flight.via_city if flight.stop_overs > 0 else False
            )

            notification_manager.send_emails(
                emails,
                price=flight.price,
                departure_city_name=flight.origin_city,
                departure_airport_code=flight.origin_airport,
                arrival_city_name=flight.destination_city,
                arrival_airport_code=flight.destination_airport,
                outbound_date=flight.out_date,
                inbound_date=flight.return_date,
                has_top_overs=True if flight.stop_overs > 0 else False,
                stop_overs=flight.stop_overs if flight.stop_overs > 0 else False,
                via_city=flight.via_city if flight.stop_overs > 0 else False
            )
