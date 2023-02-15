class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_code(self, data):
        for i in data:
            if i["iataCode"] == "":
                i["iataCode"] = "TESING"