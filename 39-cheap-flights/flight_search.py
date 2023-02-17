import requests 

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
    
    def get_price(self, destination):
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
        lowest_price = r["data"][0]["price"]

        return lowest_price
    
    def get_prices(self, data):
        for destination in data:
            print(destination["city"], self.get_price(destination["iataCode"]))

