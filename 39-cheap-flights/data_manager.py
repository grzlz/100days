import requests

class DataManager:
    def __init__(self):
        self.url = "https://api.sheety.co/9d02c5f5ce2841613a57bda5339ea48e/copiaDeFlightDeals/prices"
    
    def get_data(self):
        data = requests.get(self.url)
        data = data.json()["prices"]
        return data
    
    def upload_data(self, data):
        for row in data:
            new_row = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            r = requests.put(f"{self.url}/{row['id']}", json=new_row)
            print(r.json())
    
    #This class is responsible for talking to the Google Sheet.
    pass