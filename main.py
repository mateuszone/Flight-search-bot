# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "WMI"

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# tommorow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(30 * 6))
tommorow = datetime.now() + timedelta(days=78)
six_month_from_today = datetime.now() + timedelta(days=(30 * 6))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time=tommorow,
        # to_time=six_month_from_today
    )
    try:
        if flight.price < destination["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-"
                        f"{flight.origin_airport}"
                        f" to {flight.destination_city}"
                        f"-{flight.destination_airport},"
                        f" from {flight.out_date} to "
                        f"{flight.return_date}."
            )
    except AttributeError:
        pass


