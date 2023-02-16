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