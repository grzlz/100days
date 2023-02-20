import requests 
from twilio.rest import Client

account_sid = "AC81f2671430dc9505aaed34057ce8f306"
auth_token = "f294e23376f119d371252473411de6e9"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_code(self, data):
        for i in data:
            if i["iataCode"] == "":
                i["iataCode"] = self.fetch_code(i["city"])

    def fetch_code(self, city):
        url = "https://api.tequila.kiwi.com/locations/query"
        params = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
            "active_only": "true"
        }
        headers = {
            "apikey": "MtYDAqQ8v5jzNh6vBSAt5gZbaVuTnDwW"
        }
        r = requests.get(url, params = params, headers = headers)
        iata_code = r.json()["locations"][0]["id"]

        return iata_code
    
    def get_flight_data(self, destination):
        params = {
            "fly_from": "CUN",
            "fly_to": destination,
            "date_from": "12/05/2023",
            "date_to": "20/05/2023",
            "return_from": "10/08/2023",
            "return_to": "15/08/2023",
            "adults": 1,
            "curr": "MXN"
        }

        headers = {
            "apiKey": "MtYDAqQ8v5jzNh6vBSAt5gZbaVuTnDwW"
        }

        url = "https://api.tequila.kiwi.com/v2/search"

        r = requests.get(url, params=params, headers=headers).json()
        r = r["data"][0]
        flight_data = {key: r[key] for key in r if key in ["price", "local_departure"]}

        return flight_data
    
    def find_deal(self, data):
        for destination in data:
            threshold = destination["lowestPrice"]
            destination_code = destination["iataCode"]
            flight_data = self.get_flight_data(destination_code)
            if threshold <= flight_data["price"]:
                message_data = {
                    "city": data["city"],
                    "price": flight_data["price"],
                    "departure": flight_data["local_departure"]
                    }
                self.send_notification(message_data)

    def send_notification(self, data):
        # SEND TWILIO MESSAGE
        body = f"Found a great flight deal to {data['city']} for only {data['price']} leaving on {data['departure']}"
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=body,
                            from_='+14303051259',
                            to='+525548017016')


            # TO DO 

