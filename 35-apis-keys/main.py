import requests 

api_key = "69f04e4613056b159c2761a9d9e664d2"
parameters = {
    "q": "Cancun",
    "appid": api_key
    }

r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
print(r.json())

# Get Hourly forecast for 48 hours from https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

parameters = {
    "lat": 21.1743,
    "lon": -86.8466,
    "appid": api_key
}

next48 = requests.get("https://api.openweathermap.org/data/2.5/onecall", params = parameters)
print(next48.json())