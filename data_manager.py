import requests

SHEET_ENDPOINT = "https://api.sheety.co/c59c86e598757a2986b0cbd38954ef54/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEET_ENDPOINT)
        sheet_data1 = response.json()
        self.destination_data = sheet_data1['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            sheet_input = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            put_sheet_response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=sheet_input)
            print(put_sheet_response.text)
